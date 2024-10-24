import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define nodes (fashion designers/brands)
nodes = [
    'Chanel', 'Gucci', 'Louis Vuitton', 'Prada',
    'Versace', 'Balenciaga', 'Yves Saint Laurent', 'Dior'
]

# Add nodes to the graph
G.add_nodes_from(nodes)

# Define edges with weights (influence strength)
edges = [
    ('Chanel', 'Louis Vuitton', 8),
    ('Gucci', 'Balenciaga', 6),
    ('Prada', 'Versace', 4),
    ('Yves Saint Laurent', 'Dior', 7),
    ('Dior', 'Chanel', 5),
    ('Louis Vuitton', 'Gucci', 7),
    ('Balenciaga', 'Prada', 3)
]

# Add edges to the graph
G.add_weighted_edges_from(edges)

# Generate positions for each node using the spring layout
pos = nx.spring_layout(G, seed=42)

# Create the plot
plt.figure(figsize=(12, 10))

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightpink', edgecolors='black')

# Draw edges with arrows, width proportional to influence weight
weights = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edges(G, pos, edgelist=weights.keys(), width=[weight/1.5 for weight in weights.values()], alpha=0.6, edge_color='teal', arrows=True, arrowstyle='-|>')

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_color='darkblue')

# Add edge labels to indicate influence weight
nx.draw_networkx_edge_labels(G, pos, edge_labels=weights, font_color='darkgreen')

# Set the title, splitting into multiple lines if necessary
plt.title("Influence Network in the Fashion Industry:\nDesigners and Brands", fontsize=16, fontweight='bold', pad=20)

# Remove axes for a cleaner look
plt.axis('off')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()