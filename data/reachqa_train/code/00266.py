import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define the nodes and their connections (edges)
nodes = [
    'AI', 
    'Blockchain', 
    'Quantum Computing', 
    'Augmented Reality', 
    'Sustainable Energy', 
    'Biotechnology', 
    'Cybersecurity', 
    'IoT'
]
edges = [
    ('AI', 'IoT'),
    ('Blockchain', 'Cybersecurity'),
    ('Quantum Computing', 'AI'),
    ('Augmented Reality', 'IoT'),
    ('Sustainable Energy', 'Biotechnology'),
    ('Biotechnology', 'Sustainable Energy'),
    ('Cybersecurity', 'Quantum Computing'),
    ('IoT', 'Cybersecurity'),
    ('Blockchain', 'Augmented Reality'),
    ('AI', 'Biotechnology')
]

# Create a directed graph using NetworkX
G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Define the layout for the graph
pos = nx.circular_layout(G)

# Compute node sizes based on their degree
node_sizes = [3000 * (1 + G.degree(node)) for node in nodes]

# Set node colors by category for visual variety
node_colors = ['skyblue', 'orange', 'green', 'purple', 'red', 'yellow', 'blue', 'pink']

# Start plotting
plt.figure(figsize=(14, 12))
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.8)
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='gray', arrowsize=15, arrowstyle='-|>', width=2, connectionstyle='arc3,rad=0.2')
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_color='darkblue')

# Add a title with multiple lines and configure layout
plt.title('Interconnected Ideas in\nFuturism and Innovation', fontsize=18, fontweight='bold')
plt.axis('off')
plt.tight_layout()

# Highlight a cycle in the graph if it exists
try:
    cycle = nx.find_cycle(G, orientation='original')
    cycle_edges = [(u, v) for u, v, _ in cycle]
    nx.draw_networkx_edges(G, pos, edgelist=cycle_edges, edge_color='gold', style='dashed', width=3)
except nx.NetworkXNoCycle:
    pass

# Add a color bar for node categories
color_legend_labels = ['AI', 'Blockchain', 'Quantum Computing', 'Augmented Reality', 
                       'Sustainable Energy', 'Biotechnology', 'Cybersecurity', 'IoT']
for label, color in zip(color_legend_labels, node_colors):
    plt.scatter([], [], color=color, label=label, s=100)
plt.legend(loc='best', title='Node Categories')

# Display the plot
plt.show()