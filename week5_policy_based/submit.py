import gym
import numpy as np
import tqdm

import sys
sys.path.append("..")
import grading


def submit_cartpole(generate_session, email, token):
    env = gym.make("CartPole-v0")
    if hasattr(env, '_max_episode_steps'):
        env = env.env

    sessions = [generate_session(env) for _ in range(100)]
    session_rewards = np.array(sessions)
    grader = grading.Grader("oyT3Bt7yEeeQvhJmhysb5g")
    grader.set_answer("7QKmA", int(np.mean(session_rewards)))
    grader.submit(email, token)


def submit_kungfu(agent, env, evaluate, email, token):
    with tqdm.trange(10, desc='Evaluating your agent') as t:
        sessions = [evaluate(agent=agent, env=env, n_games=1) for _ in t]
    session_rewards = np.array(sessions)
    grader = grading.Grader("6sPnVCn6EeieSRL7rCBNJA")
    grader.set_answer("HhNVX", int(np.mean(session_rewards)))
    grader.submit(email, token)


def submit_cartpole_pytorch(generate_session, email, token):
    env = gym.make("CartPole-v0")
    if hasattr(env, '_max_episode_steps'):
        env = env.env

    sessions = [np.sum(generate_session(env)[2]) for _ in range(100)]
    session_rewards = np.array(sessions)
    grader = grading.Grader("oyT3Bt7yEeeQvhJmhysb5g")
    grader.set_answer("7QKmA", int(np.mean(session_rewards)))
    grader.submit(email, token)
