import matplotlib.pyplot as plt
import numpy as np

# Define decades for the x-axis
decades = np.arange(1970, 2021, 10)

# Population data in millions for each region
ardent_population = np.array([2, 3, 4, 5, 6, 7])
lumina_population = np.array([1, 2, 2.5, 3.5, 5, 6])
glacia_population = np.array([0.5, 1, 1.5, 2, 2.5, 3])

# Calculate the average population for each decade
average_population = (ardent_population + lumina_population + glacia_population) / 3

# Calculate the growth rate for Ardent
ardent_growth_rate = np.array([0] + [100 * (ardent_population[i] - ardent_population[i-1]) / ardent_population[i-1] 
                                      for i in range(1, len(ardent_population))])

# Combine data to create stacked area chart
populations = np.vstack([ardent_population, lumina_population, glacia_population])

# Define the colors for each region
colors = ['#FF9999', '#66B3FF', '#99FF99']

# Plotting the Area Chart
fig, ax1 = plt.subplots(figsize=(12, 7))
ax1.stackplot(decades, populations, labels=['Ardent', 'Lumina', 'Glacia'], colors=colors, alpha=0.8)
ax1.set_title('Population Growth in the\nFictional Land of Vesperia Over Decades', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Population (millions)', fontsize=12)
ax1.grid(linestyle='--', alpha=0.6)
ax1.set_xticks(decades)
ax1.set_xticklabels([str(year) for year in decades], rotation=45)
ax1.set_yticks(np.arange(0, 18, 2))

# Add a secondary y-axis for growth rate
ax2 = ax1.twinx()
ax2.plot(decades, ardent_growth_rate, 'o--', color='#FF5733', label='Ardent Growth Rate')
ax2.set_ylabel('Growth Rate (%)', fontsize=12, color='#FF5733')
ax2.tick_params(axis='y', colors='#FF5733')
ax2.set_yticks(np.arange(0, 110, 20))

# Add a line plot for average population
ax1.plot(decades, average_population, 's-', color='#6A0DAD', label='Average Population')

# Consolidate legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', title='Vesperia Metrics')

# Automatically adjust layout
fig.tight_layout()

plt.show()