import matplotlib.pyplot as plt
import numpy as np

# Years for the x-axis
years = np.arange(2000, 2021)

# Simulated energy production data (in terawatt-hours, TWh)
solar_energy = np.array([1, 2, 3, 5, 7, 10, 15, 20, 25, 35, 50, 65, 80, 100, 125, 150, 180, 220, 270, 350, 450])
wind_energy = np.array([5, 8, 12, 16, 20, 30, 35, 45, 55, 65, 75, 85, 100, 120, 140, 160, 190, 220, 250, 280, 320])
hydro_energy = np.array([50, 52, 55, 56, 58, 60, 60, 62, 63, 65, 68, 70, 72, 73, 75, 76, 78, 80, 82, 83, 85])
biomass_energy = np.array([2, 3, 4, 6, 8, 11, 13, 15, 18, 22, 28, 34, 40, 45, 52, 60, 68, 77, 85, 95, 105])
geothermal_energy = np.array([1, 1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 35])

# Create a stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))

# Stack the energy data
ax.stackplot(years, solar_energy, wind_energy, hydro_energy, biomass_energy, geothermal_energy,
             labels=['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal'],
             colors=['#FFD700', '#76C7C0', '#4682B4', '#8B4513', '#4B0082'], alpha=0.85)

# Title and labels
ax.set_title("Evolving Landscape of Renewable Energy\nin EcoLand (2000-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Production (TWh)", fontsize=12)

# Customize grid style
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Set ticks for both axes
ax.set_xticks(years[::2])  # Show every other year for clarity
ax.set_yticks(np.arange(0, 901, 100))

# Rotate the x-tick labels for better readability
ax.set_xticklabels(years[::2], rotation=45, ha='right')

# Adding a legend and positioning it outside the plot area
ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1), title="Energy Sources")

# Adjust layout to prevent overlapping text
plt.tight_layout()

# Display the plot
plt.show()