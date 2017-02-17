## Materials
* [__Lecture slides__](https://docviewer.yandex.ru/?url=ya-disk-public%3A%2F%2FG3IXcG62RwNUGSSos%2BuGhtgXNfsBjP9RxUtUfgCffIk%3D%3A%2Flecture2.pdf&name=lecture2.pdf&c=58a61e22b9fb)
* Similar lecture by David Silver (english): https://www.youtube.com/watch?v=PnHCvfgC_ZA
* Similar lecture by Pieter Abbeel (english): https://www.youtube.com/watch?v=ifma8G7LegE
* Lecture II by Dan Klein (english): https://www.youtube.com/watch?v=jUoZg513cdE
* Qlearning guide from Habr (russian): https://habrahabr.ru/post/308094/

## Homework description:

For ease of access, we have 2 versions of the same homework. They feature the same algorithmic part but a bit different examples.

You can pick whichever one you prefer but mind the technical limitations. If you have a python2 on a local machine (NOT in docker), even if it's on Windows, we recommend the ./assignment one.

### ./assignment
_this assignment borrows code from awesome [cs188](http://ai.berkeley.edu/project_overview.html)_
This homework assignment works on __python2 only__. If you stick to py3, consider alternative homework. Or just install it for this homework alone and remove afterwards.

This homework also requires some physical display (e.g. laptop monitor). It won't work on binder VM / headless server. Please run it on laptop or consider ./alternative

* Go to ./assignment, edit [__qlearningagents.py__](https://github.com/yandexdataschool/Practical_RL/blob/master/week2/assignment/qlearningAgents.py) (see instructions inside)
* Make sure you can tune agent to beat ./run_crawler.sh
 * on windows, just run `python crawler.py` from cmd in the project directory
* other ./run* files are mostly for your amusement. 
  * ./run_pacman.sh will need more epochs to converge, see [comments](https://github.com/yandexdataschool/Practical_RL/blob/master/week2/assignment/run_pacman.sh)
  
(YSDA/HSE) Please submit only qlearningAgents.py file and include a brief text report as comments in it.

Also consider [__bonus assignment__](https://github.com/yandexdataschool/Practical_RL/blob/master/week2/bonus_assignment.md), it can be quite entertaining.

### ./alternative
Alternative homework description:
* Go to [the notebook](https://github.com/yandexdataschool/Practical_RL/blob/master/week2/alternative/homework.ipynb)
* The assignment is described there.
* If you use binder/server, see week1 for example on how to run CartPole and other envs.

(YSDA/HSE) Please include a brief text report on what you did in the notebook.

