import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Data for renewable energy production in TWh
years = np.array([2018, 2019, 2020, 2021, 2022])
regions = ['North America', 'Europe', 'Asia']

# Energy production data for each region and year (in TWh)
solar_energy = np.array([
    [50, 55, 60, 70, 80],  # North America
    [60, 70, 85, 95, 110],  # Europe
    [80, 90, 105, 120, 140]  # Asia
])

wind_energy = np.array([
    [100, 115, 130, 145, 160],  # North America
    [110, 130, 150, 165, 180],  # Europe
    [95, 110, 125, 140, 155]  # Asia
])

hydro_energy = np.array([
    [150, 155, 160, 165, 170],  # North America
    [120, 125, 130, 135, 140],  # Europe
    [130, 140, 150, 160, 170]  # Asia
])

# Create a 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define positions and dimensions
x_pos = np.arange(len(years))
y_pos = np.arange(len(regions))
x_pos, y_pos = np.meshgrid(x_pos, y_pos)
x_pos = x_pos.flatten()
y_pos = y_pos.flatten()

width = depth = 0.4

# Plot each type of renewable energy source
colors = ['#FFA07A', '#87CEFA', '#98FB98']  # Soft and distinct colors
z_solar = np.zeros_like(x_pos)

# Add bars for Solar Energy
ax.bar3d(x_pos, y_pos, z_solar, width, depth, solar_energy.flatten(), color=colors[0], alpha=0.8, label='Solar Energy')

# Add bars for Wind Energy
z_wind = solar_energy.flatten()
ax.bar3d(x_pos, y_pos, z_wind, width, depth, wind_energy.flatten(), color=colors[1], alpha=0.8, label='Wind Energy')

# Add bars for Hydro Energy
z_hydro = z_wind + wind_energy.flatten()
ax.bar3d(x_pos, y_pos, z_hydro, width, depth, hydro_energy.flatten(), color=colors[2], alpha=0.8, label='Hydro Energy')

# Set axis labels and ticks
ax.set_xlabel('Year')
ax.set_ylabel('Region')
ax.set_zlabel('Energy Production (TWh)')
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years)
ax.set_yticks(np.arange(len(regions)))
ax.set_yticklabels(regions)

# Set title with line breaks for clarity
ax.set_title("Renewable Revolution: Contributions of Solar, Wind, and Hydro Energy\n(2018-2022)", fontsize=14, pad=20)

# Adjust the view angle for better visibility
ax.view_init(elev=25, azim=135)

# Add legend and ensure it does not overlap the chart
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()