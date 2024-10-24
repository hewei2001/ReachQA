import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define nodes for mythical creatures
creatures = [
    'Dragon', 'Phoenix', 'Griffin', 'Hydra', 'Minotaur', 
    'Unicorn', 'Chimera', 'Kraken'
]

# Define directed edges to show interactions
interactions = [
    ('Dragon', 'Griffin'),    # Aerial dominance contest
    ('Phoenix', 'Unicorn'),   # Healing influences
    ('Hydra', 'Chimera'),     # Transformation conflict
    ('Minotaur', 'Kraken'),   # Land-sea boundary clash
    ('Unicorn', 'Hydra'),     # Purity resistance
    ('Griffin', 'Minotaur'),  # Territorial feud
    ('Chimera', 'Phoenix'),   # Rebirth influence
    ('Kraken', 'Dragon')      # Territorial protection
]

# Mythical creature power levels over a hypothetical timeline
creature_powers = {
    'Dragon': [90, 92, 95, 96, 94],
    'Phoenix': [88, 85, 87, 89, 90],
    'Griffin': [80, 83, 82, 81, 80],
    'Hydra': [70, 72, 75, 77, 76],
    'Minotaur': [65, 64, 66, 67, 68],
    'Unicorn': [60, 63, 64, 62, 61],
    'Chimera': [55, 57, 58, 56, 55],
    'Kraken': [50, 53, 52, 51, 50]
}
timeline = ['Era 1', 'Era 2', 'Era 3', 'Era 4', 'Era 5']

# Initialize a directed graph
G = nx.DiGraph()
G.add_nodes_from(creatures)
G.add_edges_from(interactions)

# Determine node positions using a circular layout for symmetry
pos = nx.circular_layout(G)

# Calculate node sizes based on degree
node_degrees = dict(G.degree)
node_sizes = [v * 400 for v in node_degrees.values()]

# Create the plot with a subplot for the overlay
fig, axes = plt.subplots(nrows=2, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

# Main network graph
ax_main = axes[0]
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='lightblue', alpha=0.9, edgecolors='black', ax=ax_main)
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=15, edge_color='grey', ax=ax_main, connectionstyle='arc3,rad=0.1')
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', ax=ax_main)
ax_main.set_title('Ancient Mythical Creatures\nInteractions and Influences', fontsize=14, weight='bold', pad=20)
ax_main.axis('off')

# Overlay line plot for creature power levels
ax_overlay = axes[1]
for creature, powers in creature_powers.items():
    ax_overlay.plot(timeline, powers, marker='o', label=creature)

ax_overlay.set_title('Mythical Creature Power Levels Over Time', fontsize=12, weight='bold', pad=10)
ax_overlay.set_xlabel('Timeline')
ax_overlay.set_ylabel('Power Level')
ax_overlay.legend(loc='upper left', ncol=2, fontsize=10, bbox_to_anchor=(1.05, 1))
ax_overlay.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to fit all elements
plt.tight_layout()

# Display the plot
plt.show()