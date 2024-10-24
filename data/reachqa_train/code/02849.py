import matplotlib.pyplot as plt
import numpy as np

# Data representing the nectar (in grams) collected by bee colonies in various floral zones
data = [
    [100, 120, 130, 140, 115, 125, 135],  # Meadow
    [80, 95, 100, 110, 120, 105],         # Orchard
    [50, 65, 70, 75, 60, 55],             # Forest
    [70, 85, 90, 100, 80, 95],            # Urban Garden
    [130, 145, 155, 160, 150, 140]        # Wetland
]

# Creating the vertical box plot
fig, ax = plt.subplots(figsize=(10, 6))

# Boxplot customization for enhanced visuals
ax.boxplot(data, 
           patch_artist=True, notch=True,
           boxprops=dict(facecolor="lightgreen", color="darkgreen"),
           capprops=dict(color="black"),
           whiskerprops=dict(color="darkgray", linestyle='-'),
           flierprops=dict(markeredgecolor="red", marker='o', markersize=8),
           medianprops=dict(color="orange"))

# Title and labels
ax.set_title('Nectar Collection Patterns:\nAn Insight into Bee Colonies', fontsize=14, fontweight='bold')
ax.set_ylabel('Nectar Collected (grams)', fontsize=12)
ax.set_xticklabels(['Meadow', 'Orchard', 'Forest', 'Urban Garden', 'Wetland'], fontsize=10)

# Add grid and set the background color for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_facecolor('#f5f5f5')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Show the plot
plt.show()