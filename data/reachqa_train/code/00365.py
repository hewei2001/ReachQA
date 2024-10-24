import matplotlib.pyplot as plt
import networkx as nx

# Create a graph object
G = nx.Graph()

# Define major characters in the MCU, including 'Loki'
characters = ['Iron Man', 'Captain America', 'Thor', 'Hulk', 'Black Widow',
              'Hawkeye', 'Spider-Man', 'Doctor Strange', 'Black Panther', 
              'Captain Marvel', 'Loki']

# Define connections (edges) between characters based on movie interactions
connections = [
    ('Iron Man', 'Captain America'),  # Civil War
    ('Iron Man', 'Spider-Man'),       # Homecoming
    ('Iron Man', 'Doctor Strange'),   # Infinity War
    ('Iron Man', 'Hulk'),             # Avengers
    ('Captain America', 'Black Widow'),  # Winter Soldier
    ('Thor', 'Hulk'),                 # Ragnarok
    ('Thor', 'Loki'),                 # Thor
    ('Hulk', 'Black Widow'),          # Avengers
    ('Hawkeye', 'Black Widow'),       # Avengers
    ('Doctor Strange', 'Spider-Man'), # No Way Home
    ('Black Panther', 'Captain America'),  # Civil War
    ('Captain Marvel', 'Thor')        # Endgame
]

# Add nodes and edges to the graph
G.add_nodes_from(characters)
G.add_edges_from(connections)

# Use a spring layout for node placement
pos = nx.spring_layout(G, k=0.6, iterations=50)

# Define a color map for the characters
colors = ['#E27D60', '#85CDCA', '#E8A87C', '#C38D9E', '#41B3A3',
          '#CBB1C1', '#F4B95F', '#72BDA3', '#8B9DC3', '#F47B7B', '#FF6F61']

# Calculate node size based on the degree (number of connections)
node_sizes = [800 + 200 * G.degree(node) for node in G.nodes]

# Create subplot layout
fig, axs = plt.subplots(1, 2, figsize=(15, 7), gridspec_kw={'width_ratios': [2, 1]})

# Original Network Plot
ax = axs[0]
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=colors, alpha=0.9, ax=ax)
nx.draw_networkx_edges(G, pos, width=[1.5 * G.degree(e[0]) for e in G.edges], alpha=0.6, edge_color='gray', ax=ax)
nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold', font_family='sans-serif', 
                        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'), ax=ax)
ax.set_title('Interconnections of MCU Characters\nVisualized as a Network Graph', fontsize=14, fontweight='bold')
ax.axis('off')

# New Plot: Bar Chart of Character Connections
ax2 = axs[1]
character_connection_counts = [G.degree(char) for char in characters]
ax2.barh(characters, character_connection_counts, color=colors, edgecolor='black', alpha=0.8)
ax2.set_title('Character Connection Count', fontsize=12, fontweight='bold')
ax2.set_xlabel('Number of Connections')
ax2.set_ylabel('MCU Characters')
ax2.invert_yaxis()  # To have the most connected on top
ax2.grid(axis='x', linestyle='--', alpha=0.6)

# Adjust layout for clarity
plt.tight_layout()

# Show the plot
plt.show()