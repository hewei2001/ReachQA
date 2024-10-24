import matplotlib.pyplot as plt
import networkx as nx

# Define roles in the robotics research team
roles = ['Data Scientist', 'Mechanical Engineer', 'Electrical Engineer', 'AI Specialist', 'Project Manager']

# Define directed edges to represent information flow
information_flow = [
    ('Data Scientist', 'AI Specialist'),
    ('Data Scientist', 'Project Manager'),
    ('Mechanical Engineer', 'Electrical Engineer'),
    ('Electrical Engineer', 'Mechanical Engineer'),
    ('AI Specialist', 'Project Manager'),
    ('Project Manager', 'Mechanical Engineer'),
    ('Project Manager', 'Electrical Engineer')
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges
G.add_nodes_from(roles)
G.add_edges_from(information_flow)

# Define positions of nodes for visualization using a shell layout to enhance readability
pos = nx.shell_layout(G)

# Define node colors and sizes based on importance or role distinction
node_colors = ['#87CEEB', '#FFA07A', '#3CB371', '#FFD700', '#6A5ACD']
node_sizes = [2000, 1800, 1800, 2000, 2200]

# Plot the directed node graph
plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9, node_shape='o')
nx.draw_networkx_labels(G, pos, font_size=11, font_weight='bold', font_color='black')
nx.draw_networkx_edges(G, pos, width=2.5, edge_color='gray', alpha=0.7, arrowsize=15)

# Add edge labels for clarity on communication pathways
edge_labels = {
    ('Data Scientist', 'AI Specialist'): 'Data Insights',
    ('Data Scientist', 'Project Manager'): 'Reports',
    ('Mechanical Engineer', 'Electrical Engineer'): 'Design Specs',
    ('Electrical Engineer', 'Mechanical Engineer'): 'Feedback',
    ('AI Specialist', 'Project Manager'): 'Model Updates',
    ('Project Manager', 'Mechanical Engineer'): 'Plans',
    ('Project Manager', 'Electrical Engineer'): 'Budget'
}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, font_color='blue', label_pos=0.5)

# Set plot title
plt.title('Information Flow within a Robotics Research Team', fontsize=16, fontweight='bold', pad=20, loc='center')

# Hide axes for a cleaner look
plt.axis('off')

# Automatically adjust layout to prevent overlaps
plt.tight_layout()

# Show plot
plt.show()