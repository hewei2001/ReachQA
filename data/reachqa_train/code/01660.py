import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define nodes for the farm system
nodes = [
    "Rainwater", "Solar Energy", "Compost", "Crop Fields", 
    "Irrigation System", "Biogas Plant", "Livestock", "Market"
]

# Add nodes to the graph
G.add_nodes_from(nodes)

# Define the directed edges (flows between nodes)
edges = [
    ("Rainwater", "Irrigation System"),
    ("Solar Energy", "Biogas Plant"),
    ("Solar Energy", "Crop Fields"),
    ("Compost", "Crop Fields"),
    ("Compost", "Biogas Plant"),
    ("Crop Fields", "Market"),
    ("Irrigation System", "Crop Fields"),
    ("Biogas Plant", "Crop Fields"),
    ("Livestock", "Biogas Plant"),
    ("Livestock", "Compost"),
    ("Crop Fields", "Livestock"),
]

# Add edges to the graph
G.add_edges_from(edges)

# Define node positions for better visualization
pos = {
    "Rainwater": (0, 3),
    "Solar Energy": (2, 3),
    "Compost": (1, 1.5),
    "Crop Fields": (3, 2),
    "Irrigation System": (1, 4),
    "Biogas Plant": (2, 0.5),
    "Livestock": (0, 0),
    "Market": (4, 2),
}

# Draw the graph
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='lightgreen', edgecolors='black')
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='gray', arrows=True, arrowsize=20, arrowstyle='-|>')
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# Draw edge labels
edge_labels = {
    ("Rainwater", "Irrigation System"): "Water",
    ("Solar Energy", "Biogas Plant"): "Energy",
    ("Solar Energy", "Crop Fields"): "Energy",
    ("Compost", "Crop Fields"): "Nutrients",
    ("Compost", "Biogas Plant"): "Nutrients",
    ("Crop Fields", "Market"): "Crops",
    ("Irrigation System", "Crop Fields"): "Water",
    ("Biogas Plant", "Crop Fields"): "Energy",
    ("Livestock", "Biogas Plant"): "Waste",
    ("Livestock", "Compost"): "Manure",
    ("Crop Fields", "Livestock"): "Feed"
}

# Draw the edge labels
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

# Set the title
plt.title('Sustainable Resource Flow in Green Acres Farm', fontsize=16, fontweight='bold')

# Automatically adjust layout to avoid text overlap
plt.tight_layout()

# Remove axes for clarity
plt.axis('off')

# Display the plot
plt.show()