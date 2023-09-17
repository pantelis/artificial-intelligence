# The SARSA Algorithm 

As we discussed in the model-free control section, SARSA implements a $Q(s,a)$ value-based GPI. Its name is attributed to the fact that we need to know the State-Action-Reward-State-Action before performing an update. The tree for SARSA is shown below:

![sarsa-update-tree](images/sarsa-update-tree.png)

*SARSA action-value backup update tree. The name SARSA is written as you read from the top to the bottom of the tree :)*

There are two concepts that we need to grasp:

1. The first is a technique for learning the Q-function via TD-learning that we have seen in the prediction section. 
2. The second is a method for evolving the policy using the learned Q-function. 

Using the tree and following the value estimate of _temporal difference (TD) learning_, we can write the value update equation as:

$$Q(S,A) = Q(S,A) + \alpha (R + \gamma Q(S^\prime, A^\prime)-Q(S,A))$$

Effectively the equation above updates the Q function by $\alpha$ times the direction of the TD-error. What SARSA does is basically the policy iteration diagram we have seen in the control above but with a twist. Instead of trying to evaluate the policy all the way using the DP, or over an episode using MC,  SARSA does policy improvement **over each time step** significantly increasing the iteration rate - this is figuratively shown below:

![sarsa-policy-iteration](images/sarsa-policy-iteration.png)

*SARSA on-policy control*

The idea is to increase the frequency of the so called $\epsilon$-Greedy policy improvement step where we select with probability $\epsilon$ a random action instead of the action that maximizes the $Q(s,a)$ function (greedy). We do so, in order to "hit" new states that we havent seen before (exploration). 

The SARSA algorithm is summarized below:

![sarsa-on-policy-control-algorithm](images/sarsa-on-policy-control-algorithm.png)
*SARSA algorithm for on-policy control*

$Q(s,a)$ in practice is a table (matrix) stored in memory. Every step that we take an action we flip a "bent coin" and if "heads" comes up we take the maximum of the $Q(s,a)$ values and this will be the policy improvement for the subsequent step. If it comes up as "tails" we just pick a random action and update the policy accordingly.
