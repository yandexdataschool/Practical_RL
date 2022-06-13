import sys
import numpy as np
import gym
sys.path.append("..")


def test_cartpole(generate_session):
    with gym.make("CartPole-v0").env as env:
        session_rewards = [generate_session(env) for _ in range(100)]
    mean_reward = np.mean(session_rewards)
    print('Your average reward is {} over 100 episodes'.format(mean_reward))

    return mean_reward


def test_breakout(agent, env, evaluate):
    session_rewards = [evaluate(env, agent, n_games=1) for _ in range(100)]
    mean_reward = np.mean(session_rewards)
    print('Your average reward is {} over 100 episodes'.format(mean_reward))

    return mean_reward
