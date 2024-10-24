import matplotlib.pyplot as plt
import networkx as nx

# Define music genres
genres = ['Rock', 'Jazz', 'Classical', 'Hip-Hop', 'Electronic', 'Country']

# Define connections (edges) between genres with a count of performances
collaborations = {
    ('Rock', 'Jazz'): 5,
    ('Rock', 'Hip-Hop'): 3,
    ('Jazz', 'Classical'): 4,
    ('Classical', 'Electronic'): 2,
    ('Hip-Hop', 'Electronic'): 6,
    ('Electronic', 'Country'): 1,
    ('Country', 'Rock'): 2,
    ('Jazz', 'Hip-Hop'): 3
}

# Create a graph using NetworkX
G = nx.Graph()

# Add nodes with genres
G.add_nodes_from(genres)

# Add edges with collaboration weights
for (genre1, genre2), performances in collaborations.items():
    G.add_edge(genre1, genre2, weight=performances)

# Draw the graph using Matplotlib
plt.figure(figsize=(10, 8))

# Position the nodes using a spring layout
pos = nx.spring_layout(G, seed=42)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=1500)

# Draw edges with different widths based on collaboration intensity
edges = nx.draw_networkx_edges(
    G, pos,
    width=[G[u][v]['weight'] for u, v in G.edges()],
    edge_color='orange'
)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# Title and legend
plt.title('Harmony Fest: Genre Collaborations and Connections\nAnnual Music Fusion Festival', fontsize=16, fontweight='bold')

# Create a legend for edge widths (custom legend for aesthetics)
plt.text(1.15, 0.95, 'Collaboration Intensity', fontsize=12, ha='right')
plt.plot([], [], color='orange', linewidth=1, label='1-2')
plt.plot([], [], color='orange', linewidth=3, label='3-4')
plt.plot([], [], color='orange', linewidth=5, label='5+')
plt.legend(title='Performances', bbox_to_anchor=(1.2, 1))

# Adjust layout
plt.axis('off')
plt.tight_layout()

# Display the plot
plt.show()