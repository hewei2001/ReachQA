import matplotlib.pyplot as plt
import networkx as nx

# Define nodes (colonies)
colonies = ['Earth', 'Moon', 'Mars', 'Europa', 'Titan']

# Define cargo routes and volumes
cargo_routes = [
    ('Earth', 'Moon', 50),
    ('Earth', 'Mars', 30),
    ('Earth', 'Europa', 20),
    ('Earth', 'Titan', 10),
    ('Moon', 'Mars', 10),
    ('Moon', 'Europa', 10),
    ('Mars', 'Europa', 40),
    ('Mars', 'Titan', 30),
    ('Europa', 'Titan', 20)
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_nodes_from(colonies)

# Add edges with cargo volumes as weights
for route in cargo_routes:
    G.add_edge(route[0], route[1], weight=route[2])

# Determine edge widths based on cargo volume
edge_widths = [G[u][v]['weight'] / 10 for u, v in G.edges()]

# Plot the directed node chart
plt.figure(figsize=(10, 8))
pos = nx.shell_layout(G)  # Use a shell layout for better readability
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='skyblue', alpha=0.8, edgecolors='k')
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_color='darkblue')

# Draw directed edges with varying widths
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='gray', width=edge_widths, connectionstyle="arc3,rad=0.1")

# Add edge labels for cargo volumes
edge_labels = {(u, v): f"{G[u][v]['weight']} units" for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, font_color='red')

# Add title and display the plot
plt.title('Interplanetary Cargo Routes and Volumes\nAmong Solar Colonies', fontsize=16, weight='bold')
plt.axis('off')

# Automatically adjust the layout to prevent text overlap
plt.tight_layout()

# Show the plot
plt.show()