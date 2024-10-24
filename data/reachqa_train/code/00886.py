import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms import community

# Define nodes and edges
friends = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Fiona']
recommendations = [
    ('Alice', 'Bob'),
    ('Alice', 'David'),
    ('Bob', 'Charlie'),
    ('Charlie', 'David'),
    ('David', 'Emma'),
    ('Emma', 'Fiona'),
    ('Fiona', 'Alice'),
    ('Charlie', 'Alice'),
    ('Emma', 'Bob')
]

# Create a network graph
G = nx.Graph()
G.add_nodes_from(friends)
G.add_edges_from(recommendations)

# Community detection for color coding
communities = list(community.greedy_modularity_communities(G))
community_map = {node: i for i, com in enumerate(communities) for node in com}
node_colors = [community_map[n] for n in G.nodes]

# Layout and node sizes
pos = nx.spring_layout(G, seed=42)
node_sizes = [1500 + 500 * G.degree(n) for n in G.nodes]

# Create the figure
plt.figure(figsize=(14, 12))

# Draw nodes with color coding for communities
nx.draw_networkx_nodes(
    G, pos, node_size=node_sizes, cmap=plt.cm.Set2, node_color=node_colors, edgecolors='black'
)

# Curved edges to reduce clutter
edge_weights = [1.5 if G.degree(u) > 2 else 0.5 for u, v in G.edges()]
nx.draw_networkx_edges(
    G, pos, width=edge_weights, alpha=0.7, edge_color='grey', 
    connectionstyle='arc3,rad=0.2'
)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# Legend and annotations
for i, com in enumerate(communities):
    x_pos = sum(pos[node][0] for node in com) / len(com)
    y_pos = sum(pos[node][1] for node in com) / len(com)
    plt.text(
        x_pos, y_pos, f'Community {i+1}', fontsize=10, ha='center', 
        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5')
    )

# Title and descriptions
plt.title(
    "Book Recommendation Network Among Friends\nAnalysis of Key Influencers and Communities",
    fontsize=16, fontweight='bold'
)
plt.xlabel("Nodes: Friends | Edges: Book Recommendations", fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()