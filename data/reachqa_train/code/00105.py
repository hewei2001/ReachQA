import matplotlib.pyplot as plt
import networkx as nx

# Define the nodes (art galleries located in different cities)
nodes = ["New York", "Paris", "Tokyo", "London", "Berlin", "Sydney", "Sao Paulo"]

# Define the edges with weights representing the number of art pieces
edges = [
    ("New York", "Paris", 12),
    ("New York", "Tokyo", 8),
    ("Paris", "London", 15),
    ("London", "Berlin", 10),
    ("Berlin", "Tokyo", 9),
    ("Tokyo", "Sydney", 11),
    ("Sydney", "Sao Paulo", 7),
    ("Sao Paulo", "New York", 6),
    ("Paris", "Berlin", 14),
    ("London", "Sydney", 5)
]

# Create an undirected graph
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

# Plotting the undirected node chart
plt.figure(figsize=(12, 10))

# Define position layout using spring layout for better node placement
pos = nx.spring_layout(G, seed=42)

# Draw the nodes with custom sizes and colors
node_sizes = [3500 for _ in nodes]
node_colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightgrey', 'lightpink', 'lightgoldenrodyellow']
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors)

# Draw the edges with varying thickness based on weight
edge_weights = [G[u][v]['weight'] for u, v in G.edges]
edges_drawn = nx.draw_networkx_edges(G, pos, edgelist=edges, width=[0.5 + w / 3 for w in edge_weights], edge_color=edge_weights, edge_cmap=plt.cm.viridis, edge_vmin=min(edge_weights), edge_vmax=max(edge_weights))

# Draw labels for nodes and edges
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
edge_labels = {(u, v): f"{d['weight']} pieces" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkred', font_size=9)

# Add title and adjust layout
plt.title("Global Art Confluence:\nInternational Art Gallery Collaborations", fontsize=14, fontweight='bold')
plt.axis('off')

# Correct the colorbar addition
plt.colorbar(edges_drawn, label='Number of Art Pieces')

plt.tight_layout()

# Show plot
plt.show()