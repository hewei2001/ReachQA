import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Nodes representing AI/ML technologies
nodes = [
    'Neural Networks', 'Deep Learning', 'Natural Language Processing',
    'Computer Vision', 'Reinforcement Learning', 'Data Mining',
    'Bayesian Networks', 'Generative Models', 'Speech Recognition'
]

# Add nodes to the graph
G.add_nodes_from(nodes)

# Define edges representing influences or dependencies
edges = [
    ('Neural Networks', 'Deep Learning'),
    ('Deep Learning', 'Computer Vision'),
    ('Deep Learning', 'Natural Language Processing'),
    ('Reinforcement Learning', 'Data Mining'),
    ('Natural Language Processing', 'Speech Recognition'),
    ('Bayesian Networks', 'Generative Models'),
    ('Deep Learning', 'Generative Models'),
    ('Generative Models', 'Computer Vision'),
    ('Data Mining', 'Bayesian Networks')
]

# Add edges to the graph
G.add_edges_from(edges)

# Define positions for a clearer layout
pos = nx.spring_layout(G, seed=42)

# Plot the graph
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightblue', edgecolors='k')
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='gray', width=2)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', horizontalalignment='center', verticalalignment='center')

# Title and annotations
plt.title("Navigating the Web of AI:\nInterconnections in Modern Machine Learning Technologies", fontsize=16, fontweight='bold')
plt.annotate('Arrows indicate directional influence or dependency', xy=(0.5, 0), xytext=(0.5, -0.1), fontsize=11,
             ha='center', va="center", xycoords='axes fraction', textcoords='axes fraction')

# Remove axis
plt.axis('off')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()