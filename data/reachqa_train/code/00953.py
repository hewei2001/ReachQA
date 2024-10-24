import matplotlib.pyplot as plt
import networkx as nx

# Define research institutions
institutions = ['MIT', 'Stanford', 'Cambridge', 'Oxford', 'ETH Zurich']

# Define collaborations (undirected edges between nodes)
collaborations = [
    ('MIT', 'Stanford'),
    ('MIT', 'Cambridge'),
    ('Stanford', 'Cambridge'),
    ('Stanford', 'Oxford'),
    ('Cambridge', 'ETH Zurich'),
    ('Oxford', 'ETH Zurich'),
    ('MIT', 'ETH Zurich'),
    ('Oxford', 'MIT'),
    ('Stanford', 'ETH Zurich')
]

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(institutions)
G.add_edges_from(collaborations)

# Define position layout for nodes
pos = nx.spring_layout(G, seed=42)  # Using seed for consistent layout

# Degree as node size factor
node_size = [700 + 300 * G.degree(node) for node in G.nodes()]

# Draw the network
plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=node_size, edgecolors='black')
nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# Draw edge labels with connection names
edge_labels = {(u, v): f"{u}-{v}" for u, v in collaborations}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# Title and layout adjustments
plt.title('Research Collaboration Network in Quantum Computing and AI\nKey Institutions and Their Projects', fontsize=15, fontweight='bold')
plt.axis('off')  # Hide axes for a cleaner look
plt.tight_layout()  # Adjust layout to prevent overlap

# Display the plot
plt.show()