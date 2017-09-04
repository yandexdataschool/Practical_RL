## Materials
* [__Lecture slides__](https://docviewer.yandex.ru/?url=ya-disk-public%3A%2F%2FG3IXcG62RwNUGSSos%2BuGhtgXNfsBjP9RxUtUfgCffIk%3D%3A%2Flecture2.pdf&name=lecture2.pdf&c=58a61e22b9fb)
* Our [lecture](https://yadi.sk/i/cVawsPkK3EtGJj),[seminar](https://yadi.sk/i/dQmolwOy3EtGNK) (russian)
* [__main__] Lecture by David Silver (english): https://www.youtube.com/watch?v=PnHCvfgC_ZA
* Alternative lecture by Pieter Abbeel (english): https://www.youtube.com/watch?v=ifma8G7LegE
* Alternative lecture by John Schulmann (english): https://www.youtube.com/watch?v=IL3gVyJMmhg

## Bonus materials
* Policy improvement theorems from Sutton book - http://webdocs.cs.ualberta.ca/~sutton/book/ebook/node42.html
* Lecture II by Dan Klein (english): https://www.youtube.com/watch?v=jUoZg513cdE
* Qlearning guide from Habr (russian): https://habrahabr.ru/post/308094/
* A great turorial/assignment on value-based methods from CS294 - https://github.com/berkeleydeeprlcourse/homework/blob/master/hw2/HW2.ipynb

## Homework description:

For ease of access, we have 2 versions of the same homework. They feature the same algorithmic part but a bit different examples.

You can pick whichever one you prefer but mind the technical limitations. If you have a python2 on a local machine (NOT in docker), even if it's on Windows, we recommend the ./assignment one.

## ./assignment
_this assignment borrows code from awesome [cs188](http://ai.berkeley.edu/project_overview.html)_
This homework assignment works on __python2 only__. If you stick to py3, consider alternative homework. Or just install it for this homework alone and remove afterwards.

This homework also requires some physical display (e.g. laptop monitor). It won't work on binder VM / headless server. Please run it on laptop or consider ./alternative

### Part I (5 points)
* Go to ./assignment, edit [__qlearningagents.py__](https://github.com/yandexdataschool/Practical_RL/blob/master/week2/assignment/qlearningAgents.py) (see instructions inside)
* Make sure you can tune agent to beat ./run_crawler.sh
 * on windows, just run `python crawler.py` from cmd in the project directory
* other ./run* files are mostly for your amusement. 
  * ./run_pacman.sh will need more epochs to converge, see [comments](https://github.com/yandexdataschool/Practical_RL/blob/master/week2/assignment/run_pacman.sh)
  * on windows, just copy the type `python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid` in cmd from assignemnt dir
(YSDA/HSE) Please submit only qlearningAgents.py file and include a brief text report as comments in it.
  
### Part II (5+ points)
_Please make a separate copy of qlearningAgents.py for this assignment_

The default tabular q-learning requires unrealistic amount of experience to learn anything useful on pacman tasks. This is mostly due to extremely large state space, combining positions of pacman, ghosts and all dots.

To speed up training you will need to implement a preprocessor that extracts new discrete features from state space. You can design these features to account only for the most important stuff around pacman. This time, it's okay to use environment-specific duct tape :)

Please read tips on how to solve them [__here__](https://github.com/yandexdataschool/Practical_RL/blob/master/week2/homework_tips.md). Also, if you find some state spaces that work amaizingly good on pacman, weel free to propose a Pull Request with advices 

(HSE/YSDA) Please send us 
* The alternative qlearningAgents.py file (and any other files you modified)
* A short description of what you did there
* How to run it. Usually something like `python pacman.py -p PacmanQAgent -x SOMETHING -n SOMETHING -l __mediumClassic__ -SOMETHING SOMETHING ...`
* End of train/test log (or even whole log), including at least last iteration of learning and final statistics (especially winrate)

To get 5 points, your algorithm should solve __mediumGrid__ more than 50% times. Creative features and outstanding performance on __mediumClassic__ yields bonus points!
 
## ./alternative
Alternative homework description:
* Go to [the notebook](https://github.com/yandexdataschool/Practical_RL/blob/master/week2/alternative/homework.ipynb)
* The assignment is described there.
* If you use binder/server, see week1 for example on how to run CartPole and other envs.


### Grading (alternative)
* 5 points for implementing q-learning and testing on taxi
* 5 points for solving CartPole-v0
* bonus tasks listed inside
