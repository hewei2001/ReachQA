import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2020)

# Fictional energy production data in TWh
solar_energy = np.array([5, 10, 18, 30, 50, 70, 85, 100, 115, 130])
wind_energy = np.array([20, 25, 30, 35, 40, 50, 60, 75, 85, 90])
hydro_energy = np.array([40, 42, 45, 47, 50, 52, 55, 58, 60, 62])
biomass_energy = np.array([10, 12, 15, 18, 20, 25, 28, 30, 32, 35])

# New data: Percentage of total energy from renewable sources
renewable_percentage = np.array([12, 14, 16, 18, 21, 23, 26, 29, 31, 34])

# Stack the data for the area chart
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, biomass_energy])

fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot the stacked area chart
ax1.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydro', 'Biomass'], 
              colors=['gold', 'skyblue', 'lightgreen', 'sienna'], alpha=0.8)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Energy Production (TWh)', fontsize=14)

# Adding the line plot on secondary y-axis
ax2 = ax1.twinx()
ax2.plot(years, renewable_percentage, color='darkred', marker='o', linestyle='-', linewidth=2, label='Renewable %')
ax2.set_ylabel('Percentage of Total Energy (%)', fontsize=14, color='darkred')
ax2.tick_params(axis='y', labelcolor='darkred')

# Set the title and subtitle
ax1.set_title("Renewable Energy Production Trends\nA Decade of Green Growth", fontsize=18, fontweight='bold')

# Customize the x-axis
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Add a grid for better readability
ax1.grid(visible=True, which='major', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)
ax1.minorticks_on()
ax1.grid(visible=True, which='minor', linestyle=':', linewidth=0.5, color='grey', alpha=0.5)

# Add legends
ax1.legend(loc='upper left', title='Energy Source')
ax2.legend(loc='upper right', title='Renewable Percentage')

# Annotate significant data points
ax1.annotate('Significant Solar Surge', xy=(2014, 50), xytext=(2012, 90),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

plt.show()