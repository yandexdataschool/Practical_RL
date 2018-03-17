import sys
import numpy as np
sys.path.append("..")
import grading


def submit_cartpole(generate_session, email, token):
    sessions = [generate_session() for _ in range(100)]
    session_rewards, _, _ = map(np.array, zip(*sessions))
    grader = grading.Grader("RDofv-QXEeeaGw6kpIOf3g")
    grader.set_answer("NRNkl", int(np.mean(session_rewards)))
    grader.submit(email, token)


def submit_breakout(agent, env, evaluate, email, token):
    sessions = [evaluate(env, agent, n_games=1) for _ in range(100)]
    session_rewards = np.array(sessions)
    grader = grading.Grader("WTOZHCn1EeiNwAoZNi-Hrg")
    grader.set_answer("VFM7Z", int(np.mean(session_rewards)))
    grader.submit(email, token)
