import matplotlib.pyplot as plt
import networkx as nx

# Define the nodes representing different animal species
nodes = ["Deer", "Wolf", "Rabbit", "Fox", "Bird", "Tree", "Insect"]

# Define the undirected edges representing mutual interactions
edges = [
    ("Deer", "Tree"),         # Deer feed on tree leaves
    ("Rabbit", "Tree"),       # Rabbits also depend on trees for food
    ("Fox", "Rabbit"),        # Fox preys on rabbits
    ("Wolf", "Deer"),         # Wolf preys on deer
    ("Bird", "Insect"),       # Birds consume insects
    ("Tree", "Insect"),       # Insects pollinate or feed on tree sap
    ("Deer", "Insect"),       # Deer can help spread insects or their eggs
    ("Bird", "Tree"),         # Birds help with seed dispersal for trees
]

# Create an undirected graph
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Define node colors for visual distinction
node_colors = ['#8B4513', '#708090', '#D3D3D3', '#FF8C00', '#00CED1', '#228B22', '#FFD700']

# Determine positions using a spring layout
pos = nx.spring_layout(G, seed=42)

# Plot the graph
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color=node_colors, edgecolors='black')
nx.draw_networkx_edges(G, pos, width=2, alpha=0.7, edge_color='gray')

# Add labels to the nodes
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_family='sans-serif')

# Add a title and a legend for better understanding
plt.title('Forest Ecosystem: Animal Interactions\nExploring Biodiversity Connections', fontsize=16, fontweight='bold')
plt.axis('off')

# Create a custom legend to describe node types
custom_legend = [
    plt.Line2D([0], [0], marker='o', color='w', label='Herbivore', markersize=10, markerfacecolor='#8B4513'),
    plt.Line2D([0], [0], marker='o', color='w', label='Predator', markersize=10, markerfacecolor='#708090'),
    plt.Line2D([0], [0], marker='o', color='w', label='Small Mammal', markersize=10, markerfacecolor='#D3D3D3'),
    plt.Line2D([0], [0], marker='o', color='w', label='Omnivore', markersize=10, markerfacecolor='#FF8C00'),
    plt.Line2D([0], [0], marker='o', color='w', label='Bird', markersize=10, markerfacecolor='#00CED1'),
    plt.Line2D([0], [0], marker='o', color='w', label='Flora', markersize=10, markerfacecolor='#228B22'),
    plt.Line2D([0], [0], marker='o', color='w', label='Invertebrate', markersize=10, markerfacecolor='#FFD700')
]
plt.legend(handles=custom_legend, title='Species Type', loc='lower right', frameon=False)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()