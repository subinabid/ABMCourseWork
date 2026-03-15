import numpy as np
from parameters import ALPHA, BETA, TOTAL_FACTOR_PRODUCTIVITY


class Firm:
    def __init__(self, firm_id, initial_cash):
        self.id = firm_id
        self.cash = initial_cash
        self.labor = 10.0  # Simplified fixed input
        self.capital = 10.0  # Simplified fixed input
        self.output = 0.0
        self.suppliers = []
        self.customers = []

    def produce(self):
        """Cobb-Douglas: Y = A * L^α * K^β"""
        self.output = (
            TOTAL_FACTOR_PRODUCTIVITY * (self.labor**ALPHA) * (self.capital**BETA)
        )
        return self.output

    def trade(self):
        """Simple trade logic: Distribute output to customers"""
        if not self.customers:
            return 0

        per_customer_shipment = self.output / len(self.customers)
        # In a real model, cash would flow back here
        return per_customer_shipment
