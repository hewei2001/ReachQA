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
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Determine positions for the bars
xpos, ypos = np.meshgrid(np.arange(len(planets)), np.arange(len(cuisines)), indexing="ij")
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

# Data for the heights of bars (flattened for each cuisine across all planets)
dx = dy = 0.6
dz = popularity_scores.flatten()

# Colors assigned to different cuisines for clarity
colors = plt.cm.viridis(np.linspace(0, 1, len(cuisines)))

# Plot each column of bars separately for better clarity and alignment
for i, (planet, score_row) in enumerate(zip(planets, popularity_scores)):
    ax.bar3d(xpos[i::len(planets)], ypos[i::len(planets)], zpos[i::len(planets)], dx, dy, score_row, color=colors, alpha=0.8, label=cuisines[i])

# Customizing axes labels
ax.set_xticks(np.arange(len(planets)))
ax.set_yticks(np.arange(len(cuisines)))
ax.set_xticklabels(planets)
ax.set_yticklabels(cuisines, rotation=45, ha='right')
ax.set_xlabel('Planets')
ax.set_ylabel('Cuisines')
ax.set_zlabel('Popularity Score (0 - 100)')

# Adjust the view angle for better visibility
ax.view_init(elev=20, azim=130)

# Adding a grid for visual reference
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adding a descriptive title to the chart
ax.set_title('Alien Cuisine Popularity\nin the Andromeda Galaxy', fontsize=14, pad=20)

# Ensure layout is neat and non-overlapping
plt.tight_layout()

# Display the plot
plt.show()