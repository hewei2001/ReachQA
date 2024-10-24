import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define years and continents
years = np.arange(2010, 2021)
continents = ['Asia', 'Europe', 'North America', 'South America', 'Africa']

# Define artificial data for solar capacity (in GW)
asia_capacity = [5, 10, 18, 30, 42, 58, 70, 85, 98, 110, 130]
europe_capacity = [4, 8, 14, 22, 30, 40, 55, 65, 78, 90, 105]
north_america_capacity = [3, 6, 11, 18, 25, 32, 45, 58, 68, 78, 90]
south_america_capacity = [1, 2, 4, 7, 12, 15, 22, 28, 35, 42, 50]
africa_capacity = [0.5, 1.5, 3, 5, 8, 12, 18, 24, 30, 38, 48]

# Stack the data for 3D bar plot
capacities = np.array([asia_capacity, europe_capacity, north_america_capacity, south_america_capacity, africa_capacity])

# Calculate annual growth for line plot
asia_growth = np.diff(asia_capacity, prepend=0)
europe_growth = np.diff(europe_capacity, prepend=0)
north_america_growth = np.diff(north_america_capacity, prepend=0)
south_america_growth = np.diff(south_america_capacity, prepend=0)
africa_growth = np.diff(africa_capacity, prepend=0)

# Set up the figure and subplots
fig = plt.figure(figsize=(18, 8))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122)

# Define bar width and depth
width = 0.5
depth = 0.5

# Colors for each continent
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF6666']

# 3D Bar Plot
for i, continent in enumerate(continents):
    ys = np.array([i] * len(years))
    ax1.bar3d(years, ys, np.zeros_like(years), width, depth, capacities[i], color=colors[i], alpha=0.8, label=continent)

ax1.set_xlabel('Year', labelpad=10)
ax1.set_ylabel('Continent', labelpad=10)
ax1.set_zlabel('Solar Capacity (GW)', labelpad=10)
ax1.set_yticks(range(len(continents)))
ax1.set_yticklabels(continents)
ax1.set_title("Decade of Solar Power:\nContinental Growth in Solar Energy Capacity (2010-2020)", fontsize=14, pad=20)
ax1.view_init(elev=25, azim=135)

# Line Plot of Annual Growth
for i, (growth, continent) in enumerate(zip([asia_growth, europe_growth, north_america_growth, south_america_growth, africa_growth], continents)):
    ax2.plot(years, growth, marker='o', color=colors[i], label=continent)

ax2.set_xlabel('Year')
ax2.set_ylabel('Annual Growth in Solar Capacity (GW)')
ax2.set_title('Annual Growth of Solar Capacity by Continent')
ax2.grid(True)
ax2.legend(title="Continents", loc='upper left')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()