import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.MultiDiGraph()

# Define nodes and edges with more complexity
nodes = ["Italy", "India", "Mexico", "Japan", "France", "China", "Spain", "USA"]
edges = [
    ("Italy", "Mexico", "Tomatoes", 3, 10, 5),
    ("Italy", "India", "Tomatoes", 2, 8, 7),
    ("India", "Japan", "Rice", 4, 12, 6),
    ("France", "Italy", "Cheese", 5, 15, 8),
    ("France", "Mexico", "Cheese", 3, 10, 10),
    ("Japan", "France", "Soy Sauce", 1, 5, 7),
    ("Mexico", "India", "Chillies", 3, 9, 8),
    ("Mexico", "Italy", "Chillies", 2, 7, 9),
    ("China", "Japan", "Tofu", 6, 14, 5),
    ("Spain", "USA", "Olive Oil", 3, 10, 6),
    ("USA", "Italy", "Wheat", 4, 11, 4),
    ("China", "France", "Ginger", 2, 9, 7),
    ("India", "China", "Spices", 3, 8, 10),
]

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
for source, target, ingredient, weight, cost, time in edges:
    G.add_edge(source, target, ingredient=ingredient, weight=weight, cost=cost, time=time)

# Choose a layout for the graph
pos = nx.spring_layout(G, seed=42)

# Plot the network
plt.figure(figsize=(14, 10))

# Draw nodes with custom properties
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=2500, edgecolors='k')

# Draw edges with weights
edge_weights = [data['weight'] for _, _, data in G.edges(data=True)]
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=15, edge_color='grey', width=edge_weights)

# Draw labels for nodes
nx.draw_networkx_labels(G, pos, font_size=10, font_color='navy', font_weight='bold')

# Annotate edges with ingredient labels and additional attributes
edge_labels = {
    (source, target): f"{data['ingredient']} \nW:{data['weight']} C:{data['cost']} T:{data['time']}" 
    for source, target, data in G.edges(data=True)
}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkgreen', font_size=9)

# Title with line breaks for clarity
plt.title("The Network of International Cuisine:\nExploration of Ingredient Trade and Attributes", fontsize=16, fontweight='bold')

# Disable axes
plt.axis('off')

# Adjust layout to fit elements within the plot area
plt.tight_layout()

# Display the plot
plt.show()