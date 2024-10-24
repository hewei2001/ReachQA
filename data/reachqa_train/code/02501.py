import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Synthetic data representing species in the Eldergrove Sanctuary
elevation = np.array([400, 450, 500, 550, 600, 650, 700])  # Elevation in meters
tree_density_foxes = np.array([30, 40, 50, 55, 60, 65, 70])  # Trees per hectare for foxes
water_availability_foxes = np.array([80, 70, 60, 50, 45, 40, 35])  # Water availability for foxes
population_foxes = np.array([150, 130, 110, 90, 70, 50, 30])  # Population size for foxes

tree_density_owls = np.array([25, 35, 45, 50, 55, 60, 65])  # Trees per hectare for owls
water_availability_owls = np.array([75, 65, 55, 45, 40, 35, 30])  # Water availability for owls
population_owls = np.array([100, 120, 140, 160, 180, 200, 220])  # Population size for owls

tree_density_deer = np.array([40, 50, 60, 65, 70, 75, 80])  # Trees per hectare for deer
water_availability_deer = np.array([85, 75, 65, 55, 50, 45, 40])  # Water availability for deer
population_deer = np.array([80, 100, 120, 140, 160, 180, 200])  # Population size for deer

# Calculate a derived metric: Population per tree density
population_density_foxes = population_foxes / tree_density_foxes
population_density_owls = population_owls / tree_density_owls
population_density_deer = population_deer / tree_density_deer

# Create a figure with 1x2 subplots
fig = plt.figure(figsize=(16, 8))

# 3D scatter plot
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(elevation, tree_density_foxes, water_availability_foxes, s=population_foxes, color='r', alpha=0.6, edgecolor='w', label='Eldergrove Foxes')
ax1.scatter(elevation, tree_density_owls, water_availability_owls, s=population_owls, color='g', alpha=0.6, edgecolor='w', label='Eldergrove Owls')
ax1.scatter(elevation, tree_density_deer, water_availability_deer, s=population_deer, color='b', alpha=0.6, edgecolor='w', label='Eldergrove Deer')
ax1.set_xlabel('Elevation (m)', fontsize=10)
ax1.set_ylabel('Tree Density (trees/hectare)', fontsize=10)
ax1.set_zlabel('Water Availability', fontsize=10)
ax1.set_title('Eldergrove Sanctuary:\nSpecies Distribution Across Environmental Gradients', fontsize=14, fontweight='bold')
ax1.legend(title='Species', loc='upper left')
ax1.view_init(elev=20, azim=135)

# 2D line plot
ax2 = fig.add_subplot(122)
ax2.plot(elevation, population_density_foxes, marker='o', color='r', label='Eldergrove Foxes')
ax2.plot(elevation, population_density_owls, marker='o', color='g', label='Eldergrove Owls')
ax2.plot(elevation, population_density_deer, marker='o', color='b', label='Eldergrove Deer')
ax2.set_xlabel('Elevation (m)', fontsize=10)
ax2.set_ylabel('Population Density (pop/trees)', fontsize=10)
ax2.set_title('Species Population Density Across Elevation', fontsize=12, fontweight='bold')
ax2.legend(title='Species', loc='upper right')
ax2.grid(True)

# Apply tight layout
plt.tight_layout()

# Show the plots
plt.show()