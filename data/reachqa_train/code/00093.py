import matplotlib.pyplot as plt
import networkx as nx

# Original Data: Art gallery nodes and weighted edges
nodes = ["New York", "Paris", "Tokyo", "London", "Berlin", "Sydney", "Sao Paulo"]
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

# New Data: Number of annual exhibitions for each city
annual_exhibitions = {
    "New York": 20,
    "Paris": 30,
    "Tokyo": 25,
    "London": 28,
    "Berlin": 22,
    "Sydney": 18,
    "Sao Paulo": 15
}

# Create an undirected graph
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

# Set up the plotting area with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plotting the NetworkX graph
pos = nx.spring_layout(G, seed=42)
node_sizes = [3500 for _ in nodes]
node_colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightgrey', 'lightpink', 'lightgoldenrodyellow']
edge_weights = [G[u][v]['weight'] for u, v in G.edges]

# Draw nodes and edges with NetworkX
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, ax=ax1)
nx.draw_networkx_edges(G, pos, edgelist=edges, width=[0.5 + w / 3 for w in edge_weights], edge_color=edge_weights, edge_cmap=plt.cm.viridis, edge_vmin=min(edge_weights), edge_vmax=max(edge_weights), ax=ax1)
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif', ax=ax1)
edge_labels = {(u, v): f"{d['weight']} pieces" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkred', font_size=9, ax=ax1)

# Title and colorbar for NetworkX graph
ax1.set_title("Global Art Confluence:\nInternational Art Gallery Collaborations", fontsize=14, fontweight='bold')
ax1.axis('off')
cbar = plt.colorbar(plt.cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(vmin=min(edge_weights), vmax=max(edge_weights))), ax=ax1)
cbar.set_label('Number of Art Pieces')

# Plotting the bar chart for annual exhibitions
cities = list(annual_exhibitions.keys())
exhibition_counts = list(annual_exhibitions.values())
ax2.bar(cities, exhibition_counts, color='skyblue')
ax2.set_title("Annual Art Exhibitions per City", fontsize=14, fontweight='bold')
ax2.set_ylabel("Number of Exhibitions")
ax2.set_xlabel("City")
ax2.set_ylim(0, max(exhibition_counts) + 5)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.set_xticklabels(cities, rotation=45, ha='right')

# Adjust layout and show plot
plt.tight_layout()
plt.show()