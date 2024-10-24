import matplotlib.pyplot as plt
import networkx as nx

# Define the nodes in the research workflow
nodes = [
    "Digital Sources", "Preliminary Analysis", "Data Synthesis",
    "Manuscript Drafting", "Peer Review", "Scientific Publication"
]

# Define the directed edges with weights representing the flow intensity
edges = {
    ("Digital Sources", "Preliminary Analysis"): 5,
    ("Preliminary Analysis", "Data Synthesis"): 4,
    ("Data Synthesis", "Manuscript Drafting"): 6,
    ("Manuscript Drafting", "Peer Review"): 3,
    ("Peer Review", "Scientific Publication"): 4,
    ("Digital Sources", "Data Synthesis"): 2,
    ("Data Synthesis", "Peer Review"): 2
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
for (start, end), weight in edges.items():
    G.add_edge(start, end, weight=weight)

# Define positions for each node using a circular layout
pos = nx.circular_layout(G)

# Create the plot
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_size=2500, node_color='#FFA07A', edgecolors='black')
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
nx.draw_networkx_edges(G, pos, edgelist=edges.keys(), arrowstyle='->', arrowsize=20, width=[w/2 for w in edges.values()])
nx.draw_networkx_edge_labels(G, pos, edge_labels={edge: f"{weight} units" for edge, weight in edges.items()}, font_size=8)

# Chart Title
plt.title("Internet Information Flow in\nModern Academic Research", fontsize=16, fontweight='bold')

# Adjust layout to avoid text clipping
plt.axis('off')
plt.tight_layout()

# Show the plot
plt.show()