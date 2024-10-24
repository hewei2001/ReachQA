import matplotlib.pyplot as plt
import numpy as np

# Years of interest
years = np.arange(2010, 2021)

# Percentage of energy consumption
renewable_energy = np.array([5, 7, 10, 15, 20, 25, 35, 45, 55, 65, 70])
fossil_fuel_energy = np.array([95, 93, 90, 85, 80, 75, 65, 55, 45, 35, 30])

# Renewable energy sources in 2020
renewable_sources_2020 = {'Wind': 40, 'Solar': 30, 'Hydro': 20, 'Others': 10}

# Set up a subplot grid: 1 row, 2 columns
fig, axs = plt.subplots(1, 2, figsize=(15, 7))

# Plot the energy consumption trends
axs[0].plot(years, renewable_energy, label='Renewable Energy', color='green', marker='o', linewidth=2)
axs[0].plot(years, fossil_fuel_energy, label='Fossil Fuel Energy', color='grey', linestyle='--', marker='x', linewidth=2)

# Annotate key points with transitions
annotations = {2013: "Wind Farms Investment", 2015: "Solar Initiative Launched", 2018: "Green City Policy Enacted"}
for year, note in annotations.items():
    y_value = renewable_energy[year - 2010]
    axs[0].annotate(note, xy=(year, y_value), xytext=(year + 0.5, y_value + 10),
                    arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, ha='right')

# Annotate data points with their values
for i, year in enumerate(years):
    axs[0].text(year, renewable_energy[i] - 5, f'{renewable_energy[i]}%', color='green', fontsize=8, ha='center')
    axs[0].text(year, fossil_fuel_energy[i] + 2, f'{fossil_fuel_energy[i]}%', color='grey', fontsize=8, ha='center')

# Customize the main chart
axs[0].set_title('Energy Consumption Transition\nin Coastal City (2010-2020)', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Percentage of Energy Consumption (%)', fontsize=12)
axs[0].set_xlim(2010, 2020)
axs[0].set_ylim(0, 100)
axs[0].legend(loc='upper left', fontsize=10, frameon=True)
axs[0].grid(True, linestyle='--', alpha=0.6)

# Create a pie chart showing the breakdown of renewable sources in 2020
axs[1].pie(renewable_sources_2020.values(), labels=renewable_sources_2020.keys(),
           autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen', 'gold', 'lightcoral'])
axs[1].set_title('Renewable Energy Sources Breakdown in 2020', fontsize=14, fontweight='bold')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()