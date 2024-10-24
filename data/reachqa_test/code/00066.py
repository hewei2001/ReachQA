import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define the graph
G = nx.DiGraph()

# Influencers and community sectors
influencers = ['Alex', 'Jordan', 'Taylor']
sectors = ['Lifestyle', 'Politics', 'Education', 'Fashion', 'Tech', 'Health']

# Add nodes to the graph
G.add_nodes_from(influencers, type='influencer')
G.add_nodes_from(sectors, type='sector')

# Add directed edges representing influencer impact with weight indicating strength
edges = [
    ('Alex', 'Lifestyle', 0.8),
    ('Alex', 'Fashion', 0.6),
    ('Jordan', 'Politics', 0.9),
    ('Jordan', 'Education', 0.7),
    ('Jordan', 'Tech', 0.5),
    ('Taylor', 'Health', 0.95),
    ('Taylor', 'Lifestyle', 0.4),
    ('Taylor', 'Fashion', 0.7)
]

G.add_weighted_edges_from(edges)

# Create a subplot grid
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

# Use a shell layout for the graph
pos = nx.shell_layout(G, nlist=[influencers, sectors])

# Plot 1: Directed Graph of Influences
plt.sca(axes[0])  # Set current axis
nx.draw_networkx_nodes(G, pos, nodelist=influencers, node_color='#89CFF0', node_size=2000, node_shape='o')
nx.draw_networkx_nodes(G, pos, nodelist=sectors, node_color='#FFD700', node_size=2500, node_shape='s')
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='gray', arrows=True, arrowsize=15, connectionstyle='arc3,rad=0.1', width=[G[u][v]['weight'] * 3 for u, v in G.edges])
nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')
plt.title('Social Media Influences in Communities\nMapping Influence Pathways', fontsize=14)
plt.axis('off')

# Plot 2: Bar Chart of Influence Distribution
plt.sca(axes[1])  # Set current axis
sector_influence = {sector: 0 for sector in sectors}
for influencer, sector, weight in edges:
    sector_influence[sector] += weight

sectors_sorted = sorted(sector_influence.items(), key=lambda x: x[1], reverse=True)
sectors_names, influence_values = zip(*sectors_sorted)

axes[1].barh(sectors_names, influence_values, color='#FFA07A')
axes[1].set_xlabel('Total Influence', fontsize=10)
axes[1].set_title('Sector Influence Distribution', fontsize=14)
axes[1].invert_yaxis()  # To display the largest value at the top

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()