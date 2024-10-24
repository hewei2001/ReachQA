import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define the nodes representing different sectors
nodes = [
    'Transportation',
    'Energy',
    'Healthcare',
    'Education',
    'Communication',
    'Public Safety'
]

# Define the directed edges representing the flow of resources/information
edges = [
    ('Transportation', 'Energy'),
    ('Transportation', 'Healthcare'),
    ('Energy', 'Communication'),
    ('Healthcare', 'Education'),
    ('Education', 'Transportation'),
    ('Communication', 'Public Safety'),
    ('Public Safety', 'Healthcare')
]

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Define position layout for nodes
pos = nx.spring_layout(G, seed=42)

# Define colors for different sectors
color_map = {
    'Transportation': '#FF6347',
    'Energy': '#4682B4',
    'Healthcare': '#FFD700',
    'Education': '#ADFF2F',
    'Communication': '#20B2AA',
    'Public Safety': '#FF4500'
}

node_colors = [color_map[node] for node in G.nodes]

# Interaction strength matrix for heatmap
interaction_strengths = np.array([
    [0, 3, 1, 0, 0, 0],
    [0, 0, 0, 0, 4, 0],
    [0, 0, 0, 5, 0, 0],
    [2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2],
    [0, 1, 0, 0, 0, 0]
])

# Create the figure with a 2x1 grid to include the heatmap
fig, ax = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [2, 1]})

# Draw the graph
nx.draw_networkx_nodes(G, pos, ax=ax[0], node_size=2000, node_color=node_colors, edgecolors='black', linewidths=1.5)
nx.draw_networkx_edges(G, pos, ax=ax[0], edgelist=edges, arrowstyle='-|>', arrowsize=20, edge_color='gray', connectionstyle='arc3,rad=0.1')
nx.draw_networkx_labels(G, pos, ax=ax[0], font_size=10, font_color='black', font_weight='bold',
                        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2'))
ax[0].set_title("Navigating the Future:\nInnovation Nodes in Smart Cities", fontsize=14, fontweight='bold', pad=20)
ax[0].axis('off')

# Draw the heatmap
cax = ax[1].matshow(interaction_strengths, cmap='YlGnBu', alpha=0.8)
fig.colorbar(cax, ax=ax[1], fraction=0.046, pad=0.04)

ax[1].set_xticks(np.arange(len(nodes)))
ax[1].set_yticks(np.arange(len(nodes)))
ax[1].set_xticklabels(nodes, rotation=45, ha='left')
ax[1].set_yticklabels(nodes)

# Adjust labels to ensure no overlap
for label in ax[1].get_xticklabels():
    label.set_rotation(45)
    label.set_horizontalalignment('left')

ax[1].set_title("Interaction Strengths", fontsize=12, fontweight='bold', pad=20)

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()