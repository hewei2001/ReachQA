import matplotlib.pyplot as plt
import networkx as nx
from matplotlib import cm

# Define the nodes (technology hubs)
hubs = [
    "Silicon Valley", "Shenzhen", "Berlin", "Tel Aviv", 
    "Bangalore", "Stockholm", "Seoul", "Tokyo"
]

# Define the edges with weights (collaborative strength)
edges = [
    ("Silicon Valley", "Shenzhen", 8),
    ("Silicon Valley", "Berlin", 6),
    ("Silicon Valley", "Tel Aviv", 7),
    ("Shenzhen", "Bangalore", 5),
    ("Berlin", "Stockholm", 4),
    ("Tel Aviv", "Seoul", 6),
    ("Bangalore", "Tokyo", 7),
    ("Stockholm", "Tokyo", 5),
    ("Seoul", "Shenzhen", 8),
    ("Tel Aviv", "Stockholm", 4),
    ("Berlin", "Bangalore", 5)
]

# Create a NetworkX graph from the nodes and edges
G = nx.Graph()
G.add_nodes_from(hubs)
G.add_weighted_edges_from(edges)

# Set up the plot
plt.figure(figsize=(14, 12))

# Define the layout for the nodes in the graph
pos = nx.spring_layout(G, seed=42)

# Calculate degree for each node
node_degrees = dict(G.degree())

# Define node size and color based on degree
node_sizes = [node_degrees[node] * 300 for node in G.nodes()]
node_colors = [cm.viridis(node_degrees[node] / max(node_degrees.values())) for node in G.nodes()]

# Draw nodes with specific attributes
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black')

# Draw edges with weights affecting both thickness and color
edge_weights = nx.get_edge_attributes(G, 'weight')
edge_colors = [cm.coolwarm(weight / max(edge_weights.values())) for weight in edge_weights.values()]
nx.draw_networkx_edges(G, pos, edgelist=edges, width=[weight * 0.6 for weight in edge_weights.values()],
                       alpha=0.8, edge_color=edge_colors)

# Draw node labels with better spacing
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', verticalalignment='center')

# Draw edge labels with weight information
nx.draw_networkx_edge_labels(G, pos, edge_labels={k: f"{v}" for k, v in edge_weights.items()}, font_size=10)

# Customize the plot
plt.title("Global Network of Collaborative Innovation Hubs\nFostering Futuristic Technology", fontsize=16, fontweight='bold')
plt.axis('off')  # Turn off the axis for better visual

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()