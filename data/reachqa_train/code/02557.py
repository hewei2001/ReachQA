import matplotlib.pyplot as plt
import networkx as nx

# Define the nodes (social media platforms)
platforms = ["Facebook", "Twitter", "Instagram", "TikTok", "LinkedIn", "YouTube"]

# Define directed edges representing influence
influence_edges = [
    ("Facebook", "Instagram"),
    ("Facebook", "TikTok"),
    ("Twitter", "TikTok"),
    ("Twitter", "LinkedIn"),
    ("Instagram", "TikTok"),
    ("TikTok", "YouTube"),
    ("LinkedIn", "Facebook"),
    ("YouTube", "Facebook"),
    ("YouTube", "Twitter"),
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
G.add_nodes_from(platforms)
G.add_edges_from(influence_edges)

# Define positions for each node using a spring layout for improved readability
pos = nx.spring_layout(G, seed=42)

# Create the plot
plt.figure(figsize=(14, 10))

# Draw the nodes with distinct colors for better visualization
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color=['lightblue', 'lightgreen', 'lightcoral', 'lightpink', 'lightgray', 'lightyellow'])

# Draw the edges with arrows indicating direction of influence
nx.draw_networkx_edges(G, pos, edgelist=influence_edges, edge_color='gray', arrows=True, arrowsize=20)

# Draw the labels with enhanced font properties
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_family='sans-serif', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

# Set the title of the plot
plt.title("Web of Connectivity: \nMapping Digital Influence Among Global Social Media Platforms", fontsize=16, fontweight='bold')

# Turn off the axis
plt.axis('off')

# Optimize the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()