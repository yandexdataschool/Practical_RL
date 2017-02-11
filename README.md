# Practical_RL
A course on reinforcement learning in the wild. 
Taught on-campus in HSE and YSDA (russian) and maintained to be friendly to online students (english or russian).

Manifesto:
* __Optimize for the curious.__ For all the materials that aren’t covered in detail there will be links to more information and related materials (D.Silver/Sutton/blogs/whatever). Assignments will have bonus sections if you want to dig deeper.
* __Practicality first.__ Everything essential to solving reinforcement learning problems is worth mentioning. We won't shun away from covering tricks and heuristics. For every major idea there should be a lab that allows to “feel” it on a practical problem.
* __Git-course.__ Know a way to make course better? Noticed a typo in formula? Made the code more readable? Made a version for alternative framework? You're awesome! [Pull-request](https://help.github.com/articles/about-pull-requests/) it!


# Coordinates
* __HSE__ classes are on mondays at 18-10 in Room 505
* __YSDA__ classes are on thursdays at 18-00 in princeton
* E-mail for submitting homeworks and stuff: __practicalrl17@gmail.com__ (anytask will follow soon)
* Telegram chat room: https://telegram.me/practicalrl
* Magic button that creates VM: [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/yandexdataschool/practical_rl)
* [About the course](https://github.com/yandexdataschool/Practical_RL/wiki/Practical-RL)
* [Grading for YSDA and HSE](https://github.com/yandexdataschool/Practical_RL/wiki/%D0%9E%D1%82%D1%87%D1%91%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C,-%D0%B4%D0%BE%D0%BC%D0%B0%D1%88%D0%BA%D0%B8,-%D0%B4%D0%B5%D0%B4%D0%BB%D0%B0%D0%B9%D0%BD%D1%8B-(grading))
* _Grading table - coming soon_


# Announcements
* 11.02.17 - week2 success thresholds are now easier: get >+50 for LunarLander or >-180 for MountainCar. Solving env will yield bonus points.
* 10.02.17 - from now on, we'll formally describe homework and add useful links via ./week*/README.md files. [Example.](https://github.com/yandexdataschool/Practical_RL/blob/master/week0/README.md)
* 9.02.17 - YSDA track started
* 7.02.17 - HWs checked up
* 6.02.17 - week2 uploaded
* 27.01.17 - merged fix by _omtcyfz_, thanks!
* 27.01.17 - added course mail for homework submission: __practicalrl17@gmail.com__
* 23.01.17 - first class happened
* 23.01.17 - created repo

# Syllabus
* __week0__ Welcome to the MDP
 * Lecture: RL problems around us. Markov decision process. Simple solutions through combinatoric optimization.
 * Seminar: Frozenlake with genetic algorithms
    * Homework description - [./week0/README.md](https://github.com/yandexdataschool/Practical_RL/blob/master/week0/README.md)
    * HSE Homework deadline: _23.59 1.02.17_
    * YSDA Homework deadline: _23.59 19.02.17_
* __week1__ Monte-carlo methods
 * Lecture: Crossentropy method in general and for RL. Extension to continuous state & action space. Limitations.
 * Seminar: Tabular CEM for Taxi-v0, deep CEM for box2d environments.
    * HSE homework deadline: _23.59 8.02.17_
* __week2__ Temporal Difference
 * Lecture: Discounted reward MDP. Value iteration. Q-learning. Temporal difference Vs Monte-Carlo.
 * Seminar: Tabular q-learning 
    * Homework description - see [./week2/README.md](https://github.com/yandexdataschool/Practical_RL/blob/master/week2/README.md)
    * HSE homework deadline: _23.59 8.02.17_

## Future lectures:
* __week3__ Value-based algorithms
 * Lecture: SARSA. Off-policy Vs on-policy algorithms. N-step algorithms. Eligibility traces.
 * Seminar: Qlearning Vs SARSA Vs expected value sarsa in the wild

*somewhere here* introduction to theano

* __week4__ Approximate reinforcement learning
 * Lecture: Infinite/continuous state space. Value function approximation. Convergence conditions. Multiple agents trick.
 * Seminar:  Approximate Q-learning. (CartPole, MountainCar, Breakout)

* __week i+1__ Deep reinforcement learning 
 * Lecture: Deep Q-learning/sarsa/whatever. Heuristics & motivation behind them: experience replay, target networks, double/dueling/bootstrap DQN, etc.
 * Seminar: Playing atari with deep reinforcement learning. Experience replay. (classwork = doombasic)
 
* __week i+1__ Policy-based methods
 * Lecture: Motivation for policy-based, policy gradient, logderivative trick, REINFORCE/crossentropy method, variance theorem(advantage), advantage actor-critic (incl.n-step advantage), off-policy actor-critic (off-PAC), natural gradients(briefly), continuous action space(teaser). 
 * Seminar: a2c Vs qlearning for MountainCar/Doom, entropy regularization & tricks.
 
* __week i+1__ Trust Region Policy Optimization.
 * Lecture: Trust region policy optimization in detail.
 * approximate TRPO vs approximate Q-learning for gym box2d envs (robotics-themed)

* __week i+1__ Large/Continuous action space. Case study: recsys.
 * Lecture: Continuous action space MDPs. Model-based approach (NAF). Actor-critic approach (dpg, svg). Trust Region Policy Optimization. Large discrete action space problem. Action embedding.
 * Seminar: Classic Control and BipedalWalker with ddpg Vs qNAF. https://gym.openai.com/envs/BipedalWalker-v2 .

*somewhere here RNN crash-course*

* __week i+1__ Partially observable MDPs
 * Lecture: POMDP intro. Model-based solvers. RNN solvers. RNN tricks: attention, problems with normalization methods, pre-training.
 * Seminar: Deep kung-fu with recurrent A2C vs feedforward A2C

* __week i+1__ Advanced exploration methods: intrinsic motivation.
 * Lecture: Augmented rewards. Heuristics (UNREAL,density-based models), formal approach: information maximizing exploration. Model-based tricks(also refer mcts).
 * Seminar: Vime vs epsilon-greedy for Go9x9 (bonus 19x19)

* __week i+1__ Advanced exploration methods: probablistic approach.
 * Lecture: Improved exploration methods (quantile-based, etc.). Bayesian approach. Case study: Contextual bandits for RTB. 
 * Seminar: Bandits
 
* __week i+1__ Case studies I
 * Lecture: Reinforcement Learning as a general way to optimize non-differentiable loss. KL(p||q) vs KL(q||p). Case study: machine ranslation, speech synthesis, conversation models.
 * Seminar: Optimizing Levenstein for word transcription

* __week i+1__ Hierarchical MDP
 * Lecture: MDP Vs real world. Sparse and delayed rewards. When Q-learning fails. Hierarchical MDP. Hierarchy as temporal abstraction. MDP with symbolic reasoning.
 * Seminar: Hierarchical RL for atari games with rare rewards (starting from pre-trained DQN)
 
* __week i+1__ Case studies II
 * Lecture: Direct policy optimization: finance.  Inverse Reinforcement Learning: personalized medial treatment, robotics.
 * Seminar: Portfolio optimization as POMDP.
 
 





 

 
 
