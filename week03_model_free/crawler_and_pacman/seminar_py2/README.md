# Disclaimer
This assignment is not supported now. You can do it at your own risk.

_this assignment borrows code from awesome [cs188](http://ai.berkeley.edu/project_overview.html)_
This homework assignment works on __python2 only__. If you stick to py3, consider seminar_alternative. Or just install it for this homework alone and remove afterwards.

This homework also requires some physical display (e.g. laptop monitor). It won't work on a headless server. Please run it on a laptop or consider ./seminar_alternative


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
  * ./run_pacman.sh will need more epochs to converge, see [comments](https://github.com/yandexdataschool/Practical_RL/blob/master/week03_model_free/crawler_and_pacman/seminar_py2/run_pacman.sh)
  * on windows, just copy the type `python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid` in cmd from assignemnt dir


Remember seminar_py2 where your vanilla q-learning had hard time solving Pacman even on a small grid? Now's the time to fix that issue.

We'll focus on those grids for pacman setup.
* python pacman.py -p PacmanQAgent -x N_TRAIN_GAMES -n N_TOTAL_GAMES -l __mediumGrid__
* python pacman.py -p PacmanQAgent -x N_TRAIN_GAMES -n N_TOTAL_GAMES -l __mediumClassic__

Even if you adjust N_TRAIN_GAMES to 10^5 and N_TOTAL_GAMES to 10^5+100 (100 last games are for test), pacman won't solve those environments

The problem with those environments is that they have a large amount of unique states. However, you can devise a smaller environment state by choosing different observation parameters, e.g.:
 * distance and direction to nearest ghost
 * where is nearest food
 * 'center of mass' of all food points (and variance, and whatever)
 * is there a wall in each direction
 * and anything else you see fit

Here's how to get this information from [state](https://github.com/yandexdataschool/Practical_RL/blob/7a559f8/week03_model_free/seminar_py2/pacman.py#L49),
 * Get pacman position: [state.getPacmanPosition()](https://github.com/yandexdataschool/Practical_RL/blob/7a559f8/week03_model_free/seminar_py2/pacman.py#L128)
 * Is there a wall at (x,y)?: [state.hasWall(x,y)](https://github.com/yandexdataschool/Practical_RL/blob/7a559f8/week03_model_free/seminar_py2/pacman.py#L189)
 * Get ghost positions: [state.getGhostPositions()](https://github.com/yandexdataschool/Practical_RL/blob/7a559f8/week03_model_free/seminar_py2/pacman.py#L144)
 * Get all food positions: [state.getCapsules()](https://github.com/yandexdataschool/Practical_RL/blob/7a559f8/week03_model_free/seminar_py2/pacman.py#L153)

You can call those methods anywhere you see state.
 * e.g. in [agent.getValue(state)](https://github.com/yandexdataschool/Practical_RL/blob/7a559f8/week03_model_free/seminar_py2/qlearningAgents.py#L52)
 * Defining a function that extracts all features and calling it in [getQValue](https://github.com/yandexdataschool/Practical_RL/blob/7a559f8/week03_model_free/seminar_py2/qlearningAgents.py#L38) and [setQValue](https://github.com/yandexdataschool/Practical_RL/blob/7a559f8/week03_model_free/seminar_py2/qlearningAgents.py#L44) is probably enough.
 * You can also change agent parameters. The simplest way is to hard-code them in [PacmanQAgent](https://github.com/yandexdataschool/Practical_RL/blob/7a559f8/week03_model_free/seminar_py2/qlearningAgents.py#L140)

Also, don't forget to optimize ```learning_rate```, ```discount``` and ```epsilon``` params of model, this may also help to solve this env.
