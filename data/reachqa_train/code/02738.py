import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2023 to 2123
years = np.arange(2023, 2124)

# Energy source data (in percentage of total energy consumption)
fossil_fuels = np.linspace(75, 5, len(years))
nuclear = np.linspace(10, 15, len(years))
solar = np.linspace(5, 50, len(years))
wind = np.linspace(10, 30, len(years))

# Stack the data for plotting
energy_sources = np.vstack([fossil_fuels, nuclear, solar, wind])

# Simulated total energy consumption growth over the century (in exajoules)
total_energy_consumption = 2000 + 10 * (years - 2023) ** 0.5

# Create the figure and the primary axis for the stacked area plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Colors for the energy sources
colors = ['#d95f02', '#7570b3', '#1b9e77', '#e7298a']
labels = ['Fossil Fuels', 'Nuclear', 'Solar', 'Wind']

# Stacked area plot
ax1.stackplot(years, energy_sources, labels=labels, colors=colors)
ax1.set_title("Energy Transition in Metropolis 2123:\nEvolution of Energy Sources and Consumption Over a Century", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Energy Consumption (%)", fontsize=12)
ax1.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Annotations for significant transition points
ax1.annotate('Solar becomes dominant', xy=(2080, solar[57]), xytext=(2080, 70),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Create a secondary y-axis for the line plot of total energy consumption
ax2 = ax1.twinx()
ax2.plot(years, total_energy_consumption, label='Total Energy Consumption', color='black', linestyle='--', linewidth=2)
ax2.set_ylabel("Total Energy Consumption (Exajoules)", fontsize=12, color='black')
ax2.legend(loc='upper right', fontsize=10)

# Add gridlines for better readability
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
ax2.grid(False)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()