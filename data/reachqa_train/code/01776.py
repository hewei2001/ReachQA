import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define nodes and edges with weights
nodes = [
    ('Solar Panels', {'type': 'source'}),
    ('Wind Turbines', {'type': 'source'}),
    ('Biomass Plants', {'type': 'source'}),
    ('Residential', {'type': 'consumer'}),
    ('Industries', {'type': 'consumer'}),
    ('Public Transport', {'type': 'consumer'}),
    ('Commercial', {'type': 'consumer'})
]

edges = [
    ('Solar Panels', 'Residential', {'weight': 200}),
    ('Solar Panels', 'Industries', {'weight': 150}),
    ('Solar Panels', 'Public Transport', {'weight': 100}),
    ('Solar Panels', 'Commercial', {'weight': 50}),
    ('Wind Turbines', 'Residential', {'weight': 100}),
    ('Wind Turbines', 'Industries', {'weight': 150}),
    ('Wind Turbines', 'Public Transport', {'weight': 100}),
    ('Wind Turbines', 'Commercial', {'weight': 50}),
    ('Biomass Plants', 'Residential', {'weight': 50}),
    ('Biomass Plants', 'Industries', {'weight': 100}),
    ('Biomass Plants', 'Public Transport', {'weight': 50}),
    ('Biomass Plants', 'Commercial', {'weight': 100})
]

# Add nodes and edges to graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Define positions for the nodes using a shell layout for better visualization
# Ensure the correct node labels are used in nlist
pos = nx.shell_layout(G, nlist=[
    ['Solar Panels', 'Wind Turbines', 'Biomass Plants'],
    ['Residential', 'Industries', 'Public Transport', 'Commercial']
])

# Set colors for nodes based on type
node_colors = ['#ffcc99' if data['type'] == 'source' else '#99ccff' for _, data in G.nodes(data=True)]

# Draw the graph with customizations
plt.figure(figsize=(14, 9))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color=node_colors, font_size=10, font_weight='bold', arrows=True, edge_color='gray', arrowsize=20, arrowstyle='-|>')

# Draw edge labels
edge_labels = {(u, v): f"{d['weight']} units" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# Title and layout adjustment
plt.title("Flow of Renewable Energy Production and Consumption\nin Enviroscape City - 2023", fontsize=16, fontweight='bold')
plt.tight_layout()

# Display the plot
plt.show()