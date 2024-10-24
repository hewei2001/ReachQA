import matplotlib.pyplot as plt
import networkx as nx

# Initialize directed graph
G = nx.DiGraph()

# Define nodes representing genres
genres = [
    'Classical', 'Jazz', 'Blues', 'Rock', 'Pop', 'Hip-Hop',
    'Electronic', 'EDM', 'Indie', 'Folk', 'Country', 'Reggae'
]

# Add nodes to the graph
G.add_nodes_from(genres)

# Define edges representing influence pathways between genres
edges = [
    ('Classical', 'Jazz'), ('Classical', 'Blues'), ('Jazz', 'Rock'),
    ('Blues', 'Rock'), ('Rock', 'Pop'), ('Rock', 'Indie'),
    ('Blues', 'Hip-Hop'), ('Hip-Hop', 'Electronic'),
    ('Electronic', 'EDM'), ('Indie', 'Folk'),
    ('Folk', 'Country'), ('Reggae', 'Hip-Hop')
]

# Add edges to the graph
G.add_edges_from(edges)

# Create a subplot layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [1, 1.2]})

# ----- Plot 1: Genre Influence Pathways -----
# Position nodes using a circular layout for better visual clarity
pos = nx.circular_layout(G)

# Draw nodes with distinct colors
node_colors = ['#8da0cb', '#fc8d62', '#66c2a5', '#e78ac3', '#a6d854', '#ffd92f', '#e5c494', '#b3b3b3', '#1f78b4', '#33a02c', '#fb9a99', '#e31a1c']
nx.draw_networkx_nodes(G, pos, ax=ax1, node_size=1500, node_color=node_colors, alpha=0.9, edgecolors='black')

# Draw edges with arrows to indicate direction
nx.draw_networkx_edges(G, pos, ax=ax1, edgelist=edges, arrowstyle='-|>', arrowsize=15, edge_color='grey', width=2)

# Add labels to the nodes for clarity
nx.draw_networkx_labels(G, pos, ax=ax1, font_size=9, font_weight='bold', font_family='sans-serif')

# Add title to the first plot
ax1.set_title("The Evolution of Musical Genres:\nTracing Influence Pathways", fontsize=12, fontweight='bold', pad=20)
ax1.axis('off')  # Hide axes

# ----- Plot 2: Genre Popularity Over Time -----
# Hypothetical data for genre popularity (arbitrary units)
popularity = [80, 70, 60, 90, 85, 75, 65, 60, 55, 50, 45, 50]

# Horizontal bar chart
ax2.barh(genres, popularity, color=node_colors, edgecolor='black')

# Add labels and title
ax2.set_xlabel('Popularity Index', fontsize=10, fontweight='bold')
ax2.set_title('Genre Popularity Over Time', fontsize=12, fontweight='bold', pad=20)

# Annotate bars with the popularity values
for index, value in enumerate(popularity):
    ax2.text(value + 1, index, str(value), va='center', fontsize=9, fontweight='bold')

# Adjust layout
fig.tight_layout()

# Display the plots
plt.show()