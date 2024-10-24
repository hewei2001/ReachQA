import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sectors and technologies
sectors = ['Healthcare', 'Transportation', 'Education', 'Manufacturing', 'Retail']
technologies = ['AI', 'IoT', 'VR/AR', 'Blockchain', 'Robotics']

# Percentage adoption data (explicitly crafted for illustration purposes)
adoption_matrix = np.array([
    [45, 35, 20, 15, 40],  # Healthcare
    [30, 50, 25, 20, 55],  # Transportation
    [40, 30, 45, 10, 25],  # Education
    [35, 45, 30, 40, 60],  # Manufacturing
    [50, 40, 35, 30, 45]   # Retail
])

# Setup for 3D bar plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define the position of bars in the 3D space
_x = np.arange(adoption_matrix.shape[0])
_y = np.arange(adoption_matrix.shape[1])
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

# Define height of each bar
z = np.zeros_like(x)
dx = dy = 0.7
dz = adoption_matrix.T.ravel()

# Define colors for each technology
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#FF69B4']  # Colors for AI, IoT, VR/AR, Blockchain, Robotics

# Plotting the bars
ax.bar3d(x, y, z, dx, dy, dz, color=[colors[i] for i in y])

# Set labels
ax.set_xlabel('Sector', labelpad=10, fontsize=10)
ax.set_ylabel('Technology', labelpad=10, fontsize=10)
ax.set_zlabel('Adoption (%)', fontsize=10)

# Set ticks
ax.set_xticks(np.arange(len(sectors)))
ax.set_xticklabels(sectors, rotation=45, ha='right', fontsize=9)
ax.set_yticks(np.arange(len(technologies)))
ax.set_yticklabels(technologies, fontsize=9)

# Normalize the Z-axis to 0-100
ax.set_zlim(0, 100)

# Title with multiline to avoid overlap
ax.set_title('Decade of Innovation: Technological\nAdoption Across Key Sectors (2010-2020)',
             size=14, weight='bold', pad=40)

# Add a legend
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(handles, technologies, title="Technologies", loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=9)

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()