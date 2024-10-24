import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Define energy production data for each renewable source in TWh
solar_energy = np.array([1, 2, 4, 8, 12, 18, 26, 35, 47, 60, 75])
wind_energy = np.array([5, 7, 10, 14, 19, 25, 32, 40, 49, 59, 70])
hydro_energy = np.array([20, 21, 22, 21, 22, 23, 24, 23, 24, 25, 24])
biomass_energy = np.array([2, 3, 4, 5, 7, 8, 9, 11, 13, 15, 18])

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each source's contribution as a stacked bar chart
ax.bar(years, solar_energy, color='#FFD700', label='Solar Energy', alpha=0.85)
ax.bar(years, wind_energy, bottom=solar_energy, color='#00BFFF', label='Wind Energy', alpha=0.85)
ax.bar(years, hydro_energy, bottom=solar_energy + wind_energy, color='#32CD32', label='Hydro Energy', alpha=0.85)
ax.bar(years, biomass_energy, bottom=solar_energy + wind_energy + hydro_energy, color='#8B4513', label='Biomass Energy', alpha=0.85)

# Set title and labels
ax.set_title('Renewable Energy Production in Energia\n(2010-2020)', fontsize=16, fontweight='bold', pad=20)
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
    total_energy = solar_energy[i] + wind_energy[i] + hydro_energy[i] + biomass_energy[i]
    ax.annotate(f"{total_energy} TWh", (year, total_energy + 2),
                textcoords="offset points", xytext=(0, 5), ha='center', fontsize=9, weight='bold')

# Ensure y-axis accommodates all data
ax.set_ylim(0, max(solar_energy + wind_energy + hydro_energy + biomass_energy) + 10)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()