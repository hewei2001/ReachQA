import matplotlib.pyplot as plt
import networkx as nx

# Define nodes (colonies) with an attribute indicating node importance
nodes = {
    'Earth Station': {'importance': 5},
    'Mars Colony': {'importance': 4},
    'Europa Base': {'importance': 3},
    'Titan Outpost': {'importance': 2},
    'Asteroid Belt Relay': {'importance': 3},
    'Lunar Gateway': {'importance': 2}
}

# Define edges with weights indicating communication link strength
edges = [
    ('Earth Station', 'Mars Colony', {'weight': 3}),
    ('Earth Station', 'Europa Base', {'weight': 2}),
    ('Earth Station', 'Lunar Gateway', {'weight': 4}),
    ('Mars Colony', 'Asteroid Belt Relay', {'weight': 2}),
    ('Europa Base', 'Titan Outpost', {'weight': 1}),
    ('Titan Outpost', 'Asteroid Belt Relay', {'weight': 3}),
    ('Lunar Gateway', 'Mars Colony', {'weight': 1})
]

# Create a graph
G = nx.Graph()

# Add nodes with attributes
for node, attr in nodes.items():
    G.add_node(node, **attr)

# Add edges with attributes
G.add_edges_from(edges)

# Use spring layout for positioning nodes
pos = nx.spring_layout(G, seed=42)

# Extract node importance for node sizes
node_sizes = [G.nodes[node]['importance'] * 1000 for node in G.nodes]

# Extract edge weights for edge thickness
edge_widths = [G.edges[edge]['weight'] for edge in G.edges]

# Draw nodes with varying sizes
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='skyblue', edgecolors='black')

# Draw edges with varying widths
nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color='gray')

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=9, font_color='black')

# Set plot title with line breaks for clarity
plt.title('Interstellar Communication Networks:\nNode Interconnectivity Among Solar System Colonies\nYear 2150', fontsize=14, pad=20)

# Turn off the axis
plt.axis('off')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()