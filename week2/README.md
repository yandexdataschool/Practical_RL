## Materials
* [__Lecture slides__](https://docviewer.yandex.ru/?url=ya-disk-public%3A%2F%2FG3IXcG62RwNUGSSos%2BuGhtgXNfsBjP9RxUtUfgCffIk%3D%3A%2Flecture2.pdf&name=lecture2.pdf&c=58a61e22b9fb)
* Similar lecture by David Silver (english): https://www.youtube.com/watch?v=PnHCvfgC_ZA
* Similar lecture by Pieter Abbeel (english): https://www.youtube.com/watch?v=ifma8G7LegE
* Lecture II by Dan Klein (english): https://www.youtube.com/watch?v=jUoZg513cdE
* Qlearning guide from Habr (russian): https://habrahabr.ru/post/308094/

## Homework description:

__warning!__ This homework assignment works on python2 only (as per now). If you stick to py3, consider alternative homework. Or just install it for this homework alone and remove afterwards.

__warning2!__ This homework will not work on binder VM / headless server. Please run it on laptop or consider ./alternative

* Go to ./assignment, edit __qlearningagents.py__ (see instructions inside)
* Make sure your agent beats ./run_crawler.sh 
* python crawler.py
 * on windows, just run `python crawler.py` from cmd in the project directory
* other ./run* files are mostly for your amusement. 
  * ./run_pacman.sh will need more epochs to converge

Alternative homework description:
* Go to [the notebook](https://github.com/yandexdataschool/Practical_RL/blob/master/week2/alternative/homework.ipynb)
* The assignment is described there.
* If you use binder/server, see week1 for example on how to run CartPole and other envs.
