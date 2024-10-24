import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define nodes and edges
nodes = [
    'MIT', 'Stanford', 'Caltech', 'Oxford', 'Cambridge', 
    'Tsinghua', 'Tokyo U', 'ETH Zurich', 'Imperial College', 'KTH'
]

edges = [
    ('MIT', 'Stanford'),
    ('MIT', 'Caltech'),
    ('Stanford', 'Caltech'),
    ('Oxford', 'Cambridge'),
    ('Tsinghua', 'Tokyo U'),
    ('ETH Zurich', 'Imperial College'),
    ('Caltech', 'Cambridge'),
    ('Oxford', 'ETH Zurich'),
    ('Cambridge', 'KTH'),
    ('Tokyo U', 'Imperial College'),
    ('Stanford', 'Tokyo U'),
    ('KTH', 'Tsinghua')
]

# Create a graph
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Calculate node centrality
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
node_sizes = [5000 * degree_centrality[node] for node in G.nodes()]
node_colors = [betweenness_centrality[node] for node in G.nodes()]

# Position nodes
pos = nx.spring_layout(G, seed=42)

# Draw the graph
fig, ax = plt.subplots(figsize=(14, 9))
nx.draw_networkx_edges(G, pos, ax=ax, edge_color='grey', width=2, alpha=0.5)
nx.draw_networkx_nodes(G, pos, ax=ax, node_size=node_sizes, node_color=node_colors, cmap=plt.cm.coolwarm, edgecolors='black')
nx.draw_networkx_labels(G, pos, ax=ax, font_size=9, font_weight='bold', font_color='darkblue')

# Title and annotations
plt.title('Collaborative Network in Renewable Energy Research\nCentrality Analysis (2023)', fontsize=16, fontweight='bold', loc='center', pad=20)
plt.annotate('Nodes: Institutions | Edges: Collaborations\nSize: Degree Centrality | Color: Betweenness Centrality', 
             xy=(0.05, 0.02), fontsize=10, xycoords='axes fraction', alpha=0.7)

# Add color bar
sm = plt.cm.ScalarMappable(cmap=plt.cm.coolwarm, norm=plt.Normalize(vmin=min(node_colors), vmax=max(node_colors)))
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label('Betweenness Centrality', rotation=270, labelpad=20)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()