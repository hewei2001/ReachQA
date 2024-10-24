import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Create a directed graph
G = nx.DiGraph()

# Add nodes
nodes = ['Healthcare', 'Education', 'Transportation', 'Public Safety', 'Urban Planning']
G.add_nodes_from(nodes)

# Define edges with weights representing data stream bandwidth in Mbps
edges = [
    ('Healthcare', 'Education', 50),
    ('Healthcare', 'Transportation', 70),
    ('Education', 'Transportation', 40),
    ('Education', 'Public Safety', 60),
    ('Transportation', 'Public Safety', 80),
    ('Public Safety', 'Urban Planning', 90),
    ('Urban Planning', 'Healthcare', 30)
]

# Add edges to the graph
G.add_weighted_edges_from(edges)

# Calculate incoming and outgoing bandwidth for each node
in_bandwidth = {node: sum(d['weight'] for _, node, d in G.in_edges(node, data=True)) for node in nodes}
out_bandwidth = {node: sum(d['weight'] for node, _, d in G.out_edges(node, data=True)) for node in nodes}

# Create a subplot with 1 row and 2 columns
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Plot the original network graph on the first subplot
pos = nx.shell_layout(G)
nx.draw_networkx_nodes(G, pos, ax=ax1, node_size=2500, node_color='skyblue', node_shape='o')
nx.draw_networkx_edges(G, pos, ax=ax1, edgelist=edges, arrowstyle='-|>', arrowsize=15, edge_color='gray', width=2)
edge_labels = {(u, v): f"{d['weight']} Mbps" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, ax=ax1)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', ax=ax1)
ax1.set_title("Digital Data Streams:\nA Directed Network of Interconnected Sectors", size=14, fontweight='bold')
ax1.axis('off')

# Plot the new bar chart on the second subplot
x = np.arange(len(nodes))
width = 0.35
ax2.bar(x - width/2, [out_bandwidth[node] for node in nodes], width, label='Outgoing Bandwidth', color='steelblue')
ax2.bar(x + width/2, [in_bandwidth[node] for node in nodes], width, label='Incoming Bandwidth', color='lightcoral')

ax2.set_xlabel('Sectors')
ax2.set_ylabel('Total Bandwidth (Mbps)')
ax2.set_title('Sector Bandwidth Distribution')
ax2.set_xticks(x)
ax2.set_xticklabels(nodes)
ax2.legend(loc='upper left')
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust the layout
plt.tight_layout()

# Display the plots
plt.show()