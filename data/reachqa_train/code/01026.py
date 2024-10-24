import matplotlib.pyplot as plt
import numpy as np

# Time period (10 years)
years = np.arange(2010, 2020)

# Data for energy production (in GWh) from different sources
# Adjusted to ensure clarity and cumulative logic
solar_energy = np.array([30, 50, 70, 85, 100, 130, 160, 190, 220, 250])
wind_energy = np.array([20, 30, 40, 70, 90, 115, 140, 170, 210, 240])
hydropower_energy = np.array([60, 65, 70, 75, 80, 85, 90, 95, 100, 105])
biomass_energy = np.array([10, 20, 25, 35, 45, 55, 65, 75, 85, 95])
geothermal_energy = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

# Combine data for stacked area plot
energy_data = np.vstack([solar_energy, wind_energy, hydropower_energy, biomass_energy, geothermal_energy])

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Create the stacked area plot
ax.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydropower', 'Biomass', 'Geothermal'],
             colors=['#FFD700', '#87CEEB', '#4682B4', '#8B4513', '#DC143C'], alpha=0.85)

# Set the title and labels
ax.set_title("Decade of Renewable Energy Growth in Greenlandia (2010-2019)\nCumulative Energy Production by Source", fontsize=14, weight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Production (GWh)", fontsize=12)

# Add a legend outside the plot area
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Energy Sources')

# Ensure gridlines for better readability
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout to prevent label and legend overlap
plt.tight_layout()

# Display the plot
plt.show()