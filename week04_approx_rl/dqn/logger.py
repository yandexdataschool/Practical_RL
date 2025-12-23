import matplotlib.pyplot as plt
from torch.utils.tensorboard import SummaryWriter
import numpy as np

class Logger:
    def __init__(self, use_tensorboard=True, log_dir='runs'):
        """
        Initializes the Logger.

        :param use_tensorboard: If True, logs will be sent to TensorBoard.
        :param log_dir: Directory where TensorBoard logs are saved.
        """
        self.use_tensorboard = use_tensorboard
        if self.use_tensorboard:
            self.writer = SummaryWriter(log_dir=log_dir)
        else:
            # Initialize lists to store history for matplotlib
            self.mean_rw_history = []
            self.td_loss_history = []
            self.grad_norm_history = []
            self.initial_state_v_history = []

    def log_loss(self, loss, step):
        if self.use_tensorboard:
            self.writer.add_scalar("Loss", loss, step)
        else:
            self.td_loss_history.append(loss)

    def log_grad_norm(self, grad_norm, step):
        if self.use_tensorboard:
            self.writer.add_scalar("Grad Norm", grad_norm, step)
        else:
            self.grad_norm_history.append(grad_norm)

    def log_mean_reward(self, mean_reward, step):
        if self.use_tensorboard:
            self.writer.add_scalar("Mean Reward per Life", mean_reward, step)
        else:
            self.mean_rw_history.append(mean_reward)

    def log_initial_state_v(self, initial_v, step):
        if self.use_tensorboard:
            self.writer.add_scalar("Initial State V", initial_v, step)
        else:
            self.initial_state_v_history.append(initial_v)

    def plot(self):
        if not self.use_tensorboard:
            plt.figure(figsize=[16, 9])

            plt.subplot(2, 2, 1)
            plt.title("Mean Reward per Episode")
            plt.plot(self.mean_rw_history, label='Mean Reward')
            plt.legend()
            plt.grid()

            plt.subplot(2, 2, 2)
            plt.title("TD Loss History")
            plt.plot(self.td_loss_history, label='TD Loss')
            plt.legend()
            plt.grid()

            plt.subplot(2, 2, 3)
            plt.title("Initial State V")
            plt.plot(self.initial_state_v_history, label='Initial State V')
            plt.legend()
            plt.grid()

            plt.subplot(2, 2, 4)
            plt.title("Grad Norm History")
            plt.plot(self.grad_norm_history, label='Grad Norm')
            plt.legend()
            plt.grid()

            plt.tight_layout()
            plt.show()

    def close(self):
        if self.use_tensorboard:
            self.writer.close()