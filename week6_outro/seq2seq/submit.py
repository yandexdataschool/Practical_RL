import numpy as np
import sys
sys.path.append('../..')


def test_seq2seq(test_scores):
    mean_reward = np.mean(test_scores)
    print('Your average reward is {}'.format(mean_reward))

    return mean_reward
