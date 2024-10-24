import matplotlib.pyplot as plt
import networkx as nx

# Define cities and connections (with some added details for visual diversity)
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
    ("Metro City", "Sunset Bay")  # Added an additional connection for complexity
]

# Create graph and add nodes and edges
G = nx.Graph()
G.add_nodes_from(cities)
G.add_edges_from(connections)

# Position nodes using the spring layout for natural spacing
pos = nx.spring_layout(G, seed=42)  # Fixed seed for reproducibility

# Determine node sizes based on degree (number of connections)
node_sizes = [800 + 100 * G.degree(city) for city in cities]

# Draw the nodes with varying sizes
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='skyblue', edgecolors='black', linewidths=1.5)

# Draw the edges with thickness proportional to their importance
nx.draw_networkx_edges(G, pos, width=2, alpha=0.7, edge_color='gray', style='solid')

# Add labels to the nodes
nx.draw_networkx_labels(G, pos, font_size=9, font_color='darkblue', font_weight='bold')

# Customizing plot aesthetics
plt.title("Translandia's Railway Network:\nConnectivity of Major Cities", fontsize=14, fontweight='bold', pad=20)

# Remove axes
plt.axis('off')

# Ensure layout is adjusted to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()