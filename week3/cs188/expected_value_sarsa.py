"""
Expected Value SARSA
This file builds upon the same functions as Q-learning agent (qlearning.py).

[assignment]
The only thing you must implement is the getValue method.
- Recall that V(s) in SARSA is not the maximal but the expected Q-value.
- The expectation should be done under agent's policy (e-greedy).


Here's usage example:
>>>from expected_value_sarsa import EVSarsaAgent

>>>agent = EVSarsaAgent(alpha=0.5,epsilon=0.25,discount=0.99,
                       getLegalActions = lambda s: actions_from_that_state)
>>>action = agent.getAction(state)
>>>agent.update(state,action, next_state,reward)
>>>agent.epsilon *= 0.99
"""

import random,math

import numpy as np
from collections import defaultdict

class EVSarsaAgent():
  """
    Expected Value SARSA Agent.
    
    The two main methods are 
    - self.getAction(state) - returns agent's action in that state
    - self.update(state,action,nextState,reward) - returns agent's next action

    Instance variables you have access to
      - self.epsilon (exploration prob)
      - self.alpha (learning rate)
      - self.discount (discount rate aka gamma)

  """
  def __init__(self,alpha,epsilon,discount,getLegalActions):
    "We initialize agent and Q-values here."
    self.getLegalActions= getLegalActions
    self._qValues = defaultdict(lambda:defaultdict(lambda:0))
    self.alpha = alpha
    self.epsilon = epsilon
    self.discount = discount
    
  def getQValue(self, state, action):
    """
      Returns Q(state,action)
    """
    return self._qValues[state][action]

  def setQValue(self,state,action,value):
    """
      Sets the Qvalue for [state,action] to the given value
    """
    self._qValues[state][action] = value

#---------------------#start of your code#---------------------#

  def getValue(self, state):
    """
      Returns V(s) according to expected value SARSA algorithm
      This should be equal to expected action q-value over action probabilities defined
      by epsilon-greedy policy with current epsilon.
    """
    
    possibleActions = self.getLegalActions(state)
    #If there are no legal actions, return 0.0
    if len(possibleActions) == 0:
    	return 0.0

    #You'll need this to estimate action probabilities
    epsilon = self.epsilon
    
    value = <Your Code Here>
    return value
    
  def getPolicy(self, state):
    """
      Compute the best action to take in a state. 
      
    """
    possibleActions = self.getLegalActions(state)

    #If there are no legal actions, return None
    if len(possibleActions) == 0:
    	return None
    
    best_action = None

    best_action = possibleActions[np.argmax([self.getQValue(state, a) for a in possibleActions])]
    return best_action

  def getAction(self, state):
    """
      Compute the action to take in the current state, including exploration.  
      
      With probability self.epsilon, we should take a random action.
      otherwise - the best policy action (self.getPolicy).

      HINT: You might want to use util.flipCoin(prob)
      HINT: To pick randomly from a list, use random.choice(list)

    """
    
    # Pick Action
    possibleActions = self.getLegalActions(state)
    action = None
    
    #If there are no legal actions, return None
    if len(possibleActions) == 0:
    	return None

    #agent parameters:
    epsilon = self.epsilon

    if np.random.random()<=epsilon:
    	return random.choice(possibleActions)
    else:
    	action = self.getPolicy(state)
    return action

  def update(self, state, action, nextState, reward):
    """
      You should do your Q-Value update here

      NOTE: You should never call this function,
      it will be called on your behalf


    """
    #agent parameters
    gamma = self.discount
    learning_rate = self.alpha
    
    reference_qvalue = reward + gamma * self.getValue(nextState)
    updated_qvalue = (1-learning_rate) * self.getQValue(state,action) + learning_rate * reference_qvalue
    self.setQValue(state,action,updated_qvalue)


#---------------------#end of your code#---------------------#


