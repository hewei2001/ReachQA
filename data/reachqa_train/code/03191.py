import matplotlib.pyplot as plt
import networkx as nx

# Define the nodes and their relationships (edges) for literary movements
literary_movements = {
    'Romanticism': ['Realism', 'Symbolism'],
    'Realism': ['Modernism'],
    'Modernism': ['Postmodernism'],
    'Postmodernism': [],
    'Symbolism': ['Modernism', 'Surrealism'],
    'Surrealism': ['Postmodernism'],
    'Renaissance': ['Romanticism', 'Symbolism'],
    'Victorian': ['Realism'],
    'Existentialism': ['Modernism', 'Postmodernism']
}

# Define the nodes and their relationships (edges) for author influence
author_influence = {
    'Shelley': ['Keats', 'Byron'],
    'Keats': ['Yeats'],
    'Yeats': ['Eliot'],
    'Eliot': [],
    'Byron': ['Eliot', 'Fitzgerald'],
    'Fitzgerald': ['Hemingway'],
    'Joyce': ['Woolf', 'Eliot'],
    'Hemingway': ['Fitzgerald'],
    'Dostoevsky': ['Camus', 'Kafka']
}

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

# Plot 1: Literary Movements Network
G1 = nx.Graph()
for movement, influences in literary_movements.items():
    G1.add_node(movement)
    for influence in influences:
        G1.add_edge(movement, influence)

node_size_1 = [7000 if G1.degree[n] > 1 else 5000 for n in G1.nodes()]
pos1 = nx.spring_layout(G1, seed=42)

nx.draw_networkx_nodes(G1, pos1, ax=ax1, node_size=node_size_1, node_color='lightgreen', edgecolors='darkgreen', linewidths=1.5)
nx.draw_networkx_edges(G1, pos1, ax=ax1, width=2, edge_color='gray', style='dotted')
nx.draw_networkx_labels(G1, pos1, ax=ax1, font_size=10, font_weight='bold', font_color='darkslateblue')

ax1.set_title('Literary Influence Web:\nGraph of Movements and Connections', fontsize=14, weight='bold', pad=20)
ax1.axis('off')

# Plot 2: Author Influence Network
G2 = nx.DiGraph()
for author, followers in author_influence.items():
    G2.add_node(author)
    for follower in followers:
        G2.add_edge(author, follower)

node_size_2 = [6000 if G2.in_degree[n] > 1 else 4000 for n in G2.nodes()]
pos2 = nx.circular_layout(G2)

nx.draw_networkx_nodes(G2, pos2, ax=ax2, node_size=node_size_2, node_color='lightcoral', edgecolors='darkred', linewidths=1.5)
nx.draw_networkx_edges(G2, pos2, ax=ax2, width=2, edge_color='black', style='solid', arrowsize=15)
nx.draw_networkx_labels(G2, pos2, ax=ax2, font_size=10, font_weight='bold', font_color='darkred')

ax2.set_title('Author Influence Hierarchy:\nConnections Among Prominent Writers', fontsize=14, weight='bold', pad=20)
ax2.axis('off')

# Tight layout for better spacing
plt.tight_layout()

# Show plot
plt.show()