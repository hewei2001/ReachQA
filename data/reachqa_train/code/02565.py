import numpy as np
import matplotlib.pyplot as plt

# Define the years from 2020 to 2030
years = np.arange(2020, 2031)

# Define the energy consumption data in Petajoules for each energy source
solar_energy = np.array([5, 10, 18, 28, 40, 55, 70, 90, 110, 130, 150])
wind_energy = np.array([20, 25, 35, 50, 70, 90, 110, 130, 150, 170, 180])
biomass_energy = np.array([15, 20, 25, 30, 40, 50, 60, 70, 80, 85, 90])
fossil_energy = np.array([160, 150, 135, 120, 100, 85, 70, 55, 40, 25, 10])

# New dataset for Energy Efficiency Improvements (as percentages)
energy_efficiency = np.array([2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20])

# Create the figure with two subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

# First subplot: Stacked Area Chart
ax1.stackplot(years, solar_energy, wind_energy, biomass_energy, fossil_energy, 
              labels=['Solar', 'Wind', 'Biomass', 'Fossil Fuels'],
              colors=['#FFA07A', '#87CEEB', '#98FB98', '#B0C4DE'], alpha=0.85)

ax1.set_title("Evolution of Renewable Energy Utilization\nin Neo-Cities (2020-2030)", fontsize=14, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Energy Consumption (Petajoules)", fontsize=12)
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 401, 50))
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.5)

# Annotations for the first plot
ax1.annotate('Breakthrough in Solar Tech', xy=(2024, 50), xytext=(2023, 100),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkgreen')
ax1.annotate('Major Policy Shift', xy=(2027, 65), xytext=(2028, 150),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkblue')

# Second subplot: Line Plot for Energy Efficiency Improvements
ax2.plot(years, energy_efficiency, marker='o', linestyle='-', color='orange', linewidth=2)

ax2.set_title("Improvement in Energy Efficiency\nin Neo-Cities (2020-2030)", fontsize=14, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Efficiency Improvement (%)", fontsize=12)
ax2.set_xticks(years)
ax2.set_yticks(np.arange(0, 21, 2))
ax2.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the combined plots
plt.show()