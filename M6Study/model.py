"""A simple Model"""

import random

from agents import Agent
from environment import Environment
from parameters import NUMBER_OF_AGENTS, NUMBER_OF_TIME_STEPS, FRIENDSHIP_THRESHOLD


class Model:
    def __init__(self):
        self.agents = [Agent(i) for i in range(NUMBER_OF_AGENTS)]
        self.add_init_friends()
        self.env = Environment(self.agents)

    def add_init_friends(self):
        """Add few friends to each agent at the beginning of the simulation."""
        for agent in self.agents:
            num_friends = min(
                2, NUMBER_OF_AGENTS - 1
            )  # Each agent can have up to 3 friends
            friends = random.sample(
                [a.ID for a in self.agents if a.ID != agent.ID], num_friends
            )
            for friend_id in friends:
                agent.add_friend(friend_id)
                self.agents[friend_id].add_friend(
                    agent.ID
                )  # Ensure friendship is mutual

    def show_friends(self):
        """Show the friends of each agent."""
        for agent in self.agents:
            print(f"Agent {agent.ID} has friends: {agent.friends}")

    def display_results(self):
        """Display the results of the simulation."""
        for agent in self.agents:
            print(f"Agent {agent.ID}: Opinion history: {agent.history}")

    def run(self):
        """Run the simulation."""
        for t in range(NUMBER_OF_TIME_STEPS):
            for agent in self.agents:
                neighbors = self.env.get_neighbors(agent.ID)
                if neighbors:
                    neighbor_opinions = [
                        self.agents[n].return_opinion() for n in neighbors
                    ]
                    new_opinion = sum(neighbor_opinions) / len(neighbor_opinions)
                    agent.update_opinion(new_opinion)
                agent.record_opinion_history()

    def plot_opinion_dynamics(self):
        """Plot the opinion dynamics of all agents over time."""
        import matplotlib.pyplot as plt  # type: ignore

        for agent in self.agents:
            plt.plot(agent.history, label=f"Agent {agent.ID}")
        plt.xlabel("Time Step")
        plt.ylabel("Opinion")
        plt.title("Opinion Dynamics Over Time")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    model = Model()
    model.run()
    model.plot_opinion_dynamics()
