import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph using NetworkX
G = nx.DiGraph()

# Add nodes (Mathematical Concepts)
nodes = {
    'A': 'Arithmetic',
    'G': 'Geometry',
    'Al': 'Algebra',
    'C': 'Calculus',
    'S': 'Set Theory',
    'P': 'Probability',
    'T': 'Topology',
    'CS': 'Computer Science'
}

G.add_nodes_from(nodes.keys())

# Add edges (Influences)
edges = [
    ('A', 'Al'),  # Arithmetic influences Algebra
    ('G', 'Al'),  # Geometry influences Algebra
    ('Al', 'C'),  # Algebra influences Calculus
    ('C', 'P'),   # Calculus influences Probability
    ('P', 'CS'),  # Probability influences Computer Science
    ('Al', 'S'),  # Algebra influences Set Theory
    ('S', 'T'),   # Set Theory influences Topology
    ('T', 'CS')   # Topology influences Computer Science
]

G.add_edges_from(edges)

# Position the nodes using a spring layout
pos = nx.spring_layout(G, seed=42)

# Plot the directed graph
plt.figure(figsize=(12, 10))

# Draw the graph
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=3000, edgecolors='k')
nx.draw_networkx_labels(G, pos, labels=nodes, font_size=12, font_weight='bold')
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='gray', arrows=True, arrowsize=20, arrowstyle='-|>')

# Customize plot
plt.title('Historical Evolution of Mathematical Concepts\nInterconnected Influences in Mathematics', fontsize=16, fontweight='bold')
plt.axis('off')

# Adjust layout for readability
plt.tight_layout()

# Display the plot
plt.show()