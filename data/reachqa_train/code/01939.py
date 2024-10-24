import matplotlib.pyplot as plt
import numpy as np

# Define the extended years from 2000 to 2025
years = np.arange(2000, 2026)

# Define the data for renewable energy contributions over the years
solar_energy = np.array([0, 0, 1, 2, 3, 4, 6, 9, 12, 16, 20, 25, 30, 36, 42, 49, 56, 64, 73, 82, 88, 95, 102, 110, 115, 120])
wind_energy = np.array([1, 2, 3, 4, 6, 8, 10, 13, 16, 20, 25, 31, 37, 44, 51, 59, 66, 72, 78, 84, 90, 95, 100, 105, 110, 115])
hydro_energy = np.array([18, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 30, 31, 31, 31, 32, 33, 33, 34, 34, 35, 35, 35, 35])
geothermal_energy = np.array([1, 1, 1, 1, 2, 2, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 9, 10, 10, 11, 11, 12, 13, 13, 14, 14])
biomass_energy = np.array([0, 0, 1, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10, 11, 12, 13, 13, 14, 15, 15, 16, 16])

# Stack the data vertically
data = np.vstack([solar_energy, wind_energy, hydro_energy, geothermal_energy, biomass_energy])

# Define colors for each energy type
colors = ['#ffcc00', '#66c2ff', '#99e699', '#ff9966', '#cc3399']

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(14, 9))
ax.stackplot(years, data, labels=['Solar Energy', 'Wind Energy', 'Hydro Energy', 'Geothermal Energy', 'Biomass Energy'], colors=colors, alpha=0.85)

# Set the title with line breaks for readability
ax.set_title('Renewable Energy Contributions in Solaria\nfrom 2000 to 2025', fontsize=18, fontweight='bold')

# Label the axes
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Percentage of Total Energy Supply', fontsize=14)

# Add a legend and adjust its position
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title="Energy Types")

# Include a grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Ensure layout is adjusted to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()