import matplotlib.pyplot as plt
import networkx as nx

# Initialize a graph object
G = nx.Graph()

# Define subcultures
subcultures = [
    "Indie Rock", "Jazz", "Street Art", "Hip Hop", 
    "Classical Music", "Digital Art", "Folk Music", "Modern Dance"
]

# Add nodes to the graph
G.add_nodes_from(subcultures)

# Define edges for interactions between subcultures
edges = [
    ("Indie Rock", "Jazz"),
    ("Indie Rock", "Hip Hop"),
    ("Street Art", "Hip Hop"),
    ("Street Art", "Digital Art"),
    ("Hip Hop", "Modern Dance"),
    ("Classical Music", "Jazz"),
    ("Classical Music", "Folk Music"),
    ("Modern Dance", "Jazz")
]

# Add edges to the graph
G.add_edges_from(edges)

# Determine node positions using a spring layout
pos = nx.spring_layout(G, seed=42)

# Define node colors based on a thematic color palette
node_colors = [
    "#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3",
    "#a6d854", "#ffd92f", "#e5c494", "#b3b3b3"
]

# Plot configuration
plt.figure(figsize=(14, 10))
nx.draw(
    G, pos, 
    with_labels=True, 
    node_color=node_colors, 
    edge_color='gray', 
    node_size=3500, 
    font_size=11, 
    font_weight='bold', 
    linewidths=2, 
    alpha=0.9
)

# Add edge labels to illustrate the strength or type of connections
edge_labels = {
    ("Indie Rock", "Jazz"): "Fusion",
    ("Indie Rock", "Hip Hop"): "Collab",
    ("Street Art", "Hip Hop"): "Graffiti",
    ("Street Art", "Digital Art"): "Techno-Art",
    ("Hip Hop", "Modern Dance"): "Dance-Off",
    ("Classical Music", "Jazz"): "Symphonic Jazz",
    ("Classical Music", "Folk Music"): "Folklore",
    ("Modern Dance", "Jazz"): "Swing"
}

# Draw edge labels with custom styles
nx.draw_networkx_edge_labels(
    G, pos, edge_labels=edge_labels, font_color='darkred', font_size=9, font_weight='bold'
)

# Title of the graph
plt.title(
    "Harmony in the Urban Jungle:\nConnecting Subcultures through Music and Art",
    fontsize=18, fontweight='bold', pad=15
)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()