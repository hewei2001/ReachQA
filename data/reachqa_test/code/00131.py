import matplotlib.pyplot as plt
import numpy as np

# Data for wildlife sightings in different parks over twelve months
months = np.arange(1, 13)  # Representing January to December
sightings_park_a = 15 + 5 * np.sin(np.linspace(0, 2 * np.pi, 12)) + np.arange(0, 12)
sightings_park_b = 10 + 4 * np.cos(np.linspace(0, 2 * np.pi, 12)) + np.arange(1, 13)
sightings_park_c = 12 + 6 * np.sin(np.linspace(0, 2 * np.pi, 12)) + np.arange(2, 14)
sightings_park_d = 8 + 5 * np.cos(np.linspace(0, 2 * np.pi, 12)) + np.arange(3, 15)
sightings_park_e = 5 + 7 * np.sin(np.linspace(0, 2 * np.pi, 12)) + np.arange(4, 16)
sightings_park_f = 20 + 3 * np.cos(np.linspace(0, 2 * np.pi, 12)) + np.arange(2, 14)

# New data for marker size indicating species diversity
species_diversity_a = np.linspace(20, 50, 12)
species_diversity_b = np.linspace(25, 45, 12)
species_diversity_c = np.linspace(18, 40, 12)
species_diversity_d = np.linspace(22, 35, 12)
species_diversity_e = np.linspace(10, 30, 12)
species_diversity_f = np.linspace(30, 55, 12)

# Colors and markers for each park
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#45B8AC', '#EFC050']
markers = ['o', 's', 'D', '^', 'v', '*']

# Plotting the scatter chart for each park
plt.figure(figsize=(14, 8))
plt.scatter(months, sightings_park_a, c=colors[0], marker=markers[0], s=species_diversity_a*2, label='Central Park')
plt.scatter(months, sightings_park_b, c=colors[1], marker=markers[1], s=species_diversity_b*2, label='Riverside Park')
plt.scatter(months, sightings_park_c, c=colors[2], marker=markers[2], s=species_diversity_c*2, label='Greenwood Park')
plt.scatter(months, sightings_park_d, c=colors[3], marker=markers[3], s=species_diversity_d*2, label='Meadowland Park')
plt.scatter(months, sightings_park_e, c=colors[4], marker=markers[4], s=species_diversity_e*2, label='Sunnyvale Park')
plt.scatter(months, sightings_park_f, c=colors[5], marker=markers[5], s=species_diversity_f*2, label='Lakeside Park')

# Adding title and axis labels
plt.title('Urban Wildlife Sightings\nMonthly Observations in City Parks Over a Year', fontsize=16, weight='bold')
plt.xlabel('Month (1: Jan, 12: Dec)', fontsize=12)
plt.ylabel('Number of Sightings', fontsize=12)

# Adding a legend and grid lines
plt.legend(title='Parks', fontsize=10, loc='upper left', frameon=True)
plt.grid(True, linestyle='--', alpha=0.5)

# Custom tick labels for the months
plt.xticks(months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.yticks(np.arange(0, 50, 5))

# Ensure the layout is adjusted to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()