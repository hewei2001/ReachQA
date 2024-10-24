import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define decades and fantasy sport categories
decades = ['1990s', '2000s', '2010s', '2020s']
fantasy_sport_categories = ['Football', 'Basketball', 'Baseball']

# Participation data for each category per decade (in millions)
participation_data = np.array([
    [5, 3, 2],  # 1990s
    [10, 6, 4], # 2000s
    [18, 10, 8],# 2010s
    [25, 15, 10] # 2020s
])

# Initialize the figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Color map for smooth gradient and differentiation
color_map = plt.get_cmap('coolwarm')
colors = [color_map(0.2), color_map(0.5), color_map(0.8)]

# Plot each fantasy sport category as a bar in the 3D chart
for i in range(len(fantasy_sport_categories)):
    x_positions = np.arange(len(decades))
    y_positions = np.full(len(decades), i)
    z_positions = np.zeros(len(decades))

    ax.bar3d(
        x_positions, y_positions, z_positions, 
        dx=0.5, dy=0.5, dz=participation_data[:, i],
        color=colors[i], alpha=0.85, label=fantasy_sport_categories[i]
    )
    
    for (x, y, z, dz) in zip(x_positions, y_positions, z_positions, participation_data[:, i]):
        ax.text(x, y, z + dz / 2, f'{dz}M', color='black', ha='center', va='center', fontsize=9)

# Set axis labels and title
ax.set_xlabel('Decade')
ax.set_ylabel('Fantasy Sport')
ax.set_zlabel('Participation (Millions)')
ax.set_title('Evolution of Fantasy Sports Participation\nFrom 1990s to 2020s', pad=20)

# Set ticks and labels
ax.set_xticks(np.arange(len(decades)))
ax.set_xticklabels(decades)
ax.set_yticks(np.arange(len(fantasy_sport_categories)))
ax.set_yticklabels(fantasy_sport_categories, rotation=45)

# Adjust view angle for optimal visibility
ax.view_init(elev=25, azim=130)

# Grid enhancements
ax.xaxis._axinfo['grid'].update(color='gray', linestyle='-', linewidth=0.6, alpha=0.3)
ax.yaxis._axinfo['grid'].update(color='gray', linestyle='-', linewidth=0.6, alpha=0.3)
ax.zaxis._axinfo['grid'].update(color='gray', linestyle='-', linewidth=0.6, alpha=0.3)

# Add legend
ax.legend(loc='upper left', title='Fantasy Sport Categories')

# Automatically adjust the layout for optimal spacing
plt.tight_layout()

# Display the plot
plt.show()