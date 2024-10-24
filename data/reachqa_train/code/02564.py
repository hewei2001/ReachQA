import numpy as np
import matplotlib.pyplot as plt

# Define the years from 2020 to 2030
years = np.arange(2020, 2031)

# Define the energy consumption data in Petajoules for each energy source
solar_energy = np.array([5, 10, 18, 28, 40, 55, 70, 90, 110, 130, 150])
wind_energy = np.array([20, 25, 35, 50, 70, 90, 110, 130, 150, 170, 180])
biomass_energy = np.array([15, 20, 25, 30, 40, 50, 60, 70, 80, 85, 90])
fossil_energy = np.array([160, 150, 135, 120, 100, 85, 70, 55, 40, 25, 10])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))

# Stack the data with distinct colors for each energy source
ax.stackplot(years, solar_energy, wind_energy, biomass_energy, fossil_energy, 
             labels=['Solar', 'Wind', 'Biomass', 'Fossil Fuels'],
             colors=['#FFA07A', '#87CEEB', '#98FB98', '#B0C4DE'], alpha=0.85)

# Add chart details
ax.set_title("Evolution of Renewable Energy Utilization\nin Neo-Cities (2020-2030)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Consumption (Petajoules)", fontsize=12)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 401, 50))

# Position the legend outside the main plot area
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Add a grid for better readability
ax.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.5)

# Annotate significant milestones in the data
ax.annotate('Breakthrough in Solar Tech', xy=(2024, 50), xytext=(2023, 100),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkgreen')
ax.annotate('Major Policy Shift', xy=(2027, 65), xytext=(2028, 150),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkblue')

# Adjust the layout automatically to prevent text from being cut off
plt.tight_layout()

# Display the plot
plt.show()