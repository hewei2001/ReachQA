import matplotlib.pyplot as plt
import networkx as nx

# Define artists and their connections
connections = {
    "Leonardo da Vinci": ["Michelangelo", "Raphael", "Botticelli"],
    "Michelangelo": ["Leonardo da Vinci", "Raphael", "Donatello"],
    "Raphael": ["Leonardo da Vinci", "Michelangelo", "Titian"],
    "Botticelli": ["Leonardo da Vinci", "Donatello"],
    "Donatello": ["Michelangelo", "Botticelli"],
    "Titian": ["Raphael"]
}

# Create the undirected graph
G = nx.Graph(connections)

# Calculate node sizes based on degree centrality
node_sizes = [800 + 1000 * nx.degree_centrality(G)[node] for node in G.nodes()]

# Choose a layout for the nodes
pos = nx.spring_layout(G, seed=42)

# Draw nodes with varying size and color
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='skyblue', edgecolors='black')

# Draw edges with varying thickness
nx.draw_networkx_edges(G, pos, width=2, alpha=0.7, edge_color='gray')

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=12, font_family='serif')

# Adjust plot appearance
plt.title("Interconnections of Renaissance Artists:\nA Web of Influence", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.axis('off')  # Turn off the axis

# Show the plot
plt.show()