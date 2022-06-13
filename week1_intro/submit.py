from itertools import count

import gym
import numpy as np

import sys
sys.path.append("..")
import grading


def make_mountain_car(time_limit=None):
    env = gym.envs.classic_control.MountainCarEnv()
    if time_limit is not None:
        env = gym.wrappers.TimeLimit(env, max_episode_steps=time_limit + 1)
    return env


def interface_test(policy):
    with make_mountain_car(time_limit=250) as env:
        s = env.reset()
        for t in count():
            s, r, done, _ = env.step(policy(s, t))
            if done:
                break

    x, v = s
    print('Your car ended in state {{x={x}, v={v}}}.'.format(x=x, v=v))

    flag = 0.46
    print(f'The flag is located roughly at x={flag}. ' + ('You reached it!' if x >= flag else 'You did not reach it.'))

    return x


def taxi_test(generate_session, policy):
    with gym.make('Taxi-v3') as env:
        sessions = [generate_session(env, policy) for _ in range(100)]

    _, _, session_rewards = zip(*sessions)
    mean_reward = np.mean(session_rewards)
    print('Your average reward is {} over 100 episodes'.format(mean_reward))

    return mean_reward


def mountain_car_test(generate_session, agent):
    with make_mountain_car() as env:
        sessions = [generate_session(env, agent) for _ in range(100)]

    _, _, session_rewards = zip(*sessions)
    mean_reward = np.mean(session_rewards)
    print('Your average reward is {} over 100 episodes'.format(mean_reward))

    return mean_reward
