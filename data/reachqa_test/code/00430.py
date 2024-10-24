import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define colonies and their connections (edges) with message frequency
colonies = ["Earth", "Mars", "Titan", "Europa", "Ganymede"]
connections = [
    ("Earth", "Mars", 100),
    ("Mars", "Titan", 70),
    ("Titan", "Europa", 50),
    ("Europa", "Ganymede", 60),
    ("Ganymede", "Earth", 80),
    ("Earth", "Titan", 30),
    ("Mars", "Europa", 40)
]

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(colonies)
G.add_weighted_edges_from(connections)

# Define positions for a circular layout
pos = nx.circular_layout(G)

# Calculate centrality as additional data
centrality = nx.betweenness_centrality(G)

# Plot Network Graph
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_size=1800, node_color='lightblue', edgecolors='black')
nx.draw_networkx_edges(
    G, pos, arrowstyle='-|>', arrowsize=15, edge_color='grey', width=2, connectionstyle='arc3,rad=0.1'
)
edge_labels = {(start, end): f'{weight} msgs' for start, end, weight in connections}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkred', font_size=10)
nx.draw_networkx_labels(G, pos, font_size=12, font_color='darkblue')

# Overlay Plot: Bar Chart for Centrality
# Bar chart positioned near the bottom right, avoiding overlap with the network graph
ax = plt.gca()
centrality_values = list(centrality.values())
ax_bar = ax.inset_axes([0.75, 0.8, 0.2, 0.35])  # [x, y, width, height]
ax_bar.barh(range(len(colonies)), centrality_values, color='skyblue', edgecolor='black', alpha=0.7)
ax_bar.set_title("Node Centrality", fontsize=12, fontweight='bold')
ax_bar.set_xlabel("Centrality", fontsize=10)
ax_bar.set_yticks(range(len(colonies)))
ax_bar.set_yticklabels(colonies, fontsize=10)
ax_bar.xaxis.set_ticks_position('top')
ax_bar.xaxis.set_label_position('top')

# Title and layout adjustments
plt.title("Interstellar Communication Flow\nAnalyzing Message Routes Among Space Colonies", 
          fontsize=16, fontweight='bold', loc='left')
plt.axis('off')
plt.tight_layout()

# Display the plot
plt.show()