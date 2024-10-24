import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define cities and plant types
cities = ['New York', 'London', 'Tokyo']
plant_types = ['Trees', 'Shrubs', 'Flower Beds']
years = np.array(['2018', '2019', '2020', '2021', '2022'])

# Data: The number of each plant type planted in thousands
data = np.array([
    # Trees
    [[30, 25, 40], [35, 28, 38], [38, 30, 35], [40, 32, 32], [42, 34, 30]],
    # Shrubs
    [[20, 18, 22], [22, 20, 24], [24, 22, 26], [26, 24, 28], [28, 26, 30]],
    # Flower Beds
    [[15, 10, 12], [16, 11, 14], [18, 13, 16], [20, 15, 18], [22, 17, 20]],
])

# Initialize the figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define positions for the bars
x_pos = np.arange(len(years))
y_pos = np.arange(len(cities))
x_pos, y_pos = np.meshgrid(x_pos, y_pos)
x_pos = x_pos.ravel()
y_pos = y_pos.ravel()
z_pos = np.zeros_like(x_pos)

# Colors for each plant type
colors = ['#8bc34a', '#ff9800', '#e91e63']

# Plot each plant type with bars stacking on top of each other
for plant_idx, plant_type in enumerate(plant_types):
    dz = data[plant_idx].reshape(-1)
    ax.bar3d(x_pos, y_pos, z_pos, dx=0.5, dy=0.5, dz=dz, color=colors[plant_idx], alpha=0.8, label=plant_type)
    z_pos += dz

# Labeling the axes
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, rotation=45, ha='right', fontsize=10)
ax.set_yticks(np.arange(len(cities)))
ax.set_yticklabels(cities, fontsize=10)
ax.set_xlabel('Year', labelpad=10)
ax.set_ylabel('City', labelpad=10)
ax.set_zlabel('Number of Plants (Thousands)', labelpad=10)

# Title and legend
ax.set_title('Unveiling Urban Greenery:\nA 3D Stacked Analysis of Plant Types in Major Cities', pad=30, fontsize=14, weight='bold')
ax.legend(title='Plant Types', loc='upper left', bbox_to_anchor=(0.1, 0.9))

# Adjust the view angle for better visibility
ax.view_init(elev=25, azim=-60)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()