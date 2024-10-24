import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.colors as mcolors

# Define major ports involved in the global cargo network
ports = ['Shanghai', 'Singapore', 'Los Angeles', 'Rotterdam', 'Dubai', 'Hamburg', 'Panama', 'Mumbai']

# Cargo flow between ports (edges) with associated volumes (weights in thousands)
edges = [
    ('Shanghai', 'Singapore', 120),
    ('Shanghai', 'Los Angeles', 95),
    ('Singapore', 'Rotterdam', 90),
    ('Singapore', 'Dubai', 100),
    ('Los Angeles', 'Panama', 80),
    ('Rotterdam', 'Hamburg', 85),
    ('Dubai', 'Mumbai', 70),
    ('Mumbai', 'Singapore', 60),
    ('Panama', 'Rotterdam', 55)
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges with weights
G.add_nodes_from(ports)
G.add_weighted_edges_from(edges)

# Define node positions using a circular layout
pos = nx.circular_layout(G)

# Generate a color map for ports based on their importance (assuming custom values for demonstration)
importance = [150, 130, 110, 100, 95, 85, 80, 75]
node_colors = [plt.cm.viridis(i / max(importance)) for i in importance]

# Draw nodes with custom size and color based on their importance
nx.draw_networkx_nodes(G, pos, node_size=[700 + i*10 for i in importance], node_color=node_colors, edgecolors='black')

# Draw edges with arrowheads to indicate direction; using color gradients based on weight
edge_weights = [weight for _, _, weight in edges]
edge_colors = plt.cm.plasma([(weight - min(edge_weights)) / (max(edge_weights) - min(edge_weights)) for weight in edge_weights])

nx.draw_networkx_edges(
    G, pos, edgelist=edges, arrowstyle='-|>', arrowsize=15,
    edge_color=edge_colors, width=[1 + weight / 30 for _, _, weight in edges]
)

# Draw node labels with white boxes for readability
nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold', bbox=dict(facecolor='white', edgecolor='none', pad=1))

# Add edge labels indicating cargo volume in thousands of containers
edge_labels = {(source, target): f"{weight}k" for source, target, weight in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color='darkred')

# Title broken into multiple lines for better readability
plt.title("Global Cargo Network\nVisualizing the Flow of Goods\nThrough Major Ports", fontsize=13, fontweight='bold')

# Legend for node colors and edge thicknesses
sm = plt.cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(vmin=min(importance), vmax=max(importance)))
sm.set_array([])
cbar = plt.colorbar(sm, ax=plt.gca(), orientation='horizontal', fraction=0.046, pad=0.04)
cbar.set_label('Port Importance', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()