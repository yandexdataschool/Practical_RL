import gym
import numpy as np
import tqdm

import sys
sys.path.append("..")


def test_cartpole(generate_session):
    with gym.make("CartPole-v0").env as env:
        session_rewards = [np.sum(generate_session(env)[2]) for _ in range(100)]
    mean_reward = np.mean(session_rewards)
    print('Your average reward is {} over 100 episodes'.format(mean_reward))

    return mean_reward


def test_kungfu(agent, env, evaluate):
    with tqdm.trange(10, desc='Evaluating your agent') as progress_bar:
        session_rewards = [evaluate(agent=agent, env=env, n_games=1) for _ in progress_bar]
    mean_reward = np.mean(session_rewards)
    print('Your average reward is {} over 10 episodes'.format(mean_reward))

    return mean_reward

