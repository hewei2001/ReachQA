import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
DG = nx.DiGraph()

# Define academic disciplines as nodes
disciplines = [
    "Computer Science", "Mathematics", "Physics", 
    "Biology", "Chemistry", "Economics", 
    "Psychology", "Philosophy"
]

DG.add_nodes_from(disciplines)

# Define the directed edges with weights indicating influence strength
edges_with_weights = [
    ("Computer Science", "Mathematics", 8),
    ("Mathematics", "Physics", 9),
    ("Physics", "Chemistry", 6),
    ("Biology", "Chemistry", 5),
    ("Biology", "Psychology", 7),
    ("Psychology", "Philosophy", 4),
    ("Economics", "Psychology", 3),
    ("Philosophy", "Economics", 2),
    ("Physics", "Biology", 4),
    ("Computer Science", "Physics", 6),
    ("Chemistry", "Biology", 3)
]

DG.add_weighted_edges_from(edges_with_weights)

# Define node positions using a circular layout for clarity
pos = nx.circular_layout(DG)

# Draw nodes with sizes reflecting their out-degree
node_sizes = [600 * DG.out_degree(n) for n in DG.nodes()]
nx.draw_networkx_nodes(DG, pos, node_size=node_sizes, node_color='lightgreen', alpha=0.9)

# Draw directed edges with varying width based on weight
edge_weights = [d['weight'] for u, v, d in DG.edges(data=True)]
nx.draw_networkx_edges(DG, pos, edgelist=DG.edges(), width=[w/2 for w in edge_weights], 
                       alpha=0.7, edge_color='royalblue', arrows=True, arrowsize=20)

# Draw labels
nx.draw_networkx_labels(DG, pos, font_size=10, font_weight='bold', verticalalignment='center')

# Draw edge weight labels for clarity
edge_labels = {(u, v): d['weight'] for u, v, d in DG.edges(data=True)}
nx.draw_networkx_edge_labels(DG, pos, edge_labels=edge_labels, font_size=8)

# Set plot title and ensure no overlap
plt.title('Interdisciplinary Knowledge Flow in\nModern Academia', fontsize=14, weight='bold', pad=20)
plt.axis('off')
plt.tight_layout()

# Display the plot
plt.show()