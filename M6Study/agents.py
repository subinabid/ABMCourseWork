"""Agemnts for M6Study."""

import random


class Agent:
    """An agent with ID wrapped in init"""

    number_of_agents = 0

    def __init__(self, ID):
        self.ID = ID
        self.friends = []
        self.opinion = random.uniform(-1, 1)  # Initial opinion: between -1 and 1
        self.history = []
        self.__class__.number_of_agents += 1

    def add_friend(self, friend_id):
        """Add a friend to the agent's list of friends."""
        if friend_id not in self.friends:
            self.friends.append(friend_id)

    def remove_friend(self, friend_id):
        """Remove a friend from the agent's list of friends."""
        if friend_id in self.friends:
            self.friends.remove(friend_id)

    def update_opinion(self, new_opinion):
        """Update the agent's opinion"""
        self.opinion = new_opinion

    def return_opinion(self):
        """Return the agent's current opinion"""
        return self.opinion

    def record_opinion_history(self):
        """Record the agent's opinion history at a given time step"""
        self.history.append(self.opinion)
