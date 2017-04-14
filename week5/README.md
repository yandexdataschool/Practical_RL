## Materials
* Slides [here](https://yadi.sk/i/P02qoHng3G7oMt)
* Video lecture (esp. second half) by J. Schulman - https://www.youtube.com/watch?v=h1-pj4Y9-kM
* Our [lecture](https://yadi.sk/i/yBO0q4mI3GAxYd), [seminar](https://yadi.sk/i/oWC2M5803GAyFB) (russian)
* Article on dueling DQN - https://arxiv.org/pdf/1511.06581.pdf
* Article on double DQN - https://arxiv.org/abs/1509.06461
* Article on prioritized experience replay - https://arxiv.org/abs/1511.05952
* Video on asynchronuous methods (Mnih) - https://www.youtube.com/watch?v=9sx1_u2qVhQ
* Article on bootstrap DQN - https://papers.nips.cc/paper/6501-deep-exploration-via-bootstrapped-dqn.pdf, [summary](http://pemami4911.github.io/paper-summaries/2016/08/16/Deep-exploration.html)


## More materials
* [recommended] An overview of deep reinforcement learning - https://arxiv.org/pdf/1701.07274v1.pdf
* Reinforcement learning architectures list - https://github.com/5vision/deep-reinforcement-learning-networks
* Building deep q-network from ~scratch (blog) - https://jaromiru.com/2016/09/27/lets-make-a-dqn-theory/
* Another guide guide to DQN from ~scratch (blog) - https://rubenfiszel.github.io/posts/rl4j/2016-08-24-Reinforcement-Learning-and-DQN.html
* Article on asynchronuous methods in deep RL - https://arxiv.org/abs/1602.01783
* Successor representations for reinforcement learning - [article](https://arxiv.org/abs/1606.02396), [video](https://www.youtube.com/watch?v=kNqXCn7K-BM&feature=youtu.be)
* [recap] Slides on basic DQN, including target networks - https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf


## Homework

As usual, "lasagne way" and "other way"

#### Lasagne way

Basically go to [the notebook](https://github.com/yandexdataschool/Practical_RL/blob/master/week5/Seminar5_deep_rl.ipynb) and follow what's inside.

#### Other way

This week's task is to implement (and hopefully compare) target networks, double DQN and/or duelling DQN and training on atari breakout.

 * Tensorflow template: [cs294 assignment 3](https://github.com/berkeleydeeprlcourse/homework/tree/master/hw3)

Implementing prioritized experience replay or bootstrap dqn or any other cool stuff yields you bonus points. You can also choose a different environment if you have issues with breakout, but don't get too complicated. E.g. your DQN will likely _fail_ on Montezuma Revenge unless you do weird stuff with reward function.

We recommend you to upload your results to OpenAI gym and fit your solution in a notebook (ipython/torch/r) unless your framework is incompatible with that. In the latter case, please supply us some notes on what code lies where.

Again,we recommend you to read the lasagne/agentnet assignments briefly to get the grasp of what parameters to start from.

Bonus assignments remain exactly the same as in the first track.

Blindly copy-pasting code from any publically available demos will result in us interrogating you about every signifficant line of code to make sure you at least understand (and regret) what you copypasted.


