import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define the nodes (sustainable cities)
nodes = [
    "Copenhagen", "San Francisco", "Singapore", 
    "Amsterdam", "Stockholm", "Vancouver", "Melbourne"
]

# Renewable energy usage percentages for each city
renewable_energy_usage = {
    "Copenhagen": 85,
    "San Francisco": 75,
    "Singapore": 50,
    "Amsterdam": 70,
    "Stockholm": 90,
    "Vancouver": 65,
    "Melbourne": 60
}

# Define the edges (connections) with weights
edges = [
    ("Copenhagen", "Amsterdam", 8),
    ("Copenhagen", "Stockholm", 7),
    ("San Francisco", "Singapore", 6),
    ("San Francisco", "Melbourne", 5),
    ("Singapore", "Amsterdam", 7),
    ("Amsterdam", "Vancouver", 6),
    ("Stockholm", "Vancouver", 5),
    ("Vancouver", "Melbourne", 4),
    ("Copenhagen", "Vancouver", 6)
]

# Create the undirected graph
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

plt.figure(figsize=(16, 10))

# Position for network plot
ax1 = plt.subplot(121)
pos = nx.spring_layout(G, seed=24)  

# Assign colors to each node based on sustainability focus
sustainability_colors = {
    "Copenhagen": "seagreen",
    "San Francisco": "royalblue",
    "Singapore": "darkorange",
    "Amsterdam": "lightcoral",
    "Stockholm": "mediumorchid",
    "Vancouver": "gold",
    "Melbourne": "turquoise"
}
node_colors = [sustainability_colors[node] for node in G.nodes]

# Calculate node size based on degree centrality
centrality = nx.degree_centrality(G)
node_sizes = [3000 * centrality[node] for node in G.nodes]

# Draw the nodes
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black', linewidths=1.5, ax=ax1)

# Draw the edges with thickness based on weight
weights = nx.get_edge_attributes(G, 'weight').values()
nx.draw_networkx_edges(G, pos, width=[w * 0.8 for w in weights], alpha=0.7, edge_color='gray', ax=ax1)

# Draw the node labels
nx.draw_networkx_labels(G, pos, font_size=11, font_family="sans-serif", font_weight='bold', ax=ax1)

# Create a custom legend for node colors
legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=city)
                  for city, color in sustainability_colors.items()]

ax1.legend(handles=legend_handles, title='Sustainable Cities', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Title of the network graph
ax1.set_title("Network of Sustainable Cities:\nUrban Resilience Hubs", fontsize=14, fontweight='bold')

# Remove the axes
ax1.axis('off')

# Position for the bar chart
ax2 = plt.subplot(122)

# Extract cities and usage data
cities = list(renewable_energy_usage.keys())
usage = list(renewable_energy_usage.values())

# Create the bar chart
ax2.barh(cities, usage, color=[sustainability_colors[city] for city in cities])
ax2.set_xlim(0, 100)
ax2.set_xlabel('Renewable Energy Usage (%)')
ax2.set_title('Renewable Energy Usage by City', fontsize=12)

# Optimize layout to ensure everything fits
plt.tight_layout()

# Show the plot
plt.show()