import matplotlib.pyplot as plt
import numpy as np

# Define years and energy consumption data for each renewable source
years = np.arange(2010, 2020)
solar_energy = np.array([20, 25, 30, 40, 50, 65, 80, 100, 130, 160])
wind_energy = np.array([50, 55, 60, 80, 100, 120, 150, 180, 210, 240])
hydro_energy = np.array([100, 100, 110, 115, 120, 125, 130, 135, 140, 145])
bioenergy = np.array([30, 35, 40, 50, 55, 65, 75, 85, 95, 100])

# Calculate total energy consumption
total_energy = solar_energy + wind_energy + hydro_energy + bioenergy

# Hypothetical target energy consumption for the same period
target_energy = np.array([210, 220, 230, 250, 270, 290, 320, 350, 390, 450])

# Stack the data
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, bioenergy])

# Plotting the chart
fig, ax = plt.subplots(figsize=(12, 7))

# Stacked area plot for different energy sources
ax.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydro', 'Bioenergy'],
             colors=['#ffd700', '#00bfff', '#228b22', '#d2691e'], alpha=0.8)

# Overlay line plot for total energy consumption
ax.plot(years, total_energy, color='black', linestyle='-', linewidth=2, marker='o',
        label='Total Energy Consumption')

# Overlay dashed line plot for target energy consumption
ax.plot(years, target_energy, color='red', linestyle='--', linewidth=2, marker='x',
        label='Target Energy Consumption')

# Adding title and labels
ax.set_title('Renewable Energy Consumption vs Targets\n(2010-2019)', fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Consumption (Petajoules)', fontsize=12)

# Adding a legend
ax.legend(loc='upper left', title='Energy Sources', fontsize=10, title_fontsize='13')

# Adding grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Improving layout
plt.xticks(years, rotation=45)
plt.tight_layout()

# Display the plot
plt.show()