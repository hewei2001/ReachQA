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

# Total renewable energy
total_renewable_energy = solar_energy + wind_energy + hydro_energy + biomass_energy + geothermal_energy

# New data for secondary plot: percentage of renewable in total energy consumption
total_energy_consumption = np.array([300, 310, 320, 335, 350, 365, 380, 400, 420, 445, 470])
renewable_share_percentage = (total_renewable_energy / total_energy_consumption) * 100

# Calculate the bottom position for each area
wind_bottom = solar_energy
hydro_bottom = wind_bottom + wind_energy
biomass_bottom = hydro_bottom + hydro_energy
geothermal_bottom = biomass_bottom + biomass_energy

# Plotting the subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Area Chart for Renewable Energy Contribution
ax1.fill_between(years, solar_energy, label='Solar Energy', color='gold', alpha=0.8)
ax1.fill_between(years, wind_bottom, wind_bottom + wind_energy, label='Wind Energy', color='deepskyblue', alpha=0.8)
ax1.fill_between(years, hydro_bottom, hydro_bottom + hydro_energy, label='Hydro Energy', color='mediumseagreen', alpha=0.8)
ax1.fill_between(years, biomass_bottom, biomass_bottom + biomass_energy, label='Biomass Energy', color='saddlebrown', alpha=0.8)
ax1.fill_between(years, geothermal_bottom, geothermal_bottom + geothermal_energy, label='Geothermal Energy', color='darkorange', alpha=0.8)

ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Energy Contribution (TWh)', fontsize=12)
ax1.set_title('Renewable Energy Sources Contribution Over Time\n(2015-2025)', fontsize=14, fontweight='bold', pad=10)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, ha='right')
ax1.legend(loc='upper left', title='Energy Sources', fontsize=10)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Line Chart for Renewable Share in Total Energy
ax2.plot(years, renewable_share_percentage, marker='o', color='mediumseagreen', linewidth=2, label='Renewable Share (%)')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Share of Renewable (%)', fontsize=12)
ax2.set_title('Growth of Renewable Share in Total Energy\n(2015-2025)', fontsize=14, fontweight='bold', pad=10)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45, ha='right')
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)

# Annotate a key milestone
ax2.annotate('Surpasses 40%', xy=(2023, renewable_share_percentage[8]), xytext=(2020, 45),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, fontweight='bold')

# Automatically adjust layout
plt.tight_layout()

# Display the combined plots
plt.show()