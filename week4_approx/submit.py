import sys
import numpy as np
sys.path.append("..")
import grading


def submit_sessions(sessions, email, token):
    session_rewards, session_loss, session_steps = map(np.array, zip(*sessions))
    grader = grading.Grader("RDofv-QXEeeaGw6kpIOf3g")
    grader.set_answer("NRNkl", int(np.mean(session_rewards)))
    grader.submit(email, token)
