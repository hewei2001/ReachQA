import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define years and continents
years = np.arange(2010, 2021)
continents = ['Asia', 'Europe', 'North America', 'South America', 'Africa']

# Define artificial data for solar capacity (in GW)
# These are cumulative values over the years
asia_capacity = [5, 10, 18, 30, 42, 58, 70, 85, 98, 110, 130]
europe_capacity = [4, 8, 14, 22, 30, 40, 55, 65, 78, 90, 105]
north_america_capacity = [3, 6, 11, 18, 25, 32, 45, 58, 68, 78, 90]
south_america_capacity = [1, 2, 4, 7, 12, 15, 22, 28, 35, 42, 50]
africa_capacity = [0.5, 1.5, 3, 5, 8, 12, 18, 24, 30, 38, 48]

# Stack the data
capacities = np.array([asia_capacity, europe_capacity, north_america_capacity, south_america_capacity, africa_capacity])

# Set up the figure and 3D axis
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')

# Define bar width and depth
width = 0.5
depth = 0.5

# Colors for each continent
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF6666']

# Plot each continent's data as a stacked bar
for i, continent in enumerate(continents):
    # Shift along the y-axis for each continent
    ys = np.array([i] * len(years))
    ax.bar3d(years, ys, np.zeros_like(years), width, depth, capacities[i], color=colors[i], alpha=0.8, label=continent)

# Set labels
ax.set_xlabel('Year', labelpad=10)
ax.set_ylabel('Continent', labelpad=10)
ax.set_zlabel('Solar Capacity (GW)', labelpad=10)
ax.set_yticks(range(len(continents)))
ax.set_yticklabels(continents)

# Title and legend
ax.set_title("Decade of Solar Power:\nContinental Growth in Solar Energy Capacity (2010-2020)", fontsize=14, pad=20)
ax.legend(title="Continents", loc='upper left')

# Adjust the view angle for better visibility
ax.view_init(elev=25, azim=135)

# Automatically adjust layout for optimal spacing
plt.tight_layout()

# Display the plot
plt.show()