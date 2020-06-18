import numpy as np
import sys
sys.path.append('../..')

import grading


def submit_seq2seq(test_scores, email, token):
    mean_reward = np.mean(test_scores)
    print('Your average reward is {}'.format(mean_reward))

    grader = grading.Grader("Xz763cqoEemssQpwd3-dGA")
    grader.set_answer("GzE7v", mean_reward)
    grader.submit(email, token)
