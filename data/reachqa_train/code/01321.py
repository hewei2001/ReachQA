import matplotlib.pyplot as plt
import networkx as nx

# Define the nodes for the directed graph
sources = ['Solar Farm', 'Wind Farm', 'Hydropower Plant']
sectors = ['Residential', 'Commercial', 'Industrial']

# Define the directed edges with energy flow values
energy_flows = [
    ('Solar Farm', 'Residential', 40),
    ('Solar Farm', 'Commercial', 30),
    ('Wind Farm', 'Residential', 20),
    ('Wind Farm', 'Industrial', 50),
    ('Hydropower Plant', 'Commercial', 40),
    ('Hydropower Plant', 'Industrial', 60)
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_nodes_from(sources + sectors)

# Add edges with weights
for source, sector, flow in energy_flows:
    G.add_edge(source, sector, weight=flow)

# Define positions for a clear layout using a shell layout
pos = nx.shell_layout(G, nlist=[sources, sectors])

# Extract weights for edge labels
edge_labels = {(u, v): f'{d["weight"]} units' for u, v, d in G.edges(data=True)}

# Draw the directed graph
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_size=1800, node_color='#a0c4ff')
nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color='gray', arrows=True, arrowsize=20, width=2)
nx.draw_networkx_labels(G, pos, font_size=11, font_weight='bold')

# Add edge labels
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, label_pos=0.3)

# Title and layout adjustments
plt.title('GreenTown Renewable Energy\nDistribution Network', fontsize=16, fontweight='bold', pad=20)
plt.axis('off')
plt.tight_layout()

# Display the plot
plt.show()