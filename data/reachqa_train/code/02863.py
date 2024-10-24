import matplotlib.pyplot as plt
import networkx as nx

# Nodes for the stages and destinations
nodes = [
    'Farmers Market', 'Distributors', 'Italian Cuisine',
    'Mexican Cuisine', 'Indian Cuisine', 'Local Restaurants'
]

# Directed edges with weights indicating the quantity of ingredients
edges = [
    ('Farmers Market', 'Distributors', 50),
    ('Distributors', 'Italian Cuisine', 20),
    ('Distributors', 'Mexican Cuisine', 15),
    ('Distributors', 'Indian Cuisine', 15),
    ('Italian Cuisine', 'Local Restaurants', 18),
    ('Mexican Cuisine', 'Local Restaurants', 14),
    ('Indian Cuisine', 'Local Restaurants', 12)
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

# Determine the layout for our graph
pos = nx.spring_layout(G, seed=42)  # Using a spring layout for a clean visualization

plt.figure(figsize=(12, 8))

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='#FFDDC1', edgecolors='black')

# Draw edges with varying width based on weights
edge_widths = [0.1 * G[u][v]['weight'] for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, edgelist=edges, width=edge_widths, arrows=True, arrowstyle='-|>', arrowsize=20, edge_color='orange')

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=11, font_weight='bold')

# Create a dictionary for edge labels with weight
edge_labels = {(u, v): f"{G[u][v]['weight']} units" for u, v in G.edges()}

# Draw edge labels
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

# Title and adjustments
plt.title('Culinary Network:\nIngredients\' Journey in Global Cuisine', fontsize=16, weight='bold', pad=20)
plt.axis('off')  # Hide the axis for cleaner look

# Adjust the layout to fit all elements
plt.tight_layout()

# Display the plot
plt.show()