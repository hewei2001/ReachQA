import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define data for the plot
sectors = ['Alpha', 'Beta', 'Gamma']
planets = ['Planet A', 'Planet B', 'Planet C', 'Planet D', 'Planet E']
resources = ['Metals', 'Crystals', 'Isotopes']

# Predefined mining yields in tons (imaginary data)
alpha_yields = np.array([
    [500, 300, 200],  
    [400, 250, 350],  
    [300, 400, 150],  
    [450, 200, 300],  
    [350, 280, 320],  
])

beta_yields = np.array([
    [250, 350, 400],  
    [300, 500, 200],  
    [350, 300, 250],  
    [400, 150, 450],  
    [500, 200, 300],  
])

gamma_yields = np.array([
    [450, 400, 100],  
    [350, 350, 150],  
    [400, 250, 300],  
    [300, 200, 400],  
    [250, 300, 350],  
])

yields_data = [alpha_yields, beta_yields, gamma_yields]

# Create a new figure for the 3D plot
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111, projection='3d')

# Set up positions and bar dimensions
num_planets = len(planets)
colors = ['#ff9999', '#66b3ff', '#99ff99']
dx = dy = 0.4

# Plot each sector's data
for sector_idx, sector_yields in enumerate(yields_data):
    xpos = np.arange(num_planets)
    ypos = np.full(num_planets, sector_idx)

    zpos = np.zeros(num_planets)
    for resource_idx in range(len(resources)):
        dz = sector_yields[:, resource_idx]  
        ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors[resource_idx], alpha=0.8)
        zpos += dz

# Set labels and title
ax.set_xticks(np.arange(num_planets))
ax.set_xticklabels(planets)
ax.set_yticks(np.arange(len(sectors)))
ax.set_yticklabels(sectors)
ax.set_zlabel('Yield (tons)')

ax.set_title('Galactic Resource Allocation:\nInterplanetary Mining Yields Study', fontsize=16, fontweight='bold')
ax.set_xlabel('Planets')
ax.set_ylabel('Sectors')

# Create a custom legend
legend_proxy = [plt.Rectangle((0, 0), 1, 1, fc=col) for col in colors]
ax.legend(legend_proxy, resources, title="Resources", loc='upper left')

# Adjust viewing angle
ax.view_init(elev=25, azim=135)

# Automatically adjust layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()