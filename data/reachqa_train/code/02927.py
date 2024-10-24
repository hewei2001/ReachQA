import matplotlib.pyplot as plt
import numpy as np

# Years of observation
years = np.arange(2010, 2021)

# Bird populations (in numbers)
sparrow_pop = np.array([150, 170, 180, 200, 220, 250, 275, 300, 310, 320, 325])
pigeon_pop = np.array([120, 130, 140, 145, 150, 155, 160, 165, 168, 170, 175])
crow_pop = np.array([80, 85, 90, 100, 110, 115, 120, 130, 135, 140, 145])
robin_pop = np.array([60, 70, 75, 80, 90, 100, 110, 120, 125, 130, 135])

# Combine the population data
bird_population_data = np.vstack([sparrow_pop, pigeon_pop, crow_pop, robin_pop])
total_pop = sparrow_pop + pigeon_pop + crow_pop + robin_pop
percentage_change = ((total_pop - total_pop[0]) / total_pop[0]) * 100

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Stack the bird populations using stackplot
ax.stackplot(years, bird_population_data, labels=['Sparrows', 'Pigeons', 'Crows', 'Robins'],
             colors=['#4e79a7', '#f28e2b', '#e15759', '#76b7b2'], alpha=0.75)

# Overlay a line plot for the total population trend
ax.plot(years, total_pop, color='black', linewidth=2, linestyle='--', label='Total Population Trend')

# Add secondary y-axis for percentage change
ax2 = ax.twinx()
ax2.plot(years, percentage_change, color='darkgreen', linestyle='-', linewidth=2, label='Percentage Change (%)')
ax2.set_ylabel('Percentage Change (%)', fontsize=12)

# Add annotations for clarity
for i, year in enumerate(years):
    ax.text(year, sparrow_pop[i] / 2, f'{sparrow_pop[i]}', fontsize=9, ha='center', color='white', alpha=0.9)
    ax.text(year, pigeon_pop[i] / 2 + sparrow_pop[i], f'{pigeon_pop[i]}', fontsize=9, ha='center', color='white', alpha=0.9)
    ax.text(year, crow_pop[i] / 2 + pigeon_pop[i] + sparrow_pop[i], f'{crow_pop[i]}', fontsize=9, ha='center', color='white', alpha=0.9)
    ax.text(year, robin_pop[i] / 2 + crow_pop[i] + pigeon_pop[i] + sparrow_pop[i], f'{robin_pop[i]}', fontsize=9, ha='center', color='white', alpha=0.9)

# Title and labels
ax.set_title('Birdsfield Park Avian Biodiversity (2010-2020)\nDetailed Annual Bird Population Survey', fontsize=18, weight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Bird Population Count', fontsize=14)

# Legends
ax.legend(loc='upper left', title='Bird Species', bbox_to_anchor=(1, 1), fontsize=12)
ax2.legend(loc='upper right', title='Trends', bbox_to_anchor=(1.1, 0.9), fontsize=12)

# Customize the grid and ticks
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xlim(years[0], years[-1])
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Ensure no overlapping of elements
fig.tight_layout()

# Show the plot
plt.show()