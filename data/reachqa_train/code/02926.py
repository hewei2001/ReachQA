import matplotlib.pyplot as plt
import numpy as np

# Years of observation
years = np.arange(2010, 2021)

# Bird populations (in numbers)
sparrow_pop = [150, 170, 180, 200, 220, 250, 275, 300, 310, 320, 325]
pigeon_pop = [120, 130, 140, 145, 150, 155, 160, 165, 168, 170, 175]
crow_pop = [80, 85, 90, 100, 110, 115, 120, 130, 135, 140, 145]
robin_pop = [60, 70, 75, 80, 90, 100, 110, 120, 125, 130, 135]

# Combine the population data
bird_population_data = np.vstack([sparrow_pop, pigeon_pop, crow_pop, robin_pop])

# Create the area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Stack the bird populations using stackplot
ax.stackplot(years, bird_population_data, labels=['Sparrows', 'Pigeons', 'Crows', 'Robins'],
             colors=['#f4a460', '#ffa07a', '#8a2be2', '#20b2aa'], alpha=0.75)

# Add annotations for clarity
for i, year in enumerate(years):
    ax.text(year, sparrow_pop[i], f'{sparrow_pop[i]}', fontsize=9, ha='center', va='bottom', color='black', alpha=0.7)
    ax.text(year, pigeon_pop[i] + sparrow_pop[i], f'{pigeon_pop[i]}', fontsize=9, ha='center', va='bottom', color='black', alpha=0.7)
    ax.text(year, crow_pop[i] + pigeon_pop[i] + sparrow_pop[i], f'{crow_pop[i]}', fontsize=9, ha='center', va='bottom', color='black', alpha=0.7)
    ax.text(year, robin_pop[i] + crow_pop[i] + pigeon_pop[i] + sparrow_pop[i], f'{robin_pop[i]}', fontsize=9, ha='center', va='bottom', color='black', alpha=0.7)

# Title and labels
ax.set_title('Birdsfield Park Avian Biodiversity (2010-2020)\nAnnual Bird Population Survey', fontsize=18, weight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Bird Population Count', fontsize=14)

# Legend outside the plot area
ax.legend(loc='upper left', title='Bird Species', bbox_to_anchor=(1, 1), fontsize=12)

# Customize the grid and ticks
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xlim(years[0], years[-1])
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Adjust the layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()