# Manufacrturing Robot Planning in PDDL

This is a real case that we tackled for a manufacturing company. This
company devises supply chains to make pieces of medical equipments. A
supply chain consists of independent robotized units/cells, which
realize specific operations on the pieces: cleaning, checking, marking,
assembling etc. The pieces are put on trays, and mobile robots are
programmed to take and to transport the trays between the different
units. The image below illustrates this process:

![Robotics Use Case](./images/industrial_use_case.png){.with-shadow
.with-shadow}

There are different symbolType of pieces at the beginning of the supply
chain. A tray contains only one symbolType of pieces, and, each piece
undergoes a sequence of operations from the beginning to the end of the
supply chain. At the beginning of the supply chain, a unit is used to
store all the trays. The units can have several inputs named
\"conveyors\". The conveyors and the units are specific to a set of
pieces: pieces are admissible to identified conveyors and units.
Initially, every processing (unit loading/unloading, robot movements
etc.) was hard-coded in a database by human operators. Automated
planning is now used to optimize unit/robot scheduling and to increase
production efficiency.

## Defining the Domain

### Requirements

Let start by creating the domain file. For instance, `rsc-domain.pddl`
write the following PDDL to give a name to this domain and specify the
requirements of the domain.

``` text
(define (domain robotic-manufactoring)
    (:requirements :strips :typing)
```

### Types

Then, define the set of objects (types) that will be used in this
domain. Quite obviously, we will have the types *robot* (mobile robots),
*conveyor*, *unit*, *piece*, etc.

``` text
(:types
    robot - agent
    conveyor unit - location
    piece operation tray - object
)
```

### Constants

We also declare a dummy operation called *stop* as a constant of the
domain which will be used in one action:

``` text
(:constants
stop - operation
)
```

### Predicates

Now it is time to think to a model for the domain. It is based on the
following ideas: \* *Producer/consumer:* the trays are resources
consumed by the conveyors and produced by the units. A \"one-to-many\"
relation is created between each unit and the conveyors. A tuple
conveyors/unit is like a (Petri Net) \"machine\" that consumes and
produces trays. The conveyors are the inputs and the unit is the output.
Each input/output\'s capacity is one, \* *Operation stacks:* each tray
is associated to a stack of operations that have to be performed on the
pieces of the tray. The last operation of the stack is always
\_[stop](). Each time a machine consumes a tray, the associated stack is
pulled, \* *Goal:* to empty all the stacks by connecting the machines
with robots transporting trays from units (outputs) to conveyors
(inputs). The capacity of the robots is one.


Here is the vocabulary (\"predicates\") that will be used by the
actions:

``` text
(:predicates
    ;;robot
    (robot_available ?robot - robot)
    ;; is the robot available? capacity is one
    (robot_at ?robot - robot ?l - location)
    ;; location of a robot. Either a conveyor or a unit

    ;;conveyor
    (conveyor_accepted_piece ?piece - piece ?conv - conveyor)
    ;; constraint on admissible pieces
    (conveyor_available ?conv - conveyor)
    ;; is the conveyor available? capacity is one
    (conveyor_unit ?conv - conveyor ?unit - unit)
    ;; "one-to-many" relation between units and conveyors

    ;;unit
    (unit_accepted_piece ?piece - piece ?unit - unit)
    ;; constraint on admissible pieces
    (unit_available ?unit - unit)
    ;; is the unit available? unit capacity is one
    (unit_operation ?op - operation ?unit - unit)
    ;; operation provided by the unit

    ;;tray
    (tray_on_unit ?tray - tray ?unit - unit)
    ;; the tray is in the unit
    (tray_on_conv ?tray - tray ?conv - conveyor)
    ;; the tray is input into the conveyor
    (tray_on_robot ?tray - tray ?robot - robot)
    ;; the robot is at the tray
    (tray_completed ?tray - tray)
    ;; all the scheduled operations are completed

    ;;piece
    (piece_on ?piece - piece ?tray - tray)
    ;; "one-to-one" relation: trays contain only one type of pieces

    ;;stack of operations
    (start ?op - operation ?tray - tray)
    ;; ?op is on top of the stack.
    ;; The stack has a one-to-one relation with the tray (same id)
    (todo ?opontop - operation ?nextop - operation ?tray - tray)
    ;; linked list of operations: ?nextop follows ?opontop. Last operation is stop
)
```

For instance, in the problem file, you can now specify an initial state
beginning by:

``` text
(start op10 tray32)
(todo op10 op20 tray32)
(todo op20 op30 tray32)
(todo op30 stop tray32)
```

This means that the sequence *op10*, *op20*, *op30* of operations is
scheduled on *tray32*.

Likewise,

``` text
(conveyor_unit conv1 unit1)
(conveyor_unit conv2 unit1)
```

means that *unit1* has two inputs *conv1* and *conv2*.

### Operators

The new step is to define all the actions. For this domain, we will need
6 actions:

``` text
(:action pickup_tray_on_unit
    :parameters (?robot - robot ?unit - unit ?tray - tray)
    :precondition (and (robot_available ?robot)
                       (robot_at ?robot ?unit)
                       (tray_on_unit ?tray ?unit)
                   )
    :effect (and (not (tray_on_unit ?tray ?unit))
                 (not (robot_available ?robot))
                 (tray_on_robot ?tray ?robot)
                 (unit_available ?unit)
            )
)
```

Action *pickup_tray_on_unit* allows a robot to pickup a tray on a unit
provided the robot is available and located at this unit. The effects
are that the tray is no more on the unit, the tray is on the robot and
the robot is not available to pickup another tray. The unit becomes
available to process another tray.

``` text
(:action drop_tray_on_conveyor
    :parameters (?robot - robot ?conv - conveyor ?tray - tray ?piece - piece)
    :precondition (and (conveyor_available ?conv)
                       (robot_at ?robot ?conv)
                       (tray_on_robot ?tray ?robot)
                       (conveyor_accepted_piece ?piece ?conv)
                       (piece_on ?piece ?tray)
                  )
    :effect (and (not (conveyor_available ?conv))
                 (not (tray_on_robot ?tray ?robot))
                 (tray_on_conv ?tray ?conv)
                 (robot_available ?robot))
)
```

Action *drop_tray_on_conveyor* is the counterpart of
*pickup_tray_on_unit*. It allows a robot to put a tray on a conveyor.
The preconditions are that the robot and the conveyor are in the same
place, the conveyor is available and it accepts the same type of pieces
than the tray. The effects are that the conveyor is no more available,
the tray is no more on the robot (it is on the conveyor) and the robot
is now available.

``` text
(:action robot_move
    :parameters (?robot - robot ?from - location ?to - location)
    :precondition (and (robot_at ?robot ?from))
    :effect (and (robot_at ?robot ?to)
                 (not (robot_at ?robot ?from))
            )
)
```

Action *robot_move* is trivial: it moves a robot from location *?from\$
to location \$?to*. Locations are either a conveyor or a unit (see
*:types* keyword).

``` text
(:action conveyor_load_tray_in_unit
    :parameters (?conv - conveyor ?unit - unit ?tray - tray ?piece - piece)
    :precondition (and (unit_available ?unit)
                       (conveyor_unit ?conv ?unit)
                       (unit_accepted_piece ?piece ?unit)
                       (piece_on ?piece ?tray)
                       (tray_on_conv ?tray ?conv)
                  )
    :effect (and (not (tray_on_conv ?tray ?conv))
                 (not (unit_available ?unit))
                 (tray_on_unit ?tray ?unit))
    )
```

Action *conveyor_load_tray_in_unit* consumes a tray that is loaded on a
conveyor linked to a unit provided the pieces of the tray are accepted
by this unit. As a consequence, the tray is no more one the conveyor,
the unit is not available and the tray is on the unit, ready for
processing.

``` text
(:action unit_execute_operation
    :parameters (?unit - unit ?top - operation ?next - operation ?tray - tray)
    :precondition (and (unit_operation ?top ?unit)
                       (tray_on_unit ?tray ?unit)
                       (start ?top ?tray)
                       (todo ?top ?next ?tray)
                   )
    :effect (and (start ?next ?tray)
                 (not (todo ?top ?next ?tray))
                 (not (start ?top ?tray))
            )
    )
```

Action *unit_execute_operation* applies the operation pending on top of
the tray\'s stack. The preconditions are that the unit is able to
perform this operation, the tray is in the unit and this operation
operation is on top of the stack. The effects are that the operation is
pulled from the stack and the next operation becomes the top of the
stack.

``` text
(:action tray_completed
    :parameters (?op - operation ?tray - tray ?unit - unit)
    :precondition (and (start stop ?tray)
                       (tray_on_unit ?tray ?unit)
                  )
    :effect (and (tray_completed ?tray)
                 (unit_available ?unit)
                 (not (tray_on_unit ?tray ?unit)))
    )
```

Action *tray_completed* is a dummy action which purpose is to check that
all the scheduled operations on a tray have been done (*stop* operation
on top of the tray\'s stack). It is used to build a goal state and to
terminate the planning procedure for a given tray. Here we suppose that
an operator picks up the tray once all the operations have been done and
the unit becomes available to process another tray.

## Defining the problem

Let start by creating the problem file, e.g., `rsc_problem_easy.pddl`.
The problem we wish to define is a simple problem with one type of
pieces, a single tray, robot and conveyor; two units, a stocker storing
this tray at the initial state and a processing unit. The goal is for
the unit to perform three operations (*op10* \> *op20* \> *op30*) on the
tray.

### Objects

Hence, the types and objects are as follows:

``` text
(:objects
    unit1 stocker - unit
    conv1 - conveyor
    robot1 - robot

    tray1 - tray
    piece1 - piece

    op10 op20 op30 - operation
)
```

### Initial State

This snippet of code is the initial state:

``` text
(:init
    ;; Operation schedule
    (start op10 tray1)
    (todo op10 op20 tray1)
    (todo op20 op30 tray1)
    (todo op30 stop tray1)

    ;; Initiate pieces on tray
    (piece_on piece1 tray1)

    ;; At the beginning, tray1 is on the stocker
    (tray_on_unit tray1 stocker)

    ;; Initiate robot
    (robot_at robot1 stocker)
    (robot_available robot1)
    ;; Initiate conveyor
    (conveyor_unit conv1 unit1)
    ;; Setup unit
    (unit_accepted_piece piece1 unit1)
    (unit_accepted_piece piece1 stocker)
    (unit_operation op10 unit1)
    (unit_operation op20 unit1)
    (unit_operation op30 unit1)

    ;; Unit1 is ready
    (unit_available unit1)

    ;; Setup conveyor
    (conveyor_accepted_piece piece1 conv1)
    (conveyor_available conv1)

    ;; Setup robot
    (robot_available robot1)
)
```

### Goal Description

The goal is simply the completion of *tray1*:

``` text
(:goal
    (and (tray_completed tray1))
)
```
