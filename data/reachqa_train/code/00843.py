import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Create a graph to represent connections in the digital art world
G = nx.Graph()

# Define nodes representing digital art platforms
nodes = [
    'Adobe Photoshop', 'Procreate', 'ArtStation', 'DeviantArt',
    'Blender', 'CGSociety', 'Skillshare', 'Behance', 'Etsy',
    'Instagram', 'Patreon', 'YouTube'
]

G.add_nodes_from(nodes)

# Define edges representing connections/synergy among platforms
edges = [
    ('Adobe Photoshop', 'ArtStation'), ('Adobe Photoshop', 'Behance'),
    ('Procreate', 'Instagram'), ('Blender', 'CGSociety'),
    ('ArtStation', 'CGSociety'), ('DeviantArt', 'Instagram'),
    ('Skillshare', 'YouTube'), ('Etsy', 'Instagram'),
    ('Patreon', 'YouTube'), ('YouTube', 'Instagram'),
    ('Procreate', 'Adobe Photoshop'), ('Blender', 'ArtStation'),
    ('Adobe Photoshop', 'DeviantArt'), ('Blender', 'Skillshare'),
    ('Behance', 'Instagram'), ('Skillshare', 'Patreon'),
    ('Etsy', 'DeviantArt')
]

G.add_edges_from(edges)

# Define node colors for diversity
colors = {
    'Adobe Photoshop': '#f28f43', 'Procreate': '#735DD0',
    'ArtStation': '#1DA1F2', 'DeviantArt': '#B2294C',
    'Blender': '#EA7600', 'CGSociety': '#2b2b2b',
    'Skillshare': '#FF8F00', 'Behance': '#005AFF',
    'Etsy': '#D35323', 'Instagram': '#DD2A7B',
    'Patreon': '#FF424D', 'YouTube': '#FF0000'
}

# Define edge styles and thickness based on number of connections
edge_styles = {
    ('Adobe Photoshop', 'ArtStation'): 1.5, ('Adobe Photoshop', 'Behance'): 1.2,
    ('Procreate', 'Instagram'): 1.1, ('Blender', 'CGSociety'): 1.8,
    ('ArtStation', 'CGSociety'): 1.4, ('DeviantArt', 'Instagram'): 1.3,
    ('Skillshare', 'YouTube'): 1.1, ('Etsy', 'Instagram'): 1.5,
    ('Patreon', 'YouTube'): 1.0, ('YouTube', 'Instagram'): 1.2,
    ('Procreate', 'Adobe Photoshop'): 1.0, ('Blender', 'ArtStation'): 1.5,
    ('Adobe Photoshop', 'DeviantArt'): 1.1, ('Blender', 'Skillshare'): 1.3,
    ('Behance', 'Instagram'): 1.1, ('Skillshare', 'Patreon'): 1.4,
    ('Etsy', 'DeviantArt'): 1.2
}

pos = nx.circular_layout(G)

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Draw the network graph on the first subplot
nx.draw_networkx_nodes(
    G, pos, ax=axes[0], node_size=1200,
    node_color=[colors[node] for node in G.nodes()],
    alpha=0.9, edgecolors='grey'
)
nx.draw_networkx_edges(
    G, pos, ax=axes[0],
    width=[edge_styles.get(edge, 1.0) for edge in G.edges()],  # Use default thickness if edge not defined
    alpha=0.6, edge_color='grey'
)
nx.draw_networkx_labels(
    G, pos, ax=axes[0],
    font_size=10, font_family='sans-serif',
    bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, pad=0.5)
)
axes[0].set_title(
    'Network of Digital Art Platforms\n'
    'Exploring Connections and Synergies',
    fontsize=14, weight='bold', color='darkblue', pad=20
)
axes[0].axis('off')

# Generate data for bar chart
node_degrees = [degree for node, degree in G.degree()]
node_labels = list(G.nodes())
bar_colors = [colors[node] for node in node_labels]

# Plot bar chart of node degrees on the second subplot
axes[1].barh(node_labels, node_degrees, color=bar_colors)
axes[1].set_title(
    'Platform Connectivity\n'
    'Number of Connections per Platform',
    fontsize=14, weight='bold', color='darkblue', pad=20
)
axes[1].set_xlabel('Number of Connections', fontsize=12)
axes[1].set_ylabel('Platforms', fontsize=12)
axes[1].invert_yaxis()  # Invert y-axis for better readability

plt.tight_layout()
plt.show()