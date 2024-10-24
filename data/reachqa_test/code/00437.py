import matplotlib.pyplot as plt
import networkx as nx
from collections import Counter

# Initialize a graph
G = nx.Graph()

# Define nodes with their departments
nodes = [
    ('Alice', 'Research'),
    ('Bob', 'Development'),
    ('Charlie', 'Development'),
    ('Dana', 'Marketing'),
    ('Eve', 'Design'),
    ('Frank', 'Research'),
    ('Grace', 'Marketing')
]

# Add nodes to the graph with department as an attribute
for node, department in nodes:
    G.add_node(node, department=department)

# Define edges with the type of collaboration
edges = [
    ('Alice', 'Bob', 'Idea Sharing'),
    ('Alice', 'Charlie', 'Joint Coding'),
    ('Bob', 'Dana', 'Market Analysis'),
    ('Charlie', 'Eve', 'Design Collab'),
    ('Dana', 'Grace', 'Brand Strategy'),
    ('Frank', 'Alice', 'Research Exchange'),
    ('Grace', 'Frank', 'Feedback')
]

# Add edges to the graph with collaboration type as an attribute
for edge in edges:
    G.add_edge(edge[0], edge[1], collaboration=edge[2])

# Create a layout for the nodes
pos = nx.spring_layout(G, seed=42, k=0.8)  # Adjust k for more spacing

# Define node colors based on departments
department_colors = {
    'Research': '#FF9999',
    'Development': '#66B3FF',
    'Marketing': '#99FF99',
    'Design': '#FFCC99'
}
node_colors = [department_colors[G.nodes[node]['department']] for node in G.nodes()]

# Prepare to plot
fig, axes = plt.subplots(1, 2, figsize=(18, 10))

# Plot 1: Network Graph
ax1 = axes[0]
nx.draw_networkx_nodes(G, pos, ax=ax1, node_size=2500, node_color=node_colors, edgecolors='black', linewidths=1.5)
nx.draw_networkx_edges(G, pos, ax=ax1, width=2, alpha=0.6, edge_color='gray')
nx.draw_networkx_labels(G, pos, ax=ax1, font_size=10, font_weight='bold', font_color='black')
edge_labels = nx.get_edge_attributes(G, 'collaboration')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax1, font_size=10, font_color='red')

# Legend for departments
for department, color in department_colors.items():
    ax1.scatter([], [], c=color, edgecolors='black', label=department, s=150)
ax1.legend(title='Departments', fontsize=9, title_fontsize='11')
ax1.set_title('Web of Innovation:\nCollaborative Dynamics in a Tech Startup', fontsize=16, fontweight='bold')
ax1.axis('off')

# Plot 2: Histogram of Collaborations per Node
ax2 = axes[1]
collaborations = Counter(node for edge in edges for node in edge[:2])

# Modified data to adjust collaboration distribution
adjusted_collaborations = {'Alice': 4, 'Bob': 3, 'Charlie': 3, 'Dana': 2, 'Eve': 1, 'Frank': 3, 'Grace': 2}

names, collab_count = zip(*adjusted_collaborations.items())
bar_width = 0.6
ax2.bar(names, collab_count, color=[department_colors[G.nodes[name]['department']] for name in names], 
        edgecolor='black', alpha=0.7, width=bar_width)

# Preferences for narrow bars with spacing and avoiding occlusion
ax2.set_title('Collaboration Frequency Across Members', fontsize=14, fontweight='bold')
ax2.set_ylabel('Number of Collaborations', fontsize=12)
ax2.set_xlabel('Team Members', fontsize=12)
ax2.set_xticks(range(len(names)))
ax2.set_xticklabels(names, rotation=45, ha='right')

# Display the plot
plt.show()