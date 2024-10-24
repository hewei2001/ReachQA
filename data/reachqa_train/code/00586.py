import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as mpatches

# Define nodes and edges
nodes = [
    'Modernism', 'Brutalism', 'Deconstructivism',
    'Frank Lloyd Wright', 'Le Corbusier', 'Zaha Hadid', 'Rem Koolhaas'
]

edges = [
    ('Modernism', 'Brutalism'),
    ('Modernism', 'Deconstructivism'),
    ('Frank Lloyd Wright', 'Modernism'),
    ('Le Corbusier', 'Modernism'),
    ('Le Corbusier', 'Brutalism'),
    ('Zaha Hadid', 'Deconstructivism'),
    ('Rem Koolhaas', 'Deconstructivism')
]

# Create a graph
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Positions for nodes
pos = nx.spring_layout(G, seed=42)

# Node color and size configuration
node_colors = {
    'Modernism': '#FF7F0E',
    'Brutalism': '#1F77B4',
    'Deconstructivism': '#2CA02C',
    'Frank Lloyd Wright': '#D62728',
    'Le Corbusier': '#9467BD',
    'Zaha Hadid': '#8C564B',
    'Rem Koolhaas': '#E377C2'
}
node_sizes = {
    'Modernism': 1500,
    'Brutalism': 1200,
    'Deconstructivism': 1200,
    'Frank Lloyd Wright': 1000,
    'Le Corbusier': 1000,
    'Zaha Hadid': 1000,
    'Rem Koolhaas': 1000
}
node_shapes = {
    'Modernism': 'o',
    'Brutalism': 's',
    'Deconstructivism': 'v',
    'Frank Lloyd Wright': 'p',
    'Le Corbusier': 'h',
    'Zaha Hadid': 'D',
    'Rem Koolhaas': '^'
}

# Draw nodes with distinct shapes
for node in G.nodes():
    nx.draw_networkx_nodes(
        G, pos,
        nodelist=[node],
        node_size=node_sizes[node],
        node_color=node_colors[node],
        edgecolors='black',
        node_shape=node_shapes[node]
    )

# Draw edges with varying styles
edge_styles = {
    ('Modernism', 'Brutalism'): 'solid',
    ('Modernism', 'Deconstructivism'): 'dashed',
    ('Modernism', 'Frank Lloyd Wright'): 'dotted',
    ('Modernism', 'Le Corbusier'): 'dashdot',
    ('Brutalism', 'Le Corbusier'): 'solid',
    ('Deconstructivism', 'Zaha Hadid'): 'dashed',
    ('Deconstructivism', 'Rem Koolhaas'): 'dotted'
}

for edge in G.edges():
    nx.draw_networkx_edges(
        G, pos,
        edgelist=[edge],
        style=edge_styles.get((edge[1], edge[0]), edge_styles[edge]),
        width=2,
        edge_color='gray'
    )

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=9, font_family='sans-serif')

# Add a title
plt.title(
    "Influences in Modern Architecture\nMapping Styles and Architects",
    fontsize=14, fontweight='bold'
)

# Add legend for colors
handles = [mpatches.Patch(color=node_colors[node], label=node) for node in node_colors]
plt.legend(handles=handles, loc='upper left', bbox_to_anchor=(1, 1))

# Customize the layout
plt.axis('off')
plt.tight_layout()

# Show plot
plt.show()