import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Define the data for renewable energy contributions over the years
solar_energy = np.array([5, 8, 12, 16, 22, 28, 34, 40, 47, 55, 60])
wind_energy = np.array([7, 10, 13, 18, 20, 23, 27, 30, 35, 38, 42])
hydro_energy = np.array([20, 22, 24, 25, 26, 27, 29, 30, 31, 32, 34])
geothermal_energy = np.array([3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12])

# Stack the data vertically
data = np.vstack([solar_energy, wind_energy, hydro_energy, geothermal_energy])

# Define colors for each energy type
colors = ['#ffcc00', '#66c2ff', '#99e699', '#ff9966']

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, data, labels=['Solar Energy', 'Wind Energy', 'Hydro Energy', 'Geothermal Energy'], colors=colors, alpha=0.85)

# Set the title with line breaks for readability
ax.set_title('Renewable Energy Contributions in Solaria\n2010-2020', fontsize=16, fontweight='bold')

# Label the axes
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Total Energy Supply', fontsize=12)

# Add a legend and adjust its position
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title="Energy Types")

# Include a grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Ensure layout is adjusted to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()