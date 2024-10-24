import matplotlib.pyplot as plt
import numpy as np

# Expanding the dataset with more cities and varied data patterns
city_park_sizes = {
    "Metropo 3000": [12, 15, 18, 22, 25, 30, 32, 34, 37, 40, 42, 45, 48, 50, 52],
    "New NEXUS": [20, 25, 27, 29, 32, 33, 35, 37, 38, 40, 41, 44, 47, 49, 50],
    "GreenHaven": [5, 7, 10, 12, 15, 18, 20, 25, 28, 30, 32, 34, 36, 38, 40],
    "EcoSphere": [10, 14, 17, 19, 22, 24, 27, 30, 33, 35, 38, 40, 42, 44, 46],
    "Skyward Ville": [8, 10, 13, 15, 17, 20, 22, 25, 28, 30, 33, 35, 37, 39, 41],
    "Aquapolis": [30, 33, 35, 36, 38, 40, 41, 43, 45, 47, 48, 50, 52, 54, 56],
    "Terraform City": [18, 22, 25, 28, 30, 33, 35, 38, 40, 43, 45, 47, 49, 51, 54],
    "Zenith Ridge": [16, 19, 21, 23, 25, 27, 30, 32, 34, 36, 38, 40, 42, 44, 46]
}

# Extract city names and their park size data
cities = list(city_park_sizes.keys())
sizes = [city_park_sizes[city] for city in cities]

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(16, 9))

# Create the horizontal box plot
boxprops = dict(linestyle='-', linewidth=1.5, color='darkgreen', facecolor='lightgreen', alpha=0.7)
whiskerprops = dict(linestyle='--', linewidth=1.5, color='green')
capprops = dict(linewidth=1.5, color='green')
medianprops = dict(linestyle='-', linewidth=2, color='darkred')

ax.boxplot(sizes, vert=False, patch_artist=True, labels=cities, notch=True,
           boxprops=boxprops, whiskerprops=whiskerprops, capprops=capprops, medianprops=medianprops)

# Adding a secondary plot for more complexity: mean points
means = [np.mean(size) for size in sizes]
ax.scatter(means, range(1, len(cities) + 1), color='blue', zorder=3, label='Mean Park Size', marker='D')

# Customize the grid and background
ax.grid(True, linestyle='--', alpha=0.5, axis='x')
ax.set_axisbelow(True)
ax.set_facecolor('#f7f7f7')

# Add a title and labels
ax.set_title("Distribution of Urban Park Sizes in Futuristic Cities\nIncluding Mean Park Size", 
             fontsize=16, color='darkblue', pad=20)
ax.set_xlabel("Park Size (hectares)", fontsize=12)
ax.set_ylabel("Futuristic Cities", fontsize=12)

# Add legend
ax.legend(loc='upper right', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()