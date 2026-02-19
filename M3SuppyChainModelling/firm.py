"""Firms in the supply chain model."""


class Firm:
    def __init__(self, **kwargs):
        self.ID = kwargs.get("ID")
        # industry type
        # BUsiness type
        # location
        # raw materials, demand
        # Suppliers, qty, price
        # Consumers, qty, price
        # capacity
        # inventory_raw_material max capacity
        # inventory_product max capacity
        # inventory
        # costs
        #


## Vipin;s notes:
# id
# ids of suppliers
# ids of buyers
# qty of supplies
# qty of output
# Production function - Cobb Douglas, CES, Leontieff, Nested CES
# my price
# Pricing rule (pricing function) - Based on demand fom buyers
# capacity constraints
# inventory of my output
