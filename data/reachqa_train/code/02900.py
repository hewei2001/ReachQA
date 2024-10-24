import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
regions = ['North America', 'Europe', 'Asia']

# Energy production (TWh) for each region and year, broken down by energy type
solar = np.array([
    [40, 45, 50, 60, 65, 70],  # North America
    [30, 35, 40, 50, 55, 60],  # Europe
    [50, 60, 70, 80, 90, 100]  # Asia
])

wind = np.array([
    [60, 65, 70, 80, 85, 90],  # North America
    [50, 55, 65, 75, 80, 85],  # Europe
    [40, 50, 60, 70, 80, 90]   # Asia
])

hydro = np.array([
    [80, 85, 90, 95, 100, 105],  # North America
    [60, 65, 70, 75, 80, 85],    # Europe
    [70, 75, 80, 85, 90, 95]     # Asia
])

# Set up the figure and axes for the 3D plot
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Bar settings
bar_width = 0.4
bar_depth = 0.4
colors = ['#FF5733', '#33FF57', '#3357FF']  # Colors for solar, wind, hydro

# Plot each region's stacked bars
for i, region in enumerate(regions):
    x_positions = np.arange(len(years))  # X position for each year
    ax.bar3d(x_positions, i, np.zeros_like(years), bar_width, bar_depth, solar[i], color=colors[0], label='Solar' if i == 0 else "")
    ax.bar3d(x_positions, i, solar[i], bar_width, bar_depth, wind[i], color=colors[1], label='Wind' if i == 0 else "")
    ax.bar3d(x_positions, i, solar[i] + wind[i], bar_width, bar_depth, hydro[i], color=colors[2], label='Hydro' if i == 0 else "")

# Customize axes
ax.set_xlabel('Year', labelpad=10)
ax.set_ylabel('Region', labelpad=10)
ax.set_zlabel('Energy Production (TWh)', labelpad=10)

# Setting x, y ticks
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years)
ax.set_yticks(np.arange(len(regions)))
ax.set_yticklabels(regions)

# Adjust viewing angle for better visibility
ax.view_init(elev=20, azim=120)

# Adding the title with line break
ax.set_title('The Rise of Renewable Energy:\nRegional Production Trends (2020-2025)', pad=20, fontweight='bold', fontsize=14)

# Legend
ax.legend(loc='upper left', fontsize=10, title='Energy Types')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()