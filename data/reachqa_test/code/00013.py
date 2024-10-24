import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define data
regions = ['North America', 'Europe', 'Asia', 'Africa', 'South America', 'Australia']
energy_types = ['Solar', 'Wind', 'Hydropower', 'Geothermal']

# Percentage values for each type of renewable energy by region (sum may exceed 100% due to exports)
data = np.array([
    [15, 25, 10, 5],   # North America
    [20, 30, 15, 10],  # Europe
    [10, 20, 25, 15],  # Asia
    [5, 10, 20, 25],   # Africa
    [10, 15, 30, 5],   # South America
    [20, 10, 15, 10]   # Australia
])

# Define colors for different energy types
colors = ['#FFD700', '#1E90FF', '#32CD32', '#FF4500']  # Adding RedOrange for Geothermal

# Set up the figure and 3D axis
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Create meshgrid for bar positions
x_pos, y_pos = np.meshgrid(np.arange(data.shape[0]), np.arange(data.shape[1]), indexing='ij')
x_pos = x_pos.flatten()
y_pos = y_pos.flatten()
z_pos = np.zeros_like(x_pos)

# Define the width and depth of each bar
dx = dy = 0.25

# Flatten data array for z-height of each bar
dz = data.flatten()

# Create the 3D bar chart
ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, color=[colors[i % len(colors)] for i in y_pos], alpha=0.8)

# Set axis labels
ax.set_xlabel('Region', labelpad=20)
ax.set_ylabel('Energy Type', labelpad=10)
ax.set_zlabel('Percentage (%)', labelpad=10)
ax.set_xticks(np.arange(len(regions)) + dx / 2)
ax.set_xticklabels(regions, rotation=25, ha='right')
ax.set_yticks(np.arange(len(energy_types)) + dy / 2)
ax.set_yticklabels(energy_types)
ax.set_zlim(0, 40)

# Add a legend
handles = [plt.Rectangle((0, 0), 1, 1, color=colors[i]) for i in range(len(colors))]
ax.legend(handles, energy_types, loc='upper left', bbox_to_anchor=(1, 1), title='Energy Types')

# Set the title
ax.set_title('Renewable Energy Consumption by Region\nin 2022: A Comprehensive Analysis', pad=40)

# Automatically adjust the layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()