import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the data for the chart
planets = ['Zog', 'Vega', 'Orion']
cuisines = ['Martian Delicacies', 'Venusian Pastries', 'Saturnine Savories']

# Predefined popularity scores for the cuisines on each planet
popularity_scores = np.array([
    [70, 85, 90],  # Scores for Zog
    [60, 75, 95],  # Scores for Vega
    [80, 65, 70],  # Scores for Orion
])

# Setting up the figure and axis for 3D plotting
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d', azim=130, elev=30)

# Determine positions for the bars
xpos, ypos = np.meshgrid(np.arange(len(planets)), np.arange(len(cuisines)), indexing="ij")
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

# Data for the heights of bars (flattened for each cuisine across all planets)
dx = dy = 0.5
dz = popularity_scores.flatten()

# Colors assigned to different cuisines for clarity using a distinct colormap
colors = plt.cm.plasma(np.linspace(0.1, 0.9, len(dz)))

# Plot each column of bars separately for better clarity and alignment
for i in range(len(planets)):
    ax.bar3d(xpos[i::len(planets)], ypos[i::len(planets)], zpos[i::len(planets)], 
             dx, dy, popularity_scores[i], color=colors[i*len(cuisines):(i+1)*len(cuisines)], 
             edgecolor='k', linewidth=0.5, alpha=0.8)

# Adding labels above the bars
for i in range(len(xpos)):
    ax.text(xpos[i], ypos[i], dz[i] + 2, f'{dz[i]}', ha='center', va='bottom', fontsize=10)

# Customizing axes labels
ax.set_xticks(np.arange(len(planets)))
ax.set_yticks(np.arange(len(cuisines)))
ax.set_xticklabels(planets, fontsize=12)
ax.set_yticklabels(cuisines, fontsize=12, rotation=45, ha='right')
ax.set_xlabel('Planets', fontsize=12, labelpad=10)
ax.set_ylabel('Cuisines', fontsize=12, labelpad=10)
ax.set_zlabel('Popularity Score (0 - 100)', fontsize=12, labelpad=10)

# Customizing the background and grid
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis._axinfo['grid'].update(color=(0.5, 0.5, 0.5, 0.1))
ax.yaxis._axinfo['grid'].update(color=(0.5, 0.5, 0.5, 0.1))
ax.zaxis._axinfo['grid'].update(color=(0.5, 0.5, 0.5, 0.1))
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adding a descriptive title
ax.set_title('Alien Cuisine Popularity\nAcross Planets in the Andromeda Galaxy', fontsize=15, pad=20)

# Adjust layout for non-overlapping text
plt.tight_layout()

# Display the plot
plt.show()