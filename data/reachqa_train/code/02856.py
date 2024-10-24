import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
# Distances in light-years
distances = np.array([2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000])

# Apparent brightness in magnitudes (lower values indicate higher brightness)
brightness = np.array([5.1, 4.9, 5.5, 6.0, 5.2, 4.8, 5.9, 6.5, 5.0, 4.6, 5.4])

# Different cluster types for visualization
cluster_types = ['Open Cluster', 'Globular Cluster', 'Open Cluster', 'Globular Cluster',
                 'Open Cluster', 'Globular Cluster', 'Open Cluster', 'Globular Cluster',
                 'Open Cluster', 'Globular Cluster', 'Open Cluster']

# Color mapping for cluster types
colors = ['blue' if ctype == 'Open Cluster' else 'green' for ctype in cluster_types]

# Create scatter plot
fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(distances, brightness, c=colors, s=100, alpha=0.8, edgecolor='k', linewidth=0.6)

# Add labels and title
ax.set_title('Star Clusters in the Milky Way\nDistance vs Apparent Brightness', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Distance from Earth (light-years)', fontsize=12)
ax.set_ylabel('Apparent Brightness (magnitude)', fontsize=12)
ax.invert_yaxis()  # Brightness inversely proportional to magnitude

# Create legend manually
open_cluster_patch = plt.Line2D([0], [0], marker='o', color='w', label='Open Cluster',
                                markersize=10, markerfacecolor='blue', alpha=0.8)
globular_cluster_patch = plt.Line2D([0], [0], marker='o', color='w', label='Globular Cluster',
                                    markersize=10, markerfacecolor='green', alpha=0.8)
ax.legend(handles=[open_cluster_patch, globular_cluster_patch], title='Cluster Types', loc='upper right')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout for neatness
plt.tight_layout()

# Display the plot
plt.show()