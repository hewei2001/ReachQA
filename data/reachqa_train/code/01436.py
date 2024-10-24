import matplotlib.pyplot as plt
import networkx as nx

# Define nodes (civilizations)
civilizations = ["Egyptian Empire", "Greek City-States", "Roman Empire", "Phoenicians", "Mesopotamians"]

# Define edges (trade routes and knowledge exchange)
routes = [
    ("Egyptian Empire", "Greek City-States", "Papyrus & Textiles"),
    ("Greek City-States", "Roman Empire", "Philosophies & Art"),
    ("Roman Empire", "Egyptian Empire", "Engineering & Architecture"),
    ("Phoenicians", "Greek City-States", "Navigation Techniques"),
    ("Mesopotamians", "Egyptian Empire", "Astronomy & Math"),
    ("Greek City-States", "Phoenicians", "Iron Tools"),
    ("Roman Empire", "Phoenicians", "Glassware & Wine"),
]

# Create directed graph
G = nx.DiGraph()

# Add nodes
G.add_nodes_from(civilizations)

# Add edges with labels
G.add_edges_from([(src, dest, {'label': label}) for src, dest, label in routes])

# Set positions using the shell layout for clear separation
pos = nx.shell_layout(G)

# Draw nodes with distinct style
nx.draw_networkx_nodes(G, pos, node_size=2500, node_color='#FFDD44', edgecolors='black')

# Draw directed edges with arrows
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20, edge_color='#556B2F', width=2, connectionstyle='arc3,rad=0.2')

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# Draw edge labels with adjusted position for clarity
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=8, label_pos=0.5)

# Title and details
plt.title('Ancient Trade Routes and Knowledge Exchange\nAround the Mediterranean', fontsize=14, fontweight='bold', pad=20)
plt.axis('off')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()