import matplotlib.pyplot as plt
import networkx as nx

# Define the species as nodes
species = [
    'Owls', 'Hawks', 'Mice', 'Snakes', 'Frogs', 'Insects', 
    'Grass', 'Berries', 'Plants'
]

# Define interactions (edges) between the species
interactions = [
    ('Owls', 'Mice'), ('Owls', 'Snakes'),   # Owls interactions
    ('Hawks', 'Mice'), ('Hawks', 'Frogs'), # Hawks interactions
    ('Snakes', 'Mice'), ('Snakes', 'Frogs'), # Snakes interactions
    ('Frogs', 'Insects'), # Frogs interactions
    ('Mice', 'Grass'), ('Mice', 'Berries'), # Mice interactions
    ('Insects', 'Plants'), # Insects interactions
    ('Berries', 'Plants'), # Berries interactions
]

# Create a directed graph to reflect directionality in interactions
G = nx.DiGraph()
G.add_nodes_from(species)
G.add_edges_from(interactions)

# Define positions for the species using a hierarchical layout
pos = nx.spring_layout(G, seed=42)

# Define node sizes based on hypothetical ecological significance
node_sizes = [3500, 3300, 2500, 2700, 2200, 1500, 1800, 1600, 2000]

# Define edge styles and thickness for various types of interactions
edge_styles = {
    ('Owls', 'Mice'): 'solid',
    ('Hawks', 'Mice'): 'dashed',
    ('Snakes', 'Mice'): 'dotted',
    ('Hawks', 'Frogs'): 'dashdot',
    ('Snakes', 'Frogs'): 'solid',
    ('Owls', 'Snakes'): 'dotted',
    ('Frogs', 'Insects'): 'dashed',
    ('Mice', 'Grass'): 'solid',
    ('Mice', 'Berries'): 'dashdot',
    ('Insects', 'Plants'): 'dotted',
    ('Berries', 'Plants'): 'solid'
}

edge_widths = [2.5, 1.8, 2, 1.5, 2.2, 1.3, 1.5, 1.8, 2, 1, 1.5]

# Map styles to edges
edges = G.edges()
styles = [edge_styles[edge] for edge in edges]

# Plot the graph
plt.figure(figsize=(14, 10))
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='lightblue', edgecolors='black')
nx.draw_networkx_labels(G, pos, font_size=11, font_weight='bold')

for style, width, edge in zip(styles, edge_widths, edges):
    nx.draw_networkx_edges(G, pos, edgelist=[edge], style=style, width=width, edge_color='gray', arrows=True)

# Add a title to the chart, split into two lines
plt.title("Complex Ecological Interactions in the Forest of Ardentia\nExploring Trophic Relationships", fontsize=16, weight='bold')

# Add a legend for edge styles
legend_labels = {
    'Solid': 'Predation',
    'Dashed': 'Competition',
    'Dotted': 'Symbiosis',
    'Dashdot': 'Parasitism'
}

for style_name, label in legend_labels.items():
    plt.plot([], [], color='gray', linestyle=style_name.lower(), linewidth=2, label=label)

plt.legend(loc='upper right', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()