import matplotlib.pyplot as plt
import networkx as nx

# Define the nodes representing different energy sources
nodes = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Bioenergy']

# Define the edges representing collaborative relationships
edges = [
    ('Solar', 'Wind'),
    ('Solar', 'Hydroelectric'),
    ('Wind', 'Geothermal'),
    ('Hydroelectric', 'Geothermal'),
    ('Geothermal', 'Bioenergy'),
    ('Bioenergy', 'Solar'),
    ('Wind', 'Bioenergy')
]

# Create an undirected graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Use the spring layout for better aesthetics and readability
pos = nx.spring_layout(G, seed=42)

# Customize node and edge attributes
node_sizes = [3000 for _ in nodes]  # All nodes have the same size
node_colors = ['#76c7c0', '#f9a03f', '#f1c40f', '#e74c3c', '#8e44ad']
edge_widths = [3 if ('Solar' in edge or 'Wind' in edge) else 1 for edge in G.edges]

# Draw the graph with customized options
plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9, linewidths=2, edgecolors='white')
nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color='gray', style='solid', alpha=0.6)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_color='darkgreen')

# Add a meaningful title
plt.title("EcoNet: Mapping Interactions of Sustainable Energy Sources", fontsize=16, fontweight='bold', color='darkblue', pad=20)

# Remove axis for clarity
plt.axis('off')

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the graph
plt.show()