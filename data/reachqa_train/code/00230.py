import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.cm as cm

# Create a directed graph for logistic pathways
logistics_network = nx.DiGraph()

# Define logistic hubs as nodes
logistic_hubs = [
    "New York", "Los Angeles", "Shanghai", 
    "Hamburg", "Dubai", "Sydney", 
    "Tokyo", "Sao Paulo"
]

logistics_network.add_nodes_from(logistic_hubs)

# Define the directed edges with weights indicating supply chain strength
logistic_routes = [
    ("Shanghai", "Los Angeles", 9),
    ("Shanghai", "New York", 7),
    ("Hamburg", "New York", 8),
    ("Dubai", "Hamburg", 6),
    ("Tokyo", "Shanghai", 7),
    ("Sydney", "Tokyo", 5),
    ("Los Angeles", "Sydney", 4),
    ("Sao Paulo", "New York", 3),
    ("Dubai", "Shanghai", 5),
    ("Tokyo", "Hamburg", 6),
    ("New York", "Dubai", 2)
]

logistics_network.add_weighted_edges_from(logistic_routes)

# Use a spring layout for better distribution and clarity
pos = nx.spring_layout(logistics_network, seed=42)

# Create a plot
fig, ax = plt.subplots(figsize=(12, 8))

# Define edge colors based on weights for clarity
route_strengths = [d['weight'] for u, v, d in logistics_network.edges(data=True)]
edges = nx.draw_networkx_edges(
    logistics_network, pos, edgelist=logistics_network.edges(), 
    width=[w * 0.8 for w in route_strengths], alpha=0.7,
    edge_color=route_strengths, edge_cmap=cm.Blues,
    arrows=True, arrowsize=20, ax=ax
)

# Draw nodes with sizes reflecting in-degree (goods received)
node_sizes = [300 + 100 * logistics_network.in_degree(n) for n in logistics_network.nodes()]
nodes = nx.draw_networkx_nodes(
    logistics_network, pos, node_size=node_sizes, node_color='coral', alpha=0.9, ax=ax
)

# Add labels to nodes
nx.draw_networkx_labels(
    logistics_network, pos, font_size=10, font_weight='bold', verticalalignment='center',
    bbox=dict(facecolor='whitesmoke', edgecolor='black', boxstyle='round,pad=0.3'),
    ax=ax
)

# Add edge weight labels for context
edge_labels = {(u, v): d['weight'] for u, v, d in logistics_network.edges(data=True)}
nx.draw_networkx_edge_labels(
    logistics_network, pos, edge_labels=edge_labels, font_size=8, font_color='darkblue', ax=ax
)

# Add colorbar to reflect edge weight mapping
sm = plt.cm.ScalarMappable(cmap=cm.Blues, norm=plt.Normalize(vmin=min(route_strengths), vmax=max(route_strengths)))
sm._A = []
cbar = plt.colorbar(sm, label='Supply Chain Strength', ax=ax)
cbar.ax.yaxis.label.set_size(12)

# Set plot title and layout
plt.title('Global Supply Chain Dynamics:\n A Network of Logistic Pathways', fontsize=16, weight='bold', pad=20)
plt.axis('off')
plt.tight_layout()

# Display the plot
plt.show()