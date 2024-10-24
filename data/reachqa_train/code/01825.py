import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define cities and connections
cities = ["Metro City", "Harbor Town", "Green Village", "Old Hamlet", "Sunset Bay", "Mountain Peak", "Riverside"]
connections = [
    ("Metro City", "Harbor Town"),
    ("Metro City", "Green Village"),
    ("Harbor Town", "Old Hamlet"),
    ("Old Hamlet", "Sunset Bay"),
    ("Sunset Bay", "Mountain Peak"),
    ("Mountain Peak", "Riverside"),
    ("Riverside", "Green Village"),
    ("Harbor Town", "Sunset Bay"),
    ("Metro City", "Sunset Bay")
]

# Create graph
G = nx.Graph()
G.add_nodes_from(cities)
G.add_edges_from(connections)

# City data for bar chart (Population or tourist numbers as example)
city_data = {
    "Metro City": 1200,
    "Harbor Town": 800,
    "Green Village": 600,
    "Old Hamlet": 400,
    "Sunset Bay": 1100,
    "Mountain Peak": 500,
    "Riverside": 700
}

# Figure setup with two subplots
fig, ax = plt.subplots(1, 2, figsize=(14, 7))

# First subplot for the network graph
pos = nx.spring_layout(G, seed=42)
node_sizes = [800 + 100 * G.degree(city) for city in cities]
nx.draw_networkx_nodes(G, pos, ax=ax[0], node_size=node_sizes, node_color='skyblue', edgecolors='black', linewidths=1.5)
nx.draw_networkx_edges(G, pos, ax=ax[0], width=2, alpha=0.7, edge_color='gray')
nx.draw_networkx_labels(G, pos, ax=ax[0], font_size=9, font_color='darkblue', font_weight='bold')
ax[0].set_title("Translandia's Railway Network:\nConnectivity of Major Cities", fontsize=12, fontweight='bold', pad=15)
ax[0].axis('off')

# Second subplot for the bar chart
cities_sorted = sorted(cities, key=lambda x: city_data[x], reverse=True)
data_sorted = [city_data[city] for city in cities_sorted]
ax[1].bar(cities_sorted, data_sorted, color='orange', alpha=0.7, edgecolor='black')
ax[1].set_title("City Population (Thousands)", fontsize=12, fontweight='bold')
ax[1].set_xlabel("Cities")
ax[1].set_ylabel("Population (in thousands)")
ax[1].set_ylim(0, max(data_sorted) + 200)
ax[1].set_xticklabels(cities_sorted, rotation=45, ha='right')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()