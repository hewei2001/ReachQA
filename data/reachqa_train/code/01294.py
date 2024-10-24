import matplotlib.pyplot as plt
import numpy as np

# Data representing park sizes over a decade (in square kilometers)
city1 = [1.2, 1.5, 1.3, 1.4, 1.6, 1.5, 1.7, 1.8, 1.6, 1.7]
city2 = [2.1, 2.3, 2.5, 2.2, 2.4, 2.6, 2.5, 2.7, 2.8, 2.6]
city3 = [1.7, 1.6, 1.9, 1.8, 2.0, 1.9, 2.1, 2.2, 1.8, 2.0]
city4 = [0.8, 1.0, 1.1, 1.2, 1.3, 1.1, 1.0, 1.2, 1.4, 1.3]
city5 = [3.2, 3.0, 3.3, 3.5, 3.6, 3.4, 3.5, 3.6, 3.7, 3.8]

# City labels
cities = ["EcoMetropolis", "Greenwich", "LeafyVale", "ParkTown", "NatureBay"]

# Create the horizontal box plot
fig, ax = plt.subplots(figsize=(12, 7))

# Box plot settings
box = ax.boxplot([city1, city2, city3, city4, city5], vert=False, patch_artist=True, notch=True,
                 boxprops=dict(facecolor='lightgreen', color='green'),
                 whiskerprops=dict(color='green'),
                 capprops=dict(color='green'),
                 flierprops=dict(marker='o', color='red', markersize=8, alpha=0.5),
                 medianprops=dict(color='orange', linewidth=2))

# Assign different shades of green to each city's box
shades_of_green = ['#A3E4D7', '#76D7C4', '#48C9B0', '#1ABC9C', '#148F77']
for patch, color in zip(box['boxes'], shades_of_green):
    patch.set_facecolor(color)

# Set the title and labels
ax.set_title('Decadal Trends in Urban Green Spaces:\nPark Size Distribution Across Global Cities', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Park Size (Square Kilometers)', fontsize=12, fontweight='bold')
ax.set_yticks(np.arange(1, len(cities) + 1))
ax.set_yticklabels(cities, fontsize=12, fontweight='bold')
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Add a legend for the color coding of cities
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in shades_of_green]
ax.legend(handles, cities, title='Cities', loc='lower right', fontsize=10)

# Ensure layout fits well without overlapping
plt.tight_layout()

# Display the plot
plt.show()