"""Parameters for opinion dynamics simulation."""

# Simulation parameters
NUM_AGENTS = 10000  # Total number of agents in the simulation
TIME_STEPS = 1000  # Total number of time steps to simulate
PROP_INTERACTIONS = 0.1  # Proportion of interactions per time step
MEAN_DEGREE = 10  # Mean degree for network generation (if applicable)
FRIENDSHIP_THRESHOLD = 0.7  # maximum opinion difference to be friends
# Ignore if on the same side
