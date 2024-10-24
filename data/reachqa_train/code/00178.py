import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define more space agencies and extended years
agencies = ['NASA', 'ESA', 'Roscosmos', 'CNSA', 'ISRO']
years = ['2005', '2010', '2015', '2020', '2025']

# Define success rates and mission counts for each agency over the selected years
success_rates = np.array([
    [80, 85, 90, 95, 98],  # NASA
    [70, 75, 85, 88, 92],  # ESA
    [75, 80, 83, 89, 91],  # Roscosmos
    [65, 70, 78, 85, 90],  # CNSA
    [60, 65, 75, 82, 88]   # ISRO
])

mission_counts = np.array([
    [100, 110, 115, 120, 125],  # NASA
    [90, 95, 100, 105, 110],    # ESA
    [85, 90, 95, 100, 105],     # Roscosmos
    [70, 75, 80, 90, 100],      # CNSA
    [60, 70, 80, 85, 95]        # ISRO
])

# Prepare indices for the bar positions
xpos, ypos = np.meshgrid(np.arange(len(years)), np.arange(len(agencies)))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

# Flatten success rate and mission count data for 3D bars
dz = success_rates.flatten()
dm = mission_counts.flatten()

# Calculate weighted success rates (example for added complexity)
weighted_success_rates = (success_rates * mission_counts) / mission_counts.sum(axis=1, keepdims=True)

# Setup the figure and 3D axis
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Set colors for each agency
colors = ['navy', 'royalblue', 'deepskyblue', 'skyblue', 'lightsteelblue']

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
ax.set_title("Space Exploration Success Rates (2005-2025):\n"
             "Mission Outcomes by Leading Space Agencies",
             fontsize=14, weight='bold', loc='center')

# Customize plot appearance
ax.view_init(elev=30, azim=230)
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