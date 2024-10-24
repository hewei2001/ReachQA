import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define fictional countries and energy type labels
countries = ['Solaria', 'Windhaven', 'Hydropolis', 'Geoterra', 'Ecopolis']
energy_types = ['Solar', 'Wind', 'Hydro']

# Percentage distribution of renewable energy sources for each country
energy_distribution = np.array([
    [40, 35, 25],  # Solaria
    [20, 60, 20],  # Windhaven
    [10, 20, 70],  # Hydropolis
    [25, 25, 50],  # Geoterra
    [50, 20, 30]   # Ecopolis
])

# Create a grid for bar positioning
x_positions = np.arange(len(countries))
y_positions = np.arange(len(energy_types))
x_grid, y_grid = np.meshgrid(x_positions, y_positions, indexing='ij')
x_grid_flat = x_grid.flatten()
y_grid_flat = y_grid.flatten()
z_values = energy_distribution.flatten()

# Define bar dimensions
bar_width = 0.3
bar_depth = 0.3

# Setup the figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define color for each energy type
colors = ['gold', 'skyblue', 'mediumseagreen']

# Plot each set of bars
for y, color in zip(range(len(energy_types)), colors):
    ax.bar3d(
        x_grid_flat[y::len(energy_types)], y_grid_flat[y::len(energy_types)], np.zeros_like(z_values[y::len(energy_types)]),
        bar_width, bar_depth, z_values[y::len(energy_types)], color=color, alpha=0.8, edgecolor='black'
    )

# Axes and labels
ax.set_xlabel('Countries', fontsize=12, labelpad=10)
ax.set_ylabel('Energy Type', fontsize=12, labelpad=10)
ax.set_zlabel('Percentage (%)', fontsize=12, labelpad=10)
ax.set_xticks(x_positions + bar_width/2)
ax.set_xticklabels(countries, rotation=15)
ax.set_yticks(y_positions + bar_depth/2)
ax.set_yticklabels(energy_types)
ax.set_zlim(0, 100)
ax.set_title('Renewable Energy Adoption: A Glimpse into Future Landscapes\n', fontsize=16, fontweight='bold', pad=20)

# Enhance the viewing angle
ax.view_init(elev=25, azim=125)

# Create a legend
color_patches = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(color_patches, energy_types, loc='upper left', fontsize=10)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()