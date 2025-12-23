from __future__ import annotations

from collections.abc import Reversible
import numpy as np


def play_and_log_episode(env, agent, t_max=10000):
    """
    Plays an episode using the greedy policy and logs for each timestep:
    - state
    - qvalues (estimated by the agent)
    - actions
    - rewards

    Also logs:
    - the final (usually termo=inal) state.
    - whether the episode was terminated

    Uses the greedy policy.
    """
    assert t_max > 0, t_max

    states = []
    qvalues_all = []
    actions = []
    rewards = []

    s, _ = env.reset()
    for step in range(t_max):
        s = np.array(s)
        states.append(s)
        qvalues = agent.get_qvalues(s[None])[0]
        qvalues_all.append(qvalues)
        action = np.argmax(qvalues)
        actions.append(action)
        s, r, terminated, truncated, _ = env.step(action)
        rewards.append(r)
        if terminated or truncated:
            break
    states.append(s)  # the last state

    return_pack = {
        "states": np.array(states),
        "qvalues": np.array(qvalues_all),
        "actions": np.array(actions),
        "rewards": np.array(rewards),
        "episode_finished": terminated,
    }

    return return_pack
