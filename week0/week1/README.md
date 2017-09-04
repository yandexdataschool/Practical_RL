## Materials:
* [__Lecture slides__](https://docviewer.yandex.ru/?url=ya-disk-public%3A%2F%2FG3IXcG62RwNUGSSos%2BuGhtgXNfsBjP9RxUtUfgCffIk%3D%3A%2Flecture1.pdf&name=lecture1.pdf&c=58a61ec9256c)
* Lecture and seminar videos (russian) - [lecture](https://yadi.sk/i/5yf_4oGI3EDJhJ), [seminar](https://yadi.sk/i/dPsWYMK13EDJj7) _only covering crossentropy method_
* [__main__] Lecture by J Schulman with crossentropy method explained (english) - https://www.youtube.com/watch?v=aUrX-rP_ss4&list=PLCTc_C7itk-GaAMxmlChrkPnGKtjz8hv1
* [__main__] Sutton's definitive guide to monte-carlo methods - http://incompleteideas.net/sutton/book/ebook/node50.html
* Article about CEM in general - https://people.smp.uq.edu.au/DirkKroese/ps/eormsCE.pdf
* Article about CEM for optimization - https://people.smp.uq.edu.au/DirkKroese/ps/CEopt.pdf
* Article about CEM in reinforcement learning - http://www.aaai.org/Papers/ICML/2003/ICML03-068.pdf

## Homework description
* Just follow the [notebook](https://github.com/yandexdataschool/Practical_RL/blob/master/week1/crossentropy_method.ipynb)
* During the `CartPole-v0` section (and similar envs), a window will pop up, displaying some game state. The window won't respond to direct input and is instead changes each time you call env.render(). Don't force-close this process, just ignore it until you complete the notebook.
* __important__ the current newest version of gym force-stops environment in 200 steps even if you don't use env.monitor.
  * This may ruin CEM on MountainCar. To avoid this, use gym.make("MountainCar-v0").env
