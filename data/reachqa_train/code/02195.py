import matplotlib.pyplot as plt
import networkx as nx
import matplotlib as mpl

# Define the stations as nodes and the commuter flows as directed edges with weights
stations = [
    "Central Station", "Tech Hub", "Green Park", "Old Town", "University", 
    "Industrial Zone", "City Center", "Sky Port", "Maritime Dock"
]

edges = [
    ("Central Station", "Tech Hub", 50),
    ("Tech Hub", "University", 30),
    ("University", "City Center", 40),
    ("City Center", "Old Town", 20),
    ("Old Town", "Central Station", 45),
    ("Central Station", "Green Park", 25),
    ("Green Park", "Industrial Zone", 15),
    ("Industrial Zone", "Sky Port", 35),
    ("Sky Port", "Maritime Dock", 10),
    ("Maritime Dock", "Tech Hub", 30),
    ("University", "Green Park", 20),
    ("Old Town", "Industrial Zone", 5)
]

# Create the directed graph
G = nx.DiGraph()
G.add_nodes_from(stations)
G.add_weighted_edges_from(edges)

# Setup the plot
fig, ax = plt.subplots(figsize=(14, 10))  # Create a figure and axis
pos = nx.spring_layout(G, seed=42)

# Draw the nodes with customization
nx.draw_networkx_nodes(G, pos, node_size=1200, node_color='skyblue', alpha=0.9, edgecolors='k', ax=ax)

# Draw the edges with weights
edges_weights = [edge[2] for edge in edges]
nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='-|>', arrowsize=15, edge_color=edges_weights, 
                       edge_cmap=plt.cm.Blues, width=2, ax=ax)

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', verticalalignment='center', ax=ax)

# Draw edge labels for weights
edge_labels = {(u, v): f"{w}" for u, v, w in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=9, ax=ax)

# Create a ScalarMappable and add a colorbar
sm = mpl.cm.ScalarMappable(cmap=plt.cm.Blues, norm=plt.Normalize(vmin=min(edges_weights), vmax=max(edges_weights)))
sm.set_array([])
plt.colorbar(sm, label="Commuter Flow Intensity", ax=ax)

# Add title
plt.title("Flow of Commuters in CyberMetropolis:\nA Futuristic Transportation Network Analysis", fontsize=16, fontweight='bold')
plt.axis('off')

# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout()
plt.show()