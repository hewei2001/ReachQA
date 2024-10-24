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

# Create figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot each species with distinct colors and sizes
ax.scatter(elevation, tree_density_foxes, water_availability_foxes, s=population_foxes, color='r', alpha=0.6, edgecolor='w', label='Eldergrove Foxes')
ax.scatter(elevation, tree_density_owls, water_availability_owls, s=population_owls, color='g', alpha=0.6, edgecolor='w', label='Eldergrove Owls')
ax.scatter(elevation, tree_density_deer, water_availability_deer, s=population_deer, color='b', alpha=0.6, edgecolor='w', label='Eldergrove Deer')

# Set labels and title
ax.set_xlabel('Elevation (m)', fontsize=10)
ax.set_ylabel('Tree Density (trees/hectare)', fontsize=10)
ax.set_zlabel('Water Availability', fontsize=10)
ax.set_title('Eldergrove Sanctuary:\nSpecies Distribution Across Environmental Gradients', fontsize=14, fontweight='bold')

# Add a legend
ax.legend(title='Species', loc='upper left')

# Adjust the viewing angle for optimal perspective
ax.view_init(elev=20, azim=135)

# Apply tight layout to avoid overlap and improve spacing
plt.tight_layout()

# Show the plot
plt.show()