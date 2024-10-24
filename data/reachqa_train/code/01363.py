import matplotlib.pyplot as plt
import networkx as nx

# Define the genres as nodes
genres = [
    "Fiction", "Non-fiction", "Poetry", "Drama", 
    "Science Fiction", "Fantasy", "Mystery", "Romance", "Historical"
]

# Define connections (edges) between genres and their influences
connections = [
    ("Fiction", "Non-fiction"),
    ("Fiction", "Poetry"),
    ("Poetry", "Drama"),
    ("Science Fiction", "Fantasy"),
    ("Fiction", "Science Fiction"),
    ("Fantasy", "Mystery"),
    ("Mystery", "Drama"),
    ("Romance", "Historical"),
    ("Romance", "Fiction"),
    ("Historical", "Drama")
]

# Create a Graph object
G = nx.Graph()

# Add nodes and edges
G.add_nodes_from(genres)
G.add_edges_from(connections)

# Position nodes using a spring layout for better visualization
pos = nx.spring_layout(G, seed=42)

# Set node sizes and colors
node_sizes = [5000] * len(genres)
node_colors = ['#add8e6'] * len(genres)

# Draw the network
plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black', linewidths=1.5)
nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_color='darkblue')

# Draw edge labels to illustrate connections
edge_labels = {connection: '' for connection in connections}  # Empty labels just to avoid clutter, but can add weights if needed
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color='gray')

# Add a title, split into two lines for better readability
plt.title("Network of Literary Genres\nand Their Influences", fontsize=14, fontweight='bold', pad=20)

# Remove axes for a cleaner look
plt.axis('off')

# Automatically adjust layout to avoid overlap and improve spacing
plt.tight_layout()

# Display the chart
plt.show()