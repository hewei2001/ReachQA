import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D

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

# Define color maps for nodes
node_colors = ['#8A2BE2', '#7FFF00', '#FF4500', '#1E90FF', '#FFD700']

# Gradient color for edges based on weight
edge_color_map = plt.cm.coolwarm
edge_weights = nx.get_edge_attributes(G, 'weight')
edge_colors = [edge_color_map(score / 100) for score in edge_weights.values()]

# Draw the directed graph with enhancements
fig, ax = plt.subplots(figsize=(12, 10))
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9, edgecolors='black')
nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color=edge_colors, arrows=True, arrowsize=15, width=[0.5 + weight / 20 for weight in edge_weights.values()])
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_color='darkblue')

# Add edge labels with an offset
edge_labels = {(u, v): f'{d["weight"]} pts' for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, label_pos=0.3, bbox=dict(facecolor='white', alpha=0.7))

# Title and layout adjustments
plt.title('Ancient Trade Routes and Cultural Exchanges:\nMythoLand’s Cultural Web', fontsize=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()

# Create a custom legend
legend_handles = [mpatches.Patch(color=node_colors[i], label=cities[i]) for i in range(len(cities))]
edge_color_gradients = Line2D([0], [0], color=edge_color_map(0.8), lw=4, label='Edge Influence')
plt.legend(handles=legend_handles + [edge_color_gradients], title="Cities and Influence", loc='lower right', bbox_to_anchor=(1, 0))

# Display the plot
plt.show()