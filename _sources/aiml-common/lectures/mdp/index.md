# Markov Decision Processes


Many of the algorithms presented here like policy and value iteration have been developed in older repos such as [this](https://github.com/rlcode/reinforcement-learning) and [this](https://github.com/dennybritz/reinforcement-learning). This site is being migrated to be compatible with Farama and their [Gymnasium](https://gymnasium.farama.org/) tooling. See [Farama.org](https://farama.org/projects) for additional information.

We started looking at different agent behavior architectures starting from the planning agents where the _model_ of the environment is known and with _no interaction_ with it, the agent improves its policy, using this model as well as problem solving and logical reasoning skills. 

We now look at agents that can plan by:

1. _Interacting_ with the environment by receiving _reward_ signals from it during each interaction. 
2. Knowing the model (dynamics) of the environment, they have an internal _objective_ function that they try to optimize based on the _experience_ they accumulate.

The problem as will see, will be described via a set of four equations called Bellman expectation and Bellman optimality equations that connect the values (utility) with each state or action with the policy (strategy) of the agent. These equations can be solved by Dynamic Programming algorithms to produce the optimal policy  that the agent must adopt. 

Computationally we will go through approaches that solve the MDP as efficiently as possible - namely, the value and policy iteration algorithms.

![solving-mpd](images/solving-mdp.png)

*[Solving MDP Problems](https://raw.githubusercontent.com/pantelis/aiml-common/25b7bb61d967ac418eeffb1f87ee771386da590a/lectures/mdp/images/solving-mdp.png) - click this link to display a larger image*


Apart from the notes here that are largely based on [David Silver's (Deep Mind) course material](https://www.davidsilver.uk/teaching/) and [video lectures](https://www.youtube.com/watch?v=2pWv7GOvuf0&list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ), you can consult these additional resources: 

 * [in the Richard Sutton's book](http://incompleteideas.net/book/RLbook2020.pdf) - David Silver's slides and video lectures are based on this book. The code in Python of the book is [here](https://github.com/ShangtongZhang/reinforcement-learning-an-introduction)

* [in the suggested book](https://www.amazon.com/Deep-Reinforcement-Learning-Python-Hands-dp-0135172381/dp/0135172381/ref=mt_paperback?_encoding=UTF8&me=&qid=) written by Google researchers as well as on [OpenAI's website](https://openai.com/resources/). The chapters we covered is 1-4. 

* You may also want to watch Andrew Ng's, [2018 version of his ML class](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU) that includes MDP and RL lectures.

