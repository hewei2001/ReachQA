import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define data
years = np.array(['2018', '2019', '2020', '2021', '2022'])
cities = ['New York', 'London', 'Tokyo']
innovations = ['Electric Buses', 'Bike Sharing', 'Autonomous Vehicles', 'Electric Scooters']

# Number of units for each innovation in each city from 2018 to 2022
transport_data = np.array([
    # New York
    [[100, 80, 50, 120], [120, 100, 60, 140], [150, 130, 80, 160], [180, 160, 90, 180], [220, 200, 110, 210]],
    # London
    [[90, 70, 40, 100], [110, 85, 55, 120], [140, 110, 70, 140], [170, 140, 85, 170], [200, 170, 100, 200]],
    # Tokyo
    [[80, 60, 30, 90], [100, 75, 45, 110], [130, 95, 60, 130], [160, 125, 75, 160], [190, 155, 90, 190]]
])

# Create a figure and 3D axes
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define positions for bars
xpos, ypos = np.meshgrid(np.arange(len(cities)), np.arange(len(years)), indexing="ij")
xpos = xpos.flatten()
ypos = ypos.flatten()

# Initialize z position to zero (ground level of bars)
zpos = np.zeros_like(xpos, dtype=float)

# Bar dimensions
dx = dy = 0.5

# Colors for each innovation
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Plot each innovation type as stacked bars
for i, innovation in enumerate(innovations):
    dz = transport_data[:, :, i].flatten()
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors[i], label=innovation, alpha=0.8)
    zpos += dz

# Labeling the axes and title
ax.set_xlabel('Cities')
ax.set_ylabel('Years')
ax.set_zlabel('Number of Units')
ax.set_xticks(np.arange(len(cities)) + dx / 2)
ax.set_xticklabels(cities, rotation=30, ha='right')
ax.set_yticks(np.arange(len(years)) + dy / 2)
ax.set_yticklabels(years)
ax.set_title('Deployment of Urban Transportation Innovations\n in Major Cities (2018-2022)', pad=20)

# Adjust view for better visibility
ax.view_init(elev=20., azim=120)

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1))

# Adjust layout for better presentation
plt.tight_layout()

# Display plot
plt.show()