import matplotlib.pyplot as plt
import networkx as nx

# List of planetary hubs (nodes)
hubs = ['Earth', 'Mars', 'Europa', 'Vulcan', 'Andoria', 'Betazed', 'Qo\'noS', 'Risa', 'Bajor']

# List of communication pathways (edges)
pathways = [
    ('Earth', 'Mars'),
    ('Earth', 'Europa'),
    ('Mars', 'Vulcan'),
    ('Europa', 'Andoria'),
    ('Vulcan', 'Betazed'),
    ('Betazed', 'Qo\'noS'),
    ('Qo\'noS', 'Risa'),
    ('Risa', 'Bajor'),
    ('Bajor', 'Earth'),  # Completing the loop to show a circular network
    ('Mars', 'Bajor'),
    ('Andoria', 'Qo\'noS')
]

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(hubs)
G.add_edges_from(pathways)

# Choose a layout for node positioning
pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(12, 8))

# Draw nodes with custom styling
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color='skyblue', edgecolors='black', alpha=0.9)

# Draw edges with arrows and custom styling
nx.draw_networkx_edges(G, pos, edgelist=pathways, edge_color='darkgray', arrows=True, arrowstyle='-|>', arrowsize=15)

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif', font_weight='bold')

# Draw edge labels if desired, e.g., communication frequency
edge_labels = {('Earth', 'Mars'): '5 GHz', ('Earth', 'Europa'): '3 GHz', ('Mars', 'Vulcan'): '4 GHz',
               ('Europa', 'Andoria'): '2 GHz', ('Vulcan', 'Betazed'): '6 GHz', ('Betazed', 'Qo\'noS'): '7 GHz',
               ('Qo\'noS', 'Risa'): '2 GHz', ('Risa', 'Bajor'): '4 GHz', ('Bajor', 'Earth'): '5 GHz',
               ('Mars', 'Bajor'): '3 GHz', ('Andoria', 'Qo\'noS'): '6 GHz'}

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=8)

# Title
plt.title("Intergalactic Communication Network:\nMapping the Flow of Information Between Galactic Hubs", fontsize=16, fontweight='bold')

# Hide axes
plt.axis('off')

# Adjust layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()