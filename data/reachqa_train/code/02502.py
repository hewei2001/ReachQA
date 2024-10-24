import matplotlib.pyplot as plt
import numpy as np
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
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Define positions for bars
x_positions = np.arange(efficiency_data.shape[1])
y_positions = np.arange(efficiency_data.shape[0])
x_positions, y_positions = np.meshgrid(x_positions, y_positions)

# Flatten the matrices for bar plotting
x_positions = x_positions.flatten()
y_positions = y_positions.flatten()
z_positions = np.zeros_like(x_positions)

# Flatten efficiency data for the bar heights
heights = efficiency_data.flatten()

# Define the width and depth of each bar
dx = dy = 0.4

# Colors for different celestial bodies
colors = ['royalblue', 'forestgreen', 'gold']

# Plot the bars
for i in range(len(heights)):
    ax.bar3d(x_positions[i], y_positions[i], z_positions[i], dx, dy, heights[i],
             color=colors[y_positions[i]], alpha=0.8)

# Set labels and ticks
ax.set_xticks(np.arange(len(resource_types)))
ax.set_xticklabels(resource_types, fontsize=10, rotation=45, ha='right')
ax.set_yticks(np.arange(len(celestial_bodies)))
ax.set_yticklabels(celestial_bodies, fontsize=10)
ax.set_zlabel('Efficiency (kg/hour)', fontsize=12)

# Set the chart title
ax.set_title('Efficiency of Interplanetary Resource Extraction (2142)\nAcross Different Celestial Bodies', fontsize=14, fontweight='bold', pad=20)

# Adjust the viewing angle for better visibility
ax.view_init(elev=30, azim=120)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()