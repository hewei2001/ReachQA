import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Create a directed graph
G = nx.DiGraph()

# Define nodes (species) and edges (interactions)
species = [
    'Sunflower', 'Honeybee', 'Butterfly', 'Bird', 
    'Rabbit', 'Fox', 'Deer', 'Grass', 'Earthworm'
]

interactions = [
    ('Sunflower', 'Honeybee'), ('Sunflower', 'Butterfly'),
    ('Grass', 'Rabbit'), ('Grass', 'Deer'),
    ('Rabbit', 'Fox'), ('Deer', 'Fox'),
    ('Earthworm', 'Grass'), ('Earthworm', 'Sunflower'),
    ('Honeybee', 'Butterfly'), ('Bird', 'Butterfly')
]

G.add_nodes_from(species)
G.add_edges_from(interactions)

pos = nx.spring_layout(G, k=0.5, iterations=50)

node_sizes = [1500 + 300 * len(list(G.neighbors(node))) for node in G.nodes()]

edge_labels = {
    ('Sunflower', 'Honeybee'): 'Pollination', ('Sunflower', 'Butterfly'): 'Pollination',
    ('Grass', 'Rabbit'): 'Herbivory', ('Grass', 'Deer'): 'Herbivory',
    ('Rabbit', 'Fox'): 'Predation', ('Deer', 'Fox'): 'Predation',
    ('Earthworm', 'Grass'): 'Soil Enrichment', ('Earthworm', 'Sunflower'): 'Soil Enrichment',
    ('Honeybee', 'Butterfly'): 'Mutualism', ('Bird', 'Butterfly'): 'Predation'
}

# New data for the bar chart showing interaction frequency
interaction_types = ['Pollination', 'Herbivory', 'Predation', 'Soil Enrichment', 'Mutualism']
interaction_counts = [2, 2, 3, 2, 1]

# Create the figure and axes
fig, axs = plt.subplots(1, 2, figsize=(18, 8))

# First plot - Network Graph
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', 
        node_size=node_sizes, font_size=10, font_weight='bold', arrows=True, 
        arrowstyle='-|>', ax=axs[0])
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkblue', 
                             font_size=8, ax=axs[0])
axs[0].set_title("Ecosystem Interactions:\nNetwork of Species Interactions", fontsize=14, fontweight='bold')

# Second plot - Bar Chart of Interaction Frequency
axs[1].bar(interaction_types, interaction_counts, color='lightgreen')
axs[1].set_xlabel('Interaction Type', fontsize=12)
axs[1].set_ylabel('Frequency', fontsize=12)
axs[1].set_title("Frequency of Interaction Types", fontsize=14, fontweight='bold')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()