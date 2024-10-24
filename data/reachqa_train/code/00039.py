import matplotlib.pyplot as plt
import numpy as np

# Define years and energy consumption data for each renewable source
years = np.arange(2010, 2020)
solar_energy = [20, 25, 30, 40, 50, 65, 80, 100, 130, 160]
wind_energy = [50, 55, 60, 80, 100, 120, 150, 180, 210, 240]
hydro_energy = [100, 100, 110, 115, 120, 125, 130, 135, 140, 145]
bioenergy = [30, 35, 40, 50, 55, 65, 75, 85, 95, 100]

# Stack the data
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, bioenergy])

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(10, 6))

ax.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydro', 'Bioenergy'],
             colors=['#ffd700', '#00bfff', '#228b22', '#d2691e'], alpha=0.8)

# Adding title and labels
ax.set_title('Renewable Energy Consumption\n2010-2019', fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Consumption (Petajoules)', fontsize=12)

# Adding grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Adding a legend
ax.legend(loc='upper left', title='Energy Sources', fontsize=10, title_fontsize='13')

# Improve layout
plt.xticks(years, rotation=45)
plt.tight_layout()

# Display the plot
plt.show()