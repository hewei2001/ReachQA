import matplotlib.pyplot as plt
import numpy as np

# Data for global renewable energy transition from 2010 to 2020
years = np.arange(2010, 2021)
solar_energy = np.array([1, 2, 4, 6, 8, 12, 16, 21, 27, 33, 40])  # Solar energy percentages
wind_energy = np.array([3, 5, 7, 10, 13, 16, 20, 24, 29, 35, 41])  # Wind energy percentages
hydro_energy = np.array([60, 58, 55, 53, 50, 48, 45, 42, 40, 38, 35])  # Hydroelectric energy percentages
geothermal_energy = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  # Geothermal energy percentages

# Stack the data together for plotting
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, geothermal_energy])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Generate the stacked area chart
ax.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydroelectric', 'Geothermal'],
             colors=['#f9c74f', '#90be6d', '#577590', '#f8961e'], alpha=0.85)

# Add titles and labels
ax.set_title('Global Transition to Renewable Energy Sources\n(2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Total Energy Production', fontsize=12)

# Add a legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Renewable Energy Sources')

# Customize grid and ticks
ax.grid(visible=True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Annotate a significant growth point for solar energy
ax.annotate('Solar Energy Surge', xy=(2019, 27), xytext=(2015, 50),
            arrowprops=dict(facecolor='black', arrowstyle='->', shrinkA=5, shrinkB=5), fontsize=11)

# Ensure tight layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()