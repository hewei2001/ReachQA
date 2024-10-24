import matplotlib.pyplot as plt
import numpy as np

# Define the years and energy data for each source
years = np.arange(2013, 2023)
solar_energy = np.array([10, 15, 25, 35, 45, 60, 80, 100, 125, 150])
wind_energy = np.array([30, 35, 40, 42, 44, 46, 50, 55, 60, 65])
hydro_energy = np.array([50, 50, 50, 50, 55, 55, 60, 60, 65, 70])
biomass_energy = np.array([10, 12, 14, 16, 18, 20, 25, 30, 35, 40])

# Calculate total energy consumption and percent change
total_energy = solar_energy + wind_energy + hydro_energy + biomass_energy
percent_change = np.zeros_like(total_energy)
percent_change[1:] = 100 * (total_energy[1:] - total_energy[:-1]) / total_energy[:-1]

# Create a subplot with a stacked area plot and a bar chart
fig, axs = plt.subplots(1, 2, figsize=(18, 6))

# Stacked Area Plot
axs[0].stackplot(years, solar_energy, wind_energy, hydro_energy, biomass_energy,
                 labels=['Solar', 'Wind', 'Hydro', 'Biomass'],
                 colors=['#ffdd57', '#77dd77', '#84b6f4', '#c59434'], alpha=0.8)
axs[0].set_title('Greensville Renewable Energy Consumption\n(2013-2022)', fontsize=16, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Energy Consumption (GWh)', fontsize=12)
axs[0].legend(loc='upper left', title='Energy Sources', fontsize=10, framealpha=0.9)
axs[0].grid(axis='x', linestyle='--', alpha=0.7)
axs[0].text(2014, 140, "Introduction of Solar Farms", fontsize=10, color='black', fontstyle='italic',
            bbox=dict(facecolor='white', alpha=0.5))
axs[0].text(2020, 300, "Expansion in Wind Turbines", fontsize=10, color='black', fontstyle='italic',
            bbox=dict(facecolor='white', alpha=0.5))

# Line Plot for Percent Change
axs[1].plot(years, percent_change, marker='o', linestyle='-', color='purple', label='Annual % Change')
axs[1].set_title('Annual Growth Rate of Total Renewable Energy\n(2013-2022)', fontsize=14)
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Percent Change (%)', fontsize=12)
axs[1].axhline(0, color='gray', linestyle='--', linewidth=0.8)
axs[1].legend(loc='upper left', fontsize=10)
axs[1].grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()