import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

# Data for global renewable energy transition from 2010 to 2020
years = np.arange(2010, 2021)
solar_energy = np.array([1, 2, 4, 6, 8, 12, 16, 21, 27, 33, 40])
wind_energy = np.array([3, 5, 7, 10, 13, 16, 20, 24, 29, 35, 41])
hydro_energy = np.array([60, 58, 55, 53, 50, 48, 45, 42, 40, 38, 35])
geothermal_energy = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Simulated additional data for the second subplot
total_energy = solar_energy + wind_energy + hydro_energy + geothermal_energy
non_renewable_energy = 100 - total_energy  # Assuming total production is 100 for simplicity

# Create the plot with two subplots
fig = plt.figure(figsize=(14, 8))
gs = GridSpec(1, 2, width_ratios=[2, 1])

# Stacked area chart
ax1 = fig.add_subplot(gs[0])
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, geothermal_energy])
ax1.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydroelectric', 'Geothermal'],
              colors=['#f9c74f', '#90be6d', '#577590', '#f8961e'], alpha=0.85)
ax1.set_title('Global Transition to Renewable Energy Sources\n(2010-2020)', fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Percentage of Total Energy Production', fontsize=12)
ax1.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Renewable Energy Sources')
ax1.grid(visible=True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, ha='right')
ax1.annotate('Solar Energy Surge', xy=(2019, 27), xytext=(2015, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->', shrinkA=5, shrinkB=5), fontsize=11)

# Line chart for total vs non-renewable energy
ax2 = fig.add_subplot(gs[1])
ax2.plot(years, total_energy, label='Total Renewable', color='#90be6d', linewidth=2, marker='o')
ax2.plot(years, non_renewable_energy, label='Non-Renewable', color='#f94144', linewidth=2, marker='s')
ax2.set_title('Renewable vs Non-Renewable\nEnergy (2010-2020)', fontsize=14, fontweight='bold', pad=15)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Energy Production (%)', fontsize=12)
ax2.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Energy Sources')
ax2.grid(visible=True, linestyle='--', linewidth=0.5, alpha=0.7)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45, ha='right')

# Ensure tight layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()