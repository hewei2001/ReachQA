import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as mpatches

# Define nodes and edges with weights
nodes = [
    'Raw Material\nSourcing', 'Fabric\nProduction',
    'Garment\nManufacturing', 'Quality\nControl',
    'Distribution', 'Retail'
]

edges = [
    ('Raw Material\nSourcing', 'Fabric\nProduction', 8),
    ('Fabric\nProduction', 'Garment\nManufacturing', 10),
    ('Garment\nManufacturing', 'Quality\nControl', 6),
    ('Quality\nControl', 'Distribution', 4),
    ('Distribution', 'Retail', 9),
    ('Garment\nManufacturing', 'Distribution', 5)
]

# Create directed graph
G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

# Position nodes with a force-directed layout
pos = nx.spring_layout(G, seed=42)

# Define node attributes
node_shapes = ['o', 's', 'D', 'o', 's', 'D']
node_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
node_sizes = [G.degree(n, weight='weight') * 500 for n in G.nodes]

# Define edge attributes
edge_weights = [d['weight'] for _, _, d in G.edges(data=True)]
edge_colors = ['#000000' for _ in edges]

# Plot
fig, ax = plt.subplots(figsize=(10, 7))

# Draw nodes with varied shapes
for (shape, color, size, node) in zip(node_shapes, node_colors, node_sizes, nodes):
    nx.draw_networkx_nodes(G, pos, nodelist=[node], node_size=size,
                           node_color=color, node_shape=shape, ax=ax)

# Draw weighted edges with variable thickness
nx.draw_networkx_edges(G, pos, width=[weight/2 for weight in edge_weights],
                       edge_color=edge_colors, arrows=True, arrowsize=15, ax=ax)

# Add labels
nx.draw_networkx_labels(G, pos, font_size=9, font_color='black', font_weight='bold')
edge_labels = {(u, v): f'{d["weight"]}' for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, label_pos=0.5)

# Title and annotations
plt.title("Fashion Supply Chain Network\nFrom Source to Retail", fontsize=14, fontweight='bold')
legend_patches = [mpatches.Patch(color=color, label=node.replace('\n', ' ')) for color, node in zip(node_colors, nodes)]
plt.legend(handles=legend_patches, title="Node Types", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)

# Enhance layout and visualization
plt.axis('off')
plt.tight_layout()
plt.show()