import sys
import numpy as np
sys.path.append("..")
import grading

from mdp import MDP, FrozenLakeEnv


def submit_assigment(
        get_action_value,
        get_new_state_value,
        get_optimal_action,
        value_iteration,
        email,
        token):
    grader = grading.Grader("EheZDOgLEeenIA4g5qPHFA")
    sys.stdout = None

    transition_probs = {
        's0': {
            'a0': {'s1': 0.8, 's2': 0.2},
            'a1': {'s1': 0.2, 's2': 0.8},
        },
        's1': {
            'a0': {'s0': 0.2, 's2': 0.8},
            'a1': {'s0': 0.8, 's2': 0.2},
        },
        's2': {
            'a0': {'s3': 0.5, 's4': 0.5},
            'a1': {'s3': 1.0},
        },
        's3': {
            'a0': {'s1': 0.9, 's2': 0.1},
            'a1': {'s1': 0.7, 's2': 0.3},
        },
        's4': {
            'a0': {'s3': 1.0},
            'a1': {'s3': 0.7, 's1': 0.3},
        }
    }
    rewards = {
        's0': {'a0': {'s1': 0, 's2': 1}, 'a1': {'s1': 0, 's2': 1}},
        's1': {'a0': {'s0': -1, 's2': 1}, 'a1': {'s0': -1, 's2': 1}},
        's2': {'a0': {'s3': 0, 's4': 1}, 'a1': {'s3': 0, 's4': 1}},
        's3': {'a0': {'s1': -3, 's2': -3}, 'a1': {'s1': -3, 's2': -3}},
        's4': {'a1': {'s1': +10}}
    }

    mdp = MDP(transition_probs, rewards, initial_state='s0')

    test_Vs = {s: i for i, s in enumerate(mdp.get_all_states())}
    qvalue1 = get_action_value(mdp, test_Vs, 's1', 'a0', 0.9)
    qvalue2 = get_action_value(mdp, test_Vs, 's4', 'a1', 0.9)

    grader.set_answer("F16dC", qvalue1 + qvalue2)

    # ---

    svalue1 = get_new_state_value(mdp, test_Vs, 's2', 0.9)
    svalue2 = get_new_state_value(mdp, test_Vs, 's4', 0.9)

    grader.set_answer("72cBp", svalue1 + svalue2)

    # ---

    state_values = {s: 0 for s in mdp.get_all_states()}
    gamma = 0.9

    # ---

    action1 = get_optimal_action(mdp, state_values, 's1', gamma)
    action2 = get_optimal_action(mdp, state_values, 's2', gamma)

    grader.set_answer("xIuti", action1 + action2)

    # ---

    s = mdp.reset()
    rewards = []
    for _ in range(10000):
        s, r, done, _ = mdp.step(get_optimal_action(mdp, state_values, s, gamma))
        rewards.append(r)

    grader.set_answer("Y8g0j", np.mean(rewards) + np.std(rewards))

    mdp = FrozenLakeEnv(slip_chance=0.25)
    state_values = value_iteration(mdp)
    gamma = 0.9

    total_rewards = []
    for game_i in range(1000):
        s = mdp.reset()
        rewards = []
        for t in range(100):
            s, r, done, _ = mdp.step(get_optimal_action(mdp, state_values, s, gamma))
            rewards.append(r)
            if done: break
        total_rewards.append(np.sum(rewards))

    grader.set_answer("ABf1b", np.mean(total_rewards) + np.std(total_rewards))

    # ---

    mdp = FrozenLakeEnv(slip_chance=0.25, map_name='8x8')
    state_values = value_iteration(mdp)
    gamma = 0.9

    total_rewards = []
    for game_i in range(1000):
        s = mdp.reset()
        rewards = []
        for t in range(100):
            s, r, done, _ = mdp.step(get_optimal_action(mdp, state_values, s, gamma))
            rewards.append(r)
            if done: break
        total_rewards.append(np.sum(rewards))

    grader.set_answer("U3RzE", np.mean(total_rewards) + np.std(total_rewards))

    sys.stdout = sys.__stdout__
    grader.submit(email, token)
