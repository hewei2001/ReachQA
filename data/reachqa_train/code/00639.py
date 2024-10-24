import matplotlib.pyplot as plt
import networkx as nx

# Define nodes for transportation hubs
hubs = ['Downtown', 'Uptown', 'Midtown', 'Eastside', 'Westend']

# Define connections (edges) between hubs, representing transport routes
connections = [
    ('Downtown', 'Uptown', 3), 
    ('Downtown', 'Midtown', 1), 
    ('Downtown', 'Eastside', 4), 
    ('Downtown', 'Westend', 2),
    ('Uptown', 'Midtown', 5),
    ('Midtown', 'Eastside', 2), 
    ('Eastside', 'Westend', 3),
    ('Westend', 'Uptown', 1)
]

# Create an undirected graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(hubs)
G.add_weighted_edges_from(connections)

# Define layout for the graph
pos = nx.spring_layout(G, seed=42)

# Draw the nodes with colors based on their degree
node_color = [G.degree(node) for node in G.nodes]
nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=1200, cmap=plt.cm.Blues)

# Draw edges with varying widths based on weight
edges = nx.draw_networkx_edges(
    G, pos, width=[G[u][v]['weight'] for u, v in G.edges], alpha=0.6, edge_color='green'
)

# Draw labels for nodes and edges
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{G[u][v]['weight']}" for u, v in G.edges})

# Add a title and adjust layout
plt.title('Metropolitan Transportation Network\nKey Hubs and Connections', fontsize=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()

# Display the plot
plt.show()