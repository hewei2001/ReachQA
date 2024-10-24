import matplotlib.pyplot as plt
import networkx as nx

# Define genres as nodes
genres = [
    "Fantasy", "Science Fiction", "Mystery", 
    "Romance", "Horror", "Historical Fiction", 
    "Adventure", "Thriller", "Drama", "Comedy"
]

# Define connections (edges) between genres
connections = [
    ("Fantasy", "Science Fiction"),
    ("Science Fiction", "Mystery"),
    ("Mystery", "Thriller"),
    ("Thriller", "Horror"),
    ("Horror", "Fantasy"),
    ("Fantasy", "Adventure"),
    ("Adventure", "Historical Fiction"),
    ("Historical Fiction", "Romance"),
    ("Romance", "Mystery"),
    ("Romance", "Fantasy"),
    ("Drama", "Mystery"),
    ("Comedy", "Drama"),
    ("Comedy", "Romance"),
    ("Comedy", "Adventure")
]

# Create a Graph object
G = nx.Graph()

# Add nodes and edges
G.add_nodes_from(genres)
G.add_edges_from(connections)

# Draw the graph using Matplotlib
plt.figure(figsize=(14, 10))
pos = nx.spring_layout(G, seed=42, k=0.3)  # Layout for node positions

# Customize node colors based on genre types
node_colors = {
    "Fantasy": "#FFB6C1", "Science Fiction": "#ADD8E6",
    "Mystery": "#FFFF99", "Romance": "#FFC0CB",
    "Horror": "#DDA0DD", "Historical Fiction": "#C0C0C0",
    "Adventure": "#FFA07A", "Thriller": "#8B0000",
    "Drama": "#B0E0E6", "Comedy": "#98FB98"
}

# Draw nodes with labels
nx.draw_networkx_nodes(
    G, pos, node_size=3000, 
    node_color=[node_colors[genre] for genre in G.nodes], alpha=0.85
)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', verticalalignment='bottom')

# Draw edges
nx.draw_networkx_edges(G, pos, width=2, alpha=0.7, edge_color='gray', style='solid')

# Add a legend manually
for genre, color in node_colors.items():
    plt.scatter([], [], color=color, label=genre, s=100)
plt.legend(title="Literary Genres", fontsize=9, loc='upper left', bbox_to_anchor=(1, 1))

# Add title
plt.title("The Interconnected World of Literature:\nAn Exploration of Genre Connections",
          fontsize=16, fontweight='bold', pad=20)

# Remove axis
plt.axis('off')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()