import igraph as ig
from firms import Firm
from parameters import NUM_FIRMS, INITIAL_CASH, TIME_STEPS


class SupplyChainEnv:
    def __init__(self):
        # Create Scale-Free Network (Barabási-Albert model)
        self.graph = ig.Graph.Barabasi(n=NUM_FIRMS, m=2, directed=True)
        self.firms = [Firm(i, INITIAL_CASH) for i in range(NUM_FIRMS)]

        # Link firms based on the graph edges
        for edge in self.graph.get_edgelist():
            supplier_idx, customer_idx = edge
            self.firms[supplier_idx].customers.append(self.firms[customer_idx])
            self.firms[customer_idx].suppliers.append(self.firms[supplier_idx])

    def step(self):
        total_economy_output = 0
        for firm in self.firms:
            out = firm.produce()
            total_economy_output += out
            firm.trade()
        return total_economy_output

    def run(self):
        print(f"Starting simulation on scale-free network with {NUM_FIRMS} firms...")
        for t in range(TIME_STEPS):
            output = self.step()
            if t % 10 == 0:
                print(f"Step {t}: Total Economy Production = {output:.2f}")


import pandas as pd


def iterate_oecd_matrix(file_path):
    """
    Iterates through an OECD IO Matrix to identify
    the strength of supply chain links.
    """
    # Load the matrix (assuming first column/row are industry codes)
    df = pd.read_csv(file_path, index_col=0)

    links = []

    # .iterrows() for the producing side (Rows)
    # .items() for the consuming side (Columns)
    for producing_industry, row in df.iterrows():
        for consuming_industry, value in row.items():
            # Filter out zero or negligible trade links
            if value > 0:
                link_data = {
                    "origin": producing_industry,
                    "destination": consuming_industry,
                    "flow_volume": value,
                }
                links.append(link_data)

                # Logic for your ABM:
                # print(f"Industry {producing_industry} supplies {value} units to {consuming_industry}")

    return links


def build_network_from_io(self, matrix_df):
    for i, producer in enumerate(self.firms):
        for j, consumer in enumerate(self.firms):
            # Get flow from Matrix (normalized or raw)
            flow = matrix_df.iloc[i, j]

            if flow > threshold:
                # Add directed edge in igraph
                self.graph.add_edge(i, j, weight=flow)
                # Link objects
                producer.customers.append(consumer)
                consumer.suppliers.append(producer)


if __name__ == "__main__":
    env = SupplyChainEnv()
    env.run()
