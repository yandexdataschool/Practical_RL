import sys
import numpy as np
import gym
sys.path.append("..")
import grading


def submit_interface(policy, email, token):
    TIME_LIMIT = 250
    env = gym.wrappers.TimeLimit(gym.envs.classic_control.MountainCarEnv(),
                                max_episode_steps=TIME_LIMIT + 1)
    s = env.reset()
    actions = {'left': 0, 'stop': 1, 'right': 2}

    for t in range(TIME_LIMIT):
        s, r, done, _ = env.step(policy(t))
        if done:
            break
    else: 
        s = [-1]
    grader = grading.Grader("3T7pSSz0EeifGhJb4HAv7A")
    grader.set_answer("sDilm", s[0])
    grader.submit(email, token)


def submit_taxi(generate_session, policy, email, token):
    sessions = [generate_session(policy) for _ in range(100)]
    _, _, session_rewards = zip(*sessions)
    session_rewards = np.array(session_rewards)
    grader = grading.Grader("s4pTlNbTEeeQvQ7N1-Sa3A")
    grader.set_answer("GsMSL", np.mean(session_rewards))
    grader.submit(email, token)


def submit_mountain_car(generate_session, email, token):
    sessions = [generate_session() for _ in range(100)]
    _, _, session_rewards = zip(*sessions)
    session_rewards = np.array(session_rewards)
    grader = grading.Grader("EyYJW9bUEeeXyQ5ZPWKHGg")
    grader.set_answer("mXDUE", np.mean(session_rewards))
    grader.submit(email, token)
