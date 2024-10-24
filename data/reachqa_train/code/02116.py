import matplotlib.pyplot as plt
import networkx as nx

# Define nodes for mythical creatures and natural elements
creatures_and_elements = [
    'Dryad', 'Centaur', 'Griffon', 'Nymph', 'Phoenix', 
    'Tree of Life', 'Moonlight', 'Whispering Wind', 'Eldritch Fog'
]

# Create an undirected graph
G = nx.Graph()

# Add nodes representing mythical creatures and elements
G.add_nodes_from(creatures_and_elements)

# Define undirected edges showing the connections
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

# Define positions using the spring layout for a natural, spread-out appearance
pos = nx.spring_layout(G, seed=45)

# Create figure and axes for plotting
fig, ax = plt.subplots(figsize=(12, 10))

# Draw the network graph
nx.draw_networkx_nodes(
    G, pos, node_size=2500, node_color='lightgreen',
    edgecolors='darkgreen', ax=ax, linewidths=2
)
nx.draw_networkx_edges(
    G, pos, edgelist=edges, width=2.5,
    alpha=0.6, edge_color='forestgreen', style='dashed', ax=ax
)
nx.draw_networkx_labels(
    G, pos, font_size=11, font_weight='bold', 
    font_color='darkslategrey', ax=ax
)

# Add a title that reflects the mythical story
ax.set_title(
    'The Interwoven Myths of Ancient Forest Realms',
    fontsize=16, fontweight='bold'
)

# Remove axis
ax.axis('off')

# Add a legend manually to explain node colors and edge meanings
legend_labels = {
    'Mythical Creatures': 'lightgreen',
    'Natural Elements': 'lightgreen',
    'Connection (Shared Legend)': 'forestgreen'
}

# Creating custom legend items
for label, color in legend_labels.items():
    ax.scatter([], [], color=color, label=label, edgecolor='darkgreen', s=100)

# Positioning the legend
ax.legend(loc='upper right', fontsize=10, title='Legend', title_fontsize=12)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()