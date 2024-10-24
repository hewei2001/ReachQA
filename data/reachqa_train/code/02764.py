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

# Calculate the total renewable energy contribution
total_renewable = solar_energy + wind_energy + hydroelectric_energy + geothermal_energy + biomass_energy

# New data for a related subplot - Global energy consumption (fictional data)
global_energy_consumption = np.array([50, 70, 90, 120, 150, 180])

# Colors for each energy source
colors = ['#ffcc00', '#3399ff', '#66cc66', '#ff6666', '#9966ff']

# Create a subplot grid with 1 row and 2 columns
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plot the stacked area chart for renewable energy contributions
ax1.stackplot(decades, [solar_energy, wind_energy, hydroelectric_energy, geothermal_energy, biomass_energy],
              labels=['Solar Energy', 'Wind Energy', 'Hydroelectric Energy', 
                      'Geothermal Energy', 'Biomass Energy'], colors=colors, alpha=0.8)

# Customize the first subplot
ax1.set_title('The Rise of Renewable Energy Sources\nGlobal Energy Contribution by Decade',
              fontsize=16, fontweight='bold')
ax1.set_xlabel('Decade', fontsize=12)
ax1.set_ylabel('Percentage of Global Energy Mix', fontsize=12)
ax1.set_xlim(decades[0], decades[-1])
ax1.set_ylim(0, 100)
ax1.set_yticks(range(0, 101, 10))
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper left', bbox_to_anchor=(1.02, 1), title='Energy Sources', fontsize=10, frameon=False)

# Plot a bar chart for global energy consumption
ax2.bar(decades, global_energy_consumption, color='lightblue', edgecolor='black')

# Customize the second subplot
ax2.set_title('Global Energy Consumption Over Decades', fontsize=16, fontweight='bold')
ax2.set_xlabel('Decade', fontsize=12)
ax2.set_ylabel('Energy Consumption (Exajoules)', fontsize=12)
ax2.set_xlim(decades[0]-5, decades[-1]+5)
ax2.set_ylim(0, 200)
ax2.set_yticks(range(0, 201, 20))
ax2.grid(axis='y', linestyle='--', alpha=0.5)

# Adjust layout to avoid overlapping elements
plt.tight_layout(rect=[0, 0, 0.95, 1])

# Show the plot
plt.show()