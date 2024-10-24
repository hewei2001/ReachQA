import matplotlib.pyplot as plt
import networkx as nx

# Define expanded cities and the volume and cost of goods transported between them
city_connections = [
    ('Central City', 'North Ville', 10, 5),
    ('Central City', 'East Haven', 8, 4),
    ('Central City', 'South Port', 15, 6),
    ('Central City', 'West End', 12, 7),
    ('North Ville', 'East Haven', 6, 2),
    ('East Haven', 'South Port', 5, 3),
    ('South Port', 'West End', 9, 4),
    ('West End', 'North Ville', 7, 5),
    ('North Ville', 'Central City', 11, 4),
    ('East Haven', 'Central City', 9, 4),
    ('South Port', 'Central City', 13, 6),
    ('West End', 'Central City', 14, 5)
]

# Create a directed graph with multi-criteria (volume and cost)
G = nx.DiGraph()

# Add edges with volume and cost weights
for start, end, volume, cost in city_connections:
    G.add_edge(start, end, volume=volume, cost=cost)

# Define position of nodes using a circular layout for better visibility
pos = nx.circular_layout(G)

# Plot the graph
plt.figure(figsize=(14, 10))
edges = G.edges(data=True)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightblue', edgecolors='black')

# Draw edges with varying thickness and color based on volume
edges_weights = [(d['volume'], d['cost']) for (u, v, d) in edges]
edge_colors = [weight[0] for weight in edges_weights]
edge_widths = [weight[1] for weight in edges_weights]

edges_collection = nx.draw_networkx_edges(
    G, pos, edge_color=edge_colors, edge_cmap=plt.cm.Blues, width=edge_widths, alpha=0.7,
    connectionstyle='arc3,rad=0.1', arrows=True, arrowstyle='-|>', min_source_margin=15, min_target_margin=15
)

# Add labels for nodes and edges
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
edge_labels = {(u, v): f'{d["volume"]}k goods\n${d["cost"]} cost' for u, v, d in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, bbox=dict(alpha=0.1, edgecolor='none', facecolor='white'))

# Add title and adjust layout
plt.title('Advanced Goods Transportation Network\nMulti-Criteria Analysis between Major Cities', fontsize=16, fontweight='bold', pad=20)

# Create a ScalarMappable object for the color bar
sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues, norm=plt.Normalize(vmin=min(edge_colors), vmax=max(edge_colors)))
sm.set_array([])  # Dummy call to set_array, because we only need the scalar mappable

# Add color bar with the correct association
cbar = plt.colorbar(sm, ax=plt.gca(), label='Volume (in k goods)', shrink=0.8)

plt.axis('off')
plt.tight_layout()

# Display the plot
plt.show()