import numpy as np
import sys
sys.path.append('../..')

import grading


def submit_seq2seq(test_scores, email, token):
    grader = grading.Grader("Xz763cqoEemssQpwd3-dGA")
    grader.set_answer("GzE7v", np.mean(test_scores))
    grader.submit(email, token)
