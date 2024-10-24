import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Original directed graph data
sources = ['Solar', 'Wind', 'Hydroelectric']
sectors = ['Residential', 'Commercial', 'Industrial']
edges = [
    ('Solar', 'Residential', 30),
    ('Solar', 'Commercial', 20),
    ('Wind', 'Commercial', 25),
    ('Wind', 'Industrial', 40),
    ('Hydroelectric', 'Residential', 40),
    ('Hydroelectric', 'Industrial', 30)
]

# Additional data for bar chart (e.g., historical percentage contribution)
years = ['2020', '2021', '2022']
historical_data = {
    'Solar': [25, 30, 35],
    'Wind': [20, 25, 30],
    'Hydroelectric': [35, 40, 38]
}

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(sources, type='source')
G.add_nodes_from(sectors, type='sector')
G.add_weighted_edges_from(edges)

# Define positions using shell layout
pos = nx.shell_layout(G, nlist=[sources, sectors])

# Create subplots: original directed graph and additional bar chart
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Plotting the directed graph
nx.draw_networkx_nodes(G, pos, nodelist=sources, node_size=1500, node_color='skyblue', ax=axes[0])
nx.draw_networkx_nodes(G, pos, nodelist=sectors, node_size=1500, node_color='lightgreen', ax=axes[0])
nx.draw_networkx_labels(G, pos, font_size=11, font_weight='bold', ax=axes[0])
edge_labels = {(u, v): f"{d['weight']}%" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='-|>', arrowsize=15, edge_color='gray', width=2, ax=axes[0])
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=9, ax=axes[0])

# Title for the directed graph
axes[0].set_title("Energy Flow from Sources to Sectors\nin EcoMetropolis", fontsize=14, fontweight='bold')

# Plotting the bar chart for historical data
bar_width = 0.25
x_indices = np.arange(len(years))

# Plot each source's contribution over the years
for idx, source in enumerate(sources):
    axes[1].bar(x_indices + idx * bar_width, historical_data[source], bar_width, label=source)

# Customizing the bar chart
axes[1].set_title("Historical Energy Contributions", fontsize=14, fontweight='bold')
axes[1].set_xlabel("Year", fontsize=12)
axes[1].set_ylabel("Contribution (%)", fontsize=12)
axes[1].set_xticks(x_indices + bar_width)
axes[1].set_xticklabels(years)
axes[1].legend(title="Energy Source", fontsize=10)
axes[1].grid(axis='y', linestyle='--', alpha=0.7)

# Enhance layout and display
plt.tight_layout(pad=3.0)
plt.show()