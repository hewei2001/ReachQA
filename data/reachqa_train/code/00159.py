import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the celestial colonies and resource categories
colonies = ['Moon', 'Mars', 'Europa']
resources = ['Water', 'Food', 'Energy', 'Technology']

# Construct the data for each resource across the colonies
data = np.array([
    [50, 70, 90],   # Water allocations
    [80, 90, 100],  # Food allocations
    [70, 80, 110],  # Energy allocations
    [40, 60, 80]    # Technology allocations
])

# Positions on the X and Y axes
xpos = np.arange(len(colonies))
ypos = np.arange(len(resources))
xpos, ypos = np.meshgrid(xpos, ypos)

# Flatten the grid to iterate over
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

# Heights of the bars (data flattened) and cumulative starting positions for stacking
dz = data.flatten()
zpos_cumulative = np.zeros_like(dz)

# Create a color array
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Distinct colors for resources

# Create the 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot each resource as a separate stack with distinct colors
for i in range(len(resources)):
    ax.bar3d(xpos[ypos == i], ypos[ypos == i], zpos_cumulative[ypos == i], 
             dx=0.5, dy=0.5, dz=data[i], color=colors[i], alpha=0.8, label=resources[i])
    # Update cumulative positions for the next layer
    zpos_cumulative[ypos == i] += data[i]

# Set the ticks and labels
ax.set_xticks(np.arange(len(colonies)))
ax.set_xticklabels(colonies)
ax.set_yticks(np.arange(len(resources)))
ax.set_yticklabels(resources)
ax.set_zlabel('Resource Units')

# Adjust the viewing angle
ax.view_init(elev=20., azim=30)

# Title and legend
ax.set_title("Resource Allocation in Interstellar Colonies\nYear 2150", fontsize=14)
ax.legend(loc='upper left', title='Resource Type')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()