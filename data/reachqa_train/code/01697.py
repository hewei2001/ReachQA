import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define nodes for sources and sectors
sources = ['Solar', 'Wind', 'Hydroelectric']
sectors = ['Residential', 'Commercial', 'Industrial']

# Add edges with weights (representing energy contribution in percentage)
edges = [
    ('Solar', 'Residential', 30),
    ('Solar', 'Commercial', 20),
    ('Wind', 'Commercial', 25),
    ('Wind', 'Industrial', 40),
    ('Hydroelectric', 'Residential', 40),
    ('Hydroelectric', 'Industrial', 30)
]

# Add nodes and edges to the graph
G.add_nodes_from(sources, type='source')
G.add_nodes_from(sectors, type='sector')
G.add_weighted_edges_from(edges)

# Define positions using the shell layout for better clarity
pos = nx.shell_layout(G, nlist=[sources, sectors])

# Draw the graph with customized node and edge attributes
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, nodelist=sources, node_size=1500, node_color='skyblue')
nx.draw_networkx_nodes(G, pos, nodelist=sectors, node_size=1500, node_color='lightgreen')
nx.draw_networkx_labels(G, pos, font_size=11, font_weight='bold')
edge_labels = {(u, v): f"{d['weight']}%" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='-|>', arrowsize=15, edge_color='gray', width=2)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=9)

# Add a title to the chart
plt.title("Renewable Energy Flow in EcoMetropolis\nFrom Sources to Urban Sectors", 
          fontsize=16, fontweight='bold', pad=20)

# Enhance layout and display
plt.tight_layout()
plt.show()