import matplotlib.pyplot as plt
import networkx as nx

# Define the nodes and categorize them
social_media_platforms = ['Facebook', 'Instagram', 'Twitter', 'Snapchat', 'LinkedIn']
tech_brands = ['Amazon', 'Google', 'Microsoft', 'Apple']

# Define the connections (edges) indicating relationships or shared technologies
edges = [
    ('Facebook', 'Instagram'),  # Ownership
    ('Facebook', 'Microsoft'),  # Azure partnerships
    ('Instagram', 'Amazon'),    # Hosting services
    ('Twitter', 'Google'),      # Ad partnerships
    ('Snapchat', 'Google'),     # Cloud services
    ('LinkedIn', 'Microsoft'),  # Owned by Microsoft
    ('Apple', 'Twitter'),       # API integrations
    ('Apple', 'Facebook'),      # Shared tools
]

# Initialize a NetworkX graph
G = nx.Graph()

# Add nodes with attributes for categorization
for node in social_media_platforms:
    G.add_node(node, category='Social Media')
for node in tech_brands:
    G.add_node(node, category='Tech Brand')

# Add edges to the graph
G.add_edges_from(edges)

# Node color mapping based on category
node_colors = []
for node in G.nodes(data=True):
    if node[1]['category'] == 'Social Media':
        node_colors.append('#1f78b4')  # Blue for Social Media
    else:
        node_colors.append('#33a02c')  # Green for Tech Brands

# Define edge attributes, e.g., for line style
edge_styles = []
for edge in G.edges(data=True):
    if edge[0] in social_media_platforms and edge[1] in social_media_platforms:
        edge_styles.append('solid')
    else:
        edge_styles.append('dashed')

# Define the plot size and layout
fig, ax = plt.subplots(figsize=(12, 8))

# Choose a layout for nodes positioning
pos = nx.spring_layout(G, seed=42)

# Draw the graph
nx.draw(
    G, pos, with_labels=True, node_color=node_colors, node_size=2500, 
    font_size=10, font_weight='bold', edge_color='gray',
    style=edge_styles, width=2
)

# Add a title with line breaks
plt.title("Interconnections in Social Media\nand Technology Ecosystem", fontsize=16, fontweight='bold', pad=20)

# Create a custom legend
legend_labels = ['Social Media Platform', 'Tech Brand']
legend_colors = ['#1f78b4', '#33a02c']
legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in legend_colors]

ax.legend(legend_handles, legend_labels, loc='upper right', title="Node Categories", fontsize=11)

# Automatically adjust the layout to prevent overlaps
plt.tight_layout()

# Show the plot
plt.show()