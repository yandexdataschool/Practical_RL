
# Practical_RL [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/yandexdataschool/practical_rl/spring19)
An open course on reinforcement learning in the wild.
Taught on-campus at [HSE](https://cs.hse.ru) and [YSDA](https://yandexdataschool.com/)  and maintained to be friendly to online students (both english and russian).

__Note:__ this branch is an on-campus version of the for __spring 2019 YSDA and HSE students__. For full course materials, switch to the [master branch](https://github.com/yandexdataschool/Practical_RL/tree/master).


#### Manifesto:
* __Optimize for the curious.__ For all the materials that aren’t covered in detail there are links to more information and related materials (D.Silver/Sutton/blogs/whatever). Assignments will have bonus sections if you want to dig deeper.
* __Practicality first.__ Everything essential to solving reinforcement learning problems is worth mentioning. We won't shun away from covering tricks and heuristics. For every major idea there should be a lab that makes you to “feel” it on a practical problem.
* __Git-course.__ Know a way to make the course better? Noticed a typo in a formula? Found a useful link? Made the code more readable? Made a version for alternative framework? You're awesome! [Pull-request](https://help.github.com/articles/about-pull-requests/) it!

# Course info
* __Chat room__ for YSDA & HSE students is [here](https://t.me/joinchat/CDFcMVcoAQvEiI9WAo1pEQ)
* __Grading__ rules for YSDA & HSE students is [here](https://github.com/yandexdataschool/Practical_RL/wiki/Homeworks-and-grading)

* __FAQ:__ [About the course](https://github.com/yandexdataschool/Practical_RL/wiki/Practical-RL), [Technical issues thread](https://github.com/yandexdataschool/Practical_RL/issues/1), [Lecture Slides](https://yadi.sk/d/loPpY45J3EAYfU), [Online Student Survival Guide](https://github.com/yandexdataschool/Practical_RL/wiki/Online-student's-survival-guide)

* Anonymous [feedback form](https://docs.google.com/forms/d/e/1FAIpQLSdurWw97Sm9xCyYwC8g3iB5EibITnoPJW2IkOVQYE_kcXPh6Q/viewform).

* Virtual course environment: 
    * [Installing dependencies](https://github.com/yandexdataschool/Practical_RL/issues/1) on your local machine (recommended).
    * [__google colab__](https://colab.research.google.com/) - set open -> github -> yandexdataschool/pracical_rl -> {branch name} and select any notebook you want.
    * Alternatives: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/yandexdataschool/practical_rl/spring19) and [Azure Notebooks](https://notebooks.azure.com/).


# Additional materials
* [RL reading group](https://github.com/yandexdataschool/Practical_RL/wiki/RL-reading-group)


# Syllabus

The syllabus is approximate: the lectures may occur in a slightly different order and some topics may end up taking two weeks.

* [__week01_intro__](./week01_intro) Introduction
  * Lecture: RL problems around us. Decision processes. Stochastic optimization, Crossentropy method. Parameter space search vs action space search.
  * Seminar: Welcome into openai gym. Tabular CEM for Taxi-v0, deep CEM for box2d environments.
  * Homework description - see week1/README.md. 

* [__week02_value_based__](./week02_value_based) Value-based methods
  * Lecture: Discounted reward MDP. Value-based approach. Value iteration. Policy iteration. Discounted reward fails.
  * Seminar: Value iteration.  
  * Homework description - see week2/README.md. 
  
* [__week03_model_free__](./week03_model_free) Model-free reinforcement learning
  * Lecture: Q-learning. SARSA. Off-policy Vs on-policy algorithms. N-step algorithms. TD(Lambda).
  * Seminar: Qlearning Vs SARSA Vs Expected Value SARSA
  * Homework description - see week3/README.md. 

* __week04__ Approximate (deep) RL
* __week05__ Exploration
* __week06__ Policy Gradient methods
* __week07__ Applications I
* __week{++i}__ Partially Observed MDP
* __week{++i}__ Advanced policy-based methods
* __week{++i}__ Applications II
* __week{++i}__ Distributional reinforcement learning
* __week{++i}__ Inverse RL and Imitation Learning


# Course staff
Course materials and teaching by: _[unordered]_
- [Pavel Shvechikov](https://github.com/bestxolodec) - lectures, seminars, hw checkups, reading group
- [Nikita Putintsev](https://github.com/qwasser) - seminars, hw checkups, organizing our hot mess
- [Alexander Fritsler](https://github.com/Fritz449) - lectures, seminars, hw checkups
- [Oleg Vasilev](https://github.com/Omrigan) - seminars, hw checkups, technical support
- [Dmitry Nikulin](https://github.com/pastafarianist) - tons of fixes, far and wide
- [Mikhail Konobeev](https://github.com/MichaelKonobeev) - seminars, hw checkups
- [Ivan Kharitonov](https://github.com/neer201) - seminars, hw checkups
- [Ravil Khisamov](https://github.com/zshrav) - seminars, hw checkups
- [Fedor Ratnikov](https://github.com/justheuristic) - admin stuff

# Contributions
* Using pictures from [Berkeley AI course](http://ai.berkeley.edu/home.html)
* Massively refering to [CS294](http://rll.berkeley.edu/deeprlcourse/)
* Several tensorflow assignments by [Scitator](https://github.com/Scitator)
* A lot of fixes from [arogozhnikov](https://github.com/arogozhnikov)
* Other awesome people: see github [contributors](https://github.com/yandexdataschool/Practical_RL/graphs/contributors)
* [Alexey Umnov](https://github.com/alexeyum) helped us a lot during spring2018

