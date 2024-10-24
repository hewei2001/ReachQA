import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mcolors

# Define the data for marine zones
zones = ['Continental Shelf', 'Bathyal Zone', 'Abyssal Zone', 'Hadal Zone', 'Oceanic Zone']
average_depth = [200, 1500, 4000, 6000, 3000]  # in meters
biodiversity_index = [8.5, 7.0, 4.5, 3.0, 5.5]  # arbitrary units
relative_area = [50, 30, 10, 5, 20]  # arbitrary units for bubble size

# Assign numerical values to each zone for plotting
zone_numeric = np.arange(len(zones))

# Initialize a 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d', facecolor='lightcyan')

# Create the 3D scatter plot (bubble chart)
scatter = ax.scatter(average_depth, biodiversity_index, zone_numeric,
                     s=np.array(relative_area) * 100,
                     c=average_depth, cmap='cool', alpha=0.7, edgecolors='grey', linewidth=0.5)

# Add gridlines for better depth perception
ax.grid(True)

# Set labels and title with line break for clarity
ax.set_xlabel('Average Depth (m)', fontsize=10)
ax.set_ylabel('Biodiversity Index', fontsize=10)
ax.set_zlabel('Marine Zone', fontsize=10)
ax.set_zticks(zone_numeric)
ax.set_zticklabels(zones, fontsize=9)
ax.set_title('Deep Dive into Diversity:\nMarine Ecosystems by Depth & Biodiversity', fontsize=12, fontweight='bold')

# Add a color bar with label for depth
cbar = plt.colorbar(scatter, ax=ax, shrink=0.5, aspect=10)
cbar.set_label('Depth Color Intensity')

# Adjust the viewing angle for better interpretation
ax.view_init(elev=15., azim=120)

# Add annotations for each zone
for i in range(len(zones)):
    ax.text(average_depth[i], biodiversity_index[i], zone_numeric[i], f'{zones[i]}\nDepth: {average_depth[i]}m\nBI: {biodiversity_index[i]}', 
            fontsize=8, ha='left')

# Enhance layout
plt.tight_layout()

# Show the plot
plt.show()