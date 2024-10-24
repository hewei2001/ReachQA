import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Data for trading hubs
hub_identifiers = np.array([1, 2, 3, 4, 5])  # Unique identifiers for hubs
distances_from_earth = np.array([4.2, 7.6, 12.3, 15.8, 21.5])  # Distance in light-years
trade_routes = np.array([10, 15, 7, 20, 12])  # Number of active trade routes
goods_volume = np.array([50, 80, 30, 120, 60])  # Volume of goods traded in million metric tons

# Create the figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot with bubble sizes and colors based on goods volume
scatter = ax.scatter(distances_from_earth, trade_routes, hub_identifiers, 
                     s=goods_volume * 10, c=goods_volume, cmap='plasma', alpha=0.8, edgecolors='w', linewidth=0.5)

# Axis labels
ax.set_xlabel('Distance from Earth (light-years)', fontsize=12, labelpad=10)
ax.set_ylabel('Number of Active Trade Routes', fontsize=12, labelpad=10)
ax.set_zlabel('Hub Identifier', fontsize=12, labelpad=10)

# Title of the chart
ax.set_title('Galactic Trade Network:\nDistribution of Trading Hubs', fontsize=16, fontweight='bold', pad=20)

# Color bar to show the mapping from colors to volume
colorbar = fig.colorbar(scatter, ax=ax, pad=0.15)
colorbar.set_label('Volume of Goods Traded (Million Metric Tons)', fontsize=12)

# Annotating hub identifiers for better identification
for i, txt in enumerate(hub_identifiers):
    ax.text(distances_from_earth[i], trade_routes[i], hub_identifiers[i], f'Hub {txt}', fontsize=10)

# Improve the view angle to ensure no overlap
ax.view_init(elev=20, azim=30)

# Show grid for better comprehension
ax.grid(True, linestyle='--', alpha=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()