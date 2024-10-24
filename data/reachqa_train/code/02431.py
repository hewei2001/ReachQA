import matplotlib.pyplot as plt
import networkx as nx

# Nodes: Researchers (R1, R2, ...) and Universities (U1, U2, ...)
nodes = [
    "R1", "R2", "R3", "R4", "R5",  # Researchers
    "U1", "U2", "U3", "U4", "U5"   # Universities
]

# Edges (Collaborations): (node1, node2)
edges = [
    ("R1", "U1"), ("R1", "U2"), ("R1", "R3"),
    ("R2", "U1"), ("R2", "U3"), ("R2", "R4"),
    ("R3", "U2"), ("R3", "U4"), ("R3", "R5"),
    ("R4", "U3"), ("R4", "U5"), ("R4", "R5"),
    ("R5", "U1"), ("R5", "U5"), ("U1", "U3"),
    ("U2", "U5"), ("U3", "U4")
]

# Create an undirected graph
G = nx.Graph()

# Add nodes and edges
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Define positions for nodes using spring layout
pos = nx.spring_layout(G, seed=42)

# Draw nodes with color based on type (Researcher or University)
node_colors = ["#1f77b4" if node.startswith("R") else "#ff7f0e" for node in G.nodes()]

# Draw edges with different styles
edges_researchers = [(u, v) for u, v in G.edges() if u.startswith("R") and v.startswith("R")]
edges_universities = [(u, v) for u, v in G.edges() if u.startswith("U") and v.startswith("U")]
edges_collaborations = [(u, v) for u, v in G.edges() if (u.startswith("R") and v.startswith("U")) or (u.startswith("U") and v.startswith("R"))]

# Create the plot
plt.figure(figsize=(12, 9))
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color=node_colors, alpha=0.8)
nx.draw_networkx_edges(G, pos, edgelist=edges_researchers, width=2, alpha=0.7, edge_color="blue", style='dashed')
nx.draw_networkx_edges(G, pos, edgelist=edges_universities, width=2, alpha=0.7, edge_color="orange", style='dotted')
nx.draw_networkx_edges(G, pos, edgelist=edges_collaborations, width=2, alpha=0.5, edge_color="gray", style='solid')
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_color='black')

# Adding a title and labels
plt.title("Scientific Collaborations in Quantum Computing\nResearchers and Universities Network", fontsize=16, fontweight='bold')

# Automatically adjust layout to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()