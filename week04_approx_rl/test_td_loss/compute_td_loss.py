import torch
import torch.nn as nn
from typing import Protocol


class ComputeTdLossProtocol(Protocol):
    """
    An Protocol which the compute_td_loss function should match.
    """

    def __call__(
        self,
        states: torch.Tensor,
        actions: torch.Tensor,
        rewards: torch.Tensor,
        next_states: torch.Tensor,
        is_done: torch.Tensor,
        agent: nn.Module,
        target_network: nn.Module,
        gamma: float,
    ):
        pass


class MockAgent(nn.Module):
    """
    An nn.Module, which outputs a value which does not depend on its input.
    Designed to be used for testing the compute_td_loss function.
    """

    def __init__(self, output_q_values: torch.Tensor):
        super().__init__()
        assert output_q_values.dtype == torch.float, output_q_values.dtype
        assert output_q_values.ndim == 2, output_q_values.shape
        self.output_q_values = nn.Parameter(output_q_values)

    def forward(self, state):
        return torch.clone(self.output_q_values)


@torch.no_grad()
def test_is_done_is_used(compute_td_loss: ComputeTdLossProtocol):
    """
    Tries to catch the error when compute_td_loss ignores its is_done argument.
    """

    states = torch.empty(1)
    actions = torch.tensor([0])
    rewards = torch.tensor([1], dtype=torch.float)
    is_done_first = torch.tensor([True])
    is_done_second = torch.tensor([False])
    next_states = torch.empty(1)
    gamma = 0.99

    q_values_agent = torch.tensor([[1, 1, 1]], dtype=torch.float)
    q_values_target_network = torch.tensor([[1, 1, 1]], dtype=torch.float)
    agent = MockAgent(q_values_agent)
    target_network = MockAgent(q_values_target_network)

    loss_kwargs = dict(
        states=states,
        actions=actions,
        rewards=rewards,
        next_states=next_states,
        agent=agent,
        target_network=target_network,
        gamma=gamma,
    )

    loss_first = compute_td_loss(is_done=is_done_first, **loss_kwargs).item()
    loss_second = compute_td_loss(is_done=is_done_second, **loss_kwargs).item()

    abs_diff = abs(loss_first - loss_second)
    if abs_diff > 0.5:
        msg = "compute_td_loss returned close values for different is_done inputs"

    assert abs(loss_first - loss_second) > 0.5, msg


@torch.no_grad()
def test_compute_td_loss_vanilla(compute_td_loss: ComputeTdLossProtocol):
    """
    Checks compute_td_loss on manually precomputed examples.
    Note: this is a test for vanilla compute_td_loss
    and it should NOT be used for double_dqn
    """

    samples = [
        {
            "q_agent": [0, 1, 2],
            "action": 1,
            "is_done": False,
            "q_target": [0, 1, 2],
            "gamma": 0.5,
            "reward": 5,
            "answer": 25,
        },
        {
            "q_agent": [0, 1, 2],
            "action": 1,
            "is_done": False,
            "q_target": [2, 0, 1],
            "gamma": 0.5,
            "reward": 5,
            "answer": 25,
        },
        {
            "q_agent": [3, 1, 2],
            "action": 1,
            "is_done": True,
            "q_target": [0, 1, 2],
            "gamma": 0.5,
            "reward": 5,
            "answer": 16,
        },
        {
            "q_agent": [0, 1, 2],
            "action": 0,
            "is_done": False,
            "q_target": [0, 1, 2],
            "gamma": 0.5,
            "reward": 5,
            "answer": 36,
        },
    ]

    for sample in samples:
        agent = MockAgent(torch.tensor(sample["q_agent"], dtype=torch.float)[None])
        tn = MockAgent(torch.tensor(sample["q_target"], dtype=torch.float)[None])
        ans = compute_td_loss(
            states=torch.empty(1),
            actions=torch.tensor(sample["action"])[None],
            rewards=torch.tensor(sample["reward"])[None],
            next_states=torch.empty(1),
            is_done=torch.tensor(sample["is_done"])[None],
            agent=agent,
            target_network=tn,
            gamma=sample["gamma"],
        ).item()
        abs_diff = abs(ans - sample["answer"])
        assert abs_diff < 1e-8, abs_diff


@torch.no_grad()
def test_compute_td_loss_double(compute_td_loss: ComputeTdLossProtocol):
    """
    Checks compute_td_loss on manually precomputed examples.
    Note: this is a test for vanilla compute_td_loss
    and it should NOT be used for double_dqn
    """

    samples = [
        {
            "q_agent": [0, 1, 2],
            "action": 1,
            "is_done": False,
            "q_target": [0, 1, 2],
            "gamma": 0.5,
            "reward": 5,
            "answer": 25,
        },
        {
            "q_agent": [0, 1, 2],
            "action": 1,
            "is_done": False,
            "q_target": [2, 0, 1],
            "gamma": 0.5,
            "reward": 5,
            "answer": 20.25,
        },
        {
            "q_agent": [3, 1, 2],
            "action": 1,
            "is_done": False,
            "q_target": [-1, 1, 2],
            "gamma": 0.5,
            "reward": 5,
            "answer": 12.25,
        },
        {
            "q_agent": [3, 1, 2],
            "action": 1,
            "is_done": True,
            "q_target": [-1, 1, 2],
            "gamma": 0.5,
            "reward": 5,
            "answer": 16,
        },
        {
            "q_agent": [0, 1, 2],
            "action": 0,
            "is_done": False,
            "q_target": [0, 1, 2],
            "gamma": 0.5,
            "reward": 5,
            "answer": 36,
        },
    ]

    for sample in samples:
        agent = MockAgent(torch.tensor(sample["q_agent"], dtype=torch.float)[None])
        tn = MockAgent(torch.tensor(sample["q_target"], dtype=torch.float)[None])
        ans = compute_td_loss(
            states=torch.empty(1),
            actions=torch.tensor(sample["action"])[None],
            rewards=torch.tensor(sample["reward"])[None],
            next_states=torch.empty(1),
            is_done=torch.tensor(sample["is_done"])[None],
            agent=agent,
            target_network=tn,
            gamma=sample["gamma"],
        ).item()
        abs_diff = abs(ans - sample["answer"])
        assert abs_diff < 1e-8, abs_diff
