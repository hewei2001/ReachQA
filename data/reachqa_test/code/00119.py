import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define the artists (nodes) and their collaborative connections (edges)
artists = [
    "Leonardo da Vinci", "Michelangelo", "Raphael", 
    "Titian", "Donatello", "Botticelli", 
    "Caravaggio", "Tintoretto", "Verrocchio", 
    "Ghirlandaio", "Lorenzo de' Medici"
]

connections = [
    ("Leonardo da Vinci", "Verrocchio"),
    ("Leonardo da Vinci", "Botticelli"),
    ("Michelangelo", "Ghirlandaio"),
    ("Michelangelo", "Lorenzo de' Medici"),
    ("Raphael", "Michelangelo"),
    ("Raphael", "Leonardo da Vinci"),
    ("Titian", "Raphael"),
    ("Caravaggio", "Titian"),
    ("Tintoretto", "Titian"),
    ("Donatello", "Leonardo da Vinci"),
    ("Lorenzo de' Medici", "Botticelli"),
    ("Verrocchio", "Ghirlandaio")
]

# Constructing related data for the bar chart
artistic_styles = {
    "Leonardo da Vinci": 5,
    "Michelangelo": 4,
    "Raphael": 3,
    "Titian": 4,
    "Donatello": 2,
    "Botticelli": 3,
    "Caravaggio": 4,
    "Tintoretto": 3,
    "Verrocchio": 2,
    "Ghirlandaio": 3,
    "Lorenzo de' Medici": 1
}

# Create a NetworkX graph
G = nx.Graph()
G.add_nodes_from(artists)
G.add_edges_from(connections)

# Generate a layout for the graph
pos = nx.spring_layout(G, seed=42)

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 9))

# Subplot 1: Network graph
axs[0].set_title("Collaborative Network of Renaissance Artists\nConnections and Influences", fontsize=14, fontweight='bold')
nx.draw_networkx_nodes(G, pos, ax=axs[0], node_size=1000, node_color='lightgreen', alpha=0.9, edgecolors='black')
nx.draw_networkx_edges(G, pos, ax=axs[0], width=2, edge_color='darkgrey', style='dashed')
nx.draw_networkx_labels(G, pos, ax=axs[0], font_size=11, font_weight='bold', font_color='darkred')
axs[0].axis('off')

# Subplot 2: Bar chart for artistic styles
axs[1].set_title("Artistic Style Representation among Artists", fontsize=14, fontweight='bold')
axs[1].barh(list(artistic_styles.keys()), list(artistic_styles.values()), color='skyblue', edgecolor='black')
axs[1].set_xlabel('Style Representation')
axs[1].set_ylabel('Artists')
axs[1].set_xlim(0, max(artistic_styles.values()) + 1)
axs[1].invert_yaxis()  # To have the first artist at the top
axs[1].grid(axis='x', linestyle='--', alpha=0.7)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()