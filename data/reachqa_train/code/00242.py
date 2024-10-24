import matplotlib.pyplot as plt
import networkx as nx

# Define the names of the nodes (creatures)
nodes = ['Elves', 'Dwarves', 'Fairies', 'Trolls', 'Dragons']

# Define edges based on the connectivity matrix
edges = [('Elves', 'Fairies'), 
         ('Elves', 'Dragons'), 
         ('Fairies', 'Dragons'), 
         ('Dwarves', 'Trolls'), 
         ('Dwarves', 'Dragons'), 
         ('Trolls', 'Dragons')]

# Create a graph object using NetworkX
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Define a layout for the nodes
pos = nx.spring_layout(G, seed=42)  # Fixed seed for consistent layout

# Draw the nodes with custom styling
node_sizes = [len(G.edges(n)) * 2000 for n in G.nodes()]  # Size nodes based on degree
node_colors = ['lightblue', 'lightcoral', 'palegreen', 'wheat', 'violet']  # Distinct colors for visibility

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black')
nx.draw_networkx_edges(G, pos, edgelist=edges, width=2.5, alpha=0.6, edge_color='darkcyan')
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif', font_weight='bold')

# Customize edge thickness based on relationship importance
edge_labels = {
    ('Elves', 'Fairies'): 'Friendship',
    ('Elves', 'Dragons'): 'Alliance',
    ('Fairies', 'Dragons'): 'Trade',
    ('Dwarves', 'Trolls'): 'Rivalry',
    ('Dwarves', 'Dragons'): 'Trade',
    ('Trolls', 'Dragons'): 'Alliance'
}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkred', font_size=8)

# Adding a title and customizing the plot
plt.title("The Realm of Fantasy:\nConnections in Enchanted Forest", fontsize=16, color='darkgreen', pad=20)
plt.axis('off')  # Turn off the axis

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()