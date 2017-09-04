## Materials
* [__Lecture slides__] TODO
* __[main]__ Video-intro by David Silver (english) - https://www.youtube.com/watch?v=2pWv7GOvuf0
* Optional lecture by David Silver (english) - https://www.youtube.com/watch?v=lfHX2hHRMVQ
* Intro lecture (russian) - https://yadi.sk/i/bMo0qa-x3DoqkS
* Intro seminar (russian) - https://yadi.sk/i/IBq2MjoS3DoqkY
* Deep learning course (if you want to learn in parallel) - https://github.com/yandexdataschool/HSE_deeplearning

## Homework description
* Go to the [notebook](https://github.com/yandexdataschool/Practical_RL/blob/v2.0/week0/frozenlake.ipynb)
* You can find homework and bonus assignment descriptions at the end of that notebook.
* Just follow the [notebook](https://github.com/yandexdataschool/Practical_RL/blob/v2.0/week1/crossentropy_method.ipynb)
* During the `CartPole-v0` section (and similar envs), a window will pop up, displaying some game state. The window won't respond to direct input and is instead changes each time you call env.render(). Don't force-close this process, just ignore it until you complete the notebook.
* __important__ the current newest version of gym force-stops environment in 200 steps even if you don't use env.monitor.
  * This may ruin CEM on MountainCar. To avoid this, use gym.make("MountainCar-v0").env

## More on global optimization heuristics:
* __[recommended]__ - awesome openai post about evolution strategies - [blog post](https://blog.openai.com/evolution-strategies/), [article](https://arxiv.org/abs/1703.03864)
* Guide to genetic algorithms (english) - https://www.youtube.com/watch?v=ejxfTy4lI6I
* Another guide to genetic algorithm (english) - https://www.youtube.com/watch?v=zwYV11a__HQ
* PDF on Differential evolution (english) - http://jvanderw.une.edu.au/DE_1.pdf
* Video on Ant Colony Algorithm (english) - https://www.youtube.com/watch?v=D58nLNLkb0I
* Longer video on Ant Colony Algorithm (english) - https://www.youtube.com/watch?v=xpyKmjJuqhk

## More on crossentropy method:
* [__Lecture slides__](https://docviewer.yandex.ru/?url=ya-disk-public%3A%2F%2FG3IXcG62RwNUGSSos%2BuGhtgXNfsBjP9RxUtUfgCffIk%3D%3A%2Flecture1.pdf&name=lecture1.pdf&c=58a61ec9256c)
* Lecture and seminar videos (russian) - [lecture](https://yadi.sk/i/5yf_4oGI3EDJhJ), [seminar](https://yadi.sk/i/dPsWYMK13EDJj7) _only covering crossentropy method_
* [__main__] Lecture by J Schulman with crossentropy method explained (english) - https://www.youtube.com/watch?v=aUrX-rP_ss4&list=PLCTc_C7itk-GaAMxmlChrkPnGKtjz8hv1
* Article about CEM in general - https://people.smp.uq.edu.au/DirkKroese/ps/eormsCE.pdf
* Article about CEM for optimization - https://people.smp.uq.edu.au/DirkKroese/ps/CEopt.pdf
* Article about CEM in reinforcement learning - http://www.aaai.org/Papers/ICML/2003/ICML03-068.pdf


