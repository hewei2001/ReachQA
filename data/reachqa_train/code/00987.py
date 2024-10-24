import matplotlib.pyplot as plt
import numpy as np

# Years from 2013 to 2023
years = np.arange(2013, 2024)

# Energy production by each source (in TWh)
wind_energy = [10, 15, 20, 25, 30, 36, 42, 50, 58, 67, 75]
solar_energy = [5, 10, 12, 15, 22, 28, 35, 42, 50, 60, 70]
hydro_energy = [20, 18, 22, 24, 26, 27, 30, 32, 33, 35, 37]
biomass_energy = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 25]

# Combine data into an array
energy_data = np.vstack([wind_energy, solar_energy, hydro_energy, biomass_energy])

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the stacked area chart
ax.stackplot(years, energy_data, labels=['Wind', 'Solar', 'Hydro', 'Biomass'],
             colors=['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3'], alpha=0.8)

# Title and labels
ax.set_title('Rising Horizons:\nGreenslandia\'s Renewable Energy Contributions (2013-2023)', fontsize=16, weight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production (TWh)', fontsize=12)

# Add a legend outside the plot area
ax.legend(loc='upper left', title='Energy Source', bbox_to_anchor=(1, 1))

# Customizing the grid and ticks
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xlim(years[0], years[-1])
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Make layout adjustments to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()