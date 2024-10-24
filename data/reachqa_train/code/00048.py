import matplotlib.pyplot as plt
import networkx as nx

# Define the directed influence data between nodes
influence_data = {
    "Govt. Policies": ["Financial Incentives", "Public Awareness"],
    "Tech. Innovation": ["Environmental Impact", "Govt. Policies"],
    "Financial Incentives": ["Tech. Innovation"],
    "Public Awareness": ["Environmental Impact"],
    "Environmental Impact": ["Govt. Policies"]
}

# Create a directed graph using NetworkX
G = nx.DiGraph(influence_data)

# Set the position layout for the nodes
pos = nx.spring_layout(G, seed=42)

# Draw the nodes
nx.draw_networkx_nodes(G, pos, node_size=2200, node_color='lightblue', node_shape='o')

# Draw the edges with arrowheads indicating direction
nx.draw_networkx_edges(G, pos, edge_color='grey', arrowstyle='-|>', arrowsize=15, connectionstyle='arc3,rad=0.15')

# Draw the labels for nodes
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

# Title with line breaks to fit the layout
plt.title("Dynamics of Renewable\nEnergy Adoption", fontsize=15, weight='bold')

# Automatically adjust layout for a clean visualization
plt.tight_layout()

# Turn off the axis
plt.axis('off')

# Show the plot
plt.show()