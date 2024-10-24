import matplotlib.pyplot as plt
import networkx as nx

# Define the nodes representing key areas in tech and art
nodes = [
    "AI", "Robotics", "Digital Art", 
    "Music Production", "VR", 
    "Film Making", "Dance Tech"
]

# Define the adjacency matrix representing connections/collaborations
connections = [
    [0, 1, 1, 0, 1, 0, 0],  # AI
    [1, 0, 1, 0, 1, 1, 0],  # Robotics
    [1, 1, 0, 1, 1, 0, 1],  # Digital Art
    [0, 0, 1, 0, 1, 1, 1],  # Music Production
    [1, 1, 1, 1, 0, 1, 0],  # VR
    [0, 1, 0, 1, 1, 0, 1],  # Film Making
    [0, 0, 1, 1, 0, 1, 0],  # Dance Tech
]

# Initialize a graph using the adjacency matrix
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(nodes)

# Add edges to the graph based on the adjacency matrix
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        if connections[i][j] == 1:
            G.add_edge(nodes[i], nodes[j])

# Plotting
plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G, seed=42)  # Layout for node positioning

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='cornflowerblue')

# Draw edges
nx.draw_networkx_edges(G, pos, width=2, edge_color='lightgrey')

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_color='black')

# Add a title reflecting the backstory
plt.title("Symphony of Innovation:\nThe Interconnected World of Tech and Art", fontsize=16, pad=20)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Hide axes
plt.axis('off')

# Show plot
plt.show()