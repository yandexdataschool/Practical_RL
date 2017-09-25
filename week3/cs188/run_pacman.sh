#!/bin/bash
python pacman.py -p PacmanQAgent -x 1000 -n 1010 -l smallGrid

# -x is the amount of training epochs, -n is the total amount of epochs.
# hence, if you want to spend 1337 epochs training and then play 42 for evalution, you will need
# python pacman.py -p PacmanQAgent -x 1337 -n 1379 -l smallGrid
