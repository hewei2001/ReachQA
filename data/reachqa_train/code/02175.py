import matplotlib.pyplot as plt
import networkx as nx

# Define nodes (emotions and actions)
nodes = [
    "Joy", "Sadness", "Anger", "Surprise", "Trust", "Fear",
    "Laughter", "Tears", "Shouting", "Awe", "Comfort", "Anxiety"
]

# Define connections (influences)
edges = [
    ("Joy", "Laughter"), ("Sadness", "Tears"), ("Anger", "Shouting"),
    ("Surprise", "Awe"), ("Trust", "Comfort"), ("Fear", "Anxiety"),
    ("Joy", "Surprise"), ("Sadness", "Trust"), ("Anger", "Fear"),
    ("Trust", "Joy"), ("Fear", "Sadness"), ("Surprise", "Anger")
]

# Create the graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Define positions for nodes (layout)
pos = nx.spring_layout(G, seed=42)  # Using a seed for reproducibility

# Define node colors based on type (emotion vs action)
emotion_nodes = {"Joy", "Sadness", "Anger", "Surprise", "Trust", "Fear"}
node_colors = ['lightcoral' if node in emotion_nodes else 'lightgreen' for node in G.nodes]

# Define edge thickness based on types of influences
edge_styles = [
    ('dashed' if ('Joy', 'Surprise') in (edge, edge[::-1]) else 'solid') for edge in G.edges
]

# Create the plot
plt.figure(figsize=(12, 8))

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2000, edgecolors='black')

# Draw edges with styles
nx.draw_networkx_edges(G, pos, edgelist=edges, width=2, alpha=0.6, edge_color='gray', style=edge_styles)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif', font_color='darkblue')

# Add a legend manually
legend_labels = {
    'Emotions': 'lightcoral',
    'Actions': 'lightgreen'
}

for label, color in legend_labels.items():
    plt.plot([], [], color=color, marker='o', markersize=10, linestyle='', label=label)
plt.legend(loc='upper right', title='Node Type')

# Title and layout adjustments
plt.title("The Language of Emotion in Empathia\nConnections Among Emotions and Actions", 
          fontsize=16, fontweight='bold', color='navy')
plt.axis('off')  # Turn off the axis
plt.tight_layout()

# Display the plot
plt.show()