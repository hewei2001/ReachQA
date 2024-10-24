import matplotlib.pyplot as plt
import networkx as nx

# Define artists (nodes) and their relationships (edges)
artists = ["Picasso", "Braque", "Dali", "Duchamp", "Kahlo", 
           "Rivera", "O'Keeffe", "Pollock", "Warhol", "Basquiat"]

# Define collaborations and influences as edges between artists
connections = [
    ("Picasso", "Braque"),  # Collaboration
    ("Picasso", "Dali"),    # Influence
    ("Duchamp", "Dali"),    # Influence
    ("Duchamp", "Kahlo"),   # Influence
    ("Rivera", "Kahlo"),    # Collaboration
    ("O'Keeffe", "Pollock"),# Influence
    ("Warhol", "Basquiat"), # Collaboration
    ("Warhol", "Pollock"),  # Influence
    ("Dali", "Warhol"),     # Influence
    ("Basquiat", "Pollock") # Influence
]

# Create the graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(artists)
G.add_edges_from(connections)

# Draw the graph
plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G, seed=42, k=0.3)  # Layout for positioning nodes

# Draw nodes with varying sizes based on their degree
node_sizes = [800 + 100 * G.degree(n) for n in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color="lightblue", edgecolors='black')

# Draw edges with varying thickness
edge_widths = [2 if ("Collaboration" in str(conn)) else 1 for conn in connections]
nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color="gray", alpha=0.7)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=9, font_family="sans-serif")

# Set title
plt.title("Interconnections Among Famous Artists\nThrough Collaborations and Influence", fontsize=16, fontweight='bold')

# Remove axis
plt.axis("off")

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()