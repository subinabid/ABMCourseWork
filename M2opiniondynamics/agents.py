"""Agents for opinion dynamics simulation."""

import random


class Agent:
    def __init__(self, ID):
        self.ID = ID
        self.opinion = random.uniform(-1, 1)  # Initial opinion: between -1 and 1
        self.resistance = random.uniform(0, 1)  # Resistance to opinion change
        self.history = []

    def update_opinion(self, new_opinion):
        """Update the agent's opinion"""
        self.opinion = new_opinion

    def return_opinion(self):
        """Return the agent's current opinion"""
        return self.opinion

    def return_resistance(self):
        """Return the agent's resistance to opinion change"""
        return self.resistance

    def record_opinion_history(self):
        """Record the agent's opinion history at a given time step"""
        self.history.append(self.opinion)
