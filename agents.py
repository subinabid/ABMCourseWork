"""Agents for opinion dynamics simulation."""

import random


class Agent:
    def __init__(self, ID):
        self.ID = ID
        self.opinion = random.randint(0, 1)  # Initial opinion: 0 or 1
        self.resistance = random.uniform(0, 1)  # Resistance to opinion change
        self.friends = []  # List of friends (other agents)

    def update_opinion(self, new_opinion):
        """Update the agent's opinion"""
        self.opinion = new_opinion

    def return_opinion(self):
        """Return the agent's current opinion"""
        return self.opinion

    def return_resistance(self):
        """Return the agent's resistance to opinion change"""
        return self.resistance
