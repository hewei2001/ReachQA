import matplotlib.pyplot as plt
import networkx as nx

# Define the countries as nodes in the network
countries = ["China", "India", "Sri Lanka", "Japan", "Kenya", 
             "UK", "USA", "Germany", "Pakistan", "Russia"]

# Define trade relationships as edges (connections)
trade_relationships = [
    ("China", "USA"), ("China", "Germany"), ("India", "UK"),
    ("Sri Lanka", "Russia"), ("Kenya", "Pakistan"),
    ("Japan", "USA"), ("China", "India"), ("India", "Russia"),
    ("Sri Lanka", "Germany"), ("Kenya", "UK"), ("China", "Pakistan"),
    ("Japan", "Russia"), ("India", "Germany"), ("Sri Lanka", "USA")
]

# Create a graph object
G = nx.Graph()

# Add nodes and edges
G.add_nodes_from(countries)
G.add_edges_from(trade_relationships)

# Create positions for the nodes using spring layout
pos = nx.spring_layout(G, seed=42)

# Plotting the network
plt.figure(figsize=(14, 10))
nodes = nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='lightgreen', edgecolors='black')
edges = nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.7, edge_color='gray')

# Draw the node labels
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# Draw the edge labels
edge_labels = {edge: 'Trade' for edge in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='gray', font_size=9, label_pos=0.3)

# Customize the plot
plt.title("Global Tea Trade Networks:\nKey Countries and Trade Relationships", fontsize=18, fontweight='bold', loc='center')
plt.box(False)  # Remove the box around the plot
plt.axis('off')  # Turn off the axis

# Automatically adjust the layout to fit everything neatly
plt.tight_layout()

# Show plot
plt.show()