import gym
import numpy as np
import tqdm

import sys
sys.path.append("..")
import grading


def submit_cartpole(generate_session, email, token):
    with gym.make("CartPole-v0").env as env:
        session_rewards = [np.sum(generate_session(env)[2]) for _ in range(100)]
    mean_reward = np.mean(session_rewards)
    print('Your average reward is {} over 100 episodes'.format(mean_reward))

    grader = grading.Grader("oyT3Bt7yEeeQvhJmhysb5g")
    grader.set_answer("7QKmA", mean_reward)
    grader.submit(email, token)


def submit_kungfu(agent, env, evaluate, email, token):
    with tqdm.trange(10, desc='Evaluating your agent') as progress_bar:
        session_rewards = [evaluate(agent=agent, env=env, n_games=1) for _ in progress_bar]
    mean_reward = np.mean(session_rewards)
    print('Your average reward is {} over 10 episodes'.format(mean_reward))

    grader = grading.Grader("6sPnVCn6EeieSRL7rCBNJA")
    grader.set_answer("HhNVX", mean_reward)
    grader.submit(email, token)
