import matplotlib.pyplot as plt
import networkx as nx

# Define the graph
G = nx.Graph()

# List of towns (nodes)
towns = ["Oakridge", "Riverbend", "Maple Grove", "Pine Hill", "Cedar Creek"]

# Add nodes to the graph
G.add_nodes_from(towns)

# Define connections with weights (number of shared projects)
connections = [
    ("Oakridge", "Riverbend", 3),
    ("Riverbend", "Maple Grove", 2),
    ("Maple Grove", "Pine Hill", 1),
    ("Pine Hill", "Cedar Creek", 2),
    ("Oakridge", "Cedar Creek", 1),
    ("Oakridge", "Maple Grove", 2),
]

# Add edges with weights
for u, v, weight in connections:
    G.add_edge(u, v, weight=weight)

# Set positions for all nodes using a layout
pos = nx.spring_layout(G, seed=42)  # Seed for reproducibility

# Create the plot
plt.figure(figsize=(12, 10))

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=800, node_color='lightgreen', edgecolors='black')

# Draw edges with varying width based on weight
nx.draw_networkx_edges(
    G, pos,
    width=[2 * G[u][v]['weight'] for u, v in G.edges()],
    edge_color='olive',
    alpha=0.6
)

# Draw labels for towns
nx.draw_networkx_labels(G, pos, font_size=14, font_weight='bold')

# Draw labels for edges to indicate number of shared projects
edge_labels = {(u, v): f'{G[u][v]["weight"]} projects' for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, label_pos=0.5)

# Title with line breaks for better layout
plt.title(
    "Connections in the Green Alliance Network:\n"
    "A Community Engagement Initiative",
    fontsize=16,
    fontweight='bold',
    pad=20
)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()