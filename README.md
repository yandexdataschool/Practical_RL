# Practical_RL
A course on reinforcement learning in the wild.
Taught on-campus at [HSE](https://cs.hse.ru)(russian) and maintained to be friendly to online students (both english and russian).


#### Manifesto:
* __Optimize for the curious.__ For all the materials that aren’t covered in detail there are links to more information and related materials (D.Silver/Sutton/blogs/whatever). Assignments will have bonus sections if you want to dig deeper.
* __Practicality first.__ Everything essential to solving reinforcement learning problems is worth mentioning. We won't shun away from covering tricks and heuristics. For every major idea there should be a lab that makes you to “feel” it on a practical problem.
* __Git-course.__ Know a way to make the course better? Noticed a typo in a formula? Found a useful link? Made the code more readable? Made a version for alternative framework? You're awesome! [Pull-request](https://help.github.com/articles/about-pull-requests/) it!

# Course info
* Lecture slides are [here](https://yadi.sk/d/loPpY45J3EAYfU).
* Telegram chat room for YSDA & HSE students is [here](https://t.me/rlspring18)
* Online student __[survival guide](https://github.com/yandexdataschool/Practical_RL/wiki/Online-student's-survival-guide)__
* Installing the libraries - [guide and issues thread](https://github.com/yandexdataschool/Practical_RL/issues/1)
* Magical button that launches you into course environment: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/yandexdataschool/Practical_RL/master)
* Anonymous [feedback form](https://docs.google.com/forms/d/e/1FAIpQLSdurWw97Sm9xCyYwC8g3iB5EibITnoPJW2IkOVQYE_kcXPh6Q/viewform) for everything that didn't go through e-mail.
* [About the course](https://github.com/yandexdataschool/Practical_RL/wiki/Practical-RL)
* A large list of RL materials - [awesome rl](https://github.com/aikorea/awesome-rl)

# HSE and YSDA students
**This section is stricly for on-campus HSE and YSDA students**
* Anytask course is http://anytask.org/course/272
* **HSE** invite is `reHroOk`
* **YSDA** invite is TBA

# RL reading group
* __Reading group [chat room](https://t.me/theoreticalrl)__
* Everyone who wants to attend RL reading group ping Pavel Shvechikov - `1xolodec@gmail.com`


# Announcements
* 2017.12.29 - HSE track for fall'2017 is offically over. Next is spring'18 @ HSE & YSDA.
* 2017.10.02 - week4 homework is yet to be published, week3 and week4 deadlines are shifted one week into the future.
* 2017.09.24 - Week3 homework published, we're sorry for the delay
* 2017.09.13 - Gym website seems to have gone down indefinitely. Therefore,
 - week0 homework: Bonus I counts as 2 points if you beat mean reward +5.0 for Taxi-v1 or +0.95 on frozenlake8x8
 - week1 homework: Instead of 1 point for task 2.2 and 3 points for 2.3 you get 4 points for 2.3. 
 - Since you can't submit, just ignore and instructions to do so. We'll push them this weekend to avoid merge conflicts for students.
* 2017.09.04 - first class just happened. Anytask submission form TBA

# Syllabus

The syllabus is approximate: the lectures may occur in a slightly different order and some topics may end up taking two weeks.

* [__week0__](https://github.com/yandexdataschool/Practical_RL/tree/master/week0_intro) Welcome to Reinforcement Learning
  * Lecture: RL problems around us. Decision processes. Basic genetic algorithms
  * Seminar: Welcome into openai gym, basic genetic algorithms
  * Homework description - see week0/README.md

* [__week1__](https://github.com/yandexdataschool/Practical_RL/tree/master/week1_blackbox) RL as blackbox optimization
  * Lecture: Recap on genetic algorithms; Evolutionary strategies. Stochastic optimization, Crossentropy method. Parameter space search vs action space search.
  * Seminar: Tabular CEM for Taxi-v0, deep CEM for box2d environments.
  * Homework description - see week1/README.md

* [__week2__](https://github.com/yandexdataschool/Practical_RL/tree/master/week2_value_based) Value-based methods
  * Lecture: Discounted reward MDP. Value-based approach. Value iteration. Policy iteration. Discounted reward fails.
  * Seminar: Value iteration.

* [__week3__](https://github.com/yandexdataschool/Practical_RL/tree/master/week3_model_free) Model-free reinforcement learning
  * Lecture: Q-learning. SARSA. Off-policy Vs on-policy algorithms. N-step algorithms. TD(Lambda).
  * Seminar: Qlearning Vs SARSA Vs Expected Value SARSA
  * HSE Homework deadline: _23.59 13.10.17
  
* [__week4_recap__](https://github.com/yandexdataschool/Practical_RL/tree/master/week4_%5Brecap%5D_deep_learning) - deep learning recap 
  * Lecture: Deep learning 101
  * Seminar: Simple image classification with convnets
  * HSE Homework deadline: _23.59 13.10.17

* [__week4__](https://github.com/yandexdataschool/Practical_RL/tree/master/week4_approx_rl) Approximate reinforcement learning
  * Lecture: Infinite/continuous state space. Value function approximation. Convergence conditions. Multiple agents trick; experience replay, target networks, double/dueling/bootstrap DQN, etc.
  * Seminar:  Approximate Q-learning with experience replay. (CartPole, Atari)
  * HSE Homework deadline: _23.59 20.10.17

* [__week5__](https://github.com/yandexdataschool/Practical_RL/tree/master/week5_explore) Exploration in reinforcement learning
  * Lecture: Contextual bandits. Thompson Sampling, UCB, bayesian UCB. Exploration in model-based RL, MCTS. "Deep" heuristics for exploration.
  * Seminar: bayesian exploration for contextual bandits. UCB for MCTS.

* [__week6__](https://github.com/yandexdataschool/Practical_RL/tree/master/week6_policy_based) Policy gradient methods I
  * Lecture: Motivation for policy-based, policy gradient, logderivative trick, REINFORCE/crossentropy method, variance reduction(baseline), advantage actor-critic (incl. GAE)
  * Seminar: REINFORCE, advantage actor-critic

* [__week7_recap__](https://github.com/yandexdataschool/Practical_RL/tree/master/week7_%5Brecap%5D_rnn) Recurrent neural networks recap
  * Lecture: Problems with sequential data. Recurrent neural netowks. Backprop through time. Vanishing & exploding gradients. LSTM, GRU. Gradient clipping
  * Seminar: character-level RNN language model

* [__week7__](https://github.com/yandexdataschool/Practical_RL/tree/master/week7_pomdp) Partially observable MDPs
  * Lecture: POMDP intro. POMDP learning (agents with memory). POMDP planning (POMCP, etc)
  * Seminar: Deep kung-fu & doom with recurrent A3C and DRQN
    
* [__week8__](https://github.com/yandexdataschool/Practical_RL/tree/master/week8_scst) Applications II
  * Lecture: Reinforcement Learning as a general way to optimize non-differentiable loss. G2P, machine translation, conversation models, image captioning, discrete GANs. Self-critical sequence training.
  * Seminar: Simple neural machine translation with self-critical sequence training

* [__week9__](https://github.com/yandexdataschool/Practical_RL/tree/master/week9_policy_II) Policy gradient methods II
  * Lecture: Trust region policy optimization. NPO/PPO. Deterministic policy gradient. DDPG. Bonus: DPG for discrete action spaces.
  * Seminar: Approximate TRPO for simple robotic tasks.

* [Some after-course bonus materials](https://github.com/yandexdataschool/Practical_RL/tree/master/yet_another_week)


# Course staff
Course materials and teaching by
- [Fedor Ratnikov](https://github.com/justheuristic/) - lectures, seminars, hw checkups
- [Oleg Vasilev](https://github.com/Omrigan) - seminars, hw checkups, technical support
- [Pavel Shvechikov](https://github.com/bestxolodec) - lectures, seminars, hw checkups, reading group
- [Alexander Fritsler](https://github.com/Fritz449) - lectures, seminars, hw checkups

# Contributions
* Using pictures from [Berkeley AI course](http://ai.berkeley.edu/home.html)
* Massively refering to [CS294](http://rll.berkeley.edu/deeprlcourse/)
* Sevaral tensorflow assignments by [Scitator](https://github.com/Scitator)
* A lot of fixes from [arogozhnikov](https://github.com/arogozhnikov)
* Other awesome people: see github contributors


# fall17 changes
* Better support for tensorflow & pytorch
* Our notation is now compatible with Sutton's
* Reworked & reballanced some assignments
* Added more practice on model-based RL
