import matplotlib.pyplot as plt
import networkx as nx

# Define philosophical schools of thought and connections
philosophies = [
    'Stoicism', 'Epicureanism', 'Existentialism', 'Nihilism', 'Absurdism',
    'Rationalism', 'Empiricism', 'Pragmatism', 'Idealism', 'Materialism'
]

# Define connections representing influences or shared concepts
connections = [
    ('Stoicism', 'Rationalism'), 
    ('Epicureanism', 'Materialism'), 
    ('Existentialism', 'Nihilism'),
    ('Existentialism', 'Absurdism'), 
    ('Nihilism', 'Absurdism'), 
    ('Rationalism', 'Empiricism'), 
    ('Empiricism', 'Pragmatism'), 
    ('Idealism', 'Rationalism'),
    ('Materialism', 'Empiricism')
]

# Create a graph using NetworkX
G = nx.Graph()
G.add_nodes_from(philosophies)
G.add_edges_from(connections)

# Define position layout for nodes using a circular layout for better clarity
pos = nx.circular_layout(G)

# Create node colors based on philosophy categories (arbitrarily chosen for aesthetics)
node_colors = ['#FFCCCB', '#FFB6C1', '#FFD700', '#ADFF2F', '#FF69B4',
               '#6495ED', '#40E0D0', '#FFA07A', '#98FB98', '#DA70D6']

# Start plotting the network graph
plt.figure(figsize=(12, 8))

# Draw nodes with specific colors and edge borders
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color=node_colors, edgecolors='black')

# Draw edges with varying transparency to highlight connections
nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color='gray', style='solid')

# Draw labels for nodes, ensuring they're easily readable
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_color='darkslategray')

# Add the title, adjusting text wrap to ensure readability
plt.title("Web of Wisdom:\nExploring Connections in Philosophy", fontsize=16, fontweight='bold', pad=20)

# Turn off the axis for a cleaner look
plt.axis('off')

# Automatically adjust the layout to prevent overlap and ensure clarity
plt.tight_layout()

# Display the chart
plt.show()