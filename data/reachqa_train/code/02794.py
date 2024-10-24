import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define the fashion styles as nodes
fashion_styles = ['Contemporary', 'Vintage', 'Streetwear', 'Haute Couture', 'Bohemian']

# Define the connections (edges) between fashion styles
connections = [
    ('Contemporary', 'Streetwear'),
    ('Contemporary', 'Haute Couture'),
    ('Vintage', 'Contemporary'),
    ('Vintage', 'Bohemian'),
    ('Streetwear', 'Bohemian'),
    ('Haute Couture', 'Vintage'),
    ('Bohemian', 'Contemporary')
]

# Create a Graph object
G = nx.DiGraph()  # Using DiGraph for directed edges

# Add nodes and edges to the graph
G.add_nodes_from(fashion_styles)
G.add_edges_from(connections)

# Use shell layout for a visually different distribution of nodes
pos = nx.shell_layout(G)

# Define node attributes
node_size_map = [1400, 1000, 1300, 1600, 1100]
node_color_map = ['#FFC1CC', '#FFEE93', '#C1E1C1', '#AED1FF', '#FFD1DC']

# Draw nodes with gradients by using edgecolors
nx.draw_networkx_nodes(G, pos, node_size=node_size_map, node_color=node_color_map, 
                       edgecolors='black', linewidths=2, alpha=0.9)

# Define edge attributes with varying styles
edge_styles = [('solid', 'gray', 2), ('dotted', 'blue', 2.5), ('dashed', 'purple', 3),
               ('solid', 'orange', 1.5), ('dotted', 'red', 2), ('dashed', 'green', 2.5),
               ('solid', 'brown', 3)]

# Draw directed edges with different styles and colors
for (style, color, width), (src, dst) in zip(edge_styles, connections):
    nx.draw_networkx_edges(G, pos, edgelist=[(src, dst)], style=style, edge_color=color, 
                           width=width, alpha=0.7, arrowstyle='-|>', arrowsize=15)

# Draw labels for nodes
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_color='navy')

# Add title with formatting
plt.title("Interconnections of Fashion Styles\nA Multifaceted Network", fontsize=16, fontweight='bold', 
          color='purple', pad=20)

# Add legend for node colors with proper layout adjustment
for style, color in zip(fashion_styles, node_color_map):
    plt.scatter([], [], color=color, edgecolor='black', linewidth=1.5, s=120, label=style)

plt.legend(title="Fashion Styles", loc='upper right', bbox_to_anchor=(1.3, 1), fontsize='small', frameon=True)

# Automatically adjust the layout for all elements
plt.tight_layout()

# Remove the axis for clean look
plt.axis('off')

# Display the optimized plot
plt.show()