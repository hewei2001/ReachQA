import matplotlib.pyplot as plt
import networkx as nx

# Define philosophers as nodes
philosophers = [
    'Socrates', 'Plato', 'Aristotle', 'Pythagoras', 'Confucius', 
    'Laozi', 'Zeno', 'Epicurus', 'Seneca', 'Heraclitus'
]

# Define their relationships as edges
relationships = [
    ('Socrates', 'Plato'),
    ('Plato', 'Aristotle'),
    ('Aristotle', 'Epicurus'),
    ('Pythagoras', 'Plato'),
    ('Pythagoras', 'Zeno'),
    ('Confucius', 'Laozi'),
    ('Laozi', 'Zeno'),
    ('Epicurus', 'Seneca'),
    ('Seneca', 'Heraclitus'),
    ('Heraclitus', 'Socrates'),
    ('Zeno', 'Confucius')
]

# Create the graph
G = nx.Graph()
G.add_nodes_from(philosophers)
G.add_edges_from(relationships)

# Layout for the network
pos = nx.spring_layout(G, seed=42)  # Ensures consistent layout on multiple runs

# Node sizes and colors based on degree
node_sizes = [1000 + 300 * G.degree(n) for n in G.nodes]
node_colors = [
    'gold' if philosopher in ['Socrates', 'Plato', 'Aristotle', 'Pythagoras'] else 
    'skyblue' if philosopher in ['Confucius', 'Laozi'] else 
    'lightcoral' for philosopher in G.nodes
]

# Create the figure
plt.figure(figsize=(14, 12))

# Draw nodes
nx.draw_networkx_nodes(
    G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black'
)

# Draw edges with custom styling
nx.draw_networkx_edges(
    G, pos, width=2, alpha=0.6, edge_color='gray', 
    style='dashed', connectionstyle='arc3,rad=0.2'
)

# Add labels to nodes
nx.draw_networkx_labels(
    G, pos, font_size=10, font_weight='bold', font_color='darkblue'
)

# Title and labels
plt.title(
    "Network of Ancient Philosophers\nTracing the Flow of Ideas and Influence",
    fontsize=16, fontweight='bold', pad=20
)
plt.xlabel("Nodes: Philosophers | Edges: Idea Exchanges", fontsize=12)

# Legend for node colors
legend_labels = {
    'gold': 'Western Philosophy',
    'skyblue': 'Eastern Philosophy',
    'lightcoral': 'Stoicism & Epicureanism'
}
for color, label in legend_labels.items():
    plt.scatter([], [], c=color, label=label, s=200, edgecolor='black')
plt.legend(loc='upper right', title='Philosophical Schools')

# Adjust layout for clarity
plt.tight_layout()

# Display the plot
plt.show()