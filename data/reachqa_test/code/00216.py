import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the quadrant names and species
quadrants = ['Alpha', 'Beta', 'Gamma', 'Delta']
species = ['Humanoids', 'Avians', 'Reptilians']

# Create data for each species in each quadrant
# Data format: rows are species, columns are quadrants
population_data = np.array([
    [50, 30, 40, 60],  # Humanoids
    [70, 55, 45, 35],  # Avians
    [20, 25, 30, 20]   # Reptilians
])

# Create related but distinct dataset for overlay plot
# Let's assume these are growth rates in percentage
growth_rate_data = np.array([
    [1.2, 0.8, 1.0, 1.4],  # Humanoids growth rate
    [1.1, 0.9, 0.95, 0.85],  # Avians growth rate
    [1.3, 1.2, 1.15, 1.1]  # Reptilians growth rate
])

# X positions for bars (quadrants)
x = np.arange(len(quadrants))

# Y positions (species) - shift each species slightly for better visualization
y_offsets = np.arange(len(species)) * 0.4

# Create the 3D plot
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')

# Colors for species
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Loop through each species and plot their data as bars
for i, (species_name, color) in enumerate(zip(species, colors)):
    y = np.full_like(x, y_offsets[i], dtype=float)
    z = np.zeros_like(x)
    ax.bar3d(x, y, z, 0.4, 0.2, population_data[i], color=color, alpha=0.8, label=species_name)

    # Overlay line plot for growth rates
    ax.plot(x, y, growth_rate_data[i], color=color, marker='o', linestyle='-', linewidth=1.5, alpha=0.7)

# Customize the axes
ax.set_xlabel('Quadrants')
ax.set_ylabel('Species')
ax.set_zlabel('Population (Millions)')
ax.set_xticks(x)
ax.set_xticklabels(quadrants, rotation=0, ha='right')
ax.set_yticks(y_offsets)
ax.set_yticklabels(species)
ax.view_init(elev=20, azim=30)  # Adjust viewing angle for better visibility

# Add grid and legend
ax.xaxis._axinfo['grid'].update(color='gray', linestyle='--', linewidth=0.5)
ax.yaxis._axinfo['grid'].update(color='gray', linestyle='--', linewidth=0.5)
ax.zaxis._axinfo['grid'].update(color='gray', linestyle='--', linewidth=0.5)
ax.legend(loc='upper right', title="Species", bbox_to_anchor=(1.2, 1))

# Title and layout adjustments
ax.set_title('Galactic Population Trends in the Milky Way\n3D Exploration and Growth Rate Analysis', fontsize=14, pad=20)
plt.tight_layout()

# Display the plot
plt.show()