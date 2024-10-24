import matplotlib.pyplot as plt
import networkx as nx

# Define cities as nodes
cities = ["Metroville", "Skyton", "Urbania", "Cosmo City", "Riverview", "Greenfield", "Downton"]

# Define connections as edges
connections = [
    ("Metroville", "Skyton"),
    ("Metroville", "Urbania"),
    ("Metroville", "Cosmo City"),
    ("Skyton", "Urbania"),
    ("Skyton", "Riverview"),
    ("Urbania", "Cosmo City"),
    ("Urbania", "Downton"),
    ("Cosmo City", "Riverview"),
    ("Cosmo City", "Greenfield"),
    ("Riverview", "Greenfield"),
    ("Greenfield", "Downton"),
]

# Create a NetworkX graph from the connections
G = nx.Graph()
G.add_edges_from(connections)

# Choose the spring layout for clear visualization
pos = nx.spring_layout(G, seed=42)

# Calculate node degree for size scaling
node_size = [nx.degree(G, n) * 300 for n in G.nodes()]

# Draw the network graph
plt.figure(figsize=(12, 9))
nx.draw(G, pos, with_labels=True, node_color='turquoise', node_size=node_size,
        edge_color='gray', font_size=11, font_weight='bold', font_color='darkslategray')

# Customize edge styles
edges = G.edges()
edge_weights = [G[u][v]['weight'] if 'weight' in G[u][v] else 1 for u, v in edges]
nx.draw_networkx_edges(G, pos, edgelist=edges, width=edge_weights, edge_color='lightskyblue')

# Title and layout settings
plt.title("Intercity Connectivity in FutureLandia\nHyperloop Transport Network", fontsize=16, fontweight='bold', pad=30)
plt.axis('off')  # Hide axis

# Adjust layout for better spacing
plt.tight_layout()

# Display the chart
plt.show()