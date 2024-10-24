import matplotlib.pyplot as plt
import numpy as np

# Define the decades on the x-axis
decades = np.array([1970, 1980, 1990, 2000, 2010, 2020])

# Contribution percentages of each renewable energy source over time (fictional data)
solar_energy = np.array([0, 0.5, 1, 5, 15, 25])
wind_energy = np.array([0, 1, 2, 10, 20, 30])
hydroelectric_energy = np.array([5, 7, 10, 13, 15, 18])
geothermal_energy = np.array([0.5, 1, 1.5, 2, 3, 4])
biomass_energy = np.array([1, 2, 3, 4, 5, 6])

# Stack the energy data
energy_data = np.vstack([solar_energy, wind_energy, hydroelectric_energy, geothermal_energy, biomass_energy])

# Define colors for each energy source
colors = ['#ffcc00', '#3399ff', '#66cc66', '#ff6666', '#9966ff']

# Create the stacked area plot
fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(decades, energy_data, labels=[
    'Solar Energy', 'Wind Energy', 'Hydroelectric Energy', 
    'Geothermal Energy', 'Biomass Energy'], colors=colors, alpha=0.8)

# Customize the chart
ax.set_title('The Rise of Renewable Energy Sources\nGlobal Energy Contribution by Decade', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Percentage of Global Energy Mix', fontsize=12)
ax.set_xlim(decades[0], decades[-1])
ax.set_ylim(0, 100)
ax.set_yticks(range(0, 101, 10))

# Rotate x-axis labels for better readability
plt.xticks(decades, rotation=45)

# Add a grid for easier visualization
ax.grid(True, linestyle='--', alpha=0.5)

# Add a legend outside the main plot area
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), title='Energy Sources', fontsize=10, title_fontsize='12', frameon=False)

# Enhance layout for readability and avoid occlusion
plt.tight_layout(rect=[0, 0, 0.85, 1])  # Adjust layout to fit legend

# Show the plot
plt.show()