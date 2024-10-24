import matplotlib.pyplot as plt
import networkx as nx

# Define institutions and their collaborations
institutions = {
    'MIT': ['Harvard', 'Caltech', 'Oxford', 'Berkeley'],
    'Harvard': ['MIT', 'Stanford', 'Berkeley'],
    'Stanford': ['Harvard', 'Cambridge', 'Berkeley'],
    'Caltech': ['MIT', 'Cambridge'],
    'Cambridge': ['Stanford', 'Caltech'],
    'Oxford': ['MIT', 'UCL'],
    'UCL': ['Oxford'],
    'Berkeley': ['MIT', 'Harvard', 'Stanford']
}

# Create a graph from the defined collaborations
G = nx.Graph()
for institution, collaborators in institutions.items():
    for collaborator in collaborators:
        G.add_edge(institution, collaborator)

# Node size is proportional to the number of collaborations
node_sizes = [len(institutions[node]) * 400 for node in G.nodes]

# Assign different colors to nodes to enhance visual distinction
node_colors = ['skyblue' if len(institutions[node]) > 2 else 'lightgreen' for node in G.nodes]

# Draw the graph
pos = nx.spring_layout(G, seed=42)  # Position nodes with spring layout
plt.figure(figsize=(12, 9))
nx.draw(
    G, pos, with_labels=True, node_size=node_sizes,
    node_color=node_colors, font_size=10, font_weight='bold', edge_color='gray'
)

# Title and layout adjustments
plt.title(
    'The Web of Quantum Computing Research\nCollaboration Among Top Institutions',
    fontsize=15, weight='bold', pad=20
)
plt.axis('off')
plt.tight_layout()

# Display the plot
plt.show()