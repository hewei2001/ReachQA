import matplotlib.pyplot as plt
import networkx as nx

# Create an undirected graph
G = nx.Graph()

# Define nodes representing different sectors of the food and beverage industry
nodes = [
    "Farmers", "Suppliers", "Cafes", "Restaurants", "Local Markets"
]

# Add nodes to the graph
G.add_nodes_from(nodes)

# Define the undirected edges representing connections between these entities
edges = [
    ("Farmers", "Local Markets"),
    ("Local Markets", "Cafes"),
    ("Local Markets", "Restaurants"),
    ("Suppliers", "Cafes"),
    ("Suppliers", "Restaurants"),
    ("Cafes", "Restaurants")
]

# Add edges to the graph
G.add_edges_from(edges)

# Choose a layout for the nodes
pos = nx.spring_layout(G, seed=42)  # Spring layout for clearer visualization

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Draw the network graph
node_sizes = [4000 if node == "Local Markets" else 3000 for node in nodes]
node_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

nx.draw_networkx_nodes(G, pos, ax=ax, node_size=node_sizes, node_color=node_colors, edgecolors='black')
nx.draw_networkx_edges(G, pos, ax=ax, edgelist=edges, edge_color='gray', width=2, alpha=0.7)
nx.draw_networkx_labels(G, pos, ax=ax, font_size=12, font_weight='bold')

# Add edge labels for more clarity
edge_labels = {("Farmers", "Local Markets"): "Produce",
               ("Local Markets", "Cafes"): "Supply",
               ("Local Markets", "Restaurants"): "Supply",
               ("Suppliers", "Cafes"): "Goods",
               ("Suppliers", "Restaurants"): "Goods",
               ("Cafes", "Restaurants"): "Collaboration"}

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax, font_size=10, label_pos=0.3)

# Set a concise title
plt.title('Gourmetville Food Network\nInterconnections Among Key Sectors', fontsize=14, fontweight='bold')

# Remove axes for clarity
ax.set_axis_off()

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()