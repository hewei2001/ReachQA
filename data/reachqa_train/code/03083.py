import matplotlib.pyplot as plt
import numpy as np

# Define the cities and the timeframe
cities = ['EcoCity', 'AgriTown', 'FarmVille']
years = ['2019', '2020', '2021', '2022', '2023']

# Data: Output and Consumption in tonnes over the years for each city
output = np.array([
    [100, 120, 130, 150, 170],  # EcoCity
    [110, 115, 125, 140, 160],  # AgriTown
    [90, 105, 115, 130, 145]    # FarmVille
])

consumption = np.array([
    [80, 90, 100, 120, 140],  # EcoCity
    [100, 105, 110, 130, 150],# AgriTown
    [70, 85, 95, 110, 125]    # FarmVille
])

# Plot setup
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Bar width and depth
width = 0.3
depth = 0.3

# Colors for each component (output and consumption)
colors_output = ['#33a02c', '#1f78b4', '#e31a1c']
colors_consumption = ['#b2df8a', '#a6cee3', '#fb9a99']

# Creating the stacked bars
for i, city in enumerate(cities):
    x = np.array(range(len(years)))
    y = i * np.ones(len(years))
    
    # Plot output bars
    ax.bar3d(x, y, np.zeros_like(x), width, depth, output[i], color=colors_output[i], alpha=0.7, label=f'{city} Output' if i == 0 else "")
    
    # Plot consumption bars stacked on top of output bars
    ax.bar3d(x, y, output[i], width, depth, consumption[i], color=colors_consumption[i], alpha=0.7, label=f'{city} Consumption' if i == 0 else "")

# Set labels and title
ax.set_xlabel('Year', labelpad=10)
ax.set_ylabel('City', labelpad=10)
ax.set_zlabel('Tonnes', labelpad=10)
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years)
ax.set_yticks(np.arange(len(cities)))
ax.set_yticklabels(cities)
ax.set_title('FutureCities Vertical Farm Output and Consumption\n(2019-2023)', fontsize=16, fontweight='bold', pad=30)

# Add a legend
ax.legend(loc='upper left', bbox_to_anchor=(0.1, 1.05), fontsize=10)

# Set a viewing angle for better visibility
ax.view_init(elev=20., azim=-35)

# Adjust layout for better display
plt.tight_layout()

# Show plot
plt.show()