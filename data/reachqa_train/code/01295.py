import matplotlib.pyplot as plt
import numpy as np

# Data representing park sizes over a decade (in square kilometers)
city1 = [1.2, 1.5, 1.3, 1.4, 1.6, 1.5, 1.7, 1.8, 1.6, 1.7]
city2 = [2.1, 2.3, 2.5, 2.2, 2.4, 2.6, 2.5, 2.7, 2.8, 2.6]
city3 = [1.7, 1.6, 1.9, 1.8, 2.0, 1.9, 2.1, 2.2, 1.8, 2.0]
city4 = [0.8, 1.0, 1.1, 1.2, 1.3, 1.1, 1.0, 1.2, 1.4, 1.3]
city5 = [3.2, 3.0, 3.3, 3.5, 3.6, 3.4, 3.5, 3.6, 3.7, 3.8]

cities = ["EcoMetropolis", "Greenwich", "LeafyVale", "ParkTown", "NatureBay"]

# Mean values for each city
means = [np.mean(city) for city in [city1, city2, city3, city4, city5]]

fig, ax = plt.subplots(figsize=(14, 8))

# Box plot settings
box = ax.boxplot([city1, city2, city3, city4, city5], vert=False, patch_artist=True, notch=True,
                 boxprops=dict(color='green'),
                 whiskerprops=dict(color='green'),
                 capprops=dict(color='green'),
                 flierprops=dict(marker='o', color='red', markersize=8, alpha=0.5),
                 medianprops=dict(color='orange', linewidth=2))

# Different shades of green and transparency for aesthetic enhancement
shades_of_green = ['#A3E4D7', '#76D7C4', '#48C9B0', '#1ABC9C', '#148F77']
for patch, color in zip(box['boxes'], shades_of_green):
    patch.set(facecolor=color, alpha=0.7)

# Plot mean markers
ax.scatter(means, np.arange(1, len(cities) + 1), marker='D', color='blue', label='Mean', zorder=3)

# Title and labels
ax.set_title('Decadal Trends in Urban Green Spaces:\nPark Size Distribution Across Global Cities', 
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Park Size (Square Kilometers)', fontsize=12, fontweight='bold')
ax.set_yticks(np.arange(1, len(cities) + 1))
ax.set_yticklabels(cities, fontsize=12, fontweight='bold')
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Add a legend
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in shades_of_green] + [plt.Line2D([0], [0], marker='D', color='w', markerfacecolor='blue', markersize=10)]
labels = cities + ['Mean']
ax.legend(handles, labels, title='Cities & Indicators', loc='lower right', fontsize=10)

# Add horizontal lines for quartiles
quartiles = [np.percentile(city1 + city2 + city3 + city4 + city5, 25),
             np.percentile(city1 + city2 + city3 + city4 + city5, 75)]
for q in quartiles:
    ax.axvline(q, color='grey', linestyle='dashed', linewidth=1, alpha=0.6)

# Annotations for median
for i, med in enumerate([np.median(city1), np.median(city2), np.median(city3), np.median(city4), np.median(city5)]):
    ax.text(med, i+1.2, f'{med:.2f}', horizontalalignment='center', color='black', fontsize=10)

plt.tight_layout()

plt.show()