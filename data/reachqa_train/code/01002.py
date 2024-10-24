import matplotlib.pyplot as plt
import networkx as nx

# Define the nodes (guild members) with their guild affiliations
nodes = [
    "Arthur (Blacksmith)", "Beatrice (Blacksmith)", "Cedric (Blacksmith)",
    "Diana (Baker)", "Eleanor (Baker)", "Frederick (Baker)",
    "Giselle (Tailor)", "Harold (Tailor)", "Isolde (Tailor)"
]

# Define the edges (trade interactions) with weights
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

# Create the undirected graph with weights
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

# Plotting the graph
plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G, seed=42)

# Node colors based on guild affiliations
node_colors = []
guild_colors = {"Blacksmith": "gold", "Baker": "wheat", "Tailor": "orchid"}
for node in G.nodes:
    for guild, color in guild_colors.items():
        if guild in node:
            node_colors.append(color)
            break

# Node size based on degree
node_sizes = [600 + 100 * G.degree(node) for node in G.nodes]

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black')

# Draw edges with varying thickness based on weight
weights = nx.get_edge_attributes(G, 'weight').values()
nx.draw_networkx_edges(G, pos, width=[w * 0.8 for w in weights], alpha=0.7, edge_color='gray')

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=9, font_family="serif", font_weight='bold')

# Legend for node colors
legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=guild)
                  for guild, color in guild_colors.items()]

plt.legend(handles=legend_handles, title='Guild', loc='upper left', bbox_to_anchor=(1, 1))

# Title
plt.title("Interwoven Guild Networks in Medieval Elmsworth:\nA Cooperative Legacy", fontsize=14, fontweight='bold')

# Remove axes
plt.axis('off')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()