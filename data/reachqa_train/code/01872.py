import matplotlib.pyplot as plt
import networkx as nx

# Define programming languages as nodes
languages = [
    'Python', 'Java', 'JavaScript', 'C++', 'C#', 
    'Ruby', 'Go', 'Swift', 'Kotlin', 'TypeScript'
]

# Define edges to signify influence or common usage
edges = [
    ('Python', 'JavaScript'), 
    ('Java', 'C#'), 
    ('JavaScript', 'TypeScript'),
    ('C++', 'C#'), 
    ('Ruby', 'Python'), 
    ('Go', 'C++'), 
    ('Swift', 'Kotlin'), 
    ('Java', 'Kotlin'),
    ('Python', 'Go'),
    ('Swift', 'C++')
]

# Create a graph
G = nx.Graph()

# Add nodes and edges
G.add_nodes_from(languages)
G.add_edges_from(edges)

# Calculate degrees (number of connections) for each node
degrees = dict(G.degree)

# Determine node sizes based on degree
node_sizes = [degrees[lang] * 1500 for lang in languages]

# Set layout for nodes
pos = nx.spring_layout(G, seed=42)

# Plot the graph
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(
    G, pos, node_size=node_sizes, node_color='skyblue', edgecolors='black'
)
nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color='gray')
nx.draw_networkx_labels(
    G, pos, font_size=10, font_weight='bold', verticalalignment='center'
)

# Annotate the edges to show types of relationships
edge_labels = {
    ('Python', 'JavaScript'): 'Influence',
    ('Java', 'C#'): 'Interoperability',
    ('JavaScript', 'TypeScript'): 'Superset',
    ('C++', 'C#'): 'Syntax Similarity',
    ('Ruby', 'Python'): 'Scripting',
    ('Go', 'C++'): 'Performance',
    ('Swift', 'Kotlin'): 'Mobile',
    ('Java', 'Kotlin'): 'JVM',
    ('Python', 'Go'): 'Adoption',
    ('Swift', 'C++'): 'Native'
}
nx.draw_networkx_edge_labels(
    G, pos, edge_labels=edge_labels, font_size=8, font_color='red', alpha=0.7
)

# Set title and remove axes
plt.title(
    'Interconnections in the Digital Language Community\n'
    'Visualizing Influence and Shared Use Among Programming Languages',
    fontsize=14, weight='bold', pad=20
)
plt.axis('off')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()