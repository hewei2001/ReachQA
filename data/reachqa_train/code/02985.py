import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data setup
years = ['2020', '2021', '2022']
genres = ['Action', 'Role-playing', 'Sports', 'Strategy', 'Simulation']

# Percentage market share data for each genre over the years
market_share = np.array([
    [30, 20, 15, 25, 10],  # 2020
    [28, 22, 18, 22, 10],  # 2021
    [25, 25, 20, 20, 10],  # 2022
])

# Set up the figure and axis for 3D plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Colors for each genre
colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#1C2833']

# Set bar positions
x_pos = np.arange(len(genres))
y_pos = np.arange(len(years))
x_pos, y_pos = np.meshgrid(x_pos, y_pos)

# Flatten data for 3D bar plotting
x_pos = x_pos.flatten()
y_pos = y_pos.flatten()
z_pos = np.zeros_like(x_pos)

# Bar heights (market share values)
dz = market_share.flatten()

# Create 3D bar chart
ax.bar3d(x_pos, y_pos, z_pos, dx=0.5, dy=0.5, dz=dz, color=np.repeat(colors, len(years)), alpha=0.8)

# Set axis labels
ax.set_xlabel('Game Genre', fontsize=12, labelpad=10)
ax.set_ylabel('Year', fontsize=12, labelpad=10)
ax.set_zlabel('Market Share (%)', fontsize=12, labelpad=10)

# Customize tick labels
ax.set_xticks(np.arange(len(genres)) + 0.25)
ax.set_xticklabels(genres, rotation=45, ha='right', fontsize=10)
ax.set_yticks(np.arange(len(years)) + 0.25)
ax.set_yticklabels(years, fontsize=10)
ax.set_zlim(0, 100)

# Add a title
ax.set_title('Global Gaming Industry\nMarket Share by Genre (2020-2022)', fontsize=16, pad=20)

# Adjust the view angle for better visibility
ax.view_init(elev=20., azim=130)

# Adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()