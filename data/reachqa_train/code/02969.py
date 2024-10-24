import matplotlib.pyplot as plt
import networkx as nx

# Define cities (nodes) in MythoLand
cities = ['Atlantis', 'Eldoria', 'Luminar', 'Volantis', 'Draconis']

# Define cultural exchanges (directed edges) with influence scores
cultural_exchanges = [
    ('Atlantis', 'Eldoria', 80),
    ('Eldoria', 'Luminar', 65),
    ('Luminar', 'Volantis', 90),
    ('Volantis', 'Draconis', 75),
    ('Draconis', 'Atlantis', 60),
    ('Atlantis', 'Volantis', 70),
    ('Volantis', 'Eldoria', 55)
]

# Cultural influence index for each city
cultural_influence_index = {
    'Atlantis': 85,
    'Eldoria': 70,
    'Luminar': 88,
    'Volantis': 82,
    'Draconis': 78
}

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(cities)

# Add edges with influence scores
for source, target, score in cultural_exchanges:
    G.add_edge(source, target, weight=score)

# Assign node sizes based on cultural influence index
node_sizes = [1500 + cultural_influence_index[city]*10 for city in cities]

# Define positions using a spring layout
pos = nx.spring_layout(G, seed=42)

# Extract weights for edge labels and widths
edge_labels = {(u, v): f'{d["weight"]} pts' for u, v, d in G.edges(data=True)}
edge_widths = [0.5 + G[u][v]['weight'] / 20 for u, v in G.edges()]

# Define color maps for nodes
node_colors = ['#8A2BE2', '#7FFF00', '#FF4500', '#1E90FF', '#FFD700']

# Draw the directed graph
plt.figure(figsize=(12, 10))
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9, edgecolors='black')
nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color='gray', arrows=True, arrowsize=15, width=edge_widths)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_color='darkblue')

# Add edge labels with an offset
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, label_pos=0.3, bbox=dict(facecolor='white', alpha=0.7))

# Title and layout adjustments
plt.title('Ancient Trade Routes and Cultural Exchanges:\nMythoLand’s Cultural Web', fontsize=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()

# Create a custom legend
legend_lines = [plt.Line2D([0], [0], color=node_colors[i], lw=4) for i in range(len(cities))]
plt.legend(legend_lines, cities, title="Cities of MythoLand", loc='lower right', bbox_to_anchor=(1, 0))

# Display the plot
plt.show()