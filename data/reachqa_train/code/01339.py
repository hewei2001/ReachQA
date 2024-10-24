import matplotlib.pyplot as plt
import numpy as np

# Data for tree heights (in meters)
redwood_heights = [100, 110, 115, 120, 130, 140, 145, 150, 155, 160]
douglas_fir_heights = [70, 75, 80, 85, 90, 95, 100, 105, 110, 115]
oak_heights = [60, 65, 70, 75, 78, 80, 85, 90, 92, 95]
maple_heights = [45, 50, 55, 58, 60, 62, 65, 68, 70, 72]
birch_heights = [40, 42, 45, 47, 48, 50, 52, 54, 55, 57]

# Combine into a list for plotting
data = [redwood_heights, douglas_fir_heights, oak_heights, maple_heights, birch_heights]
labels = ['Redwood', 'Douglas Fir', 'Oak', 'Maple', 'Birch']

# Create the box plot
fig, ax = plt.subplots(figsize=(12, 7))
box = ax.boxplot(data, patch_artist=True, notch=True,
                 boxprops=dict(facecolor='lightgreen', color='darkgreen'),
                 medianprops=dict(color='darkred', linewidth=2),
                 whiskerprops=dict(color='green'),
                 capprops=dict(color='green'),
                 flierprops=dict(marker='o', color='red', markersize=5, alpha=0.5))

# Set colors for each box
colors = ['#8FBC8F', '#DEB887', '#F4A460', '#BC8F8F', '#DAA520']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize plot
ax.set_title("Journey Through the Woods:\nDistribution of Tree Heights in Ancient Forests", fontsize=16, fontweight='bold')
ax.set_xlabel("Tree Species", fontsize=12)
ax.set_ylabel("Height (meters)", fontsize=12)
ax.set_xticks(np.arange(1, len(labels) + 1))
ax.set_xticklabels(labels, rotation=30, ha='right')
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add a background color
ax.set_facecolor('#F5F5DC')

# Highlight a specific tree's median for emphasis
highlight_species = 'Redwood'
highlight_index = labels.index(highlight_species) + 1
ax.plot([highlight_index-0.25, highlight_index+0.25], 
        [np.median(redwood_heights), np.median(redwood_heights)], 
        color='darkorange', lw=3, label=f'{highlight_species} Median')

# Add legend
ax.legend(loc='upper right', frameon=True, fontsize=10)

# Tight layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()