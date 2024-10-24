import matplotlib.pyplot as plt
import networkx as nx

# Define the communication methods as nodes
nodes = [
    "Cave Paintings", "Smoke Signals", "Carrier Pigeons",
    "Telegraph", "Telephone", "Radio", 
    "Television", "Internet", "Social Media"
]

# Define the directed edges between communication methods
edges = [
    ("Cave Paintings", "Smoke Signals"),
    ("Smoke Signals", "Carrier Pigeons"),
    ("Carrier Pigeons", "Telegraph"),
    ("Telegraph", "Telephone"),
    ("Telephone", "Radio"),
    ("Radio", "Television"),
    ("Television", "Internet"),
    ("Internet", "Social Media")
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Define a position layout for nodes using the spring layout
pos = nx.spring_layout(G, seed=42)

# Define node sizes based on the hypothetical impact of each communication method
node_sizes = [1200, 1000, 800, 1000, 1200, 1400, 1600, 1800, 2000]

# Define edge widths representing influence strength
edge_weights = [1, 1.5, 2, 2.5, 3, 3.5, 4, 5]

# Create the figure for plotting
fig, ax = plt.subplots(figsize=(14, 10))

# Draw the directed graph
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=node_sizes, ax=ax)
nx.draw_networkx_edges(G, pos, edge_color='grey', arrows=True, arrowsize=15, width=edge_weights, ax=ax)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_color='black', ax=ax)

# Add edge labels to indicate the transitions
edge_labels = {
    ("Cave Paintings", "Smoke Signals"): "primitive",
    ("Smoke Signals", "Carrier Pigeons"): "early",
    ("Carrier Pigeons", "Telegraph"): "revolution",
    ("Telegraph", "Telephone"): "connection",
    ("Telephone", "Radio"): "airwaves",
    ("Radio", "Television"): "broadcast",
    ("Television", "Internet"): "digital",
    ("Internet", "Social Media"): "network"
}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkred', ax=ax, font_size=9)

# Set title for the plot
plt.title("The Evolutionary Path of Human Communication:\nFrom Cave Paintings to Digital Dialogues", 
          fontsize=16, fontweight='bold', pad=20)

# Turn off axes for a cleaner look
ax.axis('off')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()