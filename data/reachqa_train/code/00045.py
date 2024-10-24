import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

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

# Calculate node sizes and colors based on degree centrality
degree_centrality = nx.degree_centrality(G)
node_sizes = [800 + 1000 * degree_centrality[node] for node in G.nodes()]
node_colors = [degree_centrality[node] for node in G.nodes()]

# Create a subplot layout
fig, ax = plt.subplots(1, 2, figsize=(14, 7))

# First subplot: Network Graph
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, ax=ax[0], node_size=node_sizes, node_color=node_colors,
                       cmap=plt.cm.Blues, edgecolors='black')
nx.draw_networkx_edges(G, pos, ax=ax[0], width=2, alpha=0.7, edge_color='gray')
nx.draw_networkx_labels(G, pos, ax=ax[0], font_size=10, font_family='serif')
ax[0].set_title("Interconnections of Renaissance Artists:\nA Web of Influence", fontsize=14, fontweight='bold')
ax[0].axis('off')

# Second subplot: Bar Chart of Degree Centrality
artist_names = list(degree_centrality.keys())
centrality_values = list(degree_centrality.values())
y_positions = np.arange(len(artist_names))
ax[1].barh(y_positions, centrality_values, color=plt.cm.Blues(np.linspace(0.3, 0.7, len(artist_names))))
ax[1].set_yticks(y_positions)
ax[1].set_yticklabels(artist_names, fontsize=10)
ax[1].invert_yaxis()  # Highest centrality on top
ax[1].set_xlabel('Degree Centrality', fontsize=12)
ax[1].set_title("Artist Centrality Ranking", fontsize=14, fontweight='bold')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()