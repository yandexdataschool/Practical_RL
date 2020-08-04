# environment.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

#!/usr/bin/python

class Environment:
        
  def getCurrentState(self):
    """
    Returns the current state of enviornment
    """
    abstract
    
  def getPossibleActions(self, state):
    """
      Returns possible actions the agent 
      can take in the given state. Can
      return the empty list if we are in 
      a terminal state.
    """
    abstract
                
  def doAction(self, action):
    """
      Performs the given action in the current
      environment state and updates the enviornment.
    
      Returns a (reward, nextState) pair
    """
    abstract
        
  def reset(self):
    """
      Resets the current state to the start state
    """
    abstract

  def isTerminal(self):
    """
      Has the enviornment entered a terminal
      state? This means there are no successors
    """
    state = self.getCurrentState()
    actions = self.getPossibleActions(state)
    return len(actions) == 0
    