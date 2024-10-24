import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define years and regions
years = np.arange(2013, 2024)
regions = ['North America', 'Europe', 'Asia-Pacific', 'Latin America', 'Africa']

# Percentage contribution data for different energy sources
solar = np.array([10, 13, 15, 18, 22, 25, 28, 32, 35, 39, 42]) / 5
wind = np.array([20, 23, 27, 30, 34, 38, 41, 44, 47, 50, 53]) / 5
hydro = np.array([40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20]) / 5
others = np.array([30, 26, 22, 18, 12, 7, 3, 2, 1, 1, 1]) / 5

# 3D bar chart setup
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Define colors for each energy source
colors = ['#FFD700', '#1E90FF', '#32CD32', '#FF4500']

# Meshgrid for plotting
_x, _y = np.meshgrid(np.arange(len(years)), np.arange(len(regions)))
x, y = _x.ravel(), _y.ravel()

# Plot bars for each energy source
dz_solar = np.tile(solar, len(regions))
dz_wind = np.tile(wind, len(regions))
dz_hydro = np.tile(hydro, len(regions))
dz_others = np.tile(others, len(regions))

ax.bar3d(x, y, np.zeros_like(x), 0.8, 0.8, dz_solar, color=colors[0], alpha=0.7, label='Solar')
ax.bar3d(x, y, dz_solar, 0.8, 0.8, dz_wind, color=colors[1], alpha=0.7, label='Wind')
ax.bar3d(x, y, dz_solar + dz_wind, 0.8, 0.8, dz_hydro, color=colors[2], alpha=0.7, label='Hydro')
ax.bar3d(x, y, dz_solar + dz_wind + dz_hydro, 0.8, 0.8, dz_others, color=colors[3], alpha=0.7, label='Others')

# Set labels and titles
ax.set_xlabel('Year', fontsize=12, labelpad=10)
ax.set_ylabel('Region', fontsize=12, labelpad=10)
ax.set_zlabel('Percentage (%)', fontsize=12, labelpad=10)
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, rotation=45)
ax.set_yticks(np.arange(len(regions)))
ax.set_yticklabels(regions)

# Set title
ax.set_title('Global Renewable Energy Adoption\nby Source (2013-2023)', fontsize=16, fontweight='bold', pad=20)

# Normalize Z-axis
ax.set_zlim(0, 100)

# Legend
ax.legend(loc='upper right', fontsize=10, title='Energy Source')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()