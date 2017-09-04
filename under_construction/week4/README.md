## Materials
* [__lecture slides__](https://docviewer.yandex.ru/?url=ya-disk-public%3A%2F%2FG3IXcG62RwNUGSSos%2BuGhtgXNfsBjP9RxUtUfgCffIk%3D%3A%2Flecture4.pdf&name=lecture4.pdf&c=58b0d2eb4e0f)
* David Silver lecture - https://www.youtube.com/watch?v=UoPei5o4fps&t=3s
* More practical and less theoretical lecture from MIT 6.S191 - https://www.youtube.com/watch?v=xWe58WGWmlk
* Our [lecture](https://yadi.sk/i/AHDU2p_j3FT3nr), [seminar](https://yadi.sk/i/EeUeheri3FT3ra) (russian)
* Understanding approximate q-learning - https://danieltakeshi.github.io/2016/10/31/going-deeper-into-reinforcement-learning-understanding-q-learning-and-linear-function-approximation/
* Karpathy's post on approximate RL - http://karpathy.github.io/2016/05/31/rl/

## More materials
* __[recommended]__ How to _actually_ do deep reinforcement learning by J. Schulman - http://rll.berkeley.edu/deeprlcourse/docs/nuts-and-bolts.pdf
* interactive demos in your browser: [demo1](http://cs.stanford.edu/people/karpathy/convnetjs/demo/rldemo.html)(karpathy), [demo2](http://janhuenermann.com/projects/learning-to-drive)(Hünermann)
* A guide to deep RL from ~scratch (nervana blog) - https://www.nervanasys.com/demystifying-deep-reinforcement-learning/


## Homework

From now on, we introduce an alternative homework track that's not tied to lasagne/agentnet/rllab/any_other_framework. In that track, you'll be tasked with similar problems, but they will not be tied to jupyter notebooks with lasagne networks.

You can choose whichever track you want, but unless you're expertly familiar with your framework, we recommend you to start by completing the task in lasagne and only then reproduce your solution in your chosen framework.


#### Recommended path

* Step 1 - go to [Seminar4.1](https://github.com/yandexdataschool/Practical_RL/blob/master/week4/Seminar4.1_experience_replay.ipynb), complete it and make sure it reaches the desired reward on Acrobot-v1. Then go to homework section (at the end) and follow the instructions from there.
  * Tip - for your network to work properly on Acrobot-v1, please either use non-saturated nonlinearities (elu/leaky_relu/softplus), or normalize observations, or initialize with smaller weights. Otherwise, e.g. sigmoid may get saturated and fail to learn anything.
* Step 2 - go to [Seminar4.2](https://github.com/yandexdataschool/Practical_RL/blob/master/week4/Seminar4.2_conv_agent.ipynb) and make it beat DoomBasic. 
 
Doom environments are powered by VizDoom (via doom_py), which may require separate installation. If you're using [docker container](https://github.com/yandexdataschool/Practical_RL/blob/master/docker) or running in binder, the dependency should already be installed.

To install doom envs manually, follow the instructions at the top of the [Seminar4.2](https://github.com/yandexdataschool/Practical_RL/blob/master/week4/Seminar4.2_conv_agent.ipynb) notebook.

For example, on python2, ubuntu 14, stardate 2017.02.27 it took us to
```
apt-get install -y gcc g++ wget unzip libsdl2-dev libboost-all-dev
pip install gym_pull
pip install ppaquette-gym-doom
```

For macOS (OS X) install brew and then
```
brew install boost boost-python sdl2 cmake
pip install ppaquette-gym-doom
````

If it just won't get installed, pick `BreakoutDeterministic-v0` and try to get average reward >= +10
  

#### Alternative frameworks

The task is to implement approximate Q-learning with experience replay and show that it works on `Acrobot-v1`,`LunarLander-v2` and `ppaquette/DoomBasic-v0` (or other versions of those environments).

If you use tensorflow, there's a very convenient [notebook](https://github.com/yandexdataschool/Practical_RL/blob/master/week4/Seminar4.0_recap_approx_qlearning-tf.ipynb) for you to start (by [Scitator](https://github.com/Scitator))

We, however, recommend you to read the lasagne/agentnet assignments briefly to get the grasp of what parameters to start from.

Your're also recommended to fit your solution in a notebook (ipython/torch/r) unless your framework is incompatible with that. In the latter case, please supply us some notes on what code lies where.

Bonus assignments remain exactly the same as in the first track.

Blindly copy-pasting code from any publically available demos will result in us interrogating you about every signifficant line of code to make sure you at least understand (and regret) what you copypasted.


