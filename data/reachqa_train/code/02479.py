import matplotlib.pyplot as plt
import networkx as nx

# Define the nodes and edges for the research network
nodes = ["USA", "Germany", "China", "Japan", "Brazil"]
edges = [
    ("USA", "Germany"), 
    ("USA", "China"), 
    ("Germany", "Japan"),
    ("China", "Brazil"), 
    ("Brazil", "USA"),
    ("Japan", "China")
]

# Create the graph using NetworkX
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Calculate positions for the nodes using the spring layout
pos = nx.spring_layout(G, seed=42)

# Node attributes
node_sizes = [3000, 2500, 3500, 2700, 2300]  # Different sizes for visual interest
node_colors = ['skyblue', 'lightcoral', 'lightgreen', 'plum', 'gold']

# Draw the nodes with custom attributes
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9)

# Edge attributes
edge_weights = [2.5, 1.8, 3.0, 2.2, 2.7, 1.5]
edge_styles = ['solid', 'dashed', 'solid', 'dotted', 'dashdot', 'dashed']

# Draw the edges with custom styles and weights
for i, (u, v) in enumerate(edges):
    nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], width=edge_weights[i], style=edge_styles[i], alpha=0.7)

# Draw the node labels
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# Graph title and note
plt.title("Global Research Collaborations in Renewable Energy\nA Snapshot of Key Collaborations", fontsize=16, fontweight='bold')
plt.text(0.5, -0.15, "Nodes represent countries/institutions\nEdges represent research collaborations", fontsize=10, ha='center')

# Clean up the plot
plt.axis('off')
plt.tight_layout()

# Display the graph
plt.show()