import matplotlib.pyplot as plt
import numpy as np

# Define the years and energy data for each source
years = np.arange(2013, 2023)
solar_energy = np.array([10, 15, 25, 35, 45, 60, 80, 100, 125, 150])
wind_energy = np.array([30, 35, 40, 42, 44, 46, 50, 55, 60, 65])
hydro_energy = np.array([50, 50, 50, 50, 55, 55, 60, 60, 65, 70])
biomass_energy = np.array([10, 12, 14, 16, 18, 20, 25, 30, 35, 40])

# Create the stacked area plot
fig, ax = plt.subplots(figsize=(12, 6))
ax.stackplot(years, solar_energy, wind_energy, hydro_energy, biomass_energy,
             labels=['Solar', 'Wind', 'Hydro', 'Biomass'],
             colors=['#ffdd57', '#77dd77', '#84b6f4', '#c59434'], alpha=0.8)

# Title and labels
ax.set_title('Greensville Renewable Energy Consumption\n(2013-2022)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Consumption (GWh)', fontsize=12)

# Add a legend and grid
ax.legend(loc='upper left', title='Energy Sources', fontsize=10, framealpha=0.9)
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Annotate key insights
ax.text(2014, 140, "Introduction of Solar Farms", fontsize=10, color='black', fontstyle='italic', bbox=dict(facecolor='white', alpha=0.5))
ax.text(2020, 300, "Expansion in Wind Turbines", fontsize=10, color='black', fontstyle='italic', bbox=dict(facecolor='white', alpha=0.5))

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()