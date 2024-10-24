import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import seaborn as sns

# Define nodes for different engineering disciplines
nodes = [
    'Mechanical', 'Electrical', 'Chemical', 'Civil', 'Software', 
    'Biomedical', 'Aerospace', 'Environmental', 'Materials'
]

# Define edges to show collaborations in key research areas
edges = [
    ('Mechanical', 'Electrical'), 
    ('Electrical', 'Software'), 
    ('Software', 'Biomedical'), 
    ('Chemical', 'Environmental'), 
    ('Civil', 'Environmental'), 
    ('Aerospace', 'Mechanical'), 
    ('Biomedical', 'Chemical'), 
    ('Materials', 'Aerospace'), 
    ('Materials', 'Mechanical'), 
    ('Environmental', 'Civil'),
    ('Civil', 'Chemical'),
    ('Mechanical', 'Software')
]

# Initialize a Graph
G = nx.Graph()

# Add nodes and edges
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Calculate node degrees (number of connections)
node_degrees = dict(G.degree)

# Set up node attributes: size increases with degree, color by modularity class
node_sizes = [v * 300 for v in node_degrees.values()]
node_colors = ['#FFDDC1' if degree > 2 else '#C1E1FF' for degree in node_degrees.values()]

# Set up figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Subplot 1: Network Graph
ax1 = axes[0]
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9, edgecolors='black', ax=ax1)
nx.draw_networkx_edges(G, pos, width=2, edge_color='grey', style='dashed', ax=ax1)
nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold', ax=ax1)
ax1.set_title('Interdisciplinary Collaborations\nin Engineering Research', fontsize=14, weight='bold', pad=20)
ax1.axis('off')

# Subplot 2: Heatmap of Collaboration Frequency
ax2 = axes[1]
collaboration_matrix = np.zeros((len(nodes), len(nodes)))

# Fill the matrix with frequency of collaborations
for (start, end) in edges:
    idx_start, idx_end = nodes.index(start), nodes.index(end)
    collaboration_matrix[idx_start, idx_end] += 1
    collaboration_matrix[idx_end, idx_start] += 1

sns.heatmap(collaboration_matrix, annot=True, cmap='Blues', xticklabels=nodes, yticklabels=nodes, cbar=True, ax=ax2)
ax2.set_title('Collaboration Frequency Heatmap', fontsize=14, weight='bold', pad=10)
ax2.set_xlabel('Engineering Disciplines')
ax2.set_ylabel('Engineering Disciplines')
plt.xticks(rotation=45, ha='right', fontsize=9)
plt.yticks(fontsize=9)

# Adjust layout to fit all elements
plt.tight_layout()

# Display the plot
plt.show()