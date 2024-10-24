import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Data preparation
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal']
capacities = np.array([
    [120, 200, 80, 40],    # Africa
    [300, 500, 200, 100],  # Asia
    [250, 300, 150, 60],   # Europe
    [180, 240, 100, 50],   # North America
    [160, 180, 90, 40],    # South America
    [100, 120, 70, 30],    # Oceania
])

# Create meshgrid for bar positions
xpos, ypos = np.meshgrid(np.arange(len(continents)), np.arange(len(energy_sources)))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

# Bar dimensions and capacities
dx = dy = 0.4
dz = capacities.flatten()

# Create the figure and 3D axes
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Colors for the bars
colors = ['#FFD700', '#00FF00', '#0000FF', '#FF6347']  # Yellow, Green, Blue, Tomato

# Plot each energy source separately for clarity
for i, color in enumerate(colors):
    ax.bar3d(xpos[ypos == i], ypos[ypos == i], zpos[ypos == i], dx, dy, dz[ypos == i], color=color, alpha=0.8, label=energy_sources[i])

# Setting labels and title
ax.set_xlabel('Continent')
ax.set_ylabel('Energy Source')
ax.set_zlabel('Capacity (GW)')
ax.set_title('Renewable Energy Projections for 2025\nAcross Different Continents')

# Customizing tick labels for better visibility
ax.set_xticks(np.arange(len(continents)) + dx/2)
ax.set_xticklabels(continents, rotation=45, ha='right')
ax.set_yticks(np.arange(len(energy_sources)) + dy/2)
ax.set_yticklabels(energy_sources)

# Adjusting the view angle for better visualization
ax.view_init(elev=20, azim=130)

# Adding a grid for visual clarity
ax.grid(True)

# Adding a legend
ax.legend(loc='upper right')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()