"""Enviroment for agents to interact in opinion dynamics simulation."""

import random
import agents
import parameters as p


class Environment:
    def __init__(self):
        # Create a list of agents based
        self.agent_list = [agents.Agent(ID=i + 1) for i in range(p.NUM_AGENTS)]
        self.time_dynamics = {0: [], 1: []}  # To store data over time
        self.record_opinions()  # Record initial opinions

    # Interaction process
    def interact(self):
        """Agents interact and possibly change opinions based on resistance."""
        # sample a pair of agents
        pair = random.sample(self.agent_list, 2)
        agent1 = pair[0]
        agent2 = pair[1]

        o1 = agent1.return_opinion()
        o2 = agent2.return_opinion()

        if o1 != o2:
            # Get resistances
            r1 = agent1.return_resistance()
            r2 = agent2.return_resistance()

            if r1 < r2:
                agent1.update_opinion(agent2.return_opinion())
            elif r2 < r1:
                agent2.update_opinion(agent1.return_opinion())
            else:
                pass
                """No opinion change if resistances are equal"""

    def all_pair_interaction(self):
        """All pairs interaction process."""
        num_interactions = int(
            p.PROP_INTERACTIONS * p.NUM_AGENTS
        )  # ignoring /2 for simplicity
        for _ in range(num_interactions):
            self.interact()

    def time_steps(self):
        """Run the time steps."""
        for t in range(p.TIME_STEPS):
            self.all_pair_interaction()
            self.record_opinions()

    def record_opinions(self):
        """Record the opinions of all agents at the current time step."""
        zeros = 0
        ones = 0

        for agent in self.agent_list:
            if agent.return_opinion() == 0:
                zeros += 1
            else:
                ones += 1

        self.time_dynamics[0].append(zeros / p.NUM_AGENTS)
        self.time_dynamics[1].append(ones / p.NUM_AGENTS)
