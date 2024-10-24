import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2000, 2021)

# Define energy production data for each renewable source in TWh
solar_energy = np.array([0, 0.2, 0.4, 0.6, 1, 2, 4, 8, 12, 18, 26, 35, 47, 60, 75, 90, 110, 130, 150, 170, 190])
wind_energy = np.array([1, 1.5, 2, 2.5, 5, 7, 10, 14, 19, 25, 32, 40, 49, 59, 70, 85, 100, 120, 140, 165, 185])
hydro_energy = np.array([20, 20.5, 21, 21.5, 22, 22.5, 23, 24, 25, 25.5, 26, 26.5, 27, 27.5, 28, 29, 29.5, 30, 30.5, 31, 32])
biomass_energy = np.array([1, 1.2, 1.5, 1.8, 2, 3, 4, 5, 7, 8, 9, 11, 13, 15, 18, 20, 22, 24, 26, 28, 30])
geothermal_energy = np.array([0.5, 0.5, 0.6, 0.6, 0.7, 0.9, 1, 1.1, 1.5, 1.8, 2, 2.3, 2.5, 3, 3.2, 3.5, 3.8, 4.1, 4.5, 5, 5.5])

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 9))

# Plot each source's contribution as a stacked bar chart
ax.bar(years, solar_energy, color='#FFD700', label='Solar Energy', alpha=0.85)
ax.bar(years, wind_energy, bottom=solar_energy, color='#00BFFF', label='Wind Energy', alpha=0.85)
ax.bar(years, hydro_energy, bottom=solar_energy + wind_energy, color='#32CD32', label='Hydro Energy', alpha=0.85)
ax.bar(years, biomass_energy, bottom=solar_energy + wind_energy + hydro_energy, color='#8B4513', label='Biomass Energy', alpha=0.85)
ax.bar(years, geothermal_energy, bottom=solar_energy + wind_energy + hydro_energy + biomass_energy, color='#FF6347', label='Geothermal Energy', alpha=0.85)

# Set title and labels
ax.set_title('Renewable Energy Production in Energia\n2000-2020', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production (TWh)', fontsize=12)

# Add a legend to the plot, ensuring it does not overlap with the chart
ax.legend(loc='upper left', fontsize=10, frameon=False)

# Add grid lines for better readability
ax.grid(True, which='major', linestyle='--', alpha=0.6)

# Adjust x-axis ticks for clarity
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Annotate each year's total energy production
for i, year in enumerate(years):
    total_energy = solar_energy[i] + wind_energy[i] + hydro_energy[i] + biomass_energy[i] + geothermal_energy[i]
    ax.annotate(f"{total_energy:.1f} TWh", (year, total_energy + 2),
                textcoords="offset points", xytext=(0, 5), ha='center', fontsize=9, weight='bold')

# Include another plot for percentage change
ax2 = ax.twinx()
percent_change = np.diff(np.sum([solar_energy, wind_energy, hydro_energy, biomass_energy, geothermal_energy], axis=0)) / np.sum([solar_energy, wind_energy, hydro_energy, biomass_energy, geothermal_energy], axis=0)[:-1] * 100
percent_change = np.insert(percent_change, 0, 0) # first year has no change
ax2.plot(years, percent_change, color='gray', linestyle='-', linewidth=1.5, label='Year-over-Year % Change', alpha=0.7)
ax2.set_ylabel('Year-over-Year % Change', fontsize=12)
ax2.legend(loc='upper right', fontsize=10, frameon=False)

# Ensure y-axis accommodates all data
ax.set_ylim(0, max(solar_energy + wind_energy + hydro_energy + biomass_energy + geothermal_energy) + 20)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()