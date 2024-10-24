import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = np.arange(2010, 2021)
solar_energy = np.array([2, 3, 5, 8, 12, 20, 30, 45, 60, 80, 95])
wind_energy = np.array([4, 6, 8, 12, 18, 25, 30, 35, 40, 45, 50])
hydro_energy = np.array([10, 10, 11, 12, 13, 15, 18, 21, 24, 28, 30])
geothermal_energy = np.array([1, 1, 2, 3, 5, 7, 9, 11, 13, 14, 15])

# Stack the data for plotting
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, geothermal_energy])

# Plot the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))

# Use stackplot to create the chart
ax.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydro', 'Geothermal'], 
             colors=['#FFD700', '#87CEEB', '#3CB371', '#FF6347'], alpha=0.8)

# Customize the chart with title and labels
ax.set_title('Renewable Energy Adoption in Greenlandia\n(2010-2020)', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12, weight='bold')
ax.set_ylabel('Energy Output (TWh)', fontsize=12, weight='bold')

# Rotate x-axis labels for better readability
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Position the legend outside the plot
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Energy Sources', fontsize=11)

# Improve layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()