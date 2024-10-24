import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define platforms and years
platforms = ['YouTube', 'Medium', 'Spotify', 'Instagram']
years = [2020, 2021, 2022, 2023]

# Data for each platform (Video, Blogs, Podcasts, Infographics)
youtube_data = [
    [70, 10, 5, 15],   # 2020
    [68, 12, 7, 13],   # 2021
    [65, 15, 8, 12],   # 2022
    [63, 17, 10, 10],  # 2023
]

medium_data = [
    [10, 70, 5, 15],   # 2020
    [12, 65, 8, 15],   # 2021
    [15, 60, 10, 15],  # 2022
    [20, 55, 12, 13],  # 2023
]

spotify_data = [
    [10, 5, 75, 10],   # 2020
    [12, 7, 70, 11],   # 2021
    [15, 10, 68, 7],   # 2022
    [18, 15, 63, 4],   # 2023
]

instagram_data = [
    [20, 5, 10, 65],   # 2020
    [25, 10, 12, 53],  # 2021
    [30, 12, 15, 43],  # 2022
    [35, 15, 20, 30],  # 2023
]

# Combine data for easy iteration
data = [youtube_data, medium_data, spotify_data, instagram_data]

# Define colors for each content type
colors = ['#FF4500', '#4682B4', '#32CD32', '#FFD700']  # Video, Blogs, Podcasts, Infographics

# Initialize plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Iterate over each platform to plot bars
for i, platform in enumerate(platforms):
    for j, year in enumerate(years):
        for k, (content_type, color) in enumerate(zip(['Video', 'Blogs', 'Podcasts', 'Infographics'], colors)):
            x = i * 1.5
            y = j * 1.5
            z = 0
            dx = 0.4
            dy = 0.4
            dz = data[i][j][k]
            ax.bar3d(x, y, z, dx, dy, dz, color=color, alpha=0.8)

# Set labels
ax.set_xlabel('Platform', fontsize=12)
ax.set_ylabel('Year', fontsize=12)
ax.set_zlabel('Percentage (%)', fontsize=12)

# Set title
ax.set_title('Online Content Preferences:\nShift in Content Consumption Across Platforms (2020-2023)', fontsize=14, fontweight='bold')

# Set ticks and labels
ax.set_xticks(np.arange(len(platforms)) * 1.5)
ax.set_xticklabels(platforms, rotation=15, ha='right', fontsize=10)
ax.set_yticks(np.arange(len(years)) * 1.5)
ax.set_yticklabels(years, fontsize=10)
ax.set_zlim(0, 100)

# Create legend
legend_labels = ['Video', 'Blogs', 'Podcasts', 'Infographics']
plt.legend(legend_labels, loc='upper left', title='Content Type', fontsize=10, bbox_to_anchor=(1, 0.9))

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()