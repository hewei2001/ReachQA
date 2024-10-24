import matplotlib.pyplot as plt
import numpy as np

# Original data
distances = np.array([2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000])
brightness = np.array([5.1, 4.9, 5.5, 6.0, 5.2, 4.8, 5.9, 6.5, 5.0, 4.6, 5.4])
cluster_types = ['Open Cluster', 'Globular Cluster', 'Open Cluster', 'Globular Cluster',
                 'Open Cluster', 'Globular Cluster', 'Open Cluster', 'Globular Cluster',
                 'Open Cluster', 'Globular Cluster', 'Open Cluster']
colors = ['blue' if ctype == 'Open Cluster' else 'green' for ctype in cluster_types]

# Additional data for the new subplot
brightness_change = np.diff(brightness, prepend=brightness[0])  # Change in brightness
avg_distance = (distances[:-1] + distances[1:]) / 2  # Midpoints for line plot

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Original scatter plot
scatter = axes[0].scatter(distances, brightness, c=colors, s=100, alpha=0.8, edgecolor='k', linewidth=0.6)
axes[0].set_title('Star Clusters in the Milky Way\nDistance vs Apparent Brightness', fontsize=14, fontweight='bold', pad=20)
axes[0].set_xlabel('Distance from Earth (light-years)', fontsize=12)
axes[0].set_ylabel('Apparent Brightness (magnitude)', fontsize=12)
axes[0].invert_yaxis()

# Manually create a legend
open_cluster_patch = plt.Line2D([0], [0], marker='o', color='w', label='Open Cluster',
                                markersize=10, markerfacecolor='blue', alpha=0.8)
globular_cluster_patch = plt.Line2D([0], [0], marker='o', color='w', label='Globular Cluster',
                                    markersize=10, markerfacecolor='green', alpha=0.8)
axes[0].legend(handles=[open_cluster_patch, globular_cluster_patch], title='Cluster Types', loc='upper right')

axes[0].grid(True, linestyle='--', alpha=0.6)

# New line plot for change in brightness
axes[1].plot(avg_distance, brightness_change[1:], color='orange', marker='o', linestyle='-', linewidth=2, markersize=6)
axes[1].set_title('Change in Apparent Brightness\nAlong Distance', fontsize=14, fontweight='bold', pad=20)
axes[1].set_xlabel('Midpoint Distance from Earth (light-years)', fontsize=12)
axes[1].set_ylabel('Change in Apparent Brightness (magnitude)', fontsize=12)
axes[1].invert_yaxis()

axes[1].grid(True, linestyle='--', alpha=0.6)

# Ensure layout is optimized and tidy
plt.tight_layout()

# Show the plot
plt.show()