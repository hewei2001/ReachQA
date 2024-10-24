import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define regions, minerals, and hypothetical reserves
regions = ["Gale Crater", "Jezero Crater", "Valles Marineris"]
minerals = ["Iron Oxide", "Silica", "Magnesium", "Sulfur"]
# Hypothetical mineral reserves in million metric tons
reserves_data = {
    "Gale Crater": [75, 100, 55, 40],
    "Jezero Crater": [90, 80, 65, 50],
    "Valles Marineris": [85, 120, 70, 45]
}

# Prepare plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
bar_width = 0.4
colors = ['#FF4500', '#FFD700', '#708090', '#8B4513']  # Distinct colors for each mineral

# Create bars for each mineral across regions
x_pos = np.arange(len(regions))
for i, mineral in enumerate(minerals):
    reserves = [reserves_data[region][i] for region in regions]
    ax.bar3d(x_pos, i * np.ones_like(x_pos), np.zeros_like(reserves), bar_width, bar_width, reserves, color=colors[i], alpha=0.8)

# Configure axes
ax.set_xlabel('Region')
ax.set_ylabel('Mineral')
ax.set_zlabel('Estimated Reserves (Million Metric Tons)')
ax.set_xticks(x_pos + bar_width / 2)
ax.set_xticklabels(regions)
ax.set_yticks(np.arange(len(minerals)))
ax.set_yticklabels(minerals)

# Adjust view for optimal visibility
ax.view_init(elev=20, azim=135)

# Title and legend
ax.set_title("Mining the Red Planet:\nEstimated Mineral Reserves in Key Martian Regions", fontsize=14, fontweight='bold')
plt.legend([plt.Rectangle((0, 0), 1, 1, color=color) for color in colors], minerals, loc='upper left', fontsize=9, title="Minerals")

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display plot
plt.show()