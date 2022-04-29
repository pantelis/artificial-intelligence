---
title: Dynamic Programming Algorithms - Value Iteration
---

# Dynamic Programming Algorithms - Value Iteration

We already have seen that in the Gridworld example in the policy iteration section , we may not _need_ to reach the optimal state value function $v_*(s)$ to obtain an optimal policy result. The value function for the $k=3$ iteration results the same policy as the policy from a far more accurate value function (large k). 

We can therefore stop early and taking the argument to the limit, do the policy improvement step in _each_ iteration.  In this section we will look at an algorithm called value iteration that does that.  

![value-iteration-summary](images/value-iteration-summary.png)

*Summary of Value Iteration*

The basic principle behind value-iteration is the principle that underlines dynamic programming and is called the _principle of optimality_ as applied to policies. According to this principle an _optimal_ policy can be divided into two components.

1. An optimal first action $a_*$.
2. An optimal policy from the successor state $s^\prime$.

More formally, a policy $\pi(a|s)$ achieves the optimal value from state $s$, $v_\pi(s) = v_*(s)$ iff for any state $s^\prime$ reachable from $s$, $v_\pi(s^\prime)=v_*(s)$. 

Effectively this principle allows us to decompose the problem into two sub-problems with one of them being straightforward to determine and use the Bellman **optimality equation** that provides the one step backup induction at each iteration.  

$$v_*(s) = \max_a \left( \mathcal R_s^a + \gamma \sum_{s^\prime \in \mathcal S} \mathcal{P}^a_{ss^\prime} v_*(s^\prime) \right)$$

As an example if I want to move optimally towards a location in the room, I can make a optimal first step and at that point I can follow the optimal policy, that I was magically given, towards the desired final location. That optimal first step, think about making it by walking backwards from the goal. We start at the end of the problem where we know the final rewards and work backwards to all the states that connect to it in our look-ahead tree. 

![value-iteration-look-ahead-tree](images/value-iteration-look-ahead-tree.png)

*One step look-ahead tree representation of value iteration algorithm*

The "start from the end" intuition behind the equation is usually applied with no consideration as to if we are at the end or not. We just do the backup inductive step for each state.  In value iteration for synchronous backups, we start at $k=0$ from the value function $v_0(s)=0.0$ and at each iteration $k+1$ for all states $s \in \mathcal{S}$ we update the $v_{k+1}(s)$ from $v_k(s)$. As the iterations progress, the value function will converge to $v_*$.

The equation of value iteration is taken straight out of the Bellman optimality equation, **by turning the later into an update rule**. 

$$v_{k+1}(s) = \max_a \left( \mathcal R_s^a + \gamma \sum_{s^\prime \in \mathcal S} \mathcal{P}^a_{ss^\prime} v_k(s^\prime) \right) $$

The value iteration can be written in a vector form as,

$$\mathbf v_{k+1} = \max_a \left( \mathcal R^a + \gamma \mathcal P^a \mathbf v_k \right) $$

Notice that we are not building an explicit policy at every iteration and also, importantly, the intermediate value functions may _not_ correspond to a feasible policy. Before going into a more elaborate example, we can go back to the same simple world we have looked at in the policy iteration section and focus only on the state-value calculation using the formula above. 

![gridworld-value-iteration](images/gridworld-value-iteration-value-only.png)
*State values for an MDP with random policy (0.25 prob of taking any of the four available actions), $\gamma=1$, that rewards the agent with -1 at each transition except towards the goal states that are in the top left and bottom right corners*

## Value iteration example

In example world shown below.

![gridworld](images/gridworld.png)

*Gridworld to showcase the state-value calculation in Python code below. The states are numbered sequentially from top right.*

we can calculate the state-value function its the vector form - the function in this world maps the state space to the 11th dim real vector space  $v(s): \mathcal S \rightarrow \mathbb R^{11}$ aka the value function is a vector of size 11.

$$\mathbf v_{k+1} = \max_a \left( \mathcal R^a + \gamma \mathcal P^a \mathbf v_k \right) $$

{{<details "Grid world value iteration" >}}

```python
# Look at the backup tree above and the vector form Bellman equation to understand this code. 
# Have them side by side while you are reading. 
# Each of the 11 rows of the "matrix" P[s][a] has 4 tuples - one for each of the allowed actions. Each tuple / action is written in the format (probability, s') and is associated with the 3 possible next states that the agent may end up despite its intention to go to the desired state. The states are numbered sequentially from top left to bottom right. 

P = {
 0: {0: [(0.9,0),(0.1,1),(0,4)], 1: [(0.8,1),(0.1,4),(0.1,0)], 2: [(0.8,4),(0.1,1),(0.1,0)], 3: [(0.9,0),(0.1,4)]},
 1: {0: [(0.8,1),(0.1,2),(0.1,0)], 1: [(0.8,2),(0.2,1)], 2: [(0.8,1),(0.1,0),(0.1,2)], 3: [(0.8,0),(0.2,1)]},
 2: {0: [(0.8,2),(0.1,3),(0.1,1)], 1: [(0.8,3),(0.1,5),(0.1,2)], 2: [(0.8,5),(0.1,1),(0.1,3)], 3: [(0.8,1),(0.1,2),(0.1,5)]},
 3: {0: [(0.9,3),(0.1,2)], 1: [(0.9,3),(0.1,6)], 2: [(0.8,6),(0.1,2),(0.1,3)], 3: [(0.8,2),(0.1,3),(0.1,6)]},
 4: {0: [(0.8,0),(0.2,4)], 1: [(0.8,4),(0.1,7),(0.1,0)], 2: [(0.8,7),(0.2,4)], 3: [(0.8,4),(0.1,0),(0.1,7)]},
 5: {0: [(0.8,2),(0.1,6),(0.1,5)], 1: [(0.8,6),(0.1,9),(0.1,2)], 2: [(0.8,9),(0.1,5),(0.1,6)], 3: [(0.8,5),(0.1,2),(0.1,9)]},
 6: {0: [(0.8,3),(0.1,6),(0.1,5)], 1: [(0.8,6),(0.1,10),(0.1,3)], 2: [(0.8,10),(0.1,5),(0.1,6)], 3: [(0.8,5),(0.1,3),(0.1,10)]},
 7: {0: [(0.8,4),(0.1,8),(0.1,7)], 1: [(0.8,8),(0.1,7),(0.1,4)], 2: [(0.9,7),(0.1,8)], 3: [(0.9,7),(0.1,4)]},
 8: {0: [(0.8,8),(0.1,9),(0.1,7)], 1: [(0.8,9),(0.2,8)], 2: [(0.8,8),(0.1,7),(0.1,9)], 3: [(0.8,7),(0.2,8)]},
 9: {0: [(0.8,5),(0.1,10),(0.1,8)], 1: [(0.8,9),(0.1,9),(0.1,5)], 2: [(0.8,9),(0.1,8),(0.1,10)], 3: [(0.8,8),(0.1,5),(0.1,9)]},
 10: {0: [(0.8,6),(0.1,10),(0.1,9)], 1: [(0.9,10),(0.1,6)], 2: [(0.9,10),(0.1,9)], 3: [(0.8,9),(0.1,6),(0.1,10)]}
}

R = [0, 0, 0, 1, 0, 0, -100, 0, 0, 0, 0]
gamma = 0.9

States = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Actions = [0, 1, 2, 3] # [north, east, south, west]

v = [0]*11

# value iteration

for i in range(100):
    for s in States:
        # trans[1] = s'
        # trans[0] = P_ss'
        q_0 = sum(trans[0]*v[trans[1]] for trans in P[s][0])
        q_1 = sum(trans[0]*v[trans[1]] for trans in P[s][1])
        q_2 = sum(trans[0]*v[trans[1]] for trans in P[s][2])
        q_3 = sum(trans[0]*v[trans[1]] for trans in P[s][3])

        v[s] = R[s] + gamma*max(q_0, q_1, q_2, q_3)
    
print(v)

# [5.46991289990088, 6.313016781079707, 7.189835364530538, 8.668832766371658, 4.8028486314273, 3.346646443535637, -96.67286272722137, 4.161433444369266, 3.6539401768050603, 3.2220160316109103, 1.526193402980731]

# once v computed, we can calculate the optimal policy 
optPolicy = [0]*11

for s in States:       
    optPolicy[s] = np.argmax([sum([trans[0]*v[trans[1]] for trans in P[s][a]]) for a in Actions])

print(optPolicy)
# [1, 1, 1, 0, 0, 3, 3, 0, 3, 3, 2]
```

## Value Iteration in Gridworld Example

* To solve the non-linear equations for $U^{*}(s)$ we use an iterative approach.
* Steps:
	* Initialize estimates for the utilities of states with arbitrary values: $U(s) \leftarrow 0 \forall s \epsilon S$
	* Next use the iteration step below which is also called **Bellman Update**: 

$$V_{t+1}(s) \leftarrow R(s) + \gamma \underset{a}{ \max} \left[ \sum_{s^{'}} P(s^{'}| s,a) U_t(s^{'}) \right] \forall s \epsilon S$$ 

	This step is repeated and updated

* Let us apply this to the maze example.  Assume that $\gamma = 1$

![val-iter-initial](./images/val-iter-initial.png)

*Initialize value estimates to $0$*


## Value Iteration 

* Next we want to apply **Bellman Update**: 
  	$$V_{t+1}(s) \leftarrow R(s) + \gamma \max_{a} \left[\sum_{s^\prime} P(s^\prime | s,a)U_t(s^\prime) \right] \forall s \epsilon S$$
* Since we are taking $\max$ we only need to consider states whose next states have a positive utility value.
* For the remaining states, the utility is equal to the immediate reward in the first iteration.

![States to consider for value iteration](./images/val-iter-step1-states.png)



### Value Iteration (t=0)

$$ V_{t+1}(s_{33})  =  R(s_{33}) + \gamma \max_a \left[\sum_{s^{'}} P(s^{'}| s_{33},a)U(s^{'}) \right] \forall s \in S $$

$$ V_{t+1}(s_{33}) =  -0.04 + \max_a \left[ \sum_{s'}  P(s'| s_{33},\uparrow) U_t(s'), \sum_{s'}  P(s'| s_{33},\downarrow)U_t(s'), \sum_{s'}  P(s'| s_{33},\rightarrow) U_t(s'),  \sum_{s'}  P(s'| s_{33}, \leftarrow)U_t(s')  \right]$$

$$V_{t+1}(s_{33})  =  -0.04 + \sum_{s^{'}}  P(s^{'}| s_{33},\rightarrow) U_t(s^\prime) $$

$$V_{t+1}(s_{33}) = -0.04 + P(s_{43}|s_{33},\rightarrow)U(s_{43})+P(s_{33}|s_{33},\rightarrow)U(s_{33})+P(s_{32}|s_{33},\rightarrow)U_t(s_{32}) $$

$$V_{t+1}(s_{33}) =   -0.04 + 0.8 \times 1 + 0.1 \times 0 + 0.1 \times 0 = 0.76 $$



### Value Iteration (t=1)

![val-iter-step2](./images/val-iter-step2-initial.png)

*(A) Initial utility estimates for iteration 2. (B) States with next state positive utility*

$$V_{t+1}(s_{33}) =   -0.04 + P(s_{43}|s_{33},\rightarrow)U_t(s_{43})+P(s_{33}|s_{33},\rightarrow)U_t(s_{33}) +P(s_{32}|s_{33},\rightarrow)U_t(s_{32}) $$

$$V_{t+1}(s_{33}) = -0.04 + 0.8 \times 1 + 0.1 \times 0.76 + 0.1 \times 0 = 0.836$$

$$V_{t+1}(s_{23}) =  -0.04 + P(s_{33}|s_{23},\rightarrow)U_t(s_{23})+P(s_{23}|s_{23},\rightarrow)U_t(s_{23}) = -0.04 + 0.8 \times 0.76 = 0.568$$

$$V_{t+1}(s_{32}) =  -0.04 + P(s_{33}|s_{32},\uparrow)U_t(s_{33})+P(s_{42}|s_{32},\uparrow)U_t(s_{42}) +P(s_{32}|s_{32},\uparrow)U_t(s_{32})$$
$$V_{t+1}(s_{32}) = -0.04 + 0.8 \times 0.76 + 0.1 \times -1 + 0.1 \times 0= 0.468$$



### Value Iteration (t=2)


![val-iter-step3](./images/val-iter-step3-initial.png)

*(A)Initial utility estimates for iteration 3. (B) States with next state positive utility*

* Information propagates outward from terminal states
and eventually all states have correct value estimates 
* Notice that $s_{32}$ has a lower utility compared to $s_{23}$ due to the red oval state with negative reward next to $s_{32}$

![Optimal Policy and Utilities for Maze](./images/policy-utility.png)

### Value Iteration - Convergence

* Rate of convergence depends on the maximum reward value and more importantly on the discount factor $\gamma$. 
* The policy that we get from coarse estimates is close to the optimal policy long before $U$ has converged.
* This means that after a reasonable number of iterations, we could use: 
  $$\pi(s) = \argmax_a \left[ \sum_{s^{'}} P(s^{'}| s,a)V_{est}(s^{'}) \right]$$
* Note that this is a form of **greedy** policy.
  
![value-iter-convergence](./images/value-iter-converge.PNG)

*Convergence of utility for the maze problem (Norvig chap 17)*

* For the maze problem, convergence is reached within 5 to 10  iterations

