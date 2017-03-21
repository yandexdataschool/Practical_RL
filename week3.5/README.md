
## Materials
* [__Lecture slides__](https://yadi.sk/i/yAO2AJ3M3EKP8g)
* Lecture on deep learning (russian) - https://www.youtube.com/watch?v=8008XQzoUEs
* Seminar on theano (russian) - https://yadi.sk/i/54STsEBVpubkn
* Intro to neural nets and backprop (english) - https://www.youtube.com/watch?v=uXt8qF2Zzfo
* Intro to convnets (english) - https://www.youtube.com/watch?v=FmpDIaiMIeA
* Theano tutorial from Lamblin (english) - https://www.youtube.com/watch?v=OU8I1oJ9HhI

## Bonus materials
* Karpathy's course on deep learning (english) - http://cs231n.github.io/
* Nuts and Bolts of deep learning by Andrew Ng (english) - https://www.youtube.com/watch?v=F1ka6a13S9I
* Deep learning demystified - https://www.youtube.com/watch?v=Q9Z20HCPnww
* Karpathy's lecture on deep learning for computer vision - https://www.youtube.com/watch?v=u6aEYuemt0M
* Our humble DL course: [HSE'autumn16](https://github.com/yandexdataschool/HSE_deeplearning), [Skoltech/YSDA'spring16](https://github.com/ddtm/dl-course/) courses on deep learning (english).
* Srsly, just google `"deep learning %s"%s for s in what_you_want_to_know`.

## Homework

If you are already familiar with lasagne or you are super-good with tensorflow/pytorch/similar, pick one of the _alternative_ options. Otherwise we highly recommend the first one as we'll need convolutional networks soon enough.

* [__recommended__](https://github.com/yandexdataschool/Practical_RL/blob/master/week3.5/Seminar3.5-en-mnist.ipynb) go to Seminar3.5-*-mnist.ipynb and follow the instructions (ends with lasagne MNIST classifier)


* [__alternative task__](https://github.com/yandexdataschool/Practical_RL/blob/master/week3.5/Seminar3.5-approx-qlearning.ipynb) go to Seminar3.5-approx-q-learning.ipynb and follow the instructions (ends with simple NN for q-learning)

* [__alternative frameworks__] 
The equivalent of recommended track would be 
* [tensorflow] learning through this [google course](https://www.udacity.com/course/deep-learning--ud730) from start till "Convolutional neural networks" (inclusive).
* [manual/other] surviving past assignment2 of [cs231](http://cs231n.github.io/)

* [__alternative task and frameworks__]
Implement the simple q-learning network that solves `CartPole-v0`. You're not required to implement experience replay / any advanced stuff, just set sgd learning rate to a small enough number (10^-4) and pray that trains smoothly.

Here's a convenient translation to tensorflow: [notebook](https://github.com/yandexdataschool/Practical_RL/blob/master/week3.5/Seminar3.5-approx-qlearning-tf.ipynb)

Agent can maintain low reward for long enough, but it should at least show some progress by the end of the default loop.

