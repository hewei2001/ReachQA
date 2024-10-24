import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data setup
regions = ['North America', 'Europe', 'Asia', 'Africa']
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal']
data = np.array([
    [30, 40, 25, 5],    # North America
    [35, 30, 20, 15],   # Europe
    [20, 25, 40, 15],   # Asia
    [50, 20, 25, 5]     # Africa
])

# Create a figure and 3D axes
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Bar width and depth
bar_width = 0.2

# Define colors for each energy source
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Grid positions for x and y
x_positions = np.arange(len(regions))
y_positions = np.arange(len(energy_sources))

# Create the 3D bars
for y_idx, source in enumerate(energy_sources):
    ax.bar3d(x_positions, 
             np.full_like(x_positions, y_idx) * bar_width, 
             np.zeros_like(x_positions), 
             bar_width, bar_width, 
             data[:, y_idx], 
             color=colors[y_idx], 
             zsort='average', 
             alpha=0.8)

# Set labels
ax.set_xlabel('Regions', fontsize=12)
ax.set_ylabel('Energy Sources', fontsize=12)
ax.set_zlabel('Percentage (%)', fontsize=12)

# Set tick labels
ax.set_xticks(x_positions + bar_width / 2)
ax.set_xticklabels(regions, fontsize=10, rotation=15)
ax.set_yticks(y_positions * bar_width)
ax.set_yticklabels(energy_sources, fontsize=10)

# Title and legend
plt.title("Sustainable Energy Adoption Across Regions", fontsize=16, fontweight='bold', pad=20)
ax.legend(energy_sources, loc='upper right', title='Energy Sources', fontsize=10, bbox_to_anchor=(1.2, 1))

# Normalizing the z-axis
ax.set_zlim(0, 100)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()