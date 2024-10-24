import matplotlib.pyplot as plt
import networkx as nx

# Define the energy flow connections between nodes
energy_flow_data = {
    "WF1": ["CityA", "HE1"],
    "WF2": ["CityB", "SP1"],
    "SP1": ["CityC"],
    "SP2": ["CityA", "HE2"],
    "HE1": ["CityB"],
    "HE2": ["CityC"],
    "CityA": [],
    "CityB": [],
    "CityC": []
}

# Create an undirected graph using NetworkX
G = nx.Graph(energy_flow_data)

# Define node attributes
node_attributes = {
    "WF1": {"color": "lightblue", "shape": "o", "size": 3000, "label": "Wind Farm 1"},
    "WF2": {"color": "lightblue", "shape": "o", "size": 3000, "label": "Wind Farm 2"},
    "SP1": {"color": "orange", "shape": "s", "size": 2500, "label": "Solar Plant 1"},
    "SP2": {"color": "orange", "shape": "s", "size": 2500, "label": "Solar Plant 2"},
    "HE1": {"color": "skyblue", "shape": "p", "size": 2700, "label": "Hydro Station 1"},
    "HE2": {"color": "skyblue", "shape": "p", "size": 2700, "label": "Hydro Station 2"},
    "CityA": {"color": "darkgreen", "shape": "h", "size": 3500, "label": "City A"},
    "CityB": {"color": "darkgreen", "shape": "h", "size": 3500, "label": "City B"},
    "CityC": {"color": "darkgreen", "shape": "h", "size": 3500, "label": "City C"},
}

# Set the position layout for the nodes using a circular layout for clarity
pos = nx.circular_layout(G)

# Draw nodes with specific attributes
for node, attr in node_attributes.items():
    nx.draw_networkx_nodes(G, pos, nodelist=[node], node_size=attr["size"],
                           node_color=attr["color"], node_shape=attr["shape"])

# Draw the edges with customized styles
nx.draw_networkx_edges(G, pos, width=2, style='solid', edge_color='gray', alpha=0.7)

# Draw the labels for nodes
nx.draw_networkx_labels(G, pos, labels={node: attr["label"] for node, attr in node_attributes.items()},
                        font_size=9, font_family="sans-serif", font_weight="bold")

# Set the title with line breaks for better visibility
plt.title("Renewable Energy Flow Network\nin the Cities of Neravia", fontsize=14, weight='bold')

# Automatically adjust layout for a clean visualization
plt.tight_layout()

# Add legend manually for node colors and shapes
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', label='Wind Farms', markerfacecolor='lightblue', markersize=10),
    plt.Line2D([0], [0], marker='s', color='w', label='Solar Plants', markerfacecolor='orange', markersize=10),
    plt.Line2D([0], [0], marker='p', color='w', label='Hydro Stations', markerfacecolor='skyblue', markersize=10),
    plt.Line2D([0], [0], marker='h', color='w', label='Cities', markerfacecolor='darkgreen', markersize=10),
]

plt.legend(handles=legend_elements, loc='upper right', fontsize=8, title="Node Types")

# Turn off the axis
plt.axis('off')

# Show the plot
plt.show()