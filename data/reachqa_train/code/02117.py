import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as mpatches

# Define nodes for mythical creatures and natural elements with classification
mythical_creatures = ['Dryad', 'Centaur', 'Griffon', 'Nymph', 'Phoenix']
natural_elements = ['Tree of Life', 'Moonlight', 'Whispering Wind', 'Eldritch Fog']

# Create an undirected graph
G = nx.Graph()

# Add nodes
G.add_nodes_from(mythical_creatures, type='creature')
G.add_nodes_from(natural_elements, type='element')

# Define edges showing connections
edges = [
    ('Dryad', 'Tree of Life'),
    ('Centaur', 'Nymph'),
    ('Griffon', 'Phoenix'),
    ('Nymph', 'Whispering Wind'),
    ('Phoenix', 'Moonlight'),
    ('Tree of Life', 'Eldritch Fog'),
    ('Whispering Wind', 'Eldritch Fog'),
    ('Moonlight', 'Dryad'),
    ('Eldritch Fog', 'Griffon')
]

# Add edges to the graph
G.add_edges_from(edges)

# Define positions using a different layout for variation
pos = nx.kamada_kawai_layout(G)

# Create figure and axes
fig, ax = plt.subplots(figsize=(14, 12))
fig.patch.set_facecolor('floralwhite')

# Define node attributes
node_colors = ['cornflowerblue' if G.nodes[node]['type'] == 'creature' else 'mediumseagreen' for node in G.nodes()]
node_shapes = {'creature': 'o', 'element': 's'}
node_sizes = [3000 if G.nodes[node]['type'] == 'creature' else 2000 for node in G.nodes()]

# Draw nodes with different colors and shapes
nx.draw_networkx_nodes(
    G, pos, node_size=node_sizes, node_color=node_colors,
    edgecolors='darkgreen', ax=ax, linewidths=2, node_shape='o'
)

# Draw edges with gradient-like features by combining multiple lines
nx.draw_networkx_edges(
    G, pos, edgelist=edges, width=3.0,
    alpha=0.6, edge_color='forestgreen', style='dashed', ax=ax
)

# Draw node labels
nx.draw_networkx_labels(
    G, pos, font_size=12, font_weight='bold', 
    font_color='black', ax=ax
)

# Set title with line breaks for clarity
ax.set_title(
    'The Interwoven Myths of\nAncient Forest Realms',
    fontsize=18, fontweight='bold', ha='center'
)

# Remove axis
ax.axis('off')

# Add a legend manually
creature_patch = mpatches.Patch(color='cornflowerblue', label='Mythical Creatures', edgecolor='darkgreen')
element_patch = mpatches.Patch(color='mediumseagreen', label='Natural Elements', edgecolor='darkgreen')
edge_patch = mpatches.Patch(color='forestgreen', label='Shared Legends Connection', alpha=0.6)

ax.legend(handles=[creature_patch, element_patch, edge_patch], loc='upper right', fontsize=11, title='Legend', title_fontsize=13)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()