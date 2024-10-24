import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define celestial bodies
bodies = ['Mars', 'Europa', 'Titan', 'Ganymede', 'Venus', 'Callisto', 'Triton']

# Fictional distances from Earth in light-years
distances = np.array([0.000015, 0.00063, 0.0000012, 0.00063, 0.000011, 0.00063, 0.0007])

# Fictional trading activity indices
activity_index = np.array([75, 50, 60, 70, 80, 45, 55])

# Fictional trading volumes (size of bubbles)
volumes = np.array([300, 200, 250, 270, 320, 190, 210])

# Set up the 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the scatter chart
scatter = ax.scatter(distances, activity_index, zs=0, zdir='z', s=volumes, c=volumes, cmap='plasma', depthshade=True, alpha=0.8)

# Set labels and title
ax.set_xlabel('Distance from Earth\n(Light Years)', labelpad=10)
ax.set_ylabel('Trading Activity Index', labelpad=10)
ax.set_zlabel(' ', labelpad=10)  # Empty z-label as points are projected on a 2D plane
ax.set_title('Interplanetary Trading Post Analysis\nin the Milky Way Galaxy', fontsize=16, fontweight='bold', pad=20)

# Add annotations for each planet/moon
for i, body in enumerate(bodies):
    ax.text(distances[i], activity_index[i], 0, body, fontsize=9, ha='center')

# Add a color bar
color_bar = fig.colorbar(scatter, ax=ax, pad=0.1, aspect=20)
color_bar.set_label('Trading Volume\n(Arbitrary Units)', rotation=270, labelpad=15)

# Set a custom view angle for better perspective
ax.view_init(elev=25, azim=135)

# Adjust layout for better readability
plt.tight_layout()

# Display the plot
plt.show()