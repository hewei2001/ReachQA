import matplotlib.pyplot as plt
import networkx as nx

# Define cities and the volume of goods transported between them
city_connections = [
    ('Central City', 'North Ville', 10),
    ('Central City', 'East Haven', 8),
    ('Central City', 'South Port', 15),
    ('Central City', 'West End', 12),
    ('North Ville', 'East Haven', 6),
    ('East Haven', 'South Port', 5),
    ('South Port', 'West End', 9),
    ('West End', 'North Ville', 7)
]

# Create a directed graph
G = nx.DiGraph()

# Add edges and their respective weights
for start, end, volume in city_connections:
    G.add_edge(start, end, weight=volume)

# Define position of nodes for a clearer layout using a shell layout
pos = {
    'Central City': (0, 0),
    'North Ville': (0, 3),
    'East Haven': (3, 0),
    'South Port': (0, -3),
    'West End': (-3, 0)
}

# Plot the graph
plt.figure(figsize=(12, 8))
edges = G.edges(data=True)
weights = [d['weight'] for (u, v, d) in edges]

# Draw nodes, edges, and labels
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', edge_color='grey', font_size=10, font_weight='bold')
nx.draw_networkx_edges(G, pos, edge_color='black', arrows=True, width=2, alpha=0.6, arrowstyle='-|>', min_source_margin=15, min_target_margin=15)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{d["weight"]}k' for u, v, d in edges}, font_color='darkred', font_size=9)

# Add title and annotations
plt.title('Goods Transportation Network in Logistica\nFlow between Major Cities', fontsize=16, fontweight='bold', pad=20)

# Enhance layout to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()