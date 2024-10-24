import matplotlib.pyplot as plt
import networkx as nx

# Define the nodes representing each stage
stages = [
    "Manuscript Completion",
    "Literary Agent",
    "Publisher",
    "Marketing Team",
    "Bestseller List"
]

# Define edges and assign weights that might represent the effort or time spent in each transition
edges = [
    ("Manuscript Completion", "Literary Agent", 2),
    ("Literary Agent", "Publisher", 1),
    ("Publisher", "Marketing Team", 3),
    ("Publisher", "Bestseller List", 4),
    ("Marketing Team", "Bestseller List", 5)
]

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(stages)
for source, target, weight in edges:
    G.add_edge(source, target, weight=weight)

# Calculate the effort spent on each stage
stage_effort = {
    "Manuscript Completion": 30,
    "Literary Agent": 10,
    "Publisher": 25,
    "Marketing Team": 20,
    "Bestseller List": 15
}

# Use subplots to create two plots side by side
fig, axes = plt.subplots(1, 2, figsize=(14, 7))

# Plot 1: Directed graph
pos = nx.shell_layout(G)
node_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A5', '#F3FF33']
node_sizes = [1200, 1000, 1000, 1000, 1200]

nx.draw_networkx_nodes(G, pos, ax=axes[0], node_color=node_colors, node_size=node_sizes)
nx.draw_networkx_edges(G, pos, ax=axes[0], arrowstyle='-|>', arrowsize=20, edge_color='black', width=[G[u][v]['weight'] for u, v in G.edges()])
nx.draw_networkx_labels(G, pos, ax=axes[0], font_size=9, font_family='sans-serif')

edge_labels = {(u, v): f"Weight: {d['weight']}" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, ax=axes[0], edge_labels=edge_labels, font_size=8)

axes[0].set_title("Navigating the Path to Success:\nThe Journey of a Bestseller Book", fontsize=12, pad=20)
axes[0].axis('off')

# Plot 2: Pie chart of effort distribution
effort_labels = list(stage_effort.keys())
effort_values = list(stage_effort.values())
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']

axes[1].pie(effort_values, labels=effort_labels, autopct='%1.1f%%', startangle=140, colors=colors)
axes[1].set_title("Effort Distribution Across Stages", fontsize=12, pad=20)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()