import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define nodes as philosophical schools
philosophical_schools = [
    "Stoicism", "Epicureanism", "Platonism", "Aristotelianism",
    "Cynicism", "Skepticism", "Neoplatonism", "Hedonism",
    "Pythagoreanism", "Sophism", "Zoroastrianism", "Taoism"
]

# Define edges with weights indicating the strength of influence
influences = [
    ("Stoicism", "Cynicism", 4), ("Stoicism", "Skepticism", 6),
    ("Epicureanism", "Hedonism", 5), ("Epicureanism", "Cynicism", 2),
    ("Platonism", "Aristotelianism", 8), ("Platonism", "Neoplatonism", 7),
    ("Aristotelianism", "Platonism", 3), ("Aristotelianism", "Skepticism", 4),
    ("Cynicism", "Sophism", 5), ("Skepticism", "Stoicism", 3),
    ("Neoplatonism", "Pythagoreanism", 4), ("Neoplatonism", "Zoroastrianism", 3),
    ("Hedonism", "Epicureanism", 6), ("Pythagoreanism", "Platonism", 2),
    ("Sophism", "Taoism", 3), ("Zoroastrianism", "Taoism", 4)
]

# Historical emergence data for a bar chart
emergence_periods = {
    "Stoicism": (300, 200), "Epicureanism": (307, 201), 
    "Platonism": (427, 347), "Aristotelianism": (384, 322),
    "Cynicism": (400, 325), "Skepticism": (300, 100),
    "Neoplatonism": (250, 600), "Hedonism": (433, 300),
    "Pythagoreanism": (570, 495), "Sophism": (450, 380),
    "Zoroastrianism": (1500, 600), "Taoism": (600, 400)
}

# Create an undirected graph
G = nx.Graph()
G.add_nodes_from(philosophical_schools)
G.add_weighted_edges_from(influences)

# Calculate layout for better visualization
pos = nx.spring_layout(G, seed=42)

# Prepare subplot
fig, axes = plt.subplots(1, 2, figsize=(15, 8))
ax1, ax2 = axes

# Draw network plot
nx.draw_networkx_nodes(G, pos, node_size=1500, node_color='skyblue', ax=ax1)
nx.draw_networkx_edges(G, pos, width=[d['weight'] * 0.5 for (u, v, d) in G.edges(data=True)], edge_color='navy', ax=ax1)
nx.draw_networkx_labels(G, pos, font_size=10, font_color='darkred', font_family='serif', font_weight='bold', ax=ax1)
ax1.set_title("Interwoven Ideologies: Influence Network\nin Ancient Philosophical Schools", fontsize=12)
ax1.axis('off')

annotations = {
    "Stoicism": "Rooted in Cynicism",
    "Platonism": "Foundation for Neoplatonism",
    "Epicureanism": "Influenced by Hedonism"
}
for key, text in annotations.items():
    ax1.annotate(text, xy=pos[key], xytext=(20, 20), textcoords='offset points',
                 bbox=dict(boxstyle="round,pad=0.3", edgecolor='navy', facecolor='aliceblue'))

# Prepare data for the bar chart
schools, periods = zip(*emergence_periods.items())
start, end = zip(*periods)
durations = np.array(end) - np.array(start)

# Draw bar chart
ax2.barh(schools, durations, color='lightcoral', edgecolor='darkred')
ax2.set_xlabel('Duration of Influence (Years)')
ax2.set_title('Influence Duration of Philosophical Schools', fontsize=12)
ax2.invert_yaxis()  # To display bars from top to bottom

# Adjust layout to fit both subplots
plt.tight_layout()
plt.show()