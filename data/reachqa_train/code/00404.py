import matplotlib.pyplot as plt
import numpy as np

# Cities and coffee types
cities = ['New York', 'London', 'Tokyo']
coffee_types = ['Espresso', 'Cappuccino', 'Cold Brew']

# Daily coffee consumption data in cups (30 days) for each coffee type in each city
espresso_data = [
    [120, 150, 130, 140, 160, 145, 155, 135, 150, 165, 140, 130, 125, 160, 170, 155, 150, 145, 160, 175, 140, 135, 125, 150, 155, 160, 170, 165, 175, 180],
    [110, 115, 120, 130, 125, 135, 145, 130, 125, 120, 140, 145, 150, 155, 160, 130, 140, 150, 160, 155, 150, 145, 135, 125, 130, 135, 140, 145, 150, 155],
    [130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 140, 135, 130, 125, 120, 150, 155, 160, 165, 170, 175, 180, 160, 155, 150, 145, 140, 135, 130, 125]
]

cappuccino_data = [
    [90, 95, 100, 85, 90, 95, 105, 100, 90, 95, 100, 95, 90, 85, 80, 105, 100, 95, 90, 85, 100, 105, 90, 85, 80, 75, 100, 95, 90, 85],
    [80, 85, 90, 95, 100, 95, 85, 80, 75, 70, 90, 85, 80, 95, 100, 105, 110, 100, 105, 110, 115, 120, 125, 105, 110, 115, 120, 125, 130, 135],
    [95, 100, 105, 110, 95, 100, 95, 90, 85, 90, 95, 100, 105, 110, 115, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 110, 105, 100, 95]
]

coldbrew_data = [
    [60, 65, 70, 75, 70, 65, 60, 55, 50, 55, 70, 65, 60, 75, 80, 85, 80, 75, 70, 65, 80, 75, 70, 65, 60, 55, 70, 75, 80, 85],
    [55, 50, 45, 50, 55, 60, 65, 70, 75, 70, 85, 80, 75, 80, 85, 90, 95, 80, 75, 70, 65, 60, 55, 50, 45, 40, 85, 80, 75, 70],
    [70, 75, 80, 85, 80, 75, 70, 65, 60, 55, 50, 75, 70, 75, 80, 85, 90, 95, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25]
]

# Consolidate data into a list for boxplot (Espresso, Cappuccino, Cold Brew for each city)
box_data = [
    espresso_data[0], cappuccino_data[0], coldbrew_data[0],  # New York
    espresso_data[1], cappuccino_data[1], coldbrew_data[1],  # London
    espresso_data[2], cappuccino_data[2], coldbrew_data[2]   # Tokyo
]

# Positions for the box plots to prevent overlapping
positions = [1, 2, 3, 5, 6, 7, 9, 10, 11]

# Create the figure and axis for the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Box plot with customization for aesthetics
boxprops = dict(facecolor='#A1D99B', color='green')
whiskerprops = dict(color='green', linestyle='--')
capprops = dict(color='green')
flierprops = dict(markerfacecolor='red', marker='o', markersize=8, linestyle='none')
medianprops = dict(color='darkorange', linewidth=2)

ax.boxplot(box_data, positions=positions, patch_artist=True, notch=True,
           boxprops=boxprops, whiskerprops=whiskerprops,
           capprops=capprops, flierprops=flierprops,
           medianprops=medianprops)

# Customize the x-axis to reflect coffee types for each city
ax.set_xticks([2, 6, 10])
ax.set_xticklabels(cities, fontsize=12)
ax.set_xlabel("City", fontsize=14)
ax.set_ylabel("Number of Cups", fontsize=14)

# Add a title and grid for clarity
plt.title("Gourmet Coffee Consumption in Urban Cafes\nAverage Daily Cups (30 days)", fontsize=16, fontweight='bold')
ax.xaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Add legend indicating coffee types
colors = ['#A1D99B', '#FB9A99', '#FFCC99']
patches = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
plt.legend(patches, coffee_types, loc='upper right', fontsize=12)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()