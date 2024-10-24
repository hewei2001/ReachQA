import matplotlib.pyplot as plt
import networkx as nx

# Define directors (nodes)
directors = [
    "Luna Voss", "Arjun Patel", "Kai Nakamura", "Elena Garcia", 
    "Sofia Petrova", "Amina Jaziri", "Rajesh Khan", "Giovanni Rossi"
]

# Define collaborations (directed edges)
collaborations = [
    ("Luna Voss", "Arjun Patel"),
    ("Luna Voss", "Kai Nakamura"),
    ("Arjun Patel", "Elena Garcia"),
    ("Kai Nakamura", "Sofia Petrova"),
    ("Elena Garcia", "Amina Jaziri"),
    ("Sofia Petrova", "Giovanni Rossi"),
    ("Amina Jaziri", "Rajesh Khan"),
    ("Rajesh Khan", "Luna Voss"),
    ("Giovanni Rossi", "Elena Garcia"),
    ("Kai Nakamura", "Rajesh Khan"),
    ("Sofia Petrova", "Amina Jaziri")
]

# Create directed graph
G = nx.DiGraph()

# Add nodes and edges
G.add_nodes_from(directors)
G.add_edges_from(collaborations)

# Plot the network
plt.figure(figsize=(12, 8))

# Define positions for nodes using a circular layout
pos = nx.circular_layout(G)

# Draw nodes and edges with custom styles
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color='lightblue', edgecolors='black')
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=15, edge_color='gray', width=2)
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif', font_color='black')

# Add a title with line breaks for readability
plt.title("Network of Cinematic Visionaries in 2100:\nA Collaborative Odyssey", fontsize=14, fontweight='bold')

# Remove axis to focus on the graph
plt.axis('off')

# Automatically adjust the layout to avoid overlaps
plt.tight_layout()

# Display the plot
plt.show()