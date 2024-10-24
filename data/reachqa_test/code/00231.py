import numpy as np
import matplotlib.pyplot as plt

# Define the timeline
years = np.arange(2025, 2051)

# Define energy consumption data as a percentage of total energy
fossil_fuels = np.array([70, 68, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 8, 5, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0])
solar = np.array([5, 7, 10, 12, 15, 18, 20, 22, 25, 28, 30, 32, 33, 35, 37, 40, 42, 44, 45, 46, 46, 46, 46, 46, 46, 46])
wind = np.array([10, 11, 12, 15, 18, 20, 22, 25, 28, 30, 32, 33, 34, 35, 35, 36, 37, 38, 39, 40, 40, 40, 40, 40, 40, 40])
hydro = np.array([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
geothermal = np.array([3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 8, 8, 9, 10, 10, 10, 11, 11, 12, 12, 13, 14])
biomass = np.array([2, 2, 3, 5, 8, 10, 11, 12, 14, 17, 18, 19, 22, 23, 25, 26, 28, 30, 30, 32, 33, 33, 34, 34, 34, 34])

# Calculate total renewable energy percentage
renewable_energy = solar + wind + hydro + geothermal + biomass

# Combine all energy sources into a data array
energy_data = np.array([fossil_fuels, solar, wind, hydro, geothermal, biomass])

# Define colors for each energy source
colors = ['#808080', '#FFD700', '#00BFFF', '#40E0D0', '#FF69B4', '#228B22']

# Create the figure and plot the stacked area chart
plt.figure(figsize=(14, 8))
plt.stackplot(years, energy_data, labels=['Fossil Fuels', 'Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass'], colors=colors, alpha=0.8)

# Overlay line plot for renewable energy
plt.plot(years, renewable_energy, color='darkred', linewidth=2.5, linestyle='--', marker='o', label='Total Renewable Energy')

# Set the axes labels and title
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Consumption (%)', fontsize=12)
plt.title('Renewable Energy Evolution in Fictionland\n(2025-2050)', fontsize=14, fontweight='bold')

# Add a legend, positioning it outside the plot
plt.legend(loc='upper left', fontsize=10, title="Energy Source", bbox_to_anchor=(1.05, 1))

# Adjust the x-axis labels for better readability
plt.xticks(years, rotation=45)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()