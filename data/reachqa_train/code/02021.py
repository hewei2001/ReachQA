import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the sectors and planets
sectors = ['Agriculture', 'Technology', 'Healthcare', 'Infrastructure', 'Education']
planets = ['Aether', 'Crystalia', 'Verdantia']

# Define the allocation of resources (in arbitrary units) for each colony
resource_data = np.array([
    [20, 25, 15, 30, 10],  # Aether
    [15, 30, 25, 20, 10],  # Crystalia
    [30, 15, 20, 25, 10],  # Verdantia
])

# Define colors for each sector
colors = ['#76C7C0', '#FFB6C1', '#FFD700', '#6495ED', '#9ACD32']

# Create a 3D bar chart
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Set bar parameters
width = 0.2
depth = width

# Initialize xpos and ypos for the 3D plot
xpos = np.arange(len(sectors))
ypos = np.arange(len(planets))

# Plot each planet's resource allocation
for i, planet in enumerate(planets):
    bottom_heights = np.zeros(len(sectors))
    for j, sector in enumerate(sectors):
        ax.bar3d(xpos[j] + i * width, ypos[i], bottom_heights[j], 
                 width, depth, resource_data[i, j], 
                 color=colors[j], alpha=0.85)
        bottom_heights[j] += resource_data[i, j]

# Set ticks and labels
ax.set_xticks(xpos + width)
ax.set_xticklabels(sectors, rotation=15, ha='right')
ax.set_yticks(ypos)
ax.set_yticklabels(planets)
ax.set_zlabel('Resource Allocation Units')
ax.set_xlabel('Sectors')
ax.set_ylabel('Planets')
ax.set_title('Interplanetary Resource Allocation\nin Future Colonies - Year 2150', fontsize=14, fontweight='bold', pad=20)

# Customize the view angle for better visibility
ax.view_init(elev=20, azim=135)

# Automatically adjust layout for better fit
plt.tight_layout()

# Display the chart
plt.show()