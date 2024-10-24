import matplotlib.pyplot as plt
import numpy as np

# Years for the data
years = np.arange(2015, 2026)

# Contribution of various renewable sources in TWh
solar_energy = np.array([10, 20, 30, 45, 60, 80, 110, 140, 180, 230, 300])
wind_energy = np.array([40, 55, 70, 90, 115, 140, 170, 200, 240, 285, 340])
hydro_energy = np.array([50, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])
biomass_energy = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
geothermal_energy = np.array([5, 7, 9, 12, 15, 18, 20, 22, 25, 28, 30])

# Calculate the bottom position for each area
wind_bottom = solar_energy
hydro_bottom = wind_bottom + wind_energy
biomass_bottom = hydro_bottom + hydro_energy
geothermal_bottom = biomass_bottom + biomass_energy

# Plotting the area chart
fig, ax = plt.subplots(figsize=(12, 8))

ax.fill_between(years, solar_energy, label='Solar Energy', color='gold', alpha=0.8)
ax.fill_between(years, wind_bottom, wind_bottom + wind_energy, label='Wind Energy', color='deepskyblue', alpha=0.8)
ax.fill_between(years, hydro_bottom, hydro_bottom + hydro_energy, label='Hydro Energy', color='mediumseagreen', alpha=0.8)
ax.fill_between(years, biomass_bottom, biomass_bottom + biomass_energy, label='Biomass Energy', color='saddlebrown', alpha=0.8)
ax.fill_between(years, geothermal_bottom, geothermal_bottom + geothermal_energy, label='Geothermal Energy', color='darkorange', alpha=0.8)

# Adding titles and labels
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Contribution (TWh)', fontsize=12)
ax.set_title('Renewable Energy Sources Contribution Over Time\nA Perspective on Clean Energy Growth (2015-2025)', fontsize=16, fontweight='bold', pad=20)

# Customize x-ticks to avoid overlap
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Adding a legend
ax.legend(loc='upper left', title='Energy Sources', fontsize=10)

# Adding a grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Display the chart
plt.show()