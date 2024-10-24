import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the years and genres
years = np.array([2018, 2019, 2020, 2021, 2022])
genres = ['Strategy', 'Party', 'Cooperative', 'Abstract', 'Thematic']

# Define the sales data (in thousands of units) for each genre over the years
sales_data = np.array([
    [60, 70, 80, 95, 110],  # Strategy
    [50, 55, 65, 75, 85],   # Party
    [40, 50, 60, 80, 100],  # Cooperative
    [30, 35, 40, 45, 50],   # Abstract
    [20, 30, 45, 60, 75]    # Thematic
])

# Create a figure for the 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Bar dimensions
bar_width = 0.5
bar_depth = 0.5

# Generate positions for the bars
x_pos, y_pos = np.meshgrid(np.arange(len(years)), np.arange(len(genres)))
x_pos = x_pos.flatten()
y_pos = y_pos.flatten()

# Z positions and heights
z_pos = np.zeros_like(x_pos)
sales = sales_data.flatten()

# Set colors for different genres
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33FF', '#FF8333']
colors = np.repeat(colors, len(years))

# Create 3D bars
ax.bar3d(x_pos, y_pos, z_pos, bar_width, bar_depth, sales, color=colors, shade=True)

# Add labels and title
ax.set_xlabel('Year', labelpad=10)
ax.set_ylabel('Genre', labelpad=10)
ax.set_zlabel('Units Sold (Thousands)', labelpad=10)
ax.set_title('Board Game Genre Popularity (2018-2022)\nRising Sales in the Industry', fontsize=14, fontweight='bold', pad=20)

# Set tick labels
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, rotation=45, ha='right')
ax.set_yticks(np.arange(len(genres)))
ax.set_yticklabels(genres)

# Adjust the view
ax.view_init(elev=20, azim=120)

# Adding a grid for better readability
ax.yaxis._axinfo['grid'].update(color='grey', linestyle='--', linewidth=0.5)
ax.xaxis._axinfo['grid'].update(color='grey', linestyle='--', linewidth=0.5)
ax.zaxis._axinfo['grid'].update(color='grey', linestyle='--', linewidth=0.5)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()