import matplotlib.pyplot as plt
import networkx as nx

# Define continents as nodes
continents = ["North America", "Europe", "Asia", "Africa", "South America", "Oceania"]

# Define edges with weights indicating data flow in petabytes per month
data_flows = [
    ("North America", "Europe", 1000),
    ("North America", "Asia", 750),
    ("Europe", "Asia", 600),
    ("Europe", "Africa", 400),
    ("Asia", "Oceania", 200),
    ("Asia", "Africa", 350),
    ("Africa", "South America", 150),
    ("South America", "North America", 300),
    ("Oceania", "North America", 250)
]

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(continents)
G.add_weighted_edges_from(data_flows)

# Calculate layout for better visualization
pos = nx.spring_layout(G, seed=42)

# Prepare the plot
plt.figure(figsize=(12, 10))

# Draw nodes with customized sizes based on their degree centrality
node_sizes = [3000 * nx.degree_centrality(G)[node] for node in G]
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='lightblue', edgecolors='black')

# Draw edges with customized widths based on weight
edge_widths = [0.005 * d['weight'] for (u, v, d) in G.edges(data=True)]
nx.draw_networkx_edges(G, pos, width=edge_widths, arrowstyle='->', arrowsize=20, edge_color='gray')

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# Add edge labels for data flow magnitude
edge_labels = {(u, v): f"{d['weight']} PB" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, label_pos=0.3)

# Set title and remove axes
plt.title("Global Internet Communication:\nDirected Data Flow between Continents", fontsize=16)
plt.axis('off')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()