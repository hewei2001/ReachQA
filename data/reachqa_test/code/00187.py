import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define oceanic zones and regions
zones = ['Epipelagic', 'Mesopelagic', 'Bathypelagic']
regions = ['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic']

# Species count data in thousands
species_count = np.array([
    [15, 7, 3],   # Pacific
    [14, 6, 2.5], # Atlantic
    [13, 6.5, 2], # Indian
    [11, 5, 1],   # Southern
    [9, 4, 0.5]   # Arctic
])

# Initialize figure and 3D axis
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Setup grid for positions
_x = np.arange(len(regions))
_y = np.arange(len(zones))
_xx, _yy = np.meshgrid(_x, _y, indexing='ij')
x, y = _xx.ravel(), _yy.ravel()

# Initial Z position for the bars (use float type)
z = np.zeros_like(x, dtype=float)

# Define colors using a colormap for gradient effect
cmap = plt.get_cmap('viridis')
colors = cmap(np.linspace(0.2, 0.8, len(zones)))

# Bar width and depth
dx = dy = 0.5

# Plot 3D stacked bars with gradient effect
for i in range(len(zones)):
    ax.bar3d(x[y == i], y[y == i], z[y == i], dx, dy, species_count[:, i], color=colors[i], alpha=0.8, edgecolor='k')
    z[y == i] += species_count[:, i]

# Labeling axes
ax.set_xticks(_x)
ax.set_xticklabels(regions, rotation=25, ha='right')
ax.set_yticks(_y)
ax.set_yticklabels(zones)
ax.set_zlabel('Species Count (Thousands)')

# Title with line breaks for better readability
ax.set_title('Exploring the Depths: Marine Biodiversity\nDistribution Across Ocean Zones', pad=30, fontsize=14)

# Adding subtle gridlines
ax.xaxis._axinfo['grid'].update(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
ax.yaxis._axinfo['grid'].update(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Enhanced legend
custom_lines = [plt.Line2D([0], [0], color=colors[i], lw=4) for i in range(len(zones))]
ax.legend(custom_lines, zones, loc='upper left', bbox_to_anchor=(0.05, 0.95), title="Oceanic Zones", fontsize=10)

# Axis label style customization
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.zaxis.label.set_size(12)

# Optimize view angle
ax.view_init(elev=35, azim=60)

# Ensure layout is not overlapping
plt.tight_layout()

# Display plot
plt.show()