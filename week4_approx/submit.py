import sys
import numpy as np
import gym
sys.path.append("..")
import grading


def submit_cartpole(generate_session, email, token):
    with gym.make("CartPole-v0").env as env:
        session_rewards = [generate_session(env) for _ in range(100)]
    mean_reward = np.mean(session_rewards)
    print('Your average reward is {} over 100 episodes'.format(mean_reward))

    grader = grading.Grader("RDofv-QXEeeaGw6kpIOf3g")
    grader.set_answer("NRNkl", mean_reward)
    grader.submit(email, token)


def submit_breakout(agent, env, evaluate, email, token):
    session_rewards = [evaluate(env, agent, n_games=1) for _ in range(100)]
    mean_reward = np.mean(session_rewards)
    print('Your average reward is {} over 100 episodes'.format(mean_reward))

    grader = grading.Grader("WTOZHCn1EeiNwAoZNi-Hrg")
    grader.set_answer("VFM7Z", mean_reward)
    grader.submit(email, token)
