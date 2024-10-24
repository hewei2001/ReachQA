import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define primary data
years = np.array(['2018', '2019', '2020', '2021', '2022'])
cities = ['New York', 'London', 'Tokyo']
innovations = ['Electric Buses', 'Bike Sharing', 'Autonomous Vehicles', 'Electric Scooters']

transport_data = np.array([
    [[100, 80, 50, 120], [120, 100, 60, 140], [150, 130, 80, 160], [180, 160, 90, 180], [220, 200, 110, 210]],
    [[90, 70, 40, 100], [110, 85, 55, 120], [140, 110, 70, 140], [170, 140, 85, 170], [200, 170, 100, 200]],
    [[80, 60, 30, 90], [100, 75, 45, 110], [130, 95, 60, 130], [160, 125, 75, 160], [190, 155, 90, 190]]
])

# Additional data: Government investment in millions
investment_data = np.array([
    [50, 55, 65, 70, 85],  # New York
    [45, 50, 60, 65, 80],  # London
    [40, 47, 58, 63, 75]   # Tokyo
])

# Create a figure and 3D axes
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Define positions for bars
xpos, ypos = np.meshgrid(np.arange(len(cities)), np.arange(len(years)), indexing="ij")
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos, dtype=float)

dx = dy = 0.3
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Plot each innovation type as stacked bars
for i, innovation in enumerate(innovations):
    dz = transport_data[:, :, i].flatten()
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors[i], label=innovation, alpha=0.8)
    zpos += dz

# Overlay plot: Line plot for investment
for city_index, city in enumerate(cities):
    ax.plot([city_index] * len(years), np.arange(len(years)), investment_data[city_index], 
            zdir='z', linestyle='--', marker='o', color='k', label=f'Investment {city}' if city_index == 0 else '')

# Labeling the axes and title
ax.set_xlabel('Cities')
ax.set_ylabel('Years')
ax.set_zlabel('Number of Units / Investment ($M)')
ax.set_xticks(np.arange(len(cities)) + dx / 2)
ax.set_xticklabels(cities, rotation=30, ha='right')
ax.set_yticks(np.arange(len(years)) + dy / 2)
ax.set_yticklabels(years)
ax.set_title('Urban Transportation Innovations Deployment and Investment\n in Major Cities (2018-2022)', pad=20)

# Adjust view for better visibility
ax.view_init(elev=25, azim=135)

# Adjust layout for better presentation
plt.tight_layout()

# Add legends
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

# Display plot
plt.show()