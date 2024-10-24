import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define the nodes with guild affiliations
nodes = [
    "Arthur (Blacksmith)", "Beatrice (Blacksmith)", "Cedric (Blacksmith)",
    "Diana (Baker)", "Eleanor (Baker)", "Frederick (Baker)",
    "Giselle (Tailor)", "Harold (Tailor)", "Isolde (Tailor)"
]

# Define the edges with weights (representing trade interactions)
edges = [
    ("Arthur (Blacksmith)", "Diana (Baker)", 3), 
    ("Arthur (Blacksmith)", "Giselle (Tailor)", 2),
    ("Beatrice (Blacksmith)", "Eleanor (Baker)", 3), 
    ("Beatrice (Blacksmith)", "Harold (Tailor)", 2),
    ("Cedric (Blacksmith)", "Frederick (Baker)", 3), 
    ("Cedric (Blacksmith)", "Isolde (Tailor)", 2),
    ("Diana (Baker)", "Harold (Tailor)", 1), 
    ("Eleanor (Baker)", "Isolde (Tailor)", 2),
    ("Frederick (Baker)", "Giselle (Tailor)", 1),
    ("Arthur (Blacksmith)", "Beatrice (Blacksmith)", 2),
    ("Giselle (Tailor)", "Harold (Tailor)", 3),
    ("Diana (Baker)", "Eleanor (Baker)", 2)
]

# Additional data for scatter plot: economic value of trade
economic_values = [
    100, 150, 130, 110, 120, 160, 140, 90, 105, 115, 135, 125
]

# Create the graph
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

# Plotting the graph
plt.figure(figsize=(14, 12))
pos = nx.spring_layout(G, seed=42)

# Node colors based on guild affiliations
guild_colors = {"Blacksmith": "gold", "Baker": "wheat", "Tailor": "orchid"}
node_colors = [guild_colors[guild.split()[1][1:-1]] for guild in G.nodes]

# Node sizes based on degree
node_sizes = [600 + 100 * G.degree(node) for node in G.nodes]

# Draw network graph
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black')
nx.draw_networkx_edges(G, pos, width=[0.8 * G[u][v]['weight'] for u, v in G.edges], alpha=0.7, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=9, font_family="serif", font_weight='bold')

# Add scatter plot overlay with economic values
scatter_x = np.array([pos[node][0] for node in G.nodes])
scatter_y = np.array([pos[node][1] for node in G.nodes])
plt.scatter(scatter_x, scatter_y, s=np.array(economic_values)[:len(scatter_x)], c='skyblue', alpha=0.5, label='Trade Value (size)')

# Legend for node colors
legend_handles = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=guild)
    for guild, color in guild_colors.items()
]
plt.legend(handles=legend_handles + [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='skyblue', markersize=10, label='Trade Value')],
           title='Legend', loc='upper left', bbox_to_anchor=(1, 1))

# Title and subtitles
plt.title("Interwoven Guild Networks in Medieval Elmsworth\nwith Economic Trade Values", fontsize=14, fontweight='bold')

# Remove axes
plt.axis('off')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()