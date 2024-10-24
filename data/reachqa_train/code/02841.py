import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Planets and their resource percentage contributions
planets = ['Mars', 'Venus', 'Jupiter', 'Saturn', 'Neptune']
resources = ['Minerals', 'Gas', 'Water']

# Percentage data for each resource from each planet
percentages = np.array([
    [40, 30, 30],  # Mars
    [50, 40, 10],  # Venus
    [25, 65, 10],  # Jupiter
    [35, 55, 10],  # Saturn
    [45, 35, 20]   # Neptune
])

# Define positions for bars
x_pos = np.arange(len(planets))
y_pos = np.arange(len(resources))
x_pos, y_pos = np.meshgrid(x_pos, y_pos)
x_pos = x_pos.flatten()
y_pos = y_pos.flatten()
z_pos = np.zeros_like(x_pos)

# Flatten the percentage array for 3D bar
dz = percentages.T.flatten()

# Repeat colors for each planet
colors = ['royalblue', 'orange', 'limegreen']
colors_repeated = np.repeat(colors, len(planets))

# Create a 3D bar plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting the bars
bars = ax.bar3d(x_pos, y_pos, z_pos, dx=0.6, dy=0.6, dz=dz, color=colors_repeated, alpha=0.8)

# Customize the plot
ax.set_title('Galactic Trade Insights:\nPercentage Distribution of Key Commodities from Interplanetary Sources', fontsize=14, pad=20)
ax.set_xlabel('Planets', fontsize=12, labelpad=10)
ax.set_ylabel('Resources', fontsize=12, labelpad=10)
ax.set_zlabel('Percentage (%)', fontsize=12, labelpad=10)
ax.set_xticks(np.arange(len(planets)))
ax.set_xticklabels(planets, fontsize=10, rotation=15)
ax.set_yticks(np.arange(len(resources)))
ax.set_yticklabels(resources, fontsize=10)
ax.set_zlim(0, 100)

# Adding a legend
legend_elements = [plt.Line2D([0], [0], marker='s', color='w', label=resources[i],
                   markersize=10, markerfacecolor=colors[i], alpha=0.7) for i in range(len(resources))]
ax.legend(handles=legend_elements, title='Resources', loc='upper left', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()