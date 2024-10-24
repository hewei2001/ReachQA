import matplotlib.pyplot as plt
import numpy as np

# Data: Number of sightings (Y-axis) vs. Park area in hectares (X-axis)
park_areas = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])  # Park sizes in hectares

# Average monthly sightings of different species in urban parks
species_data = {
    'Squirrels': {
        'sightings': [20, 30, 50, 70, 65, 80, 75, 90, 100, 110],
        'marker': 'o',
        'color': '#FF5733'
    },
    'Pigeons': {
        'sightings': [40, 50, 60, 80, 85, 100, 95, 105, 120, 130],
        'marker': '^',
        'color': '#1F618D'
    },
    'Raccoons': {
        'sightings': [5, 15, 20, 30, 25, 40, 45, 60, 70, 80],
        'marker': 's',
        'color': '#239B56'
    },
    'Coyotes': {
        'sightings': [2, 5, 8, 12, 10, 15, 18, 25, 30, 35],
        'marker': 'D',
        'color': '#F4D03F'
    },
}

# Plotting the data
plt.figure(figsize=(12, 7))

for species, data in species_data.items():
    plt.scatter(park_areas, data['sightings'], label=species, marker=data['marker'],
                color=data['color'], s=100, alpha=0.7, edgecolors='k')

# Labeling the axes and the chart
plt.title('Spotting City Dwellers:\nWildlife Species Sightings in Urban Parks', fontsize=16, color='darkgreen')
plt.xlabel('Park Area (hectares)', fontsize=12)
plt.ylabel('Average Monthly Sightings', fontsize=12)

# Adding grid and legend
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend(title='Species', fontsize=10)

# Enhancing layout to prevent text overlap
plt.tight_layout()

# Show the plot
plt.show()