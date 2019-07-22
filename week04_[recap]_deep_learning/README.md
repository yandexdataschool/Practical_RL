__Note:__ This week's materials cover the basics of neural nets and deep learning and teach you how to use auto-diff frameworks. If you're already fluent in tensorflow OR pytorch OR theano - feel free to skip this week entirely..

## Materials
* [__Lecture slides__](https://yadi.sk/i/yAO2AJ3M3EKP8g)

- __In russian:__
  * Basic lecture on deep learning - [video](https://yadi.sk/i/yyHZub6R3Ej5dV)
  * Deep learning frameworks - [video](https://yadi.sk/i/hDIkaR4H3EtnXM) 
  * [Pytorch tutorial](https://yadi.sk/i/O3mQ76u43So3h9) __recommended__
  * [Tensorflow tutorial](https://www.youtube.com/watch?v=FQ660T4uu7k) (english only for now. Links are welcome)
  * [Theano tutorial](https://yadi.sk/i/54STsEBVpubkn)

- __In english:__
  * Intro to neural nets and backprop (english) - [video](https://www.youtube.com/watch?v=uXt8qF2Zzfo)
  * Intro to convnets - [video](https://www.youtube.com/watch?v=FmpDIaiMIeA)
  * Deep learning frameworks - [video](https://www.youtube.com/watch?v=Vf_-OkqbwPo)
  * [Tensorflow tutorial](https://www.youtube.com/watch?v=FQ660T4uu7k)
  * [Theano tutorial](https://www.youtube.com/watch?v=OU8I1oJ9HhI)
  * [Pytorch tutorial](https://www.youtube.com/watch?v=VMcRWYEKmhw)

## Bonus materials
* Karpathy's course on deep learning (english) - http://cs231n.github.io/
* A neat little play-ground where you can train small NNs and see what they actually learn - [playground](http://playground.tensorflow.org/)
* Nuts and Bolts of deep learning by Andrew Ng (english) - [video](https://www.youtube.com/watch?v=F1ka6a13S9I)
* Deep learning philosophy: [our humble take](https://www.youtube.com/watch?v=9qyE1Ev1Xdw) (english)
* Deep learning demystified - [video](https://www.youtube.com/watch?v=Q9Z20HCPnww)
* Karpathy's lecture on deep learning for computer vision - https://www.youtube.com/watch?v=u6aEYuemt0M
* Our humble DL course: [HSE'fall17](https://github.com/yandexdataschool/HSE_deeplearning), [Skoltech/YSDA'spring16](https://github.com/ddtm/dl-course/) courses on deep learning (english).
* Srsly, just google `"deep learning %s"%s for s in what_you_want_to_know`.

  
### Practice
__[Colab url (pytorch)](https://colab.research.google.com/github/yandexdataschool/Practical_RL/blob/master/week04_%5Brecap%5D_deep_learning/seminar_pytorch.ipynb)__
From now on, we'll have two tracks: theano and tensorflow. We'll also add pytorch seminars as soon as they're ready.

Please pick seminar_theano.ipynb, seminar_tensorflow.ipynb or seminar_pytorch.ipynb.

__Note:__ in this and all following weeks you're only required to get through practice in _one_ of the frameworks. Looking into other alternatives is great for self-education but never mandatory.

#### What to choose?
* The simplest choice is PyTorch: it's basically ye olde numpy with automatic gradients and a lot of pre-implemented DL stuff... except all the functions have different names.
* If you want to be familiar with production-related stuff from day 1, choose TensorFlow. It's much more convenient to deploy (to non-python or to mobiles). The catch is that all those conveniences become inconveniences once you want to write something simple in jupyter.
* Theano works like tensorflow but it offers a numpy-compatible interface and comes with built-in graph optimization. The payoff is that theano is not as popular as the first two. It is also not meant as a producton framework so deploying to mobiles may be a problem.

* It's not like choosing house at Hogwarts, you'll be able to switch between frameworks easily once you master the underlying principles.
  
