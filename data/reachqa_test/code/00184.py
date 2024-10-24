import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define nodes representing IoT devices with initial positions
devices = {
    'Smart Thermostat': (0, 2),
    'Security Camera': (-2, 1),
    'Smart Light': (2, 1),
    'Voice Assistant': (0, 0),
    'Smart Refrigerator': (-2, -1),
    'Energy Meter': (2, -1)
}

# Define directed edges representing data flow/interactions
interactions = [
    ('Smart Thermostat', 'Smart Light'),
    ('Smart Thermostat', 'Energy Meter'),
    ('Security Camera', 'Voice Assistant'),
    ('Smart Refrigerator', 'Energy Meter'),
    ('Voice Assistant', 'Smart Thermostat'),
    ('Voice Assistant', 'Smart Light')
]

# Data usage in MB for each device
data_usage = {
    'Smart Thermostat': 150,
    'Security Camera': 200,
    'Smart Light': 90,
    'Voice Assistant': 120,
    'Smart Refrigerator': 180,
    'Energy Meter': 140
}

# Initialize a directed graph
G = nx.DiGraph()
G.add_nodes_from(devices.keys())
G.add_edges_from(interactions)

# Use spring layout to position nodes for readability
pos = nx.spring_layout(G, pos=devices, fixed=devices.keys(), seed=100)

# Create a figure with two subplots side by side
fig, ax = plt.subplots(1, 2, figsize=(18, 8))

# Plotting the directed graph
nx.draw_networkx_nodes(G, pos, ax=ax[0], node_size=3000, node_color='lightblue', edgecolors='black', linewidths=1.5)
nx.draw_networkx_edges(G, pos, ax=ax[0], arrowstyle='-|>', arrowsize=15, edge_color='grey', style='dashed')
nx.draw_networkx_labels(G, pos, ax=ax[0], font_size=10, font_color='black', font_weight='bold')
ax[0].set_title('Smart Home IoT Ecosystem:\nDirected Interaction Network', fontsize=14, weight='bold')
ax[0].axis('off')

# Plotting the bar chart for data usage
device_names = list(data_usage.keys())
usage_values = list(data_usage.values())
ax[1].barh(device_names, usage_values, color='lightcoral', edgecolor='black')
ax[1].set_xlabel('Data Usage (MB)', fontsize=12)
ax[1].set_title('Device Data Usage in IoT Network', fontsize=14, weight='bold')
ax[1].invert_yaxis()  # Invert y-axis for better readability

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()