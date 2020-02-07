# qlearningAgents.py
# ------------------
# based on http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random
import util
import math
from collections import defaultdict


class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate aka gamma)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
        - self.getQValue(state,action)
          which returns Q(state,action)
        - self.setQValue(state,action,value)
          which sets Q(state,action) := value

      !!!Important!!!
      NOTE: please avoid using self._qValues directly to make code cleaner
    """

    def __init__(self, **args):
        "We initialize agent and Q-values here."
        ReinforcementAgent.__init__(self, **args)
        self._qValues = defaultdict(lambda: defaultdict(lambda: 0))

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
        """
        return self._qValues[state][action]

    def setQValue(self, state, action, value):
        """
          Sets the Qvalue for [state,action] to the given value
        """
        self._qValues[state][action] = value

#---------------------#start of your code#---------------------#

    def getValue(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.
        """

        possibleActions = self.getLegalActions(state)
        # If there are no legal actions, return 0.0
        if len(possibleActions) == 0:
            return 0.0

        "*** YOUR CODE HERE ***"
        raise NotImplementedError

        return 0.

    def getPolicy(self, state):
        """
          Compute the best action to take in a state. 

        """
        possibleActions = self.getLegalActions(state)

        # If there are no legal actions, return None
        if len(possibleActions) == 0:
            return None

        best_action = None

        "*** YOUR CODE HERE ***"
        raise NotImplementedError

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

        # If there are no legal actions, return None
        if len(possibleActions) == 0:
            return None

        # agent parameters:
        epsilon = self.epsilon

        "*** YOUR CODE HERE ***"
        raise NotImplementedError

        return action

    def update(self, state, action, nextState, reward):
        """
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf


        """
        # agent parameters
        gamma = self.discount
        learning_rate = self.alpha

        "*** YOUR CODE HERE ***"
        raise NotImplementedError

        reference_qvalue = PleaseImplementMe
        updated_qvalue = PleaseImplementMe

        self.setQValue(PleaseImplementMe, PleaseImplementMe, updated_qvalue)


#---------------------#end of your code#---------------------#


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05, gamma=0.8, alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self, state)
        self.doAction(state, action)
        return action


class ApproximateQAgent(PacmanQAgent):
    pass
