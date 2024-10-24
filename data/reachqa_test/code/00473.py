import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()

# Define instruments and their frequency ranges
instruments = {
    'Piano': [27.5, 4186.01],
    'Violin': [196.00, 3520.00],
    'Flute': [261.63, 2637.02],
    'Guitar': [82.41, 1250.00],
    'Trumpet': [233.08, 987.77],
    'Cello': [65.41, 1046.50]
}

# Add nodes for each instrument
for instrument, frequencies in instruments.items():
    G.add_node(instrument, freq=frequencies)

# Define edges based on overlapping frequency ranges
edges = [
    ('Piano', 'Guitar'),
    ('Piano', 'Violin'),
    ('Flute', 'Piano'),
    ('Flute', 'Guitar'),
    ('Trumpet', 'Violin'),
    ('Cello', 'Guitar')
]

# Add edges to the graph
G.add_edges_from(edges)

# Create a layout for our nodes 
pos = nx.spring_layout(G, seed=42)

# Create the figure and subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 12))

# First subplot: Network Graph
axs[0].set_title("Connections of the Celestial Symphony\nCharting Relationships Between Instruments", fontsize=14, fontweight='bold', pad=15)
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=2000, alpha=0.8, ax=axs[0])
nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, ax=axs[0])
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif', font_color='darkblue', ax=axs[0])

for instrument, (low, high) in instruments.items():
    axs[0].annotate(f'{instrument}\nFreq: {low} - {high} Hz', 
                    xy=pos[instrument], 
                    xytext=(10, 10), 
                    textcoords='offset points', 
                    fontsize=9, 
                    color='navy', 
                    bbox=dict(facecolor='lightyellow', alpha=0.6, boxstyle='round,pad=0.3'))

axs[0].axis('off')

# Second subplot: Bar Graph for Frequency Ranges
axs[1].set_title("Frequency Ranges of Instruments\nComparative View", fontsize=14, fontweight='bold', pad=15)
labels = list(instruments.keys())
low_freqs = [freq[0] for freq in instruments.values()]
high_freqs = [freq[1] for freq in instruments.values()]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

rects1 = axs[1].bar(x - width/2, low_freqs, width, label='Low Frequency', color='lightblue')
rects2 = axs[1].bar(x + width/2, high_freqs, width, label='High Frequency', color='salmon')

axs[1].set_ylabel('Frequency (Hz)')
axs[1].set_title("Comparative Frequency Ranges", fontsize=12)
axs[1].set_xticks(x)
axs[1].set_xticklabels(labels)
axs[1].legend()

# Annotate the bars with the frequency values
for rect in rects1:
    height = rect.get_height()
    axs[1].annotate(f'{height:.2f}', 
                    xy=(rect.get_x() + rect.get_width() / 2, height), 
                    xytext=(0, 5), 
                    textcoords='offset points', 
                    ha='center', fontsize=9)

for rect in rects2:
    height = rect.get_height()
    axs[1].annotate(f'{height:.2f}', 
                    xy=(rect.get_x() + rect.get_width() / 2, height), 
                    xytext=(0, 5), 
                    textcoords='offset points', 
                    ha='center', fontsize=9)

plt.tight_layout()
plt.show()