import matplotlib.pyplot as plt
import networkx as nx

# Departments in the company
departments = ['R&D', 'Marketing', 'Sales', 'HR', 'Customer Support']

# Communication Intensity Matrix
# Intensity from row department to column department
communication_matrix = [
    [0, 15, 20, 5, 10],   # R&D to others
    [10, 0, 25, 5, 15],   # Marketing to others
    [5, 10, 0, 5, 20],    # Sales to others
    [10, 5, 5, 0, 15],    # HR to others
    [5, 5, 15, 10, 0]     # Customer Support to others
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes for departments
G.add_nodes_from(departments)

# Add edges with weights for communication intensity
for i, source in enumerate(departments):
    for j, target in enumerate(departments):
        if communication_matrix[i][j] > 0:
            G.add_edge(source, target, weight=communication_matrix[i][j])

# Set up node positions using a spring layout for clarity
pos = nx.spring_layout(G, k=0.3, iterations=50)

# Plot the graph
plt.figure(figsize=(12, 8))

# Draw nodes with color and size
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='skyblue')

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=12, font_color='black', font_weight='bold')

# Draw edges with varying widths based on communication intensity
edges = G.edges(data=True)
nx.draw_networkx_edges(
    G, pos, edgelist=edges,
    width=[edge[2]['weight'] * 0.1 for edge in edges],
    arrowstyle='->', arrowsize=20
)

# Add edge labels to indicate intensity
edge_labels = {(source, target): f'{attr["weight"]}' for source, target, attr in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, label_pos=0.3)

# Add title
plt.title('Communication Flow in\nGlobeTech Solutions', fontsize=16, fontweight='bold', pad=20)

# Remove axes for cleaner look
plt.axis('off')

# Automatically adjust layout for optimal appearance
plt.tight_layout()

# Display the plot
plt.show()