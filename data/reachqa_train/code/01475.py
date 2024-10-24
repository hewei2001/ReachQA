import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Data for the 3D bar chart
celestial_bodies = ['Zypheria', 'Krypton', 'Oberon', 'Lithios', 'Andara']
missions = ['Atmosphere Study', 'Geological Survey', 'Life Search', 'Mineral Analysis', 'Cultural Relic Exploration']
exploration_times = np.array([
    [14, 18, 12, 9, 22],
    [10, 24, 8, 15, 19],
    [20, 15, 5, 14, 21],
    [9, 14, 10, 19, 12],
    [22, 10, 14, 7, 25]
])

# Compute positions for bars
x_pos, y_pos = np.meshgrid(np.arange(len(celestial_bodies)), np.arange(len(missions)))
x_pos = x_pos.flatten()
y_pos = y_pos.flatten()
z_pos = np.zeros_like(x_pos)

# Flatten the exploration times for bar heights
exploration_values = exploration_times.flatten()

# Define bar dimensions
dx = dy = 0.4
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#9370DB'] * len(celestial_bodies)

# Create 3D bar chart
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Plot 3D bars
ax.bar3d(x_pos, y_pos, z_pos, dx, dy, exploration_values, color=colors, alpha=0.8)

# Label axes
ax.set_xlabel('Celestial Bodies', fontsize=10, labelpad=20)
ax.set_ylabel('Missions', fontsize=10, labelpad=20)
ax.set_zlabel('Exploration Time (Months)', fontsize=10, labelpad=10)

# Set ticks and labels
ax.set_xticks(np.arange(len(celestial_bodies)) + dx / 2)
ax.set_xticklabels(celestial_bodies, rotation=45, ha='right')
ax.set_yticks(np.arange(len(missions)) + dy / 2)
ax.set_yticklabels(missions)

# Set viewing angle
ax.view_init(elev=30, azim=135)

# Add title
ax.set_title(
    'Intergalactic Space Missions and Exploration Time\n'
    'An Imaginary Glimpse into the Future of Space Exploration',
    fontsize=14, fontweight='bold', pad=40
)

# Show grid for better readability
ax.grid(True, linestyle='--', linewidth=0.5)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()