import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define species as nodes
species = ["Oak Tree", "Fern", "Mushroom", "Deer", "Wolf", "Rabbit", "Fox", "Grass", "Bee", "Bird", "Insects"]

# Define interactions as edges
interactions = [
    ("Oak Tree", "Bee"),      # Pollination
    ("Oak Tree", "Bird"),     # Nesting
    ("Fern", "Mushroom"),     # Symbiosis
    ("Grass", "Rabbit"),      # Grazing
    ("Rabbit", "Fox"),        # Predation
    ("Deer", "Wolf"),         # Predation
    ("Mushroom", "Deer"),     # Decomposition
    ("Deer", "Grass"),        # Grazing
    ("Bee", "Fern"),          # Pollination
    ("Bird", "Insects")       # Feeding
]

# Classify nodes by type
node_colors = {
    "Flora": ['Oak Tree', 'Fern', 'Grass'],
    "Fauna": ['Deer', 'Wolf', 'Rabbit', 'Fox', 'Bee', 'Bird', 'Insects'],
    "Decomposers": ['Mushroom']
}

# Assign colors based on node type
color_map = []
for node in species:
    if node in node_colors["Flora"]:
        color_map.append('forestgreen')
    elif node in node_colors["Fauna"]:
        color_map.append('sienna')
    elif node in node_colors["Decomposers"]:
        color_map.append('darkgoldenrod')

# Create NetworkX graph
G = nx.Graph()
G.add_nodes_from(species)
G.add_edges_from(interactions)

# Set layout for the graph
pos = nx.spring_layout(G, seed=42)

# Define population (or biomass) data for additional plot
population_data = {
    "Oak Tree": 500,
    "Fern": 300,
    "Mushroom": 400,
    "Deer": 120,
    "Wolf": 10,
    "Rabbit": 250,
    "Fox": 20,
    "Grass": 600,
    "Bee": 1000,
    "Bird": 200,
    "Insects": 800
}

# Prepare data for bar plot
species_labels = list(population_data.keys())
population_values = list(population_data.values())
colors = [color_map[species.index(species_name)] for species_name in species_labels]

# Create figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 8))
fig.suptitle('Ecosystem Interconnections and Species Population Distribution', fontsize=16, fontweight='bold', color='darkolivegreen')

# Subplot 1: Network Graph
axs[0].set_title('Biodiversity in a Forest Network', fontsize=14, color='darkolivegreen')
nx.draw_networkx_nodes(G, pos, ax=axs[0], node_size=1000, node_color=color_map, alpha=0.8)
nx.draw_networkx_edges(G, pos, ax=axs[0], width=2, alpha=0.5, edge_color='darkgray', style='solid')
nx.draw_networkx_labels(G, pos, ax=axs[0], font_size=10, font_color='black', font_family='sans-serif')
axs[0].axis('off')

# Subplot 2: Bar Plot of Population Data
axs[1].set_title('Species Population in the Ecosystem', fontsize=14, color='darkolivegreen')
axs[1].bar(species_labels, population_values, color=colors)
axs[1].set_ylabel('Population Size')
axs[1].set_xticklabels(species_labels, rotation=45, ha='right')

# Create a custom legend
flora_patch = plt.Line2D([0], [0], marker='o', color='w', label='Flora', markersize=10, markerfacecolor='forestgreen')
fauna_patch = plt.Line2D([0], [0], marker='o', color='w', label='Fauna', markersize=10, markerfacecolor='sienna')
decomposer_patch = plt.Line2D([0], [0], marker='o', color='w', label='Decomposer', markersize=10, markerfacecolor='darkgoldenrod')
fig.legend(handles=[flora_patch, fauna_patch, decomposer_patch], loc='lower center', fontsize=12, frameon=True, shadow=True, ncol=3)

# Automatically adjust the layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plot
plt.show()