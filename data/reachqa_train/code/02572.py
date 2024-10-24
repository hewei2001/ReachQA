import matplotlib.pyplot as plt
import networkx as nx

# Define the energy sources and consumption sectors
energy_sources = ['Solar', 'Wind', 'Hydro', 'Biomass']
consumption_sectors = ['Residential', 'Industrial', 'Transport']

# Create a directed graph
G = nx.DiGraph()

# Add nodes for energy sources and consumption sectors
G.add_nodes_from(energy_sources, type='source')
G.add_nodes_from(consumption_sectors, type='sink')

# Define edges with their respective energy flow values (in arbitrary units)
edges = [
    ('Solar', 'Residential', 25),
    ('Solar', 'Industrial', 10),
    ('Wind', 'Residential', 20),
    ('Wind', 'Transport', 25),
    ('Hydro', 'Industrial', 30),
    ('Biomass', 'Residential', 15),
    ('Biomass', 'Transport', 10),
]

# Add edges to the graph
G.add_weighted_edges_from(edges)

# Define position layout for the nodes using a shell layout for better visibility
pos = nx.shell_layout(G)

# Color map for sources and sinks
node_colors = ['#ffd700' if G.nodes[node]['type'] == 'source' else '#87ceeb' for node in G.nodes()]

# Draw the graph
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color=node_colors, alpha=0.8)
nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='-|>', arrowsize=15, width=2, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', verticalalignment='center', horizontalalignment='center')

# Annotate edges with energy flow values
edge_labels = {(u, v): f"{d}" for u, v, d in G.edges(data='weight')}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

# Title and additional plot details
plt.title("Renewable Energy Distribution on EcoIsland\nExploring the Flow from Sources to Sectors", fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.axis('off')

# Display the plot
plt.show()