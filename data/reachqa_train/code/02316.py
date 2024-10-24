import matplotlib.pyplot as plt
import networkx as nx

# Initialize a directed graph
G = nx.DiGraph()

# Define nodes with positions
nodes = {
    "Social Media": (0, 1),
    "Email Campaign": (0, 2),
    "Search Ads": (0, 3),
    "Website": (1, 2),
    "Blog": (2, 1),
    "Affiliate": (2, 3),
    "Product Page": (3, 2),
    "Checkout": (4, 2)
}

# Add nodes to the graph
G.add_nodes_from(nodes.keys())

# Define edges with weights representing the traffic volume
edges = [
    ("Social Media", "Website", 1500),
    ("Email Campaign", "Website", 1200),
    ("Search Ads", "Website", 1000),
    ("Website", "Blog", 300),
    ("Blog", "Product Page", 200),
    ("Website", "Product Page", 800),
    ("Search Ads", "Affiliate", 500),
    ("Affiliate", "Product Page", 400),
    ("Product Page", "Checkout", 600),
    ("Email Campaign", "Product Page", 300)
]

# Add edges to the graph
for source, target, weight in edges:
    G.add_edge(source, target, weight=weight)

# Setup plot
plt.figure(figsize=(14, 10))

# Use shell layout for better readability
pos = nx.shell_layout(G)

# Draw nodes with customized appearance
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='#ADD8E6', alpha=0.9)

# Draw edges with arrows, specifying directionality and edge thickness
nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='-|>', arrowsize=15, width=2, edge_color='grey')

# Extract edge weights to display them
edge_labels = nx.get_edge_attributes(G, 'weight')

# Draw node labels with specified font properties
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# Draw edge labels positioned near the middle of the edges
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)

# Title and layout adjustments
plt.title("TechGear's Digital Marketing Campaign Flow\nNew Product Launch", fontsize=16, fontweight='bold', pad=20)
plt.axis('off')
plt.tight_layout()

# Show plot
plt.show()