import matplotlib.pyplot as plt
import networkx as nx

# Define nodes for organisms in the forest ecosystem
organisms = [
    "Trees", "Shrubs", "Herbivores", "Carnivores",
    "Decomposers", "Soil Microbes", "Birds", "Insects"
]

# Define directed edges showing nutrient and energy flow
flow_connections = [
    ("Trees", "Herbivores"),
    ("Shrubs", "Herbivores"),
    ("Herbivores", "Carnivores"),
    ("Herbivores", "Decomposers"),
    ("Carnivores", "Decomposers"),
    ("Decomposers", "Soil Microbes"),
    ("Soil Microbes", "Trees"),
    ("Soil Microbes", "Shrubs"),
    ("Insects", "Birds"),
    ("Insects", "Decomposers"),
    ("Birds", "Decomposers"),
    ("Trees", "Insects"),
    ("Shrubs", "Insects"),
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
G.add_nodes_from(organisms)
G.add_edges_from(flow_connections)

# Define positions for nodes using the shell layout for better flow representation
pos = nx.shell_layout(G)

# Define node colors based on the type of organism
node_colors = {
    "Trees": "forestgreen",
    "Shrubs": "darkolivegreen",
    "Herbivores": "gold",
    "Carnivores": "firebrick",
    "Decomposers": "saddlebrown",
    "Soil Microbes": "peru",
    "Birds": "royalblue",
    "Insects": "darkorange"
}

# Create the plot
plt.figure(figsize=(12, 10))

# Draw nodes with specified colors and edge colors
nx.draw_networkx_nodes(
    G, pos, node_color=[node_colors[node] for node in G.nodes],
    node_size=1500, edgecolors='black'
)

# Draw directed edges with arrows
nx.draw_networkx_edges(
    G, pos, edgelist=flow_connections, arrowstyle='-|>', arrowsize=20,
    edge_color='gray', width=2
)

# Draw labels for nodes
nx.draw_networkx_labels(
    G, pos, font_size=10, font_family='sans-serif', font_weight='bold'
)

# Manually add a legend to distinguish node types
for organism, color in node_colors.items():
    plt.plot([], [], color=color, marker='o', markersize=10, linestyle='', label=organism)
plt.legend(loc='upper left', title='Organisms', fontsize=10, frameon=False)

# Title with line break for clarity
plt.title("The Web of Nutrients:\nFlow in a Forest Ecosystem",
          fontsize=16, fontweight='bold', color='darkgreen')

# Turn off the axis to focus on the graph
plt.axis('off')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()