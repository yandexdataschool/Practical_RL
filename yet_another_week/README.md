In this week you can find several sections covering advanced topics in RL, along with less advanced topics that we couldn't squeeze into the main track

## Advanced policy gradient methods
This section covers some steroids for policy gradient methods, along with a cool general trick called 

* Lecture on NPG and TRPO by J. Schulman - [video](https://www.youtube.com/watch?v=_t5fpZuuf-4)
* Alternative lecture on TRPO and open problems by... J. schulman - [video](https://www.youtube.com/watch?v=gb5Q2XL5c8A)
* Our [__slides__](https://yadi.sk/i/9j6S4WVp3HgEdn) on TRPO, video: [lecture](https://yadi.sk/i/1oyihBnm3HiKHm), [seminar](https://yadi.sk/i/b0ol2gUV3HiKKJ) (russian)
* Original articles - [TRPO](https://arxiv.org/abs/1502.05477), [NPG](https://papers.nips.cc/paper/2073-a-natural-policy-gradient.pdf)


* __Assignment:__ [seminar_TRPO.ipynb](https://github.com/yandexdataschool/Practical_RL/blob/master/yet_another_week/seminar_TRPO.ipynb)
  * TF version: [pending]

## Model-based RL: Planning
* Planning by dynamic programming (D. Silver) - [video](https://www.youtube.com/watch?v=Nd1-UUMVfz4)
* Planning via tree search [videos 2-6 from CS188](https://www.youtube.com/channel/UCHBzJsIcRIVuzzHVYabikTQ)
* Our lecture:
  * Slides [part1](https://yadi.sk/i/3PM9zCP33J3ub3) (intro), [part2](https://yadi.sk/i/M03xvZ2y3JMQre) (pomdp)
  * [Lecture](https://yadi.sk/i/lOAUu7o13JBHFz) & [seminar](https://yadi.sk/i/bkmjEZrk3JBHGF)
* Monte-carlo tree search
  *  Udacity video on monte-carlo tree search (first part of a chain) - [video](https://www.youtube.com/watch?v=onBYsen2_eA)
  * Reminder: UCB-1 - [slides](https://www.cs.bham.ac.uk/internal/courses/robotics/lectures/ucb1.pdf)
  * Monte-carlo tree search step-by-step by J.Levine - [video](https://www.youtube.com/watch?v=UXW2yZndl7U)
  * Guide to MCTS (monte-carlo tree search) - [post](http://www.cameronius.com/research/mcts/about/index.html)
  * Another guide to MCTS - [url](https://jeffbradberry.com/posts/2015/09/intro-to-monte-carlo-tree-search/)
* Integrating learning and planning (D. Silver) - [video](https://www.youtube.com/watch?v=ItMutbeOHtc&t=1241s)

* __Assignment:__ [seminar_MCTS.ipynb](https://github.com/yandexdataschool/Practical_RL/blob/master/yet_another_week/seminar_MCTS.ipynb)

* Approximating the MCTS optimal actions - 5vision solution for deephack.RL, code by Mikhail Pavlov - [repo](https://github.com/5vision/uct_atari)

## Reinforcement learning in large/continuous action spaces
While you already know algorithms that will work with continuously many actions, it can't hurt to learn something more specialized.
 * Deterministic policy gradient - [article](https://arxiv.org/pdf/1512.07679.pdf), [post+code](https://yanpanlau.github.io/2016/10/11/Torcs-Keras.html)
 * Stochastic value gradient - [article](https://arxiv.org/abs/1510.09142)
 * Q-learning with normalized advantage functions - [article](https://arxiv.org/abs/1603.00748), [code1](https://github.com/carpedm20/NAF-tensorflow), [code2](http://bit.ly/2qx2087)
 * Embedding large discrete action spaces for RL - [article](https://arxiv.org/pdf/1512.07679.pdf)
 * Lecture by A. Seleznev, 5vision (russian) - [video](www.youtube.com/watch?v=j1L2FnanXPo&t=119m45s)

## Other
* Learning by imitation - [video](https://www.youtube.com/watch?v=kl_G95uKTHw), [assignment](http://rll.berkeley.edu/deeprlcourse/docs/hw1.pdf)(berkeley cs294)
* Knowledge transfer in RL - [video](https://www.youtube.com/watch?v=Hx4XpVdJOI0)(berkeley cs294)
* Inverse reinforcement learning - [video](https://www.youtube.com/watch?v=J2blDuU3X1I)
* Hierarchical reinforcemnt learning - [pending]
* [Your contribution]

## A list of lists
* [awesome_rl](https://github.com/aikorea/awesome-rl/) - a curated list of resources dedicated to reinforcement learning.
* [junhyukoh's list](https://github.com/junhyukoh/deep-reinforcement-learning-papers)
* [muupan's list](https://github.com/muupan/deep-reinforcement-learning-papers)
* Courses:
 * [CS294: deep reinforcement learning](http://rll.berkeley.edu/deeprlcourse/)
 * [Silver's RL course](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)
 * [Sutton's book, 2nd edition](http://incompleteideas.net/sutton/book/the-book-2nd.html)
* [Implementations of many basic RL algorithms (raw and/or tensorflow)](https://github.com/dennybritz/reinforcement-learning)
* Reddit: [General ML](https://www.reddit.com/r/MachineLearning/), [RL](https://www.reddit.com/r/reinforcementlearning/), [CS294](https://www.reddit.com/r/berkeleydeeprlcourse/)
* [This great link you could have contributed]

