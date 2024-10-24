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

# Define a layout for the nodes
pos = nx.spring_layout(G, seed=42)

# Create figure and subplots with a 1x2 layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Draw the network graph in the first subplot
node_sizes = [4000 if node == "Local Markets" else 3000 for node in nodes]
node_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

nx.draw_networkx_nodes(G, pos, ax=ax1, node_size=node_sizes, node_color=node_colors, edgecolors='black')
nx.draw_networkx_edges(G, pos, ax=ax1, edgelist=edges, edge_color='gray', width=2, alpha=0.7)
nx.draw_networkx_labels(G, pos, ax=ax1, font_size=12, font_weight='bold')

# Add edge labels
edge_labels = {("Farmers", "Local Markets"): "Produce",
               ("Local Markets", "Cafes"): "Supply",
               ("Local Markets", "Restaurants"): "Supply",
               ("Suppliers", "Cafes"): "Goods",
               ("Suppliers", "Restaurants"): "Goods",
               ("Cafes", "Restaurants"): "Collaboration"}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax1, font_size=10, label_pos=0.3)

# Set a title for the network graph
ax1.set_title('Gourmetville Food Network\nInterconnections Among Key Sectors', fontsize=14, fontweight='bold')

# Remove axes for clarity in the network graph
ax1.set_axis_off()

# Data for the bar chart
sectors = ["Farmers", "Suppliers", "Cafes", "Restaurants", "Local Markets"]
sales = [150, 120, 200, 250, 180]  # Example sales data in millions

# Plot the bar chart in the second subplot
bars = ax2.bar(sectors, sales, color=node_colors, edgecolor='black')

# Add labels and title for the bar chart
ax2.set_title('Annual Sales in Sectors\n(In Millions)', fontsize=14, fontweight='bold')
ax2.set_ylabel('Sales (Million $)', fontsize=12)
ax2.set_xlabel('Sector', fontsize=12)

# Add value annotations on top of the bars
for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 5, f'{yval}', ha='center', va='bottom', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()