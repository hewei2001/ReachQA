import matplotlib.pyplot as plt
import networkx as nx

# List of mythical creatures and artifacts
nodes = [
    'Dragon', 'Phoenix', 'Unicorn', 'Griffin', 'Mermaid',
    'Sword of Light', 'Phoenix Feather', 'Unicorn Horn', 
    'Griffin Claw', 'Mermaid Scale'
]

# Connections between creatures and artifacts
edges = [
    ('Dragon', 'Sword of Light'),
    ('Dragon', 'Griffin Claw'),
    ('Phoenix', 'Phoenix Feather'),
    ('Phoenix', 'Sword of Light'),
    ('Unicorn', 'Unicorn Horn'),
    ('Griffin', 'Griffin Claw'),
    ('Mermaid', 'Mermaid Scale'),
    ('Mermaid', 'Unicorn Horn'),
    ('Phoenix', 'Mermaid Scale')
]

# Create an undirected graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Define node colors based on their type (creature or artifact)
node_colors = ['skyblue' if ' ' not in node else 'lightgreen' for node in nodes]

# Use spring layout for positioning nodes
pos = nx.spring_layout(G, seed=42)

# Create the plot
plt.figure(figsize=(10, 8))

# Draw nodes with customized colors and sizes
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color=node_colors, edgecolors='black', linewidths=1.5)

# Draw edges with varying style for mythical and artifact links
nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color='darkgrey')

# Draw labels with font size
nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')

# Add a title to the plot
plt.title('Connections in the Enchanted Realms:\nMythical Creatures and Artifacts', fontsize=14, fontweight='bold', pad=20)

# Turn off axes
plt.axis('off')

# Use tight layout for better fitting
plt.tight_layout()

# Display the plot
plt.show()