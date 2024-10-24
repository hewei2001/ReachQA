import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import matplotlib.colors as mcolors

# Define the cities
cities = ['Alexandria', 'Babylon', 'Xi\'an', 'Rome', 'Samarkand']

# Define trade routes and volumes (source, target, volume)
trade_routes = [
    ('Alexandria', 'Babylon', 40),
    ('Babylon', 'Xi\'an', 65),
    ('Xi\'an', 'Samarkand', 80),
    ('Samarkand', 'Rome', 55),
    ('Rome', 'Alexandria', 60),
    ('Babylon', 'Alexandria', 35),
    ('Xi\'an', 'Babylon', 50),
    ('Rome', 'Xi\'an', 45),
    ('Samarkand', 'Babylon', 70),
]

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(cities)
G.add_weighted_edges_from(trade_routes)

# Calculate total trade volume for each city
trade_volume = {city: 0 for city in cities}
for u, v, data in G.edges(data=True):
    trade_volume[u] += data['weight']
    trade_volume[v] += data['weight']

# Positions for visualization
positions = nx.spring_layout(G, seed=42)

# Color palette for nodes and bars
node_colors = list(mcolors.TABLEAU_COLORS.values())[:len(cities)]
bar_colors = mcolors.TABLEAU_COLORS['tab:green']

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 10), gridspec_kw={'width_ratios': [3, 2]})

# Plot Network Graph on first subplot
nx.draw_networkx_nodes(G, positions, ax=axes[0], node_size=1200, node_color=node_colors, alpha=0.5)
nx.draw_networkx_labels(G, positions, ax=axes[0], font_size=12, font_color='black')
edges = nx.draw_networkx_edges(
    G, positions, ax=axes[0], arrowstyle='-|>', arrowsize=15, edge_color='grey', width=2,
    connectionstyle='arc3,rad=0.2', alpha=1
)
edge_labels = {(u, v): f'{d["weight"]} tons' for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, positions, ax=axes[0], edge_labels=edge_labels, font_color='darkred')

axes[0].set_title("Ancient Trade Routes Along the Silk Road", fontsize=16, fontweight='bold')
axes[0].axis('off')

# Plot Bar Chart on second subplot
bars = axes[1].bar(trade_volume.keys(), trade_volume.values(), color=bar_colors, alpha=0.8)
for bar, city in zip(bars, cities):
    bar.set_color(node_colors[cities.index(city)])

axes[1].set_title("Total Trade Volume per City", fontsize=14, fontweight='bold')
axes[1].set_xlabel("Cities", fontsize=12)
axes[1].set_ylabel("Trade Volume (Tons)", fontsize=12)
axes[1].set_xticks(np.arange(len(cities)))
axes[1].set_xticklabels(cities, rotation=30, ha='right')

# Layout adjustment
plt.tight_layout()

# Display the plot
plt.show()