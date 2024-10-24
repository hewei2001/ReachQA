import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define data
years = np.array(['2015', '2016', '2017', '2018', '2019'])
continents = ['Asia', 'Africa', 'South America']
spices = ['Turmeric', 'Black Pepper', 'Cinnamon', 'Saffron']

# Production volume (in tons) for each spice on each continent from 2015 to 2019
production_data = np.array([
    # Asia
    [[250, 300, 150, 50], [270, 320, 160, 55], [290, 340, 170, 60], [310, 360, 180, 65], [330, 380, 190, 70]],
    # Africa
    [[200, 150, 100, 30], [220, 170, 110, 35], [240, 190, 120, 40], [260, 210, 130, 45], [280, 230, 140, 50]],
    # South America
    [[180, 100, 90, 20], [200, 120, 100, 25], [220, 140, 110, 30], [240, 160, 120, 35], [260, 180, 130, 40]],
])

# Create a figure and 3D axes
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define positions for bars
xpos, ypos = np.meshgrid(np.arange(len(continents)), np.arange(len(years)), indexing="ij")
xpos = xpos.flatten()
ypos = ypos.flatten()

# Initialize z position to zero (ground level of bars)
zpos = np.zeros_like(xpos, dtype=float)

# Bar dimensions
dx = dy = 0.5

# Colors for each spice
colors = ['#FFA07A', '#FF4500', '#8B4513', '#FFD700']

# Plot each spice as stacked bars
for i, spice in enumerate(spices):
    dz = production_data[:, :, i].flatten()
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors[i], label=spice, alpha=0.8)
    zpos += dz

# Labeling the axes and title
ax.set_xlabel('Continents')
ax.set_ylabel('Years')
ax.set_zlabel('Production Volume (tons)')
ax.set_xticks(np.arange(len(continents)) + dx / 2)
ax.set_xticklabels(continents, rotation=45, ha='right')
ax.set_yticks(np.arange(len(years)) + dy / 2)
ax.set_yticklabels(years)
ax.set_title('Evolution of Culinary Ingredients:\nGlobal Spice Production Across Continents (2015-2019)', pad=20)

# Adjust view for better visibility
ax.view_init(elev=30., azim=135)

# Add legend
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

# Adjust layout for better presentation
plt.tight_layout()

# Display plot
plt.show()