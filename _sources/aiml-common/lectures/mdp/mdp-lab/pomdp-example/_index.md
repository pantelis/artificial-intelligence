
# POMDP Example

## Partially Observable MDPs

* We considered "uncertainty" in the action outcome previously. Now, the environment is partially observable. 
* We now deal with a **belief** state which is the agent's current belief about the state that it is in. 

![POMDP](images/pomdp.png)



### POMDP Parameters

* The MDP parameters we listed previously continue to hold for POMDP:
    * a set of states $S$. State at time $t$ is $s_t$
    * actions  $A$. Action at time $t$ is $a_t$.
    * transition model describing outcome of each action in each state $P( s_{t+1} | s_t, a_t)$ 
    * reward function $r_t=R(s_t)$ 
* Additional POMDP parameters:
	* initial belief of state $s$: $b(s)=P(s)$
	* if $b(s)$ was the previous belief state, agent does an action $a$ then perceives evidence $e$ then the new belief state is given by: 
  	$$b^\prime(s^\prime) = P(s^\prime | e,a,b)$$
	* observation probability: $P(e|s^{'},a)$
* The belief state $b$ also satisfies the Markov property




### POMDP versus other models
 

![](images/pomdp-versus-others.PNG)
[source](https://www.cs.cmu.edu/~ggordon/780-fall07/lectures/POMDP_lecture.pdf)




### POMDP Example

![Tiger Problem](./images/tiger-1.png)

* We want to find the optimal policy...i.e. what is the best action the person should take?




### POMDP Example - Transition Probabilities

* The "Listen" action does not change the tiger location

| $P(s^{'}$\| $s, Listen)$ | TL  | TR  |
|  | --- | --- |
| TL                       | 1.0 | 0   |
| TR                       | 0   | 1.0 |

* The "open-left" or "open-right" action resets the problem in which case the tiger can be on the left or right with equal probability

| $P(s^{'}$\| $s, open-right)$ | TL  | TR  |
|  | --- | --- |
| TL                           | 0.5 | 0   |
| TR                           | 0   | 0.5 |

| $P(s^{'}$ \| $s, open-left)$ | TL  | TR  |
|  | --- | --- |
| TL                           | 0.5 | 0   |
| TR                           | 0   | 0.5 |




### POMDP Example - Observation Probabilities

* Only the "Listen" action is informative 

| $P(e$ \| $s, Listen)$ | TL   | TR   |
| - |  |  |
| TL                    | 0.85 | 0.15 |
| TR                    | 0.15 | 0.85 |

* Any observation without the "listen" action is uninformative

| $P(e$ \| $s, open-right)$ | TL  | TR  |
| - | --- | --- |
| TL                        | 0.5 | 0   |
| TR                        | 0   | 0.5 |

| $P(e$ \| $s, open-left)$ | TL  | TR  |
|  | --- | --- |
| TL                       | 0.5 | 0   |
| TR                       | 0   | 0.5 |



### POMDP Example - Immediate Rewards 

* "Listen" action results in a small penalty 

| $R(s)$ \| $Listen$ |     |
| -- | --- |
| TL                 | -1  |
| TR                 | -1  |

* Opening the wrong door results in large penalty 

| $R(s)$ \| $open-left$ |      |
| - |  |
| TL                    | -100 |
| TR                    | +10  |

| $R(s)$ \| $open-right$ |      |
| -- |  |
| TL                     | +10  |
| TR                     | -100 |

#### Belief State Space

* b(left) versus b(right)



### POMDP as a Belief-state MDP

* Solving a POMDP on a physical state space reduces to solving an MDP on the corresponding belief-state space
* The resulting MDP has a **high dimensional continuous**(typically in real world problems) belief state space  which makes it more difficult to solve
* Approach to solving this:
	* Each policy is a plan conditioned on belief $b$ 
	* Each conditional plan is a hyperplane
	* Optimal policy then is the conditional plan with the highest expected utility
	* The optimal action depends only on the agents's current belief state. That is, the optimal policy $\pi^{*}(b)$ maps from belief states to actions.
	* The decision cycle in this case would comprise of the following $3$ steps:
		* Given the current belief state, execute the action $a=\pi^{*}(b)$
		* Receive percept $e$
		* Set the current belief state to $b^{'}(s^{'})$ given by 
  $$b^{'}(s^{'}) = \alpha P(e|s^{'}) \sum_{s} P(s^{'}|s,a)b(s)$$



### Solving POMDP

* The value iteration approach for POMDP looks something like this:
  
$$V_{t+1}(b) \leftarrow \max_{a}[ \sum_s b(s)R(s,a) +\gamma \sum_eP(e|b,a)U(\tau(e,b,a)]$$ 

where $\tau(e,b,a)$ is the transition function for the belief state.

* This is in general very hard to solve as it is a continuous space MDP
* Instead one resorts to exploiting special properties in terms of 
	* Policy Tree
	* Piecewise linear and convex property of the value function



### Solving the tiger problem - 1-step horizon

* Suppose that you were told the $b(left) = \rho = 0.5$ i.e. tiger could be either on the left or right with equal probability.
* **You are told that you have only 1 chance to take an action, what would that be and why?**

![Tiger Problem](images/tiger-1.png)
*The Tiger Problem*



### Solving the tiger problem - 1-step horizon

* Determine expected utility for each possible action for different belief distributions

| action | expected utility for  $\rho=0.5$        | expected utility for $\rho=0.4$         |
| -- | --- | --- |
| LEFT   | $0.5 \times -100 + 0.5 \times 10 = -45$ | $0.4 \times -100 + 0.6 \times 10 = -36$ |
| RIGHT  | $-45$                                   | $0.6 \times -100 + 0.4 \times 10 = -56$ |
| LISTEN | $-1$                                    | $-1$                                    |

* For the above cases, we would pick "listen" as it has the highest expected utility 
* How low should $\rho$ go so that the utility of picking "left" is better than picking "listen"
	* Find $x \ni \rho \times -100 + (1-\rho) \times 10 \lt -1$
	* Solving we get $\rho \lt 0.1$. This means that if that if $0 \lt b(left) \lt 0.1$ then choose "left. This range is called the **belief interval** for which we would select "left".
	* Based on the above analysis, the optimal 1 step policy is as below 

![Optimal policy for 1-step horrizon](./images/tiger-1step.png)



### Solving the tiger problem - t-step horrizon

* The value function of POMDPs can be represented as max of linear segments

![(A) Utility as function of plan (B) Value function](./images/tiger-1step-value.png)

* How about if you were given $2$ chances? i.e. $t=2$ and $b(left)=0.5$.
	* It turns out that the optimal policy for the first step is to always "listen". 
	* The reason is that if you opened the door on the first step
		* the tiger would be randomly placed behind one of the doors and the agent's belief state would be reset to $(0.5, 0.5)$. 
		* The agent would be left with no information about the tiger's location and with one action remaining.



### Solving the tiger problem - t-step horrizon

![Optimal policy tree for $2$-step horrizon](./images/tiger-2step.png)
![Convergence of policies](./images/tiger-t-step.PNG)

---