import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Data preparation
age_groups = ['Teens', 'Adults', 'Seniors']
coffee_types = ['Espresso', 'Latte', 'Cappuccino']
preferences = np.array([
    [20, 50, 30],  # Teens
    [35, 40, 25],  # Adults
    [25, 30, 45]   # Seniors
])

# Create meshgrid for bar positions
xpos, ypos = np.meshgrid(np.arange(len(age_groups)), np.arange(len(coffee_types)))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

# Bar dimensions and data
dx = dy = 0.4
dz = preferences.flatten()

# Create the figure and 3D axes
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Colors for the bars
colors = ['#D2691E', '#FFDEAD', '#8B4513']  # Chocolate, NavajoWhite, SaddleBrown

# Plot each coffee type separately for clarity
for i, color in enumerate(colors):
    ax.bar3d(xpos[ypos == i], ypos[ypos == i], zpos[ypos == i], dx, dy, dz[ypos == i], color=color, alpha=0.8, label=coffee_types[i])

# Setting labels and title
ax.set_xlabel('Age Group', labelpad=10)
ax.set_ylabel('Coffee Type', labelpad=10)
ax.set_zlabel('Preference (%)', labelpad=10)
ax.set_title('Coffee Consumption Preferences by Age Group\nA Global Survey', fontsize=14, fontweight='bold', pad=20)

# Customizing tick labels for better visibility
ax.set_xticks(np.arange(len(age_groups)) + dx/2)
ax.set_xticklabels(age_groups, rotation=45, ha='right')
ax.set_yticks(np.arange(len(coffee_types)) + dy/2)
ax.set_yticklabels(coffee_types)

# Adjusting the view angle for better visualization
ax.view_init(elev=30, azim=120)

# Adding a grid for visual clarity
ax.grid(True)

# Adding a legend
ax.legend(loc='upper right', title="Coffee Types")

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()