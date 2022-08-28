import numpy as np

import sys
sys.path.append("..")


def test_qlearning(rewards_q1, rewards_q2):
    test_outputs = {}
    flag1 = np.mean(rewards_q1[-10:])
    test_outputs['Q-learning I'] = flag1

    flag2 = np.mean(rewards_q2[-10:])
    test_outputs['Q-learning 2'] = flag2
    
    return test_outputs


def test_sarsa(rewards_ql, rewards_sarsa):
    test_outputs = {}
    flag1 = np.mean(rewards_ql[-100:])
    flag2 = np.mean(rewards_sarsa[-100:])
    flag3 = np.mean(rewards_sarsa[-100:]) - np.mean(rewards_ql[-100:])

    test_outputs['Q-learning rewards'] = flag1
    test_outputs['SARSA rewards'] = flag2
    test_outputs['Advantage rewards'] = flag3
    
    return test_outputs


def test_experience_replay(rewards_replay, rewards_baseline):
    test_outputs = {}
    flag1 = np.mean(rewards_replay[-100:])
    flag2 = np.mean(rewards_baseline[-100:])
    flag3 = np.mean(rewards_replay[:100]) - np.mean(rewards_baseline[:100])
    
    test_outputs['Replay reward'] = flag1
    test_outputs['Baseline reward'] = flag2
    test_outputs['Advantage reward'] = flag3
    
    return test_outputs

