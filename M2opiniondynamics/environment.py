"""Enviroment for agents to interact in opinion dynamics simulation."""

import random
import agents
import parameters as p
import numpy as np  # type: ignore
import igraph as ig  # type: ignore


class Environment:
    def __init__(self):
        # Create a list of agents based
        self.agent_list = [agents.Agent(ID=i) for i in range(p.NUM_AGENTS)]
        self.opinions = []
        self.g = ig.Graph.Erdos_Renyi(
            n=p.NUM_AGENTS,
            p=p.MEAN_DEGREE / (p.NUM_AGENTS - 1),
            directed=False,
            loops=False,
        )
        self.network = {v.index: self.g.neighbors(v.index) for v in self.g.vs}

    def select_agents(self):
        """Select a random agent from the network along with a friend."""
        friends = []
        while not friends:  # ensure the selected agent has at least one friend
            index1 = random.randint(0, p.NUM_AGENTS - 1)  # select first agent index
            friends = self.network[index1]  # get friends of the first agent
            try:
                index2 = random.choice(friends)  # select a random friend index
            except IndexError:
                pass
        return [index1, index2]

    # Interaction process
    def interact(self):
        """Agents interact and possibly change opinions."""
        # sample a pair of agents
        pair = self.select_agents()  # list of two agent indices
        agent1 = self.agent_list[pair[0]]
        agent2 = self.agent_list[pair[1]]

        o1 = agent1.return_opinion()
        o2 = agent2.return_opinion()

        if o1 * o2 > 0:  # Same opinion
            # Opinion update rules - OG
            #     d1 = 1 - abs(o1)
            #     d2 = 1 - abs(o2)

            #     factor = 0.7  # Influence factor
            #     new_d1 = d1 * factor
            #     new_d2 = d2 * factor

            #     if o1 > 0:
            #         agent1.update_opinion(1 - new_d1)
            #         agent2.update_opinion(1 - new_d2)
            #     else:
            #         agent1.update_opinion(-1 + new_d1)
            #         agent2.update_opinion(-1 + new_d2)
            # End OG

            # Johns's logic
            new_op = min(abs(o1 + o2), 1)
            new_op = -new_op if o1 < 0 else new_op
            # End John's logic

        else:  # Different opinions
            new_op = (o1 + o2) / 2

        agent1.update_opinion(new_op)
        agent2.update_opinion(new_op)

    def change_friends(self):
        """Change friendship connections in the network.

        For a randomly selected agent, identify the friend with the maximum opinion difference.
        If the differnce is greater than a threshold, unfriend that friend and
        form a new friendship with a randomly selected agent not already a friend.
        """
        index1 = random.randint(0, p.NUM_AGENTS - 1)
        friends = self.network[index1]
        agent_opinion = self.agent_list[index1].return_opinion()
        unfriend_list = []

        if not friends:  # Ensure the agent has friends
            return

        # Identify friends with opinion difference greater than threshold
        for friend_index in friends:
            friend_opinion = self.agent_list[friend_index].return_opinion()
            opinion_diff = abs(agent_opinion - friend_opinion)
            if opinion_diff > p.FRIENDSHIP_THRESHOLD and (
                agent_opinion * friend_opinion < 0
            ):
                unfriend_list.append(friend_index)

        # Remove the friend with the opinion difference > threshold
        if unfriend_list:
            for f in unfriend_list:
                # Remove the old connection
                self.g.delete_edges([(index1, f)])

                # Add a new connection to a random agent not already a friend
                new_friend = random.randint(0, p.NUM_AGENTS - 1)
                while new_friend in friends or new_friend == index1:
                    new_friend = random.randint(0, p.NUM_AGENTS - 1)
                self.g.add_edges([(index1, new_friend)])

                # Update the network dictionary
                self.network[index1].remove(f)
                self.network[f].remove(index1)
                self.network[index1].append(new_friend)
                self.network[new_friend].append(index1)

    def all_pair_interaction(self):
        """All pairs interaction process."""
        num_interactions = int(p.PROP_INTERACTIONS * p.NUM_AGENTS / 2)
        for _ in range(num_interactions):
            self.interact()

    def time_steps(self):
        """Run the time steps."""
        for t in range(p.TIME_STEPS):
            self.all_pair_interaction()  # Interaction phase
            # self.change_friends()  # Friendship update phase
            self.record_opinions()  # Record opinions

    def record_opinions(self):
        """Record the opinions of all agents at the current time step."""
        all_op = []
        friend_count = []

        for agent in self.agent_list:
            agent.record_opinion_history()
            all_op.append(agent.return_opinion())
            friend_count.append(len(self.network[agent.ID]))

        op_mean = np.mean(all_op)
        op_sd = np.std(all_op)
        op_min = np.min(all_op)
        op_max = np.max(all_op)
        friends_mean = np.mean(friend_count)
        friends_sd = np.std(friend_count)

        self.opinions.append(
            (op_mean, op_sd, op_min, op_max, friends_mean, friends_sd)
        )  # Record mean and std dev as tuple

    def plot_network(self):
        """Plot the network of agents."""
        # Generate initial layout
        layout = self.g.layout("fr")
        ig.plot(
            self.g,
            layout=layout,
            vertex_size=5,
            vertex_color="skyblue",
            edge_color="gray",
            bbox=(800, 800),
            margin=20,
            target="network_plot.png",
        )
