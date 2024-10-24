import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Years and cities
years = np.arange(2015, 2026)
cities = ['New York', 'Tokyo', 'Paris']

# Plant production data (units in 1000s of plants)
new_york_data = [
    [50, 20, 10], [60, 25, 12], [72, 28, 15], [85, 30, 18],
    [100, 35, 20], [115, 38, 22], [130, 42, 25], [145, 45, 28],
    [160, 50, 30], [175, 55, 33], [190, 60, 35]
]
tokyo_data = [
    [40, 15, 8], [52, 18, 10], [65, 22, 12], [78, 25, 14],
    [90, 28, 16], [105, 31, 18], [120, 35, 20], [135, 40, 22],
    [150, 44, 24], [165, 48, 27], [180, 52, 30]
]
paris_data = [
    [30, 10, 5], [42, 12, 7], [55, 15, 9], [68, 18, 11],
    [80, 20, 13], [95, 23, 15], [110, 27, 17], [125, 30, 19],
    [140, 34, 21], [155, 37, 24], [170, 40, 27]
]

# Create the figure and 3D axes
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# X positions for the bars
x_positions = np.arange(len(years))

# Width and depth of each bar
width = 0.2
depth = width

# Plotting 3D stacked bars for each city
for i, (city, data) in enumerate(zip(cities, [new_york_data, tokyo_data, paris_data])):
    # Extracting individual plant types
    veggies = np.array([year[0] for year in data])
    fruits = np.array([year[1] for year in data])
    herbs = np.array([year[2] for year in data])

    # Stacking the bars
    ax.bar3d(x_positions + i * width, np.full_like(x_positions, i), np.zeros_like(veggies), width, depth, veggies, color='#76C7C0', alpha=0.8, label=f'{city} Vegetables' if i == 0 else "")
    ax.bar3d(x_positions + i * width, np.full_like(x_positions, i), veggies, width, depth, fruits, color='#FFB347', alpha=0.8, label=f'{city} Fruits' if i == 0 else "")
    ax.bar3d(x_positions + i * width, np.full_like(x_positions, i), veggies + fruits, width, depth, herbs, color='#FF6961', alpha=0.8, label=f'{city} Herbs' if i == 0 else "")

# Setting ticks and labels
ax.set_xlabel('Year', labelpad=10)
ax.set_ylabel('City', labelpad=10)
ax.set_zlabel('Production (1000s)', labelpad=10)
ax.set_xticks(x_positions + width)
ax.set_xticklabels(years, rotation=45)
ax.set_yticks(np.arange(len(cities)))
ax.set_yticklabels(cities)

# Adjust viewing angle
ax.view_init(elev=30, azim=120)

# Adding title and legend
ax.set_title('The Evolution of Urban Agriculture:\nPlant Growth in City Vertical Farms (2015-2025)', fontsize=14, pad=30)
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title="Plant Types")

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()