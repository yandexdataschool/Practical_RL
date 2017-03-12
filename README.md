# Practical_RL
A course on reinforcement learning in the wild.
Taught on-campus in [HSE](https://cs.hse.ru) and [Yandex SDA](https://yandexdataschool.com) (russian) and maintained to be friendly to online students (both english and russian).

#### Manifesto:
* __Optimize for the curious.__ For all the materials that aren’t covered in detail there are links to more information and related materials (D.Silver/Sutton/blogs/whatever). Assignments will have bonus sections if you want to dig deeper.
* __Practicality first.__ Everything essential to solving reinforcement learning problems is worth mentioning. We won't shun away from covering tricks and heuristics. For every major idea there should be a lab that allows to “feel” it on a practical problem.
* __Git-course.__ Know a way to make the course better? Noticed a typo in a formula? Found a useful link? Made the code more readable? Made a version for alternative framework? You're awesome! [Pull-request](https://help.github.com/articles/about-pull-requests/) it!

# Coordinates and useful links
* __HSE__ classes are on mondays at 18-10 in Room 505
* __YSDA__ classes are on thursdays at 18-00 in "Princeton" classroom
* Lecture slides are [here](https://yadi.sk/d/loPpY45J3EAYfU).
* Online student __[survival guide](https://github.com/yandexdataschool/Practical_RL/wiki/Online-student's-survival-guide)__
* Installing the libraries - [guide and issues thread](https://github.com/yandexdataschool/Practical_RL/issues/1)
* Magical button that creates VM: [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/yandexdataschool/practical_rl) (may be down time to time. If it won't load for 2-3 minutes, it's down)
* Telegram __[chat room](https://telegram.me/practicalrl)__ __(russian)__
* Gitter __[chat room](https://gitter.im/yandexdataschool/Practical_RL)__ __(english)__
* __How to submit homeworks[HSE and YSDA only]:__ [anytask instructions and grading rules](https://github.com/yandexdataschool/Practical_RL/wiki/Homeworks-and-grading-(HSE-and-YSDA))
* E-mail for everything else : __practicalrl17@gmail.com__ (please don't submit homeworks via e-mail)
* Anonymous [feedback form](https://docs.google.com/forms/d/e/1FAIpQLSdurWw97Sm9xCyYwC8g3iB5EibITnoPJW2IkOVQYE_kcXPh6Q/viewform) for everything that didn't go through e-mail.
* [About the course](https://github.com/yandexdataschool/Practical_RL/wiki/Practical-RL)


# Announcements
* 10.03.17 - (ysda/hse students) __important__ please consider [Course Projects](https://github.com/yandexdataschool/Practical_RL/wiki/Course-projects) as an alternative way of completing the course.
* 8.03.17 - YSDA deadlines announced for weeks 3 and 3.5, sry for only doing this now.
* 01.03.17 - YSDA deadline on week2 homework moved to 08.03.17
* 28.02.17 - (HSE) homework 4 published
* 24.02.17 - Dependencies updated ([same url](https://github.com/yandexdataschool/Practical_RL/issues/1)). Please install theano/lasagne/agentnet until week4 or make sure you're familiar enough with your deep learning framework of choice.
* 23.02.17 - YSDA homework 2 can be found [here](https://github.com/yandexdataschool/Practical_RL/tree/master/week2). If you're from HSE you can opt to submit either old or new whichever you prefer.
* 17.02.17 - warning! we force-pushed into the repository. Please back-up your github files before you pull!
* 16.02.17 - Lecture slides are now available through urls in README files for each week like [this](https://github.com/yandexdataschool/Practical_RL/tree/master/week1#materialshttps://github.com/yandexdataschool/Practical_RL/tree/master/week1#materials). You can also find full archive [here](https://yadi.sk/d/loPpY45J3EAYfU).

<details><summary>Previous announcements</summary>
<p><!-- trick from http://stackoverflow.com/questions/32814161/how-to-make-spoiler-text-in-github-wiki-pages -->
* 30.03.17 - YSDA deadlines announced for HW 4
* 16.02.17 - HSE homework 3 added
* 14.02.17 - HSE deadlines for weeks 1-2 extended!
* 14.02.17 - anytask invites moved [here](https://github.com/yandexdataschool/Practical_RL/wiki/Homeworks-and-grading-(HSE-and-YSDA))
* 14.02.17 - if you're from HSE track and we didn't reply to your week0 homework submission, raise panic!
* 11.02.17 - week2 success thresholds are now easier: get >+50 for LunarLander or >-180 for MountainCar. Solving env will yield bonus points.
* 13.02.17 - Added invites for anytask.org
* 10.02.17 - from now on, we'll formally describe homework and add useful links via ./week*/README.md files. [Example.](https://github.com/yandexdataschool/Practical_RL/blob/master/week0/README.md)
* 9.02.17 - YSDA track started
* 7.02.17 - HWs checked up
* 6.02.17 - week2 uploaded
* 27.01.17 - merged fix by _omtcyfz_, thanks!
* 27.01.17 - added course mail for homework submission: __practicalrl17@gmail.com__
* 23.01.17 - first class happened
* 23.01.17 - created repo
</p></details>


# Syllabus
* __week0__ Welcome to the MDP
 * Lecture: RL problems around us. Markov decision process. Simple solutions through combinatoric optimization.
 * Seminar: Frozenlake with genetic algorithms
 * Homework description - [week0/README.md](https://github.com/yandexdataschool/Practical_RL/blob/master/week0/README.md)
    * HSE Homework deadline: _23.59 1.02.17_
    * YSDA Homework deadline: _23.59 19.02.17_
* __week1__ Crossentropy method and monte-carlo algorithms
 * Lecture: Crossentropy method in general and for RL. Extension to continuous state & action space. Limitations.
 * Seminar: Tabular CEM for Taxi-v0, deep CEM for box2d environments.
 * Homework description - [week1/README.md](https://github.com/yandexdataschool/Practical_RL/blob/master/week1/README.md)
    * HSE homework deadline: _23.59 15.02.17_
    * YSDA homework deadline: _23.59 26.02.17_
* __week2__ Temporal Difference
 * Lecture: Discounted reward MDP. Value iteration. Q-learning. Temporal difference Vs Monte-Carlo.
 * Seminar: Tabular q-learning
 * Homework description - [week2/README.md](https://github.com/yandexdataschool/Practical_RL/blob/master/week2/README.md)
    * HSE homework deadline: _23.59 15.02.17_
    * YSDA homework deadline: _23.59 8.03.17_

* __week3__ Value-based algorithms
 * Lecture: SARSA. Off-policy Vs on-policy algorithms. N-step algorithms. Eligibility traces.
 * Seminar: Qlearning Vs SARSA Vs expected value sarsa in the wild
 * Homework description - [week3/README.md](https://github.com/yandexdataschool/Practical_RL/blob/master/week3/README.md)
    * HSE homework deadline _23.59 22.02.17_
    * YSDA homework deadline: _23.59 14.03.17_

* __week3.5__ Deep learning recap
 * Lecture: deep learning, convolutional nets, batchnorm, dropout, data augmentation and all that stuff.
 * Seminar: Theano/Lasagne on mnist, simple deep q-learning with CartPole (TF version contrib is welcome)
 * Homework - convnets on MNIST or simple deep q-learning - [week3.5/README.md](https://github.com/yandexdataschool/Practical_RL/blob/master/week3.5/README.md)
    * HSE homework deadline _23.59 1.03.17_
    * YSDA homework deadline: _23.59 14.03.17_ (5 pts)

* __week4__ Approximate reinforcement learning
 * Lecture: Infinite/continuous state space. Value function approximation. Convergence conditions. Multiple agents trick.
 * Seminar:  Approximate Q-learning with experience replay. (CartPole, Acrobot, Doom)
 * Homework - convnets on MNIST or simple deep q-learning - [week4/README.md](https://github.com/yandexdataschool/Practical_RL/blob/master/week4/README.md)
    * HSE homework deadline _23.59 8.03.17_
    * YSDA homework deadline _23.59 19.03.17_

* __week5__ Deep reinforcement learning
 * Lecture: Deep Q-learning/sarsa/whatever. Heuristics & motivation behind them: experience replay, target networks, double/dueling/bootstrap DQN, etc.
 * Seminar: DQN on atari
 * Homework - convnets on MNIST or simple deep q-learning - [week5/README.md](https://github.com/yandexdataschool/Practical_RL/blob/master/week5/README.md)
    * HSE homework deadline _23.59 15.03.17_

## Future lectures:

* __week6__ Policy gradient methods (coming 13.03.2017)
 * Lecture: Motivation for policy-based, policy gradient, logderivative trick, REINFORCE/crossentropy method, variance theorem(advantage), advantage actor-critic (incl.n-step advantage), off-policy actor-critic (off-PAC), natural gradients(briefly), continuous action space(teaser).
 * Seminar: a2c Vs qlearning for MountainCar/Doom, entropy regularization & tricks, simple demo with continuous action spaces

*somewhere here comes RNN crash-course* (coming 20.03.2017)

* __week7__ Partially observable MDPs (coming 27.03.2017)
 * Lecture: POMDP intro. Model-based solvers. RNN solvers. RNN tricks: attention, problems with normalization methods, pre-training.
 * Seminar: Deep kung-fu & doom with recurrent A3C vs feedforward A3C


* __week i+1__ Case studies (coming 3.04.2017
 * Lecture: Reinforcement Learning as a general way to optimize non-differentiable loss. Seq2seq tasks: g2p, machine translation, conversation models. Tricks for seq2seq models. Financial world applications as RL problems. KL(p||q) vs KL(q||p) and generative adversarial nets.
 * Seminar: Optimizing Levenshtein distance with seq2seq for g2p OR using deterministic policy gradient for portfolio management.

_The dark side clouds everything. From this point, impossible to see the future is._

* __week i+1__ RL in Large/Continuous action spaces.
 * Lecture: Continuous action space MDPs. Model-based approach (NAF). Actor-critic approach (dpg, svg). Trust Region Policy Optimization. Large discrete action space problem. Action embedding.
 * Seminar: Classic Control and BipedalWalker with ddpg Vs qNAF. https://gym.openai.com/envs/BipedalWalker-v2 .

* __week i+1__ Trust Region Policy Optimization.
 * Lecture: Trust region policy optimization in detail.
 * approximate TRPO vs approximate Q-learning for gym box2d envs (robotics-themed)

* __week i+1__ Advanced exploration methods: intrinsic motivation
 * Lecture: Augmented rewards. Heuristics (UNREAL,density-based models), formal approach: information maximizing exploration. Model-based tricks(also refer mcts).
 * Seminar: Vime vs epsilon-greedy for Go9x9 (bonus 19x19)

* __week i+1__ Advanced exploration methods: probablistic approach.
 * Lecture: Improved exploration methods (quantile-based, etc.). Bayesian approach. Case study: Contextual bandits for RTB.
 * Seminar: Bandits


* __week i+1__ Hierarchical MDP
 * Lecture: MDP Vs real world. Sparse and delayed rewards. When Q-learning fails. Hierarchical MDP. Hierarchy as temporal abstraction. MDP with symbolic reasoning.
 * Seminar: Hierarchical RL for atari games with rare rewards (starting from pre-trained DQN)

* __week i+1__ Case studies II
 * Lecture: Direct policy optimization: finance.  Inverse Reinforcement Learning: personalized medial treatment, robotics.
 * Seminar: Portfolio optimization as POMDP.


# Course staff
Course materials and teaching by
- [Fedor Ratnikov](https://github.com/justheuristic/) - lectures, seminars, hw checkups
- [Alexander Fritsler](https://github.com/Fritz449) - lectures, seminars, hw checkups
- [Oleg Vasilev](https://github.com/Omrigan) - seminars, hw checkups, technical support
- [Pavel Shvechikov](https://github.com/bestxolodec) - lectures, seminars, HW checkups

# Contributors
* Using pictures from http://ai.berkeley.edu/home.html
* Tensorflow assignments by [Scitator](https://github.com/Scitator)
* Other contributions: [omtcyfz](https://github.com/omtcyfz) [dmittov](https://github.com/dmittov) [arogozhnikov](https://github.com/arogozhnikov)
