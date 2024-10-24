import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define nodes
departments = ['Scriptwriting', 'Casting', 'Pre-production', 'Filming', 'Post-production', 'Marketing', 'Release']

# Define edges with weights (relationships)
edges = [
    ('Scriptwriting', 'Pre-production', 2),
    ('Scriptwriting', 'Casting', 1),
    ('Pre-production', 'Filming', 3),
    ('Casting', 'Filming', 2),
    ('Filming', 'Post-production', 4),
    ('Post-production', 'Marketing', 2),
    ('Post-production', 'Release', 3),
    ('Marketing', 'Release', 1)
]

# Add nodes and edges to the graph
G.add_nodes_from(departments)
G.add_weighted_edges_from(edges)

# Position nodes in a shell layout for better readability
pos = nx.shell_layout(G)

# Draw nodes with customized appearance
nx.draw_networkx_nodes(G, pos, node_size=2500, node_color='skyblue', node_shape='o', edgecolors='black')

# Draw edges with arrows
nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='-|>', arrowsize=15, edge_color='gray', connectionstyle='arc3,rad=0.1')

# Draw labels on nodes
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

# Draw edge labels (weights)
edge_labels = {(u, v): d for u, v, d in G.edges(data='weight')}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=8, font_color='maroon')

# Title with line breaks for readability
plt.title("Movie Production Workflow:\nDepartment Interdependencies", fontsize=16, fontweight='bold', pad=20)

# Remove axis for a cleaner look
plt.axis('off')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()