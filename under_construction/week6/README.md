## Materials
* [Slides](https://docviewer.yandex.ru/?url=ya-disk-public%3A%2F%2FG3IXcG62RwNUGSSos%2BuGhtgXNfsBjP9RxUtUfgCffIk%3D%3A%2Flecture6.pdf&name=lecture6.pdf&c=58c876c4863a)
* Video lecture by D. Silver - https://www.youtube.com/watch?v=KHZVXao4qXs
* Our [lecture](https://yadi.sk/i/I3M09HKQ3GKBiP), [seminar](https://yadi.sk/i/8f9NX_E73GKBkT)
* Alternative lecture by J. Schulman part 1 - https://www.youtube.com/watch?v=BB-BhTn6DCM
* Alternative lecture by J. Schulman part 2 - https://www.youtube.com/watch?v=Wnl-Qh2UHGg


## More materials
* Generalizing log-derivative trick - http://blog.shakirm.com/2015/11/machine-learning-trick-of-the-day-5-log-derivative-trick/
* Combining policy gradient and q-learning - https://arxiv.org/abs/1611.01626
* Bayesian perspective on why reparameterization & logderivative tricks matter (Vetrov's take) - https://www.sdsj.ru/slides/Vetrov.pdf


## Homework

As usual, "lasagne way" and "other way"

#### Lasagne way

First go to Seminar6.0 notebook and implement a vanilla REINFORCE algorithm from scratch. Follow up by playing with advantage actor-critic in Seminar 6.1 - just follow the steps you'll find in the notebook.

#### Other way

This week's task is to implement REINFORCE on any continuous state space env (simplest being CartPole-v0) and advantage actor-critic on LunarLander-v2.

You will find some helpful materials there:
* Tensorflow similar assignment: [cs294 assignment 4](https://github.com/berkeleydeeprlcourse/homework/blob/master/hw4/homework.md)


_[copy-pasted section]_

We recommend you to upload your results to OpenAI gym and fit your solution in a notebook (ipython/torch/r) unless your framework is incompatible with that. In the latter case, please supply us some notes on what code lies where.

Again, we recommend you to read the lasagne/agentnet assignments briefly to get the grasp of what parameters to start from.

Bonus assignments remain exactly the same as in the first track.

Blindly copy-pasting code from any publically available demos will result in us interrogating you about every signifficant line of code to make sure you at least understand (and regret) what you copypasted.


