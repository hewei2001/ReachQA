import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Data Setup: Countries and Renewable Energy Types
countries = ['Norway', 'Germany', 'India', 'Brazil', 'Canada']
energy_types = ['Solar', 'Wind', 'Hydro']

# Percentage growth of renewable energy adoption for each country and energy type
growth_percentages = np.array([
    [12, 8, 15],  # Norway
    [18, 25, 5],  # Germany
    [20, 10, 7],  # India
    [8, 5, 12],   # Brazil
    [10, 15, 10]  # Canada
])

# Setup the 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define the grid for bar placement
x_data, y_data = np.meshgrid(np.arange(len(countries)), np.arange(len(energy_types)))
x_data = x_data.flatten()
y_data = y_data.flatten()
z_data = np.zeros_like(x_data)

# Flatten the growth percentages for easy plotting
dz = growth_percentages.flatten()

# Bar dimensions
dx = dy = 0.6

# Define colors for different energy types
colors = ['#f4a582', '#92c5de', '#a6dba0']  # Shades for Solar, Wind, Hydro

# Plot each set of bars
ax.bar3d(x_data, y_data, z_data, dx, dy, dz, color=[colors[i % len(energy_types)] for i in range(len(x_data))])

# Label axes and adjust ticks
ax.set_xlabel('Countries', labelpad=10)
ax.set_ylabel('Energy Types', labelpad=10)
ax.set_zlabel('Growth (%)', labelpad=10)
ax.set_xticks(np.arange(len(countries)))
ax.set_xticklabels(countries, rotation=20, ha='right', fontsize=10)
ax.set_yticks(np.arange(len(energy_types)))
ax.set_yticklabels(energy_types, fontsize=10)

# Configure the Z-axis to handle percentages
ax.set_zlim(0, 30)

# Title
ax.set_title('Renewable Energy Growth by Country and Type\nPercentage Increase from Previous Year', pad=20, fontsize=16)

# Legend for energy types
legend_patches = [plt.Rectangle((0,0),1,1, color=color) for color in colors]
ax.legend(legend_patches, energy_types, loc='upper left', bbox_to_anchor=(0.02, 0.9), fontsize=10)

# Adjust the layout to prevent overlaps
plt.tight_layout()

# Show the plot
plt.show()