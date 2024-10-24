import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define healthcare sectors as nodes
sectors = [
    "Diagnostics", "Patient Monitoring", "Drug Discovery",
    "Personalized Medicine", "Hospital Management", "Predictive Analytics"
]

# Define directed connections between sectors
connections = [
    ("Diagnostics", "Patient Monitoring"),
    ("Drug Discovery", "Personalized Medicine"),
    ("Personalized Medicine", "Predictive Analytics"),
    ("Hospital Management", "Predictive Analytics"),
    ("Predictive Analytics", "Diagnostics"),
    ("Patient Monitoring", "Hospital Management")
]

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(sectors)
G.add_edges_from(connections)

# Circular layout for nodes
pos = nx.circular_layout(G)

# Node colors
sector_colors = {
    "Diagnostics": "lightcoral", 
    "Patient Monitoring": "lightskyblue", 
    "Drug Discovery": "yellowgreen",
    "Personalized Medicine": "gold", 
    "Hospital Management": "lightpink", 
    "Predictive Analytics": "violet"
}
node_colors = [sector_colors[sector] for sector in G.nodes]

# Edge labels
edge_labels = {
    ("Diagnostics", "Patient Monitoring"): "Tool Sharing",
    ("Drug Discovery", "Personalized Medicine"): "Data Transfer",
    ("Personalized Medicine", "Predictive Analytics"): "Data Modeling",
    ("Hospital Management", "Predictive Analytics"): "Optimization",
    ("Predictive Analytics", "Diagnostics"): "Feedback",
    ("Patient Monitoring", "Hospital Management"): "Efficiency"
}

# Activity levels for additional subplot
activity_levels = [5, 7, 3, 6, 4, 8]  # Example data for "activity levels"

# Create the plot
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Original network plot
axs[0].set_title("AI Applications in Healthcare:\nMapping the Network of Innovations", fontsize=14, fontweight='bold')
nx.draw_networkx_nodes(G, pos, node_size=1600, node_color=node_colors, edgecolors='black', ax=axs[0])
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20, edge_color='gray', width=2, ax=axs[0])
nx.draw_networkx_labels(G, pos, font_size=10, font_family="serif", font_weight='bold', ax=axs[0])
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkblue', font_size=8, label_pos=0.3, ax=axs[0])
axs[0].legend(
    handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=sector)
             for sector, color in sector_colors.items()],
    title='Healthcare Sectors',
    loc='upper left'
)
axs[0].axis('off')

# Additional subplot: Activity Levels Bar Chart
axs[1].barh(sectors, activity_levels, color=[sector_colors[sector] for sector in sectors])
axs[1].set_title("Sector Activity Levels", fontsize=12, fontweight='bold')
axs[1].set_xlabel("Activity Level")
axs[1].set_xlim(0, max(activity_levels) + 2)
axs[1].invert_yaxis()
axs[1].grid(axis='x', linestyle='--', alpha=0.6)

# Adjust layout
plt.tight_layout()
plt.show()