import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data Setup
planets = ['Earth', 'Mars', 'Venus', 'Jupiter', 'Saturn', 'Neptune']
resources = ['Energy Crystals', 'Organic Materials', 'Metal Alloys']

# Explicit data for resource distribution (in thousands of tons)
distribution = np.array([
    [50, 60, 40],  # Earth
    [70, 50, 60],  # Mars
    [65, 55, 70],  # Venus
    [40, 75, 65],  # Jupiter
    [55, 45, 80],  # Saturn
    [60, 50, 70]   # Neptune
])

# Bar positions
num_planets = len(planets)
num_resources = len(resources)
xpos, ypos = np.meshgrid(np.arange(num_planets), np.arange(num_resources), indexing="ij")
xpos = xpos.flatten()
ypos = ypos.flatten()

# Bottom position (cumulative) for the stacked bar
zpos = np.zeros(num_planets * num_resources)

# Bar dimensions
dx = dy = 0.5
dz = distribution.flatten()

# Colors for each resource type
colors = ['#FF9999', '#66B2FF', '#99FF99']

# Plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Stack the bars for each planet by resources
for i, color in enumerate(colors):
    ax.bar3d(
        xpos[i::num_resources], ypos[i::num_resources], zpos[i::num_resources],
        dx, dy, dz[i::num_resources],
        color=color, alpha=0.8, edgecolor='k', label=resources[i] if xpos[i] == 0 else ""
    )
    # Update zpos for stacking
    zpos[i::num_resources] += dz[i::num_resources]

# Customizing axes labels and title
ax.set_xlabel('Planets', labelpad=10)
ax.set_ylabel('Resources', labelpad=10)
ax.set_zlabel('Quantity (thousands of tons)', labelpad=10)
ax.set_xticks(np.arange(num_planets))
ax.set_xticklabels(planets, rotation=45, ha='right')
ax.set_yticks(np.arange(num_resources))
ax.set_yticklabels(resources)
ax.set_title('Galactic Trade Federation:\n2142 Resource Distribution', fontsize=14, weight='bold', pad=20)

# Adjust viewing angle for better visibility
ax.view_init(elev=20, azim=45)

# Creating a legend
ax.legend(title='Resource Types', title_fontsize='12', loc='upper left', bbox_to_anchor=(1.05, 1))

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()