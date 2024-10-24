import matplotlib.pyplot as plt
import networkx as nx

# Initialize a directed graph
G = nx.DiGraph()

# Define nodes representing different healthcare systems
nodes = [
    ("Patient Records", {"category": "Data Storage"}),
    ("Telemedicine", {"category": "Remote Care"}),
    ("AI Diagnostics", {"category": "Decision Support"}),
    ("Wearable Devices", {"category": "Health Monitoring"}),
    ("Pharmacy Systems", {"category": "Medication Management"}),
    ("Billing System", {"category": "Financial"})
]

# Add nodes to the graph
G.add_nodes_from(nodes)

# Define edges with weights (strength of influence) between systems
edges = [
    ("Patient Records", "AI Diagnostics", 0.7),
    ("Patient Records", "Telemedicine", 0.5),
    ("Wearable Devices", "AI Diagnostics", 0.8),
    ("Telemedicine", "Billing System", 0.6),
    ("Pharmacy Systems", "Billing System", 0.4),
    ("AI Diagnostics", "Telemedicine", 0.3),
    ("Wearable Devices", "Patient Records", 0.6),
    ("AI Diagnostics", "Pharmacy Systems", 0.5)
]

# Add edges to the graph
for u, v, weight in edges:
    G.add_edge(u, v, weight=weight)

# Position nodes using the spring layout for clarity and aesthetics
pos = nx.spring_layout(G, seed=42)

# Define node colors based on category
category_colors = {
    "Data Storage": "#1f77b4",
    "Remote Care": "#ff7f0e",
    "Decision Support": "#2ca02c",
    "Health Monitoring": "#d62728",
    "Medication Management": "#9467bd",
    "Financial": "#8c564b"
}

node_colors = [category_colors[G.nodes[node]["category"]] for node in G.nodes]

# Draw the directed graph
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color=node_colors, alpha=0.9)
nx.draw_networkx_labels(G, pos, font_size=10, font_color="white")
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20, edge_color='gray', alpha=0.6)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{d["weight"]:.1f}' for u, v, d in G.edges(data=True)}, font_size=9)

# Create a custom legend
handles = [plt.Line2D([0], [0], marker='o', color='w', label=cat, markersize=10, markerfacecolor=col, alpha=0.9)
           for cat, col in category_colors.items()]
plt.legend(handles=handles, title='System Category', loc='upper left', bbox_to_anchor=(1, 1))

# Title and layout adjustments
plt.title("Digital Transformation in Healthcare:\nInterconnected Systems and Their Influences", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.axis('off')

# Display the plot
plt.show()