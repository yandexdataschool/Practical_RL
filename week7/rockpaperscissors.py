"""
Toy game for explaining how to work with POMDPs
"""
import gym
from gym import spaces
from gym.utils import seeding
import numpy as np

class RockPaperScissors(gym.Env):
    """
    Rock-paper-scissors game against an imperfect adversary.
    Your opponent operates in sequences of 3-7 actions.
    There are 5 such pre-defined sequences.
    Once enemy finishes his current sequence, he picks next one at random from 5 pre-defined sequences.
    
    Your observation is enemy's last turn:
    - [1,0,0] for rock
    - [0,1,0] for paper
    - [0,0,1] for scissors
    
    This game is a toy environment to play with recurrent networks in RL.
    """
    #codes of rock, papes and scissors respectively
    codes = np.eye(3)
    
    #list of possible sequences
    sequences = (
        (0,1,2,0,1,2),
        (1,0,0,1,1),
        (2,2,2),
        (2,2,1,1,0,0),
        (0,0,1,2,1,0,0)
    )
    #reward for [i-th] action against [j-th] enemy reaction
    reward = (
        # r   p  s
        ( 0, -1, 1), #r
        ( 1,  0,-1), #p
        (-1,  1, 0), #s
    )
    
    def __init__(self):
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(0,1,3)
        self.reset()

    def get_observation(self):
        return self.codes[self.current_sequence[self.current_position]]
    
    def new_sequence(self):
        self.current_sequence = np.random.choice(self.sequences)
        self.current_position = 0
    
    ###public methods
    def reset(self):
        self.new_sequence()
        return self.get_observation()

    def step(self, action):
        assert self.action_space.contains(action)
        
        self.current_position+=1
        if self.current_position >= len(self.current_sequence):
            self.new_sequence()
        
        enemy_action = self.current_sequence[self.current_position]
        reward = self.reward[action][enemy_action]
        return self.get_observation(), reward, False, {}
    
    def render(*args,**kwargs):
        return 0

