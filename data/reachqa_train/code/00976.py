import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the years and regions
years = np.arange(2011, 2021)
regions = ['North America', 'Europe', 'Asia', 'Africa']

# Data for each renewable energy source
# Each row corresponds to a region, each column to a year
solar = np.array([
    [5, 7, 10, 12, 15, 18, 20, 25, 27, 30],  # North America
    [6, 8, 11, 14, 17, 20, 23, 26, 28, 32],  # Europe
    [2, 4, 6, 9, 13, 17, 20, 24, 28, 31],    # Asia
    [1, 2, 3, 5, 8, 10, 14, 17, 19, 21]     # Africa
])

wind = np.array([
    [3, 5, 8, 10, 13, 16, 19, 22, 24, 27],  # North America
    [4, 7, 9, 13, 16, 19, 21, 24, 27, 29],  # Europe
    [1, 3, 5, 8, 11, 14, 16, 19, 22, 25],   # Asia
    [0, 1, 2, 4, 6, 9, 11, 14, 16, 19]      # Africa
])

hydroelectric = np.array([
    [20, 22, 23, 24, 25, 26, 27, 28, 29, 30],  # North America
    [15, 17, 18, 19, 20, 22, 23, 24, 26, 27],  # Europe
    [25, 27, 29, 30, 32, 34, 35, 36, 37, 39],  # Asia
    [12, 13, 14, 16, 18, 19, 21, 23, 24, 26]   # Africa
])

# Initialize the figure and 3D axis
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')

# Define positions for the bars
x_data, y_data = np.meshgrid(np.arange(len(years)), np.arange(len(regions)))
x_data = x_data.flatten()
y_data = y_data.flatten()
z_data = np.zeros_like(x_data)

# Define the width of bars
dx = dy = 0.6

# Flatten the data arrays to use in bar3d
solar_data = solar.flatten()
wind_data = wind.flatten()
hydro_data = hydroelectric.flatten()

# Plot each energy source stacked one over another
ax.bar3d(x_data, y_data, z_data, dx, dy, solar_data, color='yellow', label='Solar', alpha=0.8)
z_data += solar_data
ax.bar3d(x_data, y_data, z_data, dx, dy, wind_data, color='skyblue', label='Wind', alpha=0.8)
z_data += wind_data
ax.bar3d(x_data, y_data, z_data, dx, dy, hydro_data, color='lightgreen', label='Hydroelectric', alpha=0.8)

# Set labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Region')
ax.set_zlabel('Percentage of Total Energy (%)')
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, rotation=45, ha='right')
ax.set_yticks(np.arange(len(regions)))
ax.set_yticklabels(regions)
ax.set_zlim(0, 100)  # Ensure the Z-axis represents percentage
ax.set_title('Decade of Change:\nRenewable Energy Adoption by Region (2011-2020)', pad=20)

# Set viewing angle for better visualization
ax.view_init(elev=30, azim=130)

# Add legend
ax.legend(loc='upper right', fontsize='small')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show plot
plt.show()