import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyBboxPatch

# Define the regions and operating systems
regions = ['North America', 'Europe', 'Asia']
os_types = ['Android', 'iOS', 'Others']

# Market share data in percentages
market_share = [
    [40, 55, 5],  # North America
    [65, 30, 5],  # Europe
    [80, 15, 5]   # Asia
]

# Set up positions for the bars
x_pos = np.arange(len(regions))
y_pos = np.arange(len(os_types))
x_pos, y_pos = np.meshgrid(x_pos, y_pos)
x_pos, y_pos = x_pos.flatten(), y_pos.flatten()
z_pos = np.zeros_like(x_pos)

# Heights of the bars
dx = dy = 0.3
dz = np.array(market_share).flatten()

# Create the 3D bar plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Define color for each operating system using a gradient
colors = ['#8FCB9B', '#4682B4', '#FFD700']

# Plot the bars with the assigned colors
ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, color=[colors[i % 3] for i in y_pos], alpha=0.9)

# Annotate data on top of bars
for i in range(len(dz)):
    ax.text(x_pos[i], y_pos[i], dz[i] + 2, '%d' % dz[i], ha='center', va='bottom', fontsize=9, fontweight='bold')

# Set axis labels and title with line breaks
ax.set_xlabel('Regions', labelpad=15)
ax.set_ylabel('Operating Systems', labelpad=15)
ax.set_zlabel('Market Share (%)', labelpad=15)
ax.set_title('Global Market Share of Smartphones\nby Operating System (2023)', fontsize=16, fontweight='bold')

# Configure ticks and labels
ax.set_xticks(np.arange(len(regions)))
ax.set_xticklabels(regions, rotation=20, ha='right')
ax.set_yticks(np.arange(len(os_types)))
ax.set_yticklabels(os_types)
ax.set_zlim(0, 100)

# Improve 3D perspective and shading
ax.view_init(elev=20., azim=135)

# Adding a legend for operating systems
legend_patches = [FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.2", fc=color) for color in colors]
ax.legend(legend_patches, os_types, title='Operating Systems', loc='upper left', bbox_to_anchor=(1.1, 1))

# Ensure layout is clear and elements don't overlap
plt.tight_layout()

# Show the plot
plt.show()