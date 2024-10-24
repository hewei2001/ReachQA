import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define nodes: fashion influencers and fashion brands
influencers = ['Alice Couture', 'Bella Trend', 'Chic Diva', 'Denim Guru', 'Fashionista']
brands = ['GlamourCo', 'ElegantWear', 'ChicBoutique', 'StyleHub', 'TrendSetter']

# Add nodes to the graph
G.add_nodes_from(influencers, bipartite=0)  # Group 0 for influencers
G.add_nodes_from(brands, bipartite=1)  # Group 1 for brands

# Define directed edges (influencer to brand or vice versa)
edges = [
    ('Alice Couture', 'GlamourCo'),
    ('Alice Couture', 'StyleHub'),
    ('Bella Trend', 'ElegantWear'),
    ('Chic Diva', 'ChicBoutique'),
    ('Denim Guru', 'GlamourCo'),
    ('Fashionista', 'TrendSetter'),
    ('Fashionista', 'ChicBoutique'),
    ('GlamourCo', 'Alice Couture'),
    ('ChicBoutique', 'Bella Trend'),
    ('StyleHub', 'Denim Guru')
]

# Add edges to the graph
G.add_edges_from(edges)

# Draw the network graph
plt.figure(figsize=(12, 8))

# Use a circular layout for better visualization
pos = nx.circular_layout(G)

# Draw nodes
nx.draw_networkx_nodes(G, pos, nodelist=influencers, node_size=1000, node_color='lightpink', node_shape='o', label='Influencers')
nx.draw_networkx_nodes(G, pos, nodelist=brands, node_size=1200, node_color='lightblue', node_shape='s', label='Brands')

# Draw edges with arrows
nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='-|>', arrowsize=15, edge_color='gray')

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=9, font_family='sans-serif')

# Add a legend
plt.legend(scatterpoints=1, loc='upper left', title='Node Type')

# Set plot title
plt.title('Fashion Influencer Network\nConnections with Fashion Brands', fontsize=14, fontweight='bold')

# Automatically adjust layout
plt.tight_layout()

# Remove axis
plt.axis('off')

# Show plot
plt.show()