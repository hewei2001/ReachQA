import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define departments and edges with weights
departments = ['Product', 'Engineering', 'Marketing', 'Customer Support', 'HR']
edges = [
    ('Product', 'Engineering', 8),
    ('Product', 'Marketing', 7),
    ('Engineering', 'Customer Support', 5),
    ('Marketing', 'HR', 6),
    ('Customer Support', 'Engineering', 3),
    ('HR', 'Product', 4)
]

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph with weights
for source, target, weight in edges:
    G.add_edge(source, target, weight=weight)

# Performance metrics for each department
performance_metrics = {
    'Product': 15,
    'Engineering': 20,
    'Marketing': 10,
    'Customer Support': 25,
    'HR': 8
}

# Create subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 12), gridspec_kw={'height_ratios': [2, 1]})

# First subplot: Collaboration Dynamics
pos = nx.spring_layout(G, seed=42)  # positions for all nodes
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightblue', alpha=0.8, ax=axs[0])
nx.draw_networkx_edges(G, pos, edgelist=G.edges(data=True), arrows=True, width=2, alpha=0.6, ax=axs[0])
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif', ax=axs[0])
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', ax=axs[0])
axs[0].set_title('Collaboration Dynamics\nin a Tech Company', fontsize=16, fontweight='bold')
axs[0].axis('off')

# Second subplot: Department Performance Metrics
axs[1].bar(performance_metrics.keys(), performance_metrics.values(), color='lightgreen')
axs[1].set_title('Department Performance Metrics', fontsize=16, fontweight='bold')
axs[1].set_ylabel('Number of Projects Handled', fontsize=12)
axs[1].set_xlabel('Departments', fontsize=12)
axs[1].grid(axis='y', linestyle='--', alpha=0.7)
axs[1].set_ylim(0, max(performance_metrics.values()) + 5)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()