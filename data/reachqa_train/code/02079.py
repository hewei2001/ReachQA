import matplotlib.pyplot as plt
import networkx as nx

# Create a graph representing the rainforest ecosystem
ecosystem = nx.Graph()

# Define species in the ecosystem
species = [
    'Jaguar', 'Deer', 'Macaw', 'Frog', 'Ant', 
    'Tree', 'Bush', 'Snake', 'Eagle', 'Butterfly'
]

# Add nodes
ecosystem.add_nodes_from(species)

# Define interactions (edges) between species
interactions = [
    ('Jaguar', 'Deer'),        # Predation
    ('Deer', 'Bush'),          # Herbivory
    ('Macaw', 'Tree'),         # Nesting
    ('Frog', 'Ant'),           # Mutualism
    ('Ant', 'Tree'),           # Seed dispersal
    ('Tree', 'Bush'),          # Competition
    ('Snake', 'Frog'),         # Predation
    ('Eagle', 'Snake'),        # Predation
    ('Butterfly', 'Bush'),     # Pollination
    ('Frog', 'Butterfly'),     # Food source
]

# Add edges
ecosystem.add_edges_from(interactions)

# Define positions for nodes using a circular layout for better visibility
pos = nx.circular_layout(ecosystem)

# Draw nodes with specific styles
nx.draw_networkx_nodes(
    ecosystem, pos, node_size=1000, node_color='forestgreen',
    edgecolors='black', linewidths=1.5
)

# Draw edges with specific styles
nx.draw_networkx_edges(
    ecosystem, pos, width=2, alpha=0.7, edge_color='olive'
)

# Draw labels for the nodes
nx.draw_networkx_labels(
    ecosystem, pos, font_size=9, font_weight='bold', font_color='white'
)

# Draw edge labels to indicate interaction type
edge_labels = {
    ('Jaguar', 'Deer'): 'Predation',
    ('Deer', 'Bush'): 'Herbivory',
    ('Macaw', 'Tree'): 'Nesting',
    ('Frog', 'Ant'): 'Mutualism',
    ('Ant', 'Tree'): 'Seed Dispersal',
    ('Tree', 'Bush'): 'Competition',
    ('Snake', 'Frog'): 'Predation',
    ('Eagle', 'Snake'): 'Predation',
    ('Butterfly', 'Bush'): 'Pollination',
    ('Frog', 'Butterfly'): 'Food Source'
}
nx.draw_networkx_edge_labels(
    ecosystem, pos, edge_labels=edge_labels, font_color='darkgreen',
    font_size=8, bbox=dict(facecolor='none', edgecolor='none', boxstyle='round,pad=0.3')
)

# Set the title of the plot
plt.title("Rainforest Ecosystem: Species Interactions", fontsize=16, fontweight='bold', pad=20)

# Hide axes for a cleaner look
plt.axis('off')

# Display the plot
plt.show()