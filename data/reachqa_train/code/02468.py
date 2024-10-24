import matplotlib.pyplot as plt
import numpy as np

# Population variability (standard deviation) data for each conservation zone across decades
variability_data = [
    [25, 30, 27, 22, 20, 19, 18],  # Amazon Rainforest
    [35, 40, 38, 34, 30, 28, 25],  # African Savannah
    [18, 20, 21, 19, 17, 15, 14],  # Himalayan Foothills
    [28, 32, 29, 25, 22, 18, 15],  # Great Barrier Reef
    [12, 15, 14, 11, 10, 9, 8]     # Arctic Tundra
]

# Conservation zones
zones = ['Amazon', 'Savannah', 'Himalayan', 'Barrier Reef', 'Arctic']

# Create the vertical box plot
fig, ax = plt.subplots(figsize=(12, 7))
box = ax.boxplot(variability_data, vert=True, patch_artist=True, notch=True,
                 boxprops=dict(facecolor='lightgreen', color='green'),
                 whiskerprops=dict(color='green'),
                 capprops=dict(color='green'),
                 medianprops=dict(color='darkred', linewidth=2),
                 flierprops=dict(marker='o', color='orange', markersize=6, alpha=0.7))

# Assign different colors to each box
colors = ['#77dd77', '#ffb347', '#779ecb', '#ff6961', '#cb99c9']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set titles and labels
ax.set_title('Conservation Efforts Impact:\nVariability in Species Populations Across Zones', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Conservation Zones', fontsize=12, labelpad=10)
ax.set_ylabel('Population Variability (Standard Deviation)', fontsize=12, labelpad=10)
ax.set_xticks(range(1, len(zones) + 1))
ax.set_xticklabels(zones, fontsize=10)

# Add grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Annotate with additional information
annotations = [
    (1, 30, "Stable flora\ndensity"),
    (2, 40, "Poaching\nchallenges"),
    (3, 21, "Climate\nadaptations"),
    (4, 32, "Bleaching\nimpact"),
    (5, 15, "Ice melt\nreduces habitat")
]

for (x, y, text) in annotations:
    ax.annotate(text, xy=(x, y), xytext=(x, y + 5),
                bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow', alpha=0.8),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3', color='black'),
                fontsize=9, ha='center')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()