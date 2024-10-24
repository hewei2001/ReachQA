import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as mpatches

# Define the social network as an undirected graph
G = nx.Graph()

# Add nodes representing team members
members = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen', 'Ian', 'Julia']
G.add_nodes_from(members)

# Add edges representing communication paths between team members
edges = [
    ('Alice', 'Bob'), ('Alice', 'Charlie'), ('Alice', 'Eva'),
    ('Bob', 'Charlie'), ('Bob', 'Grace'),
    ('Charlie', 'Frank'),
    ('David', 'Eva'), ('David', 'Ian'),
    ('Eva', 'Julia'),
    ('Frank', 'Grace'),
    ('Grace', 'Helen'),
    ('Helen', 'Ian')
]
G.add_edges_from(edges)

# Determine the layout for the nodes
pos = nx.spring_layout(G, seed=42)

# Customize node sizes and colors based on degree (number of connections)
node_sizes = [800 + 200 * G.degree(node) for node in G.nodes()]
node_colors = ['#4A90E2' if G.degree(node) > 2 else '#50E3C2' for node in G.nodes()]

# Set up plot
plt.figure(figsize=(14, 12))

# Draw nodes with customized size and color
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black', linewidths=1.5)

# Draw edges with varying styles
edge_widths = [2.5 if 'Alice' in edge else 1.5 for edge in edges]
nx.draw_networkx_edges(G, pos, edgelist=edges, width=edge_widths, edge_color='gray', style='solid')

# Add labels to the nodes
nx.draw_networkx_labels(G, pos, font_size=12, font_color='black', font_family='sans-serif')

# Customize the title and layout
title = "Social Connections in a Remote Working Environment\nVisualization of InnoTech Team Communication"
plt.title(title, fontsize=16, fontweight='bold')
plt.axis('off')

# Add enhanced legend using custom markers
team_member_patch = mpatches.Patch(color='#4A90E2', label='Highly Connected Team Member')
other_member_patch = mpatches.Patch(color='#50E3C2', label='Team Member')
edge_patch = plt.Line2D([0], [0], color='gray', lw=2, label='Communication Path')
plt.legend(handles=[team_member_patch, other_member_patch, edge_patch], loc='upper right', fontsize=10, title='Legend')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()