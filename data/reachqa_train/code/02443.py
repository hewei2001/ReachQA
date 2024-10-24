import matplotlib.pyplot as plt
import networkx as nx

# Define species and their interactions with weights
species = [
    'Bacillus subtilis', 
    'Escherichia coli', 
    'Staphylococcus aureus', 
    'Lactobacillus acidophilus', 
    'Streptococcus pneumoniae'
]

# Define directed edges with weights
edges = [
    ('Bacillus subtilis', 'Escherichia coli', 3),
    ('Escherichia coli', 'Staphylococcus aureus', 4),
    ('Staphylococcus aureus', 'Lactobacillus acidophilus', 5),
    ('Lactobacillus acidophilus', 'Streptococcus pneumoniae', 2),
    ('Streptococcus pneumoniae', 'Bacillus subtilis', 1),
    ('Bacillus subtilis', 'Lactobacillus acidophilus', 2),
    ('Escherichia coli', 'Lactobacillus acidophilus', 3),
    ('Streptococcus pneumoniae', 'Escherichia coli', 3),
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges
G.add_nodes_from(species)
G.add_weighted_edges_from(edges)

# Use a circular layout for better visualization
pos = nx.circular_layout(G)

# Draw the nodes with custom attributes
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightgreen', linewidths=2, edgecolors='black')

# Draw the edges with arrowheads and weight-based widths
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=15, width=[G[u][v]['weight'] for u, v in G.edges()], edge_color='black')

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')

# Add edge labels (weights)
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=8)

# Set plot title and customize its appearance
plt.title('Communication Pathways in the Microbial Metropolis\nChemical Signaling Among Bacterial Species', fontsize=14, fontweight='bold', pad=20)

# Remove axes for a cleaner look
plt.axis('off')

# Adjust layout to ensure nothing is cut off
plt.tight_layout()

# Display the chart
plt.show()