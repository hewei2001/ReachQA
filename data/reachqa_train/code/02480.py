import matplotlib.pyplot as plt
import networkx as nx

# Define nodes (countries involved in quantum computing)
countries = ['USA', 'Germany', 'Japan', 'China', 'UK', 'Canada', 'Australia', 'India']

# Define edges (collaborations between countries)
collaborations = [
    ('USA', 'Germany'), 
    ('USA', 'Japan'), 
    ('Germany', 'UK'), 
    ('China', 'Japan'),
    ('UK', 'Canada'),
    ('Canada', 'Australia'),
    ('Australia', 'India'),
    ('India', 'China'),
    ('USA', 'China'),
    ('Germany', 'Japan')
]

# Initialize the graph
G = nx.Graph()

# Add nodes and edges
G.add_nodes_from(countries)
G.add_edges_from(collaborations)

# Generate positions for the nodes in a circular layout
pos = nx.circular_layout(G)

# Plot the graph
fig, ax = plt.subplots(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color='lightblue', edgecolors='black')
nx.draw_networkx_edges(G, pos, width=2, edge_color='gray', style='solid')
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

# Add title and adjust layout
plt.title("Mapping Connections in Quantum Computing\nCollaborations (2024)", fontsize=16, fontweight='bold', pad=20)
plt.axis('off')
plt.tight_layout()

# Display the plot
plt.show()