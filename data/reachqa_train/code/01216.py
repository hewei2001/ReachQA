import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define months and platforms
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
platforms = ['VR Gaming', 'VR Education', 'VR Social']

# Engagement hours in thousands
gaming_engagement = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 110])
education_engagement = np.array([30, 32, 35, 37, 40, 45, 50, 53, 55, 60, 65, 70])
social_engagement = np.array([20, 25, 28, 30, 32, 35, 37, 40, 42, 45, 48, 50])

# Monthly growth rates (percent)
gaming_growth = np.array([10, 9, 8, 7, 8, 9, 7, 6, 6, 5, 10, 9])
education_growth = np.array([6, 7, 9, 6, 8, 10, 11, 6, 4, 9, 8, 7])
social_growth = np.array([10, 9, 12, 7, 6, 9, 7, 8, 5, 6, 7, 6])

# Create 3D bar plot
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

x_pos = np.arange(len(months))
dx = dy = 0.6
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Plot bar3d for each platform separately
data = [gaming_engagement, education_engagement, social_engagement]
for i, platform_data in enumerate(data):
    y_pos = np.full_like(x_pos, i)  # Set the y position for each platform
    ax.bar3d(x_pos, y_pos, np.zeros_like(x_pos), dx, dy, platform_data, color=colors[i], alpha=0.8, zsort='average')

# Overlay line plots for growth rates
growth_data = [gaming_growth, education_growth, social_growth]
for i, (growth, color) in enumerate(zip(growth_data, colors)):
    ax.plot(x_pos, np.full_like(x_pos, i), growth, color=color, marker='o', label=f"{platforms[i]} Growth", zorder=5)

# Customizing ticks and labels
ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months, rotation=45, ha='right')
ax.set_yticks(np.arange(len(platforms)))
ax.set_yticklabels(platforms)
ax.set_xlabel('Months', labelpad=10)
ax.set_ylabel('Platforms', labelpad=10)
ax.set_zlabel('Engagement & Growth (Thousands of Hours / Percentage)', labelpad=10)
ax.set_title('Virtual Reality Expansion:\nMonthly User Engagement & Growth Across Platforms (2023)', pad=30)

# Adjust view angle
ax.view_init(elev=25, azim=35)

# Add legends for both bars and lines
bar_legend = [plt.Line2D([0], [0], color=colors[i], lw=4, label=platforms[i]) for i in range(len(platforms))]
line_legend = [plt.Line2D([0], [0], color=colors[i], marker='o', lw=1, label=f"{platforms[i]} Growth") for i in range(len(platforms))]
ax.legend(handles=bar_legend + line_legend, title='VR Platforms', loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()