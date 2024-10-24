import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Initialize directed graph
G = nx.DiGraph()

# Nodes represent institutions
institutions = [
    "Alpha Inst. of Space Research", 
    "Beta Labs", 
    "Gamma Space Tech", 
    "Delta University", 
    "Epsilon Aeronautics"
]

# Add nodes to the graph
G.add_nodes_from(institutions)

# Define directed edges with weights representing collaborative projects
collaborations = [
    ("Alpha Inst. of Space Research", "Beta Labs", 12),
    ("Beta Labs", "Gamma Space Tech", 8),
    ("Gamma Space Tech", "Delta University", 15),
    ("Delta University", "Epsilon Aeronautics", 5),
    ("Epsilon Aeronautics", "Alpha Inst. of Space Research", 10),
    ("Alpha Inst. of Space Research", "Gamma Space Tech", 7),
    ("Beta Labs", "Delta University", 10),
    ("Gamma Space Tech", "Epsilon Aeronautics", 12),
    ("Delta University", "Alpha Inst. of Space Research", 3),
    ("Epsilon Aeronautics", "Beta Labs", 6)
]

# Add edges with weights to the graph
G.add_weighted_edges_from(collaborations)

# Define position layout for better clarity
pos = nx.spring_layout(G, seed=42)

# Prepare data for the new bar chart subplot
institution_collaboration_counts = {institution: 0 for institution in institutions}
for u, v, data in G.edges(data=True):
    institution_collaboration_counts[u] += data['weight']

# Create the subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Network Graph
plt.sca(axes[0])
node_sizes = [1500 + 50 * sum(G[u][v]['weight'] for v in G.neighbors(u)) for u in G.nodes()]
edge_weights = [G[u][v]['weight'] for u, v in G.edges()]
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='#87CEFA', edgecolors='black')
nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold', verticalalignment='center')

nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=15, edge_color=edge_weights, width=2.5, 
                       edge_cmap=plt.cm.Blues, connectionstyle='arc3,rad=0.1')
edge_labels = {(u, v): f"{G[u][v]['weight']} projects" for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7, label_pos=0.3)

plt.title("Interstellar Research Collaboration\nNetwork of Leading Institutions", fontsize=14, weight='bold', pad=20)
plt.axis('off')

# Bar Chart
plt.sca(axes[1])
institution_names, collaboration_counts = zip(*institution_collaboration_counts.items())
colors = plt.cm.viridis(np.linspace(0, 1, len(institution_names)))
axes[1].barh(institution_names, collaboration_counts, color=colors)
axes[1].set_title("Total Collaborations by Institution", fontsize=12, weight='bold', pad=10)
axes[1].set_xlabel("Number of Projects")
axes[1].invert_yaxis()  # Ensures the highest bar is on top

# Adjust layout
plt.tight_layout()
plt.show()