import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define species as nodes
species = [
    'Pigeons', 'Urban Foxes', 'Squirrels', 
    'Sparrows', 'Bats', 'Raccoons', 'City Cats'
]

# Define edges (interactions) between species
interactions = [
    ('Pigeons', 'Sparrows'),     
    ('Urban Foxes', 'Raccoons'), 
    ('Squirrels', 'Sparrows'),   
    ('Bats', 'Urban Foxes'),     
    ('City Cats', 'Pigeons'),    
    ('Raccoons', 'City Cats'),   
]

# Interaction strengths - a new dataset
interaction_strengths = {
    ('Pigeons', 'Sparrows'): 5,
    ('Urban Foxes', 'Raccoons'): 3,
    ('Squirrels', 'Sparrows'): 4,
    ('Bats', 'Urban Foxes'): 1,
    ('City Cats', 'Pigeons'): 7,
    ('Raccoons', 'City Cats'): 2,
}

# Create a graph object
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(species)
G.add_edges_from(interactions)

# Define position layout for nodes
pos = nx.spring_layout(G, seed=42)

# Create the figure and subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 7))

# Plot the network graph
node_colors = ['#1f78b4', '#33a02c', '#e31a1c', '#ff7f00', '#6a3d9a', '#b15928', '#a6cee3']
nx.draw_networkx_nodes(G, pos, node_size=5000, node_color=node_colors, edgecolors='black', linewidths=1.5, ax=axes[0])
nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color='gray', ax=axes[0])
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', verticalalignment='center', font_color="black", ax=axes[0])
axes[0].set_title("Ecosystem Connectivity:\nA Glimpse into the Web of Urban Wildlife", fontsize=14, fontweight='bold')
axes[0].axis('off')

# Data for the bar chart subplot
inter_pairs = ["Pigeons-Sparrows", "Urban Foxes-Raccoons", "Squirrels-Sparrows", "Bats-Urban Foxes", "City Cats-Pigeons", "Raccoons-City Cats"]
strengths = [interaction_strengths[interaction] for interaction in interactions]

# Plot the bar chart
bars = axes[1].bar(inter_pairs, strengths, color='#4daf4a', edgecolor='black')
axes[1].set_title("Interaction Strengths Among Urban Wildlife", fontsize=14, fontweight='bold')
axes[1].set_ylabel("Interaction Strength")
axes[1].set_xticklabels(inter_pairs, rotation=45, ha='right')

# Add value labels on top of bars
for bar in bars:
    yval = bar.get_height()
    axes[1].text(bar.get_x() + bar.get_width()/2, yval + 0.1, f'{yval}', ha='center', va='bottom', fontweight='bold')

# Adjust layout for better visibility
plt.tight_layout()

# Display the combined plot
plt.show()