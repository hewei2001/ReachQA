import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap

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
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Color map for the bars
cmap = LinearSegmentedColormap.from_list('capacity_cmap', ['#f7fcfd', '#00441b'])
norm = plt.Normalize(dz.min(), dz.max())

# Plot each energy source separately
for i in range(len(energy_sources)):
    xi = xpos[ypos == i]
    yi = ypos[ypos == i]
    zi = dz[ypos == i]
    ax.bar3d(xi, yi, zpos[ypos == i], dx, dy, zi, color=cmap(norm(zi)), alpha=0.9)
    for x, y, z in zip(xi, yi, zi):
        ax.text(x, y, z + 5, f'{z}', ha='center', va='bottom', fontsize=8, color='black')

# Setting labels and title
ax.set_xlabel('Continent', labelpad=16)
ax.set_ylabel('Energy Source', labelpad=16)
ax.set_zlabel('Capacity (GW)', labelpad=16)
ax.set_title('Renewable Energy Projections for 2025\nAcross Different Continents and Sources', pad=20)

# Customizing tick labels
ax.set_xticks(np.arange(len(continents)) + dx/2)
ax.set_xticklabels(continents, rotation=45, ha='right')
ax.set_yticks(np.arange(len(energy_sources)) + dy/2)
ax.set_yticklabels(energy_sources)

# Adjusting the view angle for better visualization
ax.view_init(elev=25, azim=135)

# Adding a grid
ax.grid(True, linestyle='--', alpha=0.5)

# Adding a colorbar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, shrink=0.5, aspect=10)
cbar.set_label('Capacity Color Scale')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()