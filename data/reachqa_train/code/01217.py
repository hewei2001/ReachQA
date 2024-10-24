import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define the nodes and their hypothetical importance scores based on connectivity
nodes = {
    "Digital Sources": 6, 
    "Preliminary Analysis": 7, 
    "Data Synthesis": 8,
    "Manuscript Drafting": 6, 
    "Peer Review": 5, 
    "Scientific Publication": 4
}

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
G.add_nodes_from(nodes.keys())
for (start, end), weight in edges.items():
    G.add_edge(start, end, weight=weight)

# Define positions for each node using spring layout for better readability
pos = nx.spring_layout(G, seed=42)

# Create the plot
plt.figure(figsize=(14, 10))

# Nodes: Size and color based on importance
node_sizes = [nodes[node] * 400 for node in G.nodes]
node_colors = [plt.cm.plasma(nodes[node] / max(nodes.values())) for node in G.nodes]

# Draw nodes and edges
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black', alpha=0.9)
nx.draw_networkx_edges(G, pos, edgelist=edges.keys(), arrowstyle='-|>', arrowsize=15, 
                       width=[w for w in edges.values()], edge_color='gray')

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', verticalalignment='center')
nx.draw_networkx_edge_labels(G, pos, edge_labels={edge: f"{weight}" for edge, weight in edges.items()}, font_size=8)

# Add a color bar for node significance
sm = plt.cm.ScalarMappable(cmap=plt.cm.plasma, norm=plt.Normalize(vmin=min(nodes.values()), vmax=max(nodes.values())))
sm._A = []
cbar = plt.colorbar(sm, ax=plt.gca(), shrink=0.8)  # Specify the current axes for the color bar
cbar.set_label('Node Importance', rotation=270, labelpad=20)

# Add a concise, multi-line title
plt.title("Internet Information Flow in\nModern Academic Research Workflow", fontsize=16, fontweight='bold')

# Adjust layout
plt.axis('off')
plt.tight_layout()

# Show the plot
plt.show()