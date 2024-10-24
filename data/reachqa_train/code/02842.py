import matplotlib.pyplot as plt
import numpy as np

# Data Definitions
planets = ['Mars', 'Venus', 'Jupiter', 'Saturn', 'Neptune']
resources = ['Minerals', 'Gas', 'Water']

percentages = np.array([
    [40, 30, 30],  # Mars
    [50, 40, 10],  # Venus
    [25, 65, 10],  # Jupiter
    [35, 55, 10],  # Saturn
    [45, 35, 20]   # Neptune
])

# Colors
colors = ['royalblue', 'orange', 'limegreen']

# Set up the figure and subplots
fig = plt.figure(figsize=(16, 8))

# 3D Bar Plot
ax1 = fig.add_subplot(121, projection='3d')
x_pos, y_pos = np.meshgrid(np.arange(len(planets)), np.arange(len(resources)))
x_pos = x_pos.flatten()
y_pos = y_pos.flatten()
z_pos = np.zeros_like(x_pos)
dx = dy = 0.6  # Size of each bar along x and y axes
dz = percentages.T.flatten()

bars = ax1.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, color=[colors[i % len(resources)] for i in y_pos], alpha=0.8)

# Labels and customization for 3D bar plot
ax1.set_title('Galactic Trade Insights:\n3D Distribution of Commodities', fontsize=12, pad=20)
ax1.set_xlabel('Planets', fontsize=10, labelpad=10)
ax1.set_ylabel('Resources', fontsize=10, labelpad=10)
ax1.set_zlabel('Percentage (%)', fontsize=10, labelpad=10)
ax1.set_xticks(np.arange(len(planets)))
ax1.set_xticklabels(planets, fontsize=9, rotation=15)
ax1.set_yticks(np.arange(len(resources)))
ax1.set_yticklabels(resources, fontsize=9)
ax1.set_zlim(0, 100)

legend_elements = [plt.Line2D([0], [0], marker='s', color='w', label=resources[i],
                   markersize=10, markerfacecolor=colors[i], alpha=0.7) for i in range(len(resources))]
ax1.legend(handles=legend_elements, title='Resources', loc='upper left', fontsize=9)

# Stacked Bar Plot
ax2 = fig.add_subplot(122)
bar_width = 0.5
indices = np.arange(len(planets))

# Calculate cumulative percentages for stacking
cumulative_percentages = np.zeros(len(planets))
for i, color in enumerate(colors):
    ax2.bar(indices, percentages[:, i], bar_width, bottom=cumulative_percentages, color=color, label=resources[i])
    cumulative_percentages += percentages[:, i]

# Labels and customization for stacked bar plot
ax2.set_title('Aggregate Planetary Contributions\nby Resource Type', fontsize=12, pad=10)
ax2.set_xlabel('Planets', fontsize=10)
ax2.set_ylabel('Total Contribution (%)', fontsize=10)
ax2.set_xticks(indices)
ax2.set_xticklabels(planets, fontsize=9, rotation=15)
ax2.set_ylim(0, 100)
ax2.legend(title='Resources', fontsize=9)

# Adjust layout
plt.tight_layout()

# Show plots
plt.show()