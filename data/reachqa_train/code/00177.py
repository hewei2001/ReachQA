import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define space agencies and years
agencies = ['NASA', 'ESA', 'Roscosmos']
years = ['2010', '2015', '2020']

# Define success rates for each agency over the selected years
success_rates = np.array([
    [85, 90, 95],  # NASA
    [75, 85, 88],  # ESA
    [80, 83, 89]   # Roscosmos
])

# Prepare indices for the bar positions
xpos, ypos = np.meshgrid(np.arange(len(years)), np.arange(len(agencies)))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

# Flatten success rate data for 3D bars
dz = success_rates.flatten()

# Setup the figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Set colors for each agency
colors = ['navy', 'royalblue', 'deepskyblue']

# Plot the 3D bar chart
for i, color in enumerate(colors):
    ax.bar3d(xpos[ypos == i], ypos[ypos == i], zpos[ypos == i],
             dx=0.3, dy=0.3, dz=dz[ypos == i], color=color, alpha=0.7, label=agencies[i])

# Set the labels and ticks
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, rotation=45, ha='right', fontsize=10)
ax.set_yticks(np.arange(len(agencies)))
ax.set_yticklabels(agencies, fontsize=10)
ax.set_zlim(0, 100)
ax.set_zlabel('Success Rate (%)', fontsize=10)

# Set a split title for better readability
ax.set_title("Space Exploration Success Rates (2010-2020):\n"
             "Mission Outcomes by Leading Space Agencies",
             fontsize=14, weight='bold', loc='center')

# Customize plot appearance
ax.view_init(elev=30, azim=220)
ax.xaxis.pane.set_visible(False)
ax.yaxis.pane.set_visible(False)
ax.zaxis.pane.set_edgecolor('gray')
ax.grid(True, linestyle='--', linewidth=0.5, color='gray', which='both')

# Add legend for better understanding
ax.legend(loc='upper left', bbox_to_anchor=(0.8, 0.9), title='Space Agencies', fontsize=10)

# Automatically adjust layout for optimal space usage
plt.tight_layout()

# Display the plot
plt.show()