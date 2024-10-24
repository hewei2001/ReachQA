import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Create a directed graph
G = nx.DiGraph()

# Define nodes (cities)
cities = ['Xi\'an', 'Samarkand', 'Baghdad', 'Constantinople', 'Venice']

# Add nodes to the graph
G.add_nodes_from(cities)

# Define edges with commodities
trade_routes = [
    ('Xi\'an', 'Samarkand', 'Silk'),
    ('Samarkand', 'Baghdad', 'Spices'),
    ('Baghdad', 'Constantinople', 'Gold'),
    ('Constantinople', 'Venice', 'Textiles'),
    ('Venice', 'Xi\'an', 'Porcelain')
]

# Add edges with labels (commodities)
for start, end, commodity in trade_routes:
    G.add_edge(start, end, commodity=commodity)

# Define the layout for the graph
pos = nx.shell_layout(G)

# Create the subplot layout (1 row, 2 columns)
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Plot 1: Directed graph of the Silk Road network
axes[0].set_title('The Silk Road Network:\nA Journey of Cultural Exchange and Trade', fontsize=14, fontweight='bold')
nx.draw_networkx_nodes(G, pos, ax=axes[0], node_size=2500, node_color='skyblue', alpha=0.9, node_shape='o')
nx.draw_networkx_edges(G, pos, ax=axes[0], edgelist=G.edges, arrowstyle='-|>', arrowsize=20, edge_color='gray', width=2)
nx.draw_networkx_labels(G, pos, ax=axes[0], font_size=12, font_family='sans-serif', font_weight='bold')
edge_labels = {(start, end): f'{G.edges[start, end]["commodity"]}' for start, end in G.edges}
nx.draw_networkx_edge_labels(G, pos, ax=axes[0], edge_labels=edge_labels, font_color='darkred', font_size=10)
axes[0].axis('off')

# Plot 2: Historical trade volume line chart
# Example constructed data for demonstration
years = np.arange(1000, 1500, 100)
silk_trade = [500, 550, 600, 580, 620]
spices_trade = [300, 350, 400, 420, 480]
gold_trade = [200, 250, 230, 260, 270]

axes[1].set_title('Trade Volume over Time (1000-1500)', fontsize=14, fontweight='bold')
axes[1].plot(years, silk_trade, label='Silk', color='cyan', marker='o')
axes[1].plot(years, spices_trade, label='Spices', color='orange', marker='s')
axes[1].plot(years, gold_trade, label='Gold', color='gold', marker='^')

axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Trade Volume (arbitrary units)', fontsize=12)
axes[1].legend(title='Commodities')
axes[1].grid(True)

# Automatically adjust the layout
plt.tight_layout()

# Show the plots
plt.show()