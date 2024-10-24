import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Elemental composition data for each planet (percentages)
elements = ['Iron', 'Silicon', 'Oxygen', 'Carbon', 'Hydrogen']
arcturus_i = [32, 16, 30, 10, 12]
arcturus_ii = [22, 24, 28, 15, 11]
arcturus_iii = [28, 19, 33, 8, 12]

# Data for each planet
data = np.array([arcturus_i, arcturus_ii, arcturus_iii])
planet_names = ['Arcturus I', 'Arcturus II', 'Arcturus III']

# Set up the figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define bar positions and their attributes
num_elements = len(elements)
num_planets = data.shape[0]

x_pos, y_pos = np.meshgrid(np.arange(num_elements), np.arange(num_planets))
x_pos = x_pos.flatten()
y_pos = y_pos.flatten()
z_pos = np.zeros_like(x_pos)

dx = dy = 0.8
dz = data.flatten()

# Define colors for visual distinction
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the bars
ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, color=[colors[i % num_elements] for i in range(len(dz))], edgecolor='black')

# Set axis labels
ax.set_xlabel('Elements', fontsize=12)
ax.set_ylabel('Planets', fontsize=12)
ax.set_zlabel('Percentage (%)', fontsize=12)

# Set ticks and labels with adjustments to avoid overlap
ax.set_xticks(np.arange(num_elements))
ax.set_xticklabels(elements, fontsize=10, rotation=45, ha='right')
ax.set_yticks(np.arange(len(planet_names)))
ax.set_yticklabels(planet_names, fontsize=10)

# Title and legend for clarity
ax.set_title('Elemental Composition of Planets\nin the Arcturus System', fontsize=14, pad=20)
custom_legend = [plt.Line2D([0], [0], color=colors[i], lw=4) for i in range(num_elements)]
ax.legend(custom_legend, elements, loc='upper left', bbox_to_anchor=(1.05, 1), fontsize='small')

# Normalize the Z-axis for percentage scale
ax.set_zlim(0, 100)

# Experiment with viewing angle for better visualization
ax.view_init(elev=20., azim=120)

# Adjust layout for better fit
plt.tight_layout()

# Show the plot
plt.show()