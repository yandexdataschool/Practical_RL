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


def submit_interface(policy, email, token):
    with make_mountain_car(time_limit=250) as env:
        s = env.reset()
        for t in count():
            s, r, done, _ = env.step(policy(s, t))
            if done:
                break

    x, v = s
    print('Your car ended in state {{x={x}, v={v}}}.'.format(x=x, v=v))

    flag = 0.46  # Used only for reporting to the learner. Coursera grader stores this number separately.
    print(f'The flag is located roughly at x={flag}. ' + ('You reached it!' if x >= flag else 'You did not reach it.'))

    grader = grading.Grader("3T7pSSz0EeifGhJb4HAv7A")
    grader.set_answer("sDilm", x)
    grader.submit(email, token)


def submit_taxi(generate_session, policy, email, token):
    with gym.make('Taxi-v3') as env:
        sessions = [generate_session(env, policy) for _ in range(100)]

    _, _, session_rewards = zip(*sessions)
    mean_reward = np.mean(session_rewards)
    print('Your average reward is {} over 100 episodes'.format(mean_reward))

    grader = grading.Grader("s4pTlNbTEeeQvQ7N1-Sa3A")
    grader.set_answer("GsMSL", mean_reward)
    grader.submit(email, token)


def submit_mountain_car(generate_session, agent, email, token):
    with make_mountain_car() as env:
        sessions = [generate_session(env, agent) for _ in range(100)]

    _, _, session_rewards = zip(*sessions)
    mean_reward = np.mean(session_rewards)
    print('Your average reward is {} over 100 episodes'.format(mean_reward))

    grader = grading.Grader("EyYJW9bUEeeXyQ5ZPWKHGg")
    grader.set_answer("mXDUE", mean_reward)
    grader.submit(email, token)
