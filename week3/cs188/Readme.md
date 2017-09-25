# 0. cs188 crawler and pacman demo
The first part of today's seminar will happen outside <s>the box</s> jupyter notebook.

You need to implement **QLearining** algorithm. You should go to ```cs188/``` folder and open file ```qlearningAgent.py```. You should implement missing functions and test your algo.

To run use those commands:
```
python crawler.py # Crawler with qlearning
python pacman.py -p <your agent> -x <number of train samples> -n <total number of samples> -l <grid env>
python pacman.py -p PacmanQAgent -x 5000 -n 5010 -l smallGrid # example
```
You have two agents: 
 - **PacmanQAgent** uses qlearning
 - **KeyboardAgent** <s>if you are getting tired with a seminar and want to play pacman</s> only for testing purposes
 
Grid can be:
 - **smallGrid** - simplies one
 - **mediumGrid** - harder
 - **mediumClassic** - original pacman
 - many other are at ```cs188/mediumGrid```
