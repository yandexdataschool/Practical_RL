## Materials
* [Slides](https://docviewer.yandex.ru/?url=ya-disk-public%3A%2F%2FG3IXcG62RwNUGSSos%2BuGhtgXNfsBjP9RxUtUfgCffIk%3D%3A%2Flecture6.pdf&name=lecture6.pdf&c=58c876c4863a)
* Video lecture by D. Silver - [video](https://www.youtube.com/watch?v=KHZVXao4qXs)
* Our [lecture](https://yadi.sk/i/yPIPkO_f3TPsNK),  [seminar(pytorch)](https://yadi.sk/i/flW8ezGk3TPsQ5), [seminar(theano)](https://yadi.sk/i/8f9NX_E73GKBkT)
* Alternative lecture by J. Schulman part 1 - [video](https://www.youtube.com/watch?v=BB-BhTn6DCM)
* Alternative lecture by J. Schulman part 2 - [video](https://www.youtube.com/watch?v=Wnl-Qh2UHGg)


## More materials
* Actually proving the policy gradient for discounted rewards - [article](https://papers.nips.cc/paper/1713-policy-gradient-methods-for-reinforcement-learning-with-function-approximation.pdf)
* On variance of policy gradient and optimal baselines: [article](https://papers.nips.cc/paper/4264-analysis-and-improvement-of-policy-gradient-estimation.pdf), another [article](https://arxiv.org/pdf/1301.2315.pdf)
* Generalized Advantage Estimation - a way you can speed up training for homework_*.ipynb - [article](https://arxiv.org/abs/1506.02438)


* Generalizing log-derivative trick - [url](http://blog.shakirm.com/2015/11/machine-learning-trick-of-the-day-5-log-derivative-trick/)
* Combining policy gradient and q-learning - [arxiv](https://arxiv.org/abs/1611.01626)
* Bayesian perspective on why reparameterization & logderivative tricks matter (Vetrov's take) - [pdf](https://www.sdsj.ru/slides/Vetrov.pdf)
* Adversarial review of policy gradient - [blog](http://www.argmin.net/2018/02/20/reinforce/)


## Homework

As usual, pick reinfoce_<framework_name>.ipynb for starters and then proceed with homework_<framework_name>.ipynb.

To run seminar notebook in colab
* run it [here](https://colab.research.google.com/github/yandexdataschool/Practical_DL/blob/fall18/week10_rl/reinforce_pytorch.ipynb#scrollTo=y9nfDwJY3sGI)
* paste this to install libraries
```
!pip install gym
!apt-get install -y xvfb
!wget https://raw.githubusercontent.com/yandexdataschool/Practical_DL/fall18/xvfb
!apt-get install -y python-opengl ffmpeg
!pip install pyglet==1.2.4

!bash ./xvfb start
%env DISPLAY=:1
```
