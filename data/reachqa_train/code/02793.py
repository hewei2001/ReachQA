import matplotlib.pyplot as plt
import networkx as nx

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
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(fashion_styles)
G.add_edges_from(connections)

# Use spring layout for a visually appealing distribution of nodes
pos = nx.spring_layout(G, seed=42)

# Draw the nodes with custom colors and sizes
node_color_map = ['#FFC1CC', '#FFEE93', '#C1E1C1', '#AED1FF', '#FFD1DC']
nx.draw_networkx_nodes(G, pos, node_size=1200, node_color=node_color_map, edgecolors='black', linewidths=1.5)

# Draw the edges with custom styles
edge_styles = [(2, (3, 1)), (1, (5, 2)), (2, (2, 3)), (1, (5, 2)), (2, (3, 1)), (1, (5, 2)), (2, (2, 3))]
edges = nx.draw_networkx_edges(G, pos, width=2, alpha=0.7, edge_color='gray', style='solid')

# Draw the labels on the nodes
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_color='navy')

# Draw legend for the node colors
for style, color in zip(fashion_styles, node_color_map):
    plt.scatter([], [], color=color, edgecolor='black', linewidth=1.5, s=120, label=style)

# Set title for the plot
plt.title("Interconnections of Fashion Styles:\nAn Influential Web", fontsize=16, fontweight='bold', color='purple', pad=20)

# Display the legend
plt.legend(title="Fashion Styles", loc='upper left', bbox_to_anchor=(1, 1), fontsize='small', frameon=True)

# Remove the axis
plt.axis('off')

# Automatically adjust the layout for the elements
plt.tight_layout()

# Display the plot
plt.show()