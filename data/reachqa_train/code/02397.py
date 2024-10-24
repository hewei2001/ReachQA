import matplotlib.pyplot as plt
import networkx as nx

# Define park features as nodes
features = [
    "Playground", "Picnic Area", "Fountain", "Walking Path", 
    "Dog Park", "Garden", "Amphitheater", "Restrooms", "Food Stall"
]

# Define connections between features as edges
connections = [
    ("Playground", "Picnic Area"),
    ("Picnic Area", "Garden"),
    ("Garden", "Fountain"),
    ("Fountain", "Walking Path"),
    ("Walking Path", "Amphitheater"),
    ("Amphitheater", "Restrooms"),
    ("Restrooms", "Food Stall"),
    ("Food Stall", "Dog Park"),
    ("Dog Park", "Playground")
]

# Create an undirected graph
G = nx.Graph()

# Add nodes and edges
G.add_nodes_from(features)
G.add_edges_from(connections)

# Position nodes using spring layout for a natural appearance
pos = nx.spring_layout(G, seed=42)

# Define node colors and sizes to enhance distinction
node_colors = ['#9acd32', '#ff6347', '#1e90ff', '#ffeb3b', '#f4a460', '#adff2f', '#dda0dd', '#8b4513', '#ff69b4']
node_sizes = [1200, 1000, 800, 1100, 900, 950, 1050, 850, 800]

# Plot the graph
plt.figure(figsize=(12, 10))
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes,
        font_size=10, font_weight='bold', edge_color='gray', width=2.0, alpha=0.7)

# Add a title with adjusted placement for clarity
plt.title(
    'Interaction Network of Urban Park Features\nEnhancing Visitor Experience Through Connectivity', 
    fontsize=16, fontweight='bold', pad=20
)

# Hide axes for a clean visualization
plt.axis('off')

# Automatically adjust layout to prevent overlaps
plt.tight_layout()

# Display the plot
plt.show()