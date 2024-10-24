import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define the nodes
sources = ['Residential', 'Commercial', 'Industrial']
waste_types = ['Organic', 'Recyclables', 'Non-recyclables']
destinations = ['Compost', 'Recycling Center', 'Landfill']

# Combine all nodes
nodes = sources + waste_types + destinations

# Define the directed edges with weights
edges = [
    ('Residential', 'Organic', 0.3),
    ('Residential', 'Recyclables', 0.5),
    ('Residential', 'Non-recyclables', 0.2),
    ('Commercial', 'Organic', 0.1),
    ('Commercial', 'Recyclables', 0.6),
    ('Commercial', 'Non-recyclables', 0.3),
    ('Industrial', 'Organic', 0.05),
    ('Industrial', 'Recyclables', 0.7),
    ('Industrial', 'Non-recyclables', 0.25),
    ('Organic', 'Compost', 0.9),
    ('Recyclables', 'Recycling Center', 1.0),
    ('Non-recyclables', 'Landfill', 1.0),
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
for source, target, weight in edges:
    G.add_edge(source, target, weight=weight)

# Data for the new subplot (stacked bar chart)
waste_data = {
    'Residential': [30, 50, 20],
    'Commercial': [10, 60, 30],
    'Industrial': [5, 70, 25]
}

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 8))

# First subplot: Directed flow network
pos = nx.shell_layout(G, nlist=[sources, waste_types, destinations])
nx.draw(G, pos, ax=axs[0], with_labels=True, node_size=3000, node_color="lightgreen",
        edge_color="gray", linewidths=1, font_size=10, arrows=True,
        arrowsize=20, arrowstyle='->')

edge_labels = {(u, v): f"{d['weight']*100:.0f}%" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, ax=axs[0])

axs[0].set_title("Flow of Waste Materials\nin EcoVille's Urban Waste Management System",
                 fontsize=14, fontweight='bold', pad=15)

# Second subplot: Stacked bar chart
x = np.arange(len(sources))
bar_width = 0.6

# Stack values
y_organic, y_recyclables, y_non_recyclables = [waste_data[source] for source in sources]
axs[1].bar(x, y_organic, bar_width, label='Organic', color='green')
axs[1].bar(x, y_recyclables, bar_width, bottom=y_organic, label='Recyclables', color='blue')
axs[1].bar(x, y_non_recyclables, bar_width, bottom=np.array(y_organic) + np.array(y_recyclables),
           label='Non-recyclables', color='red')

axs[1].set_xlabel('Source Types', fontsize=12)
axs[1].set_ylabel('Percentage of Waste (%)', fontsize=12)
axs[1].set_xticks(x)
axs[1].set_xticklabels(sources, fontsize=10)
axs[1].legend(title='Waste Types')
axs[1].set_title('Waste Composition by Source', fontsize=14, fontweight='bold', pad=15)

plt.tight_layout()

# Show the plots
plt.show()