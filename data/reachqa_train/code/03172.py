import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data for the chart
years = np.arange(2010, 2020)
learning_methods = ['Textbooks', 'Online Courses', 'Mobile Apps', 'Immersive Tech']

# Percentage data for each method over the years
data = np.array([
    [70, 15, 10, 5],  # 2010
    [65, 20, 12, 3],  # 2011
    [60, 25, 13, 2],  # 2012
    [55, 30, 13, 2],  # 2013
    [50, 35, 12, 3],  # 2014
    [45, 37, 14, 4],  # 2015
    [40, 35, 18, 7],  # 2016
    [35, 33, 22, 10], # 2017
    [30, 30, 25, 15], # 2018
    [25, 28, 27, 20]  # 2019
])

# Setting up the 3D plot
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Colors for each learning method
colors = ['#8E44AD', '#3498DB', '#2ECC71', '#E74C3C']

# Create positions for the bars
x_positions = np.arange(data.shape[0])
y_positions = np.arange(data.shape[1])
x_positions, y_positions = np.meshgrid(x_positions, y_positions)

x_positions = x_positions.flatten()
y_positions = y_positions.flatten()
z_positions = np.zeros_like(x_positions)

# Flatten data for the bar plot
dz = data.T.flatten()

# Bar dimensions
dx = dy = 0.8

# Plotting 3D bars
ax.bar3d(x_positions, y_positions, z_positions, dx, dy, dz, color=[colors[y] for y in y_positions], zsort='average')

# Set the axes labels
ax.set_xlabel('Year', labelpad=15)
ax.set_ylabel('Learning Method', labelpad=15)
ax.set_zlabel('Adoption Percentage (%)', labelpad=15)
ax.set_title('Evolution of Language Learning Preferences\n(2010-2019)', pad=20, fontsize=16, fontweight='bold')

# Configure the tick labels and positions
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, rotation=45, ha='right')
ax.set_yticks(np.arange(len(learning_methods)))
ax.set_yticklabels(learning_methods)

# Manually adding a legend
legend_elements = [plt.Line2D([0], [0], color=colors[i], lw=4, label=learning_methods[i]) for i in range(len(learning_methods))]
ax.legend(handles=legend_elements, loc='upper left', title="Learning Methods", bbox_to_anchor=(1.1, 0.8))

# Set z-axis limits for percentage representation
ax.set_zlim(0, 100)

# Adjust layout to prevent label overlap
plt.tight_layout()

# Show the plot
plt.show()