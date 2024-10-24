import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Celestial bodies and resources
celestial_bodies = ['Moon', 'Mars', 'Europa', 'Titan']
resources = ['Water (H2O)', 'Helium-3 (He-3)', 'Rare Earth Elements (REEs)']

# Data: Amounts of resources extracted (in millions of tons)
data = np.array([
    [20, 5, 1],  # Moon
    [35, 3, 4],  # Mars
    [50, 1, 2],  # Europa
    [45, 2, 3]   # Titan
])

# Create figure and 3D axes
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define the position of bars
xpos, ypos = np.meshgrid(np.arange(len(celestial_bodies)), np.arange(len(resources)))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

# Dimensions of the bars
dx = dy = 0.4
dz = data.flatten()

# Colors for each type of resource
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Plot bars
for i in range(len(resources)):
    ax.bar3d(xpos[i::len(resources)], ypos[i::len(resources)], zpos[i::len(resources)], 
             dx, dy, dz[i::len(resources)], color=colors[i], alpha=0.8, label=resources[i])

# Customize the plot
ax.set_xticks(np.arange(len(celestial_bodies)))
ax.set_xticklabels(celestial_bodies, rotation=45, ha='right')
ax.set_yticks(np.arange(len(resources)))
ax.set_yticklabels(resources)
ax.set_zlabel('Extraction (Millions of Tons)', labelpad=10)
ax.set_title('Interplanetary Resource Utilization\nin the Solar System (2142)', fontsize=14, fontweight='bold', pad=20)

# Add legend
ax.legend(title='Resources', loc='upper right')

# Enhance readability by adjusting the view
ax.view_init(elev=25, azim=35)

# Add grid for better readability
ax.xaxis.grid(True, linestyle='--', color='gray', alpha=0.5)
ax.yaxis.grid(True, linestyle='--', color='gray', alpha=0.5)

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()