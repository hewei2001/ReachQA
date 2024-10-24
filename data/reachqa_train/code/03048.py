import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

# List of influential tech leaders
leaders = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry"]

# Adjacency matrix representing connections between leaders
adjacency_matrix = np.array([
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
])

# Create a NetworkX graph from the adjacency matrix
G = nx.from_numpy_array(adjacency_matrix)

# Assign node labels based on the leaders list
labels = {i: leaders[i] for i in range(len(leaders))}

# Calculate node size based on degree of connectivity
node_sizes = [700 + G.degree(i) * 300 for i in G.nodes]

# Calculate edge weights to vary edge width
edge_weights = [0.5 + 1.5 * np.random.rand() for _ in G.edges]

# Draw the graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)  # Define position layout for better visualization

# Draw nodes with varying sizes and colors
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='skyblue', alpha=0.9)

# Draw edges with varying widths
nx.draw_networkx_edges(G, pos, width=edge_weights, edge_color='gray', alpha=0.5)

# Draw labels for each node
nx.draw_networkx_labels(G, pos, labels=labels, font_size=10, font_weight='bold')

# Customize plot aesthetics
plt.title("Networking Giants: Mapping Influences in\nTech Leadership", fontsize=16, fontweight='bold', pad=20)
plt.axis('off')  # Hide axis

# Use tight_layout to adjust layout automatically
plt.tight_layout()

# Display the plot
plt.show()