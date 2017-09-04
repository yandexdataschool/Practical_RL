# textDisplay.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import pacman, time

DRAW_EVERY = 1
SLEEP_TIME = 0 # This can be overwritten by __init__
DISPLAY_MOVES = False
QUIET = False # Supresses output

class NullGraphics:
  def initialize(self, state, isBlue = False):
    pass
  
  def update(self, state):
    pass
  
  def pause(self):
    time.sleep(SLEEP_TIME)
    
  def draw(self, state):
    print state
  
  def finish(self):
    pass

class PacmanGraphics:
  def __init__(self, speed=None):
    if speed != None:
      global SLEEP_TIME
      SLEEP_TIME = speed
  
  def initialize(self, state, isBlue = False):
    self.draw(state)
    self.pause()
    self.turn = 0
    self.agentCounter = 0
    
  def update(self, state):
    numAgents = len(state.agentStates)
    self.agentCounter = (self.agentCounter + 1) % numAgents
    if self.agentCounter == 0:
      self.turn += 1
      if DISPLAY_MOVES:
        ghosts = [pacman.nearestPoint(state.getGhostPosition(i)) for i in range(1, numAgents)]
        print "%4d) P: %-8s" % (self.turn, str(pacman.nearestPoint(state.getPacmanPosition()))),'| Score: %-5d' % state.score,'| Ghosts:', ghosts
      if self.turn % DRAW_EVERY == 0:
        self.draw(state)
        self.pause()
    if state._win or state._lose:
      self.draw(state)
    
  def pause(self):
    time.sleep(SLEEP_TIME)
    
  def draw(self, state):
    print state
  
  def finish(self):
    pass
