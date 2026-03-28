"""The environment for the M6Study model."""

import igraph as ig  # type: ignore
import matplotlib.pyplot as plt  # type: ignore


class Environment:
    """The environment for the M6Study model, which includes a social network."""

    def __init__(self, agents):
        self.num_agents = len(agents)
        self.network = self.create_social_network()
        self.agent_network = self.create_agent_network(agents)

    def create_social_network(self):
        """Create a random social network using igraph."""
        g = ig.Graph.Erdos_Renyi(n=self.num_agents, p=0.1)  # 10% chance of connection
        return g

    def create_agent_network(self, agents):
        """create a mapping of agent IDs to their neighbors in the social network."""
        g = ig.Graph()
        for agent in agents:
            g.add_vertex(obj=agent, name=str(agent.ID))
        for agent in agents:
            for friend_id in agent.friends:
                g.add_edge(str(agent.ID), str(friend_id))
        return g

    def get_neighbors(self, agent_id):
        """Get the neighbors of a given agent in the social network."""
        return self.agent_network.neighbors(agent_id)

    def display_agent_network(self):
        """Display the social network."""
        fig, ax = plt.subplots(figsize=(8, 8))
        ig.plot(
            self.agent_network,
            target=ax,
            layout="fr",
            vertex_size=20,
            vertex_color="lightblue",
            vertex_label=[v["name"] for v in self.agent_network.vs],
            edge_color="gray",
        )
        plt.show()
