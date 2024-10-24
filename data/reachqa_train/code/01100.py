import matplotlib.pyplot as plt
import networkx as nx

# Initialize the directed graph
G = nx.DiGraph()

# Add nodes representing influential users
nodes = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
G.add_nodes_from(nodes)

# Add edges representing the flow of different types of content
edges_news = [('Alice', 'Bob'), ('Bob', 'Charlie'), ('Charlie', 'Eve')]
edges_memes = [('David', 'Alice'), ('Alice', 'Charlie'), ('Charlie', 'Bob'), ('Eve', 'Bob')]
edges_tech_updates = [('Eve', 'David'), ('David', 'Charlie'), ('Charlie', 'Alice')]

G.add_edges_from(edges_news + edges_memes + edges_tech_updates)

# Position nodes using a shell layout for improved readability
pos = nx.shell_layout(G)

# Draw nodes with distinct shapes and colors
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color=['#FFDDC1', '#B5EAD7', '#FF9AA2', '#FFDAC1', '#E2F0CB'], 
                       node_shape='o', edgecolors='black')

# Draw directed edges with different colors and arrows for clarity
nx.draw_networkx_edges(G, pos, edgelist=edges_news, edge_color='red', arrows=True, arrowsize=15, width=2, label='News')
nx.draw_networkx_edges(G, pos, edgelist=edges_memes, edge_color='green', arrows=True, arrowsize=15, width=2, label='Memes')
nx.draw_networkx_edges(G, pos, edgelist=edges_tech_updates, edge_color='blue', arrows=True, arrowsize=15, width=2, label='Tech Updates')

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_color='black')

# Set title with proper formatting to avoid overlap
plt.title("Information Flow in ConnectSphere\nA Hypothetical Social Media Network", fontsize=14, fontweight='bold', pad=20)

# Add a legend to explain edge colors
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False, fontsize=10)

# Remove axes for a cleaner look
plt.axis('off')

# Automatically adjust the plot to prevent overlap and improve layout
plt.tight_layout()

# Show the plot
plt.show()