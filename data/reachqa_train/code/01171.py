import matplotlib.pyplot as plt
import networkx as nx

# Define the stages in the coffee supply chain
nodes = ["Farmer", "Exporter", "Importer", "Roaster", "Retailer", "Consumer"]

# Define the directed edges between stages
edges = [
    ("Farmer", "Exporter"),
    ("Exporter", "Importer"),
    ("Importer", "Roaster"),
    ("Roaster", "Retailer"),
    ("Retailer", "Consumer")
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Define a position layout for nodes
pos = nx.shell_layout(G)

# Plot the directed graph
plt.figure(figsize=(10, 6))
nx.draw_networkx_nodes(G, pos, node_color='cornflowerblue', node_size=2500)
nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowsize=20, width=2)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_color='black')

# Add title and supplementary labels
plt.title("Tracing the Journey of Coffee Beans:\nFrom Farm to Cup", fontsize=16, fontweight='bold')

# Additional annotations to explain each node (use shorter labels to avoid clutter)
labels_legend = {
    "Farmer": "Cultivation",
    "Exporter": "Export",
    "Importer": "Import",
    "Roaster": "Roast",
    "Retailer": "Sell",
    "Consumer": "Consume"
}

# Display legend annotations beneath each node
for node, (x, y) in pos.items():
    plt.text(x, y - 0.1, labels_legend[node], fontsize=9, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.8))

# Turn off axes
plt.axis('off')

# Optimize layout
plt.tight_layout()

# Show plot
plt.show()