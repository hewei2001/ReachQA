import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define nodes (departments)
departments = ['Emergency', 'Radiology', 'Laboratory', 'Pharmacy', 'Inpatient Care']

# Add nodes to the graph
G.add_nodes_from(departments)

# Define directed edges with weights (number of interactions)
edges = [
    ('Emergency', 'Radiology', 50),
    ('Emergency', 'Laboratory', 70),
    ('Emergency', 'Inpatient Care', 30),
    ('Radiology', 'Inpatient Care', 40),
    ('Laboratory', 'Pharmacy', 60),
    ('Pharmacy', 'Inpatient Care', 80),
    ('Inpatient Care', 'Emergency', 20)
]

# Add edges to the graph
G.add_weighted_edges_from(edges)

# Use a layout for better visualization
pos = nx.spring_layout(G, seed=42)

# Draw the nodes with specific properties
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='skyblue', edgecolors='black')

# Draw the edges with arrows
nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='-|>', arrowsize=15, edge_color='grey')

# Add labels to nodes
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# Add edge labels with the number of interactions
edge_labels = {(u, v): f"{w} interactions" for u, v, w in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, label_pos=0.3)

# Set the title for the plot with line breaks for readability
plt.title("Information Flow in Healthcare:\nA Hospital's Network of Departments", fontsize=14, fontweight='bold')

# Automatically adjust the layout for better presentation
plt.tight_layout()

# Remove axes for a cleaner look
plt.axis('off')

# Display the directed node chart
plt.show()