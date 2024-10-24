import matplotlib.pyplot as plt
import numpy as np

# Data representing park sizes (in hectares) for each futuristic city
city_park_sizes = {
    "Metropo 3000": [12, 15, 18, 22, 25, 30, 32, 34, 37, 40, 42],
    "New NEXUS": [20, 25, 27, 29, 32, 33, 35, 37, 38, 40, 41, 44],
    "GreenHaven": [5, 7, 10, 12, 15, 18, 20, 25, 28, 30, 32],
    "EcoSphere": [10, 14, 17, 19, 22, 24, 27, 30, 33, 35, 38],
    "Skyward Ville": [8, 10, 13, 15, 17, 20, 22, 25, 28, 30, 33]
}

# Extract city names and their park size data
cities = list(city_park_sizes.keys())
sizes = [city_park_sizes[city] for city in cities]

# Set up the figure and axis for the horizontal box plot
fig, ax = plt.subplots(figsize=(14, 7))

# Create the horizontal box plot, filled with color
boxprops = dict(linestyle='-', linewidth=1.5, color='darkgreen', facecolor='lightgreen', alpha=0.7)
whiskerprops = dict(linestyle='--', linewidth=1.5, color='green')
capprops = dict(linewidth=1.5, color='green')
medianprops = dict(linestyle='-', linewidth=2, color='darkred')

ax.boxplot(sizes, vert=False, patch_artist=True, labels=cities, notch=True,
           boxprops=boxprops, whiskerprops=whiskerprops, capprops=capprops, medianprops=medianprops)

# Customize the grid and background for better readability
ax.grid(True, linestyle='--', alpha=0.5, axis='x')
ax.set_axisbelow(True)
ax.set_facecolor('#f7f7f7')

# Adding a title and labels to the plot
ax.set_title("Distribution of Urban Park Sizes\nin Futuristic Cities", fontsize=16, color='darkblue', pad=20)
ax.set_xlabel("Park Size (hectares)", fontsize=12)
ax.set_ylabel("Futuristic Cities", fontsize=12)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()