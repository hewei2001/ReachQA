import matplotlib.pyplot as plt
import networkx as nx

# Define species and their connections with interaction strengths
species = ['Glowing Mushrooms', 'Whispering Trees', 'Ethereal Butterflies', 
           'Mystical Owls', 'Fairy Ferns', 'Singing Crickets']

connections = [
    ('Glowing Mushrooms', 'Whispering Trees', 5),
    ('Glowing Mushrooms', 'Ethereal Butterflies', 3),
    ('Whispering Trees', 'Mystical Owls', 4),
    ('Whispering Trees', 'Fairy Ferns', 2),
    ('Ethereal Butterflies', 'Fairy Ferns', 6),
    ('Mystical Owls', 'Singing Crickets', 7),
    ('Fairy Ferns', 'Singing Crickets', 4),
    ('Ethereal Butterflies', 'Mystical Owls', 5),
    ('Glowing Mushrooms', 'Singing Crickets', 3)
]

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(species)

# Add edges with interaction strength as weight
G.add_weighted_edges_from(connections)

# Position nodes using a circular layout for visual appeal
pos = nx.spring_layout(G, seed=42)

# Create a color map for the nodes
node_colors = ['lightgreen', 'lightblue', 'violet', 'orange', 'pink', 'yellow']

# Draw the nodes
nx.draw_networkx_nodes(G, pos, node_size=1200, node_color=node_colors, alpha=0.9, node_shape='o')

# Draw the edges with varying thickness based on strength
edges = G.edges(data=True)
nx.draw_networkx_edges(G, pos, edgelist=edges, width=[d['weight'] for (u, v, d) in edges], alpha=0.5, edge_color='gray')

# Draw the labels for nodes
nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')

# Draw labels for edges
edge_labels = {(u, v): f'{d["weight"]}' for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, font_color='red')

# Adding a title
plt.title("Mystical Forest Network:\nWeb of Interconnections Between Enchanted Species", fontsize=16, fontweight='bold')

# Show plot without axis
plt.axis('off')
plt.tight_layout()
plt.show()