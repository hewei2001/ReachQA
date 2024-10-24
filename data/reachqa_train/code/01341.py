import matplotlib.pyplot as plt
import networkx as nx

# Define marine species and their interactions
interactions = {
    "Clownfish": ["Anemones", "Larger Fish"],
    "Anemones": ["Clownfish", "Corals"],
    "Corals": ["Anemones", "Crustaceans", "Algae"],
    "Larger Fish": ["Clownfish", "Sharks"],
    "Crustaceans": ["Corals", "Algae"],
    "Algae": ["Crustaceans", "Corals"],
    "Sharks": ["Larger Fish"]
}

# Create the undirected graph
G = nx.Graph(interactions)

# Calculate node sizes based on degree centrality
node_sizes = [800 + 1000 * nx.degree_centrality(G)[node] for node in G.nodes()]

# Assign colors to nodes based on their role
node_colors = {
    "Clownfish": "#ffcc00",
    "Anemones": "#66c2a5",
    "Corals": "#fc8d62",
    "Larger Fish": "#8da0cb",
    "Crustaceans": "#e78ac3",
    "Algae": "#a6d854",
    "Sharks": "#ffd92f"
}

# Extract colors for each node in the graph
colors = [node_colors[node] for node in G.nodes()]

# Choose a layout for the nodes
pos = nx.spring_layout(G, seed=123)

# Draw nodes with varying size and assigned color
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=colors, edgecolors='black')

# Draw edges with fixed thickness
nx.draw_networkx_edges(G, pos, width=2, alpha=0.7, edge_color='lightblue')

# Draw labels with careful positioning
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

# Title and layout adjustments
plt.title("Ecosystem of Marine Biodiversity:\nA Web of Life in Coral Reefs", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.axis('off')  # Turn off the axis for clarity

# Display the plot
plt.show()