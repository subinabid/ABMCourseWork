import environment
from matplotlib import pyplot as plt

env = environment.Environment()


def plot_opinion_dynamics(filename="time_dynamics.png"):
    """Plot the opinion dynamics"""
    data = env.time_dynamics
    plt.scatter(range(len(data[0])), data[0], label="Opinion 0s")
    plt.scatter(range(len(data[1])), data[1], label="Opinion 1s")

    plt.xlabel("Time Steps")
    plt.ylabel("Proportion of Agents")
    plt.title("Opinion Dynamics Over Time")
    plt.legend()
    plt.savefig(filename)
    plt.close()


def run_simulations():
    for i in range(10):
        env.time_steps()
        plot_opinion_dynamics(filename=f"time_dynamics_{i}.png")


run_simulations()
