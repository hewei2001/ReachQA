import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define planets and minerals
planets = ['Aurora', 'Zenthia', 'Thalios']
minerals = ['Helium-3', 'Iron', 'Lithium']

# Quantities of minerals (in arbitrary units) extracted from each planet
quantities = np.array([
    [120, 180, 90],   # Aurora
    [150, 130, 100],  # Zenthia
    [100, 160, 110]   # Thalios
])

# Set up the figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define positions for the bars
x_pos, y_pos = np.meshgrid(np.arange(quantities.shape[1]), np.arange(quantities.shape[0]))
x_pos = x_pos.flatten()
y_pos = y_pos.flatten()
z_pos = np.zeros_like(x_pos)

# Flatten the quantities array for plotting
quantities_flat = quantities.flatten()

# Define width and depth for each bar
dx = dy = 0.4

# Define colors for each mineral type
colors = ['skyblue', 'coral', 'limegreen']

# Assign colors to each bar based on the mineral
mineral_colors = np.array(colors)[np.tile(np.arange(len(minerals)), len(planets))]

# Create 3D bars
ax.bar3d(x_pos, y_pos, z_pos, dx, dy, quantities_flat, color=mineral_colors, alpha=0.8, shade=True)

# Set labels and title
ax.set_xlabel('Minerals')
ax.set_ylabel('Planets')
ax.set_zlabel('Quantity (Units)')
ax.set_title('Futuristic Space Mineral Extraction\nby Planet and Mineral Type', fontsize=14, fontweight='bold', pad=20)

# Customize tick labels and set view angle
ax.set_xticks(np.arange(len(minerals)))
ax.set_xticklabels(minerals, fontsize=10, rotation=30, ha='right')
ax.set_yticks(np.arange(len(planets)))
ax.set_yticklabels(planets, fontsize=10)
ax.view_init(elev=30, azim=210)

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Add a legend
legend_handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(legend_handles, minerals, loc='upper left', bbox_to_anchor=(1.1, 0.85), fontsize=10, title='Minerals')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()