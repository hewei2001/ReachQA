import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Art Styles and Regions
styles = ['Renaissance', 'Impressionism', 'Cubism', 'Abstract', 'Digital Art']
regions = ['North America', 'South America', 'Europe', 'Asia', 'Africa']

# Artificial percentage data for each art style across different regions
popularity = np.array([
    [30, 20, 10, 25, 15],  # North America
    [15, 25, 20, 15, 25],  # South America
    [40, 30, 10, 15, 5],   # Europe
    [10, 15, 25, 30, 20],  # Asia
    [25, 10, 15, 20, 30],  # Africa
])

# Set up the figure and axes
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Bar positions and dimensions
x, y = np.meshgrid(np.arange(len(regions)), np.arange(len(styles)))
x, y = x.flatten(), y.flatten()
z = np.zeros_like(x)

# Flatten the popularity data for bar heights
dz = popularity.flatten()

# Define colors
base_colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF6666']

# Plot the bars
ax.bar3d(x, y, z, dx=0.6, dy=0.6, dz=dz,
         color=[base_colors[i % len(base_colors)] for i in range(len(dz))], alpha=0.9)

# Set the ticks and labels
ax.set_xticks(np.arange(len(regions)))
ax.set_yticks(np.arange(len(styles)))
ax.set_xticklabels(regions, rotation=45, ha='right', fontsize=11)
ax.set_yticklabels(styles, fontsize=11)
ax.set_zlabel('Popularity (%)', fontsize=12)

# Normalize the Z-axis to a 0-50 scale for percentage representation
ax.set_zlim(0, 50)

# Title and layout adjustments
plt.title('Global Art Movement Styles\nRegional Popularity Analysis', fontsize=16, fontweight='bold', pad=20)

# Improve layout
ax.xaxis.set_tick_params(width=0.5)
ax.yaxis.set_tick_params(width=0.5)
ax.zaxis.set_tick_params(width=0.5)
ax.grid(color='gray', linestyle='--', linewidth=0.5)

# Add annotations for extreme values
max_idx = np.unravel_index(np.argmax(popularity, axis=None), popularity.shape)
min_idx = np.unravel_index(np.argmin(popularity, axis=None), popularity.shape)
ax.text(max_idx[1], max_idx[0], popularity[max_idx]+2, 'Max', color='red', fontsize=10, weight='bold')
ax.text(min_idx[1], min_idx[0], popularity[min_idx]+2, 'Min', color='blue', fontsize=10, weight='bold')

# Legend
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=style,
                              markersize=10, markerfacecolor=base_colors[i])
                   for i, style in enumerate(styles)]
ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0.0, -0.15), ncol=3, frameon=False)

# Automatically adjust to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()