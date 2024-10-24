import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import seaborn as sns

# Adjusted node positions for better distribution
nodes = {
    'Central Hub': (0, 0),
    'North Gate': (-2, 4),
    'East Gate': (4, 2),
    'South Gate': (-2, -4),
    'Northeast Hub': (5, 5),
    'Southeast Hub': (6, -3),
    'Innovation Park': (8, 2),
    'Industrial Zone': (-6, -5)
}

# Modified edges with traffic volume and modes
edges = [
    ('Central Hub', 'North Gate', (20, 'Automated Cars')),
    ('Central Hub', 'East Gate', (35, 'Hyperloops')),
    ('Central Hub', 'South Gate', (15, 'Drones')),
    ('North Gate', 'Northeast Hub', (22, 'Hyperloops')),
    ('East Gate', 'Innovation Park', (25, 'Automated Cars')),
    ('South Gate', 'Industrial Zone', (30, 'Drones')),
    ('Northeast Hub', 'Innovation Park', (18, 'Automated Cars')),
    ('Southeast Hub', 'Industrial Zone', (12, 'Hyperloops')),
    ('Innovation Park', 'Southeast Hub', (14, 'Drones'))
]

# Updated travel time data
travel_times = {
    ('Central Hub', 'North Gate'): 12,
    ('Central Hub', 'East Gate'): 8,
    ('Central Hub', 'South Gate'): 15,
    ('North Gate', 'Northeast Hub'): 14,
    ('East Gate', 'Innovation Park'): 18,
    ('South Gate', 'Industrial Zone'): 22,
    ('Northeast Hub', 'Innovation Park'): 10,
    ('Southeast Hub', 'Industrial Zone'): 16,
    ('Innovation Park', 'Southeast Hub'): 14
}

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from([(u, v, {'traffic': t[0], 'mode': t[1], 'time': travel_times[(u, v)]}) for u, v, t in edges])

# Define colors for transportation modes
mode_colors = {'Automated Cars': '#FF6666', 'Hyperloops': '#66B3FF', 'Drones': '#99FF99'}

# Extract edge colors and weights
edge_colors = [mode_colors[G[u][v]['mode']] for u, v in G.edges()]
edge_weights = [G[u][v]['traffic'] / 4 for u, v in G.edges()]  # Increased weight scale for better visibility

# Set up the figure and subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Plot 1: Network Graph
nx.draw_networkx_nodes(G, nodes, ax=axes[0], node_size=800, node_color='lightgray')
nx.draw_networkx_edges(G, nodes, ax=axes[0], arrowstyle='-|>', arrowsize=15, edge_color=edge_colors, width=edge_weights)
nx.draw_networkx_labels(G, nodes, ax=axes[0], font_size=10, font_weight='bold')

# Annotate edges with traffic volume and travel times
edge_labels = {(u, v): f"{G[u][v]['traffic']} vol" for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, nodes, edge_labels=edge_labels, ax=axes[0], font_size=8)

# Legend for the network graph
for mode, color in mode_colors.items():
    axes[0].plot([], [], color=color, label=mode, linewidth=5)
axes[0].legend(loc='upper left', title='Transportation Modes', fontsize=9)

axes[0].set_title('Futurapolis Traffic Flow\nExploring Innovative Transportation Modes', fontsize=14, fontweight='bold')
axes[0].axis('off')

# Plot 2: Heatmap of Travel Times
# Prepare data for heatmap
heatmap_data = np.zeros((len(nodes), len(nodes)))
for (u, v), time in travel_times.items():
    u_idx = list(nodes.keys()).index(u)
    v_idx = list(nodes.keys()).index(v)
    heatmap_data[u_idx][v_idx] = time

sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="YlGnBu", xticklabels=list(nodes.keys()), yticklabels=list(nodes.keys()), ax=axes[1])
axes[1].set_title('Travel Times Between Locations\n(in minutes)', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Destination')
axes[1].set_ylabel('Origin')

plt.tight_layout()
plt.show()