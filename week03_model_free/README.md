#### __Lecture slides__ - [here](https://yadi.sk/i/54qWKtDB3NDeuh)
### Materials
* Russian materials:
   - Lecture - [video](https://yadi.sk/i/jcQ1Bg8n3SrhuQ)
   - Q-learning seminar - [video](https://yadi.sk/i/dQmolwOy3EtGNK)
   - Sarsa & stuff - [seminar2](https://yadi.sk/i/XbqNQmjm3ExNsq)
* English materials:
   - Lecture by David Silver (english) - [video part I](https://www.youtube.com/watch?v=PnHCvfgC_ZA), [video part II](https://www.youtube.com/watch?v=0g4j2k_Ggc4&t=43s)
   - Alternative lecture by Pieter Abbeel (english) - [video](https://www.youtube.com/watch?v=ifma8G7LegE)
   - Alternative lecture by John Schulmann (english) - [video](https://www.youtube.com/watch?v=IL3gVyJMmhg)
   - Blog post on q-learning Vs SARSA - [url](https://studywolf.wordpress.com/2013/07/01/reinforcement-learning-sarsa-vs-q-learning/)

### More materials
* N-step temporal difference from Sutton's book - [suttonbook](http://incompleteideas.net/book/RLbook2018.pdf) __chapter 7__
* Eligibility traces from Sutton's book - [suttonbook](http://incompleteideas.net/book/RLbook2018.pdf) __chapter 12__
* Blog post on eligibility traces - [url](http://pierrelucbacon.com/traces/)

### Assignments

Just as usual, start with 
- `seminar_qlearning.ipynb` 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yandexdataschool/Practical_RL/blob/master/week03_model_free/seminar_qlearning.ipynb)

and then proceed to 

- `homework.ipynb`
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yandexdataschool/Practical_RL/blob/master/week03_model_free/homework.ipynb)

Please pay attention for uncommenting first lines in code if you use Colab.

---
(optional) If you're running on a local machine (e.g. your pc) with python2, you can also try `seminar_py2`. It has some neat RL problems with cool visualizations.

### ./seminar_py2
_this assignment borrows code from awesome [cs188](http://ai.berkeley.edu/project_overview.html)_
This homework assignment works on __python2 only__. If you stick to py3, consider seminar_alternative. Or just install it for this homework alone and remove afterwards.

This homework also requires some physical display (e.g. laptop monitor). It won't work on binder VM / headless server. Please run it on laptop or consider ./seminar_alternative


* You need to implement **QLearining** algorithm.

Once you're done, run use those commands:
```
python crawler.py # Crawler with qlearning
python pacman.py -p <your agent> -x <number of train samples> -n <total number of samples> -l <grid env>
python pacman.py -p PacmanQAgent -x 5000 -n 5010 -l smallGrid # example
```
* Make sure you can tune agent to beat ./run_crawler.sh
 * on windows, just run `python crawler.py` from cmd in the project directory
* other ./run* files are mostly for your amusement. 
  * ./run_pacman.sh will need more epochs to converge, see [comments](https://github.com/yandexdataschool/Practical_RL/blob/master/week03_model_free/seminar_py2/run_pacman.sh)
  * on windows, just copy the type `python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid` in cmd from assignemnt dir
(YSDA/HSE) Please submit only qlearningAgents.py file and include a brief text report as comments in it.

