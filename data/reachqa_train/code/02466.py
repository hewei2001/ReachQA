import matplotlib.pyplot as plt
import networkx as nx

# Define planets (nodes) in the galaxy
planets = ['Terra Nova', 'Zargon Prime', 'Arcanis IV', 'Lunarus', 'Oberon']

# Define trade routes (directed edges) with trade volumes
trade_routes = [
    ('Terra Nova', 'Zargon Prime', 500),
    ('Terra Nova', 'Arcanis IV', 300),
    ('Zargon Prime', 'Lunarus', 400),
    ('Lunarus', 'Oberon', 600),
    ('Arcanis IV', 'Terra Nova', 200),
    ('Oberon', 'Terra Nova', 350),
    ('Oberon', 'Arcanis IV', 250)
]

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(planets)

# Add edges with weights
for source, dest, volume in trade_routes:
    G.add_edge(source, dest, weight=volume)

# Compute total trade volume per planet (in and out)
trade_volumes = {planet: sum(d['weight'] for u, v, d in G.edges(planet, data=True)) + 
                             sum(d['weight'] for u, v, d in G.in_edges(planet, data=True)) for planet in planets}

# Assign node sizes based on total trade volume
node_sizes = [1500 + trade_volumes[planet]*2 for planet in planets]

# Define positions using a circular layout
pos = nx.circular_layout(G)

# Extract weights for edge labels and widths
edge_labels = {(u, v): f'{d["weight"]} tons' for u, v, d in G.edges(data=True)}
edge_widths = [1 + G[u][v]['weight'] / 100 for u, v in G.edges()]

# Define color maps for nodes and edges
node_colors = ['#FFD700', '#ADFF2F', '#1E90FF', '#FF69B4', '#BA55D3']

# Draw the directed graph
plt.figure(figsize=(12, 10))
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9, edgecolors='black')
nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color='gray', arrows=True, arrowsize=15, width=edge_widths)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# Add edge labels with an offset to prevent overlap
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, label_pos=0.3, bbox=dict(facecolor='white', alpha=0.7))

# Title and layout adjustments
plt.title('Galactic Trade Routes in the Year 3025:\nAn Economic Nexus', fontsize=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()

# Create a custom legend
legend_lines = [plt.Line2D([0], [0], color=node_colors[i], lw=4) for i in range(len(planets))]
plt.legend(legend_lines, planets, title="Planets", loc='upper right', bbox_to_anchor=(1.2, 1))

# Display the plot
plt.show()