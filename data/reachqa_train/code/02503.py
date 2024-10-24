import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from mpl_toolkits.mplot3d import Axes3D

# Define celestial bodies and resource types
celestial_bodies = ['Mars', 'Moon', 'Asteroid Belt']
resource_types = ['Rare Minerals', 'Valuable Metals', 'Water Ice']

# Define extraction efficiency (kg/hour) for each resource type on each celestial body
efficiency_data = np.array([
    [500, 800, 300],  # Mars
    [450, 650, 400],  # Moon
    [600, 700, 500]   # Asteroid Belt
])

# Create a figure and a 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define positions for bars
x_positions, y_positions = np.meshgrid(np.arange(efficiency_data.shape[1]), 
                                       np.arange(efficiency_data.shape[0]))
x_positions = x_positions.flatten()
y_positions = y_positions.flatten()
z_positions = np.zeros_like(x_positions)

# Flatten efficiency data for bar heights
heights = efficiency_data.flatten()

# Define the width and depth of each bar
dx = dy = 0.4

# Colors for bars using a gradient
norm = mcolors.Normalize(vmin=heights.min(), vmax=heights.max())
colors = plt.cm.viridis(norm(heights))

# Plot the bars with annotations
for i in range(len(heights)):
    ax.bar3d(x_positions[i], y_positions[i], z_positions[i], dx, dy, heights[i],
             color=colors[i], alpha=0.9)
    ax.text(x_positions[i], y_positions[i], heights[i], f'{heights[i]}',
            color='black', ha='center', va='bottom', fontsize=8)

# Set labels and ticks with adjustments
ax.set_xticks(np.arange(len(resource_types)))
ax.set_xticklabels(resource_types, fontsize=10, rotation=45, ha='right')
ax.set_yticks(np.arange(len(celestial_bodies)))
ax.set_yticklabels(celestial_bodies, fontsize=10)
ax.set_zlabel('Efficiency (kg/hour)', fontsize=12)

# Set the chart title with line breaks for readability
ax.set_title('Efficiency of Interplanetary Resource Extraction\n'
             'Across Different Celestial Bodies (2142)', 
             fontsize=14, fontweight='bold', pad=20)

# Add grid lines for better readability
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Adjust the viewing angle for better visibility
ax.view_init(elev=30, azim=120)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()