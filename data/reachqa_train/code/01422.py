import matplotlib.pyplot as plt
import numpy as np

# Define districts and types of green spaces
districts = ['North', 'South', 'East', 'West', 'Central']
green_spaces = ['Parks', 'Gardens', 'Urban Forests']

# Percentage of area covered by each type of green space in each district
area_distribution = np.array([
    [25, 15, 10],  # North
    [30, 10, 15],  # South
    [20, 25, 15],  # East
    [15, 20, 20],  # West
    [35, 10, 5]    # Central
])

# Setup positions for the 3D bar chart
xpos, ypos = np.meshgrid(np.arange(len(districts)), np.arange(len(green_spaces)))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

# Values for bar heights
dz = area_distribution.flatten()

# Width and depth of bars
dx = dy = 0.3

# Colors for different types of green spaces
colors = ['#66c2a5', '#fc8d62', '#8da0cb']

# Create a 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot each type of green space with different colors
for i in range(len(green_spaces)):
    ax.bar3d(xpos[ypos == i], ypos[ypos == i], zpos[ypos == i], dx, dy, dz[ypos == i],
             color=colors[i], alpha=0.8, label=green_spaces[i])

# Set axis labels and title
ax.set_xlabel('Districts', fontsize=12, labelpad=10)
ax.set_ylabel('Green Space Type', fontsize=12, labelpad=10)
ax.set_zlabel('Percentage (%)', fontsize=12, labelpad=10)

# Set ticks and labels
ax.set_xticks(np.arange(len(districts)))
ax.set_xticklabels(districts, fontsize=10, rotation=45, ha='right')
ax.set_yticks(np.arange(len(green_spaces)))
ax.set_yticklabels(green_spaces, fontsize=10)
ax.set_zlim(0, 40)

# Improve visibility by adjusting the viewing angle
ax.view_init(elev=20, azim=135)

# Add a grid for better readability
ax.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.5)

# Title and legend
ax.set_title('Green Space Distribution in EcoCity Districts', fontsize=14, weight='bold', pad=20)
ax.legend(title='Type of Green Space', loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1))

# Optimize layout
plt.tight_layout()

# Show the plot
plt.show()