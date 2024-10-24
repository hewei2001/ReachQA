import matplotlib.pyplot as plt
import networkx as nx

# List of popular social media platforms
platforms = ['Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'Snapchat', 'YouTube', 'TikTok']

# Define connections based on shared features
connections = [
    ('Facebook', 'Instagram'), # Photo Sharing
    ('Instagram', 'Snapchat'), # Photo Sharing
    ('Twitter', 'Facebook'),   # Microblogging
    ('Twitter', 'Snapchat'),   # Microblogging
    ('LinkedIn', 'Facebook'),  # Business Networking
    ('LinkedIn', 'Twitter'),   # Business Networking
    ('YouTube', 'Facebook'),   # Video Streaming
    ('YouTube', 'Instagram'),  # Video Streaming
    ('YouTube', 'TikTok'),     # Video Streaming
    ('TikTok', 'Snapchat')     # Video Creation and Sharing
]

# Create the graph using NetworkX
G = nx.Graph()

# Add nodes and edges based on the connections
G.add_nodes_from(platforms)
G.add_edges_from(connections)

# Assign colors to nodes based on the platform's type or unique feature
colors = ['#4267B2', '#E1306C', '#1DA1F2', '#0077B5', '#FFFC00', '#FF0000', '#69C9D0']

# Draw the graph
fig, ax = plt.subplots(figsize=(12, 10))
pos = nx.spring_layout(G, seed=24)

# Draw nodes with color variation
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color=colors, edgecolors='black', alpha=0.9)

# Draw edges with uniform gray color and slight transparency
nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color='gray')

# Draw labels with a slight offset to avoid overlap
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', verticalalignment='center', horizontalalignment='center')

# Add a title with context about the connections
plt.title("Interconnected Social Media Ecosystem:\nShared Features Among Popular Platforms",
          fontsize=16, fontweight='bold', pad=20)

# Annotate major shared features for clarity
feature_annotations = {
    'Photo Sharing': (['Facebook', 'Instagram', 'Snapchat'], (0.05, -0.15)),
    'Microblogging': (['Twitter', 'Facebook', 'Snapchat'], (-0.2, 0.2)),
    'Video Streaming': (['YouTube', 'TikTok', 'Instagram'], (0.2, 0.1)),
    'Business Networking': (['LinkedIn', 'Facebook', 'Twitter'], (-0.15, 0.25))
}

for feature, (nodes, offset) in feature_annotations.items():
    xs = [pos[node][0] for node in nodes]
    ys = [pos[node][1] for node in nodes]
    mid_x = sum(xs) / len(xs) + offset[0]
    mid_y = sum(ys) / len(ys) + offset[1]
    ax.text(mid_x, mid_y, feature, fontsize=10, color='black', fontstyle='italic', ha='center', va='center', bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.3'))

# Remove axis for clarity
plt.axis('off')

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()