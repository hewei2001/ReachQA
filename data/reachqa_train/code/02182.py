import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2015 to 2035
years = np.arange(2015, 2036)

# Renewable energy contribution in gigawatts (GW)
solar_energy = np.array([5, 8, 12, 16, 20, 24, 28, 35, 40, 46, 52, 60, 70, 82, 95, 110, 126, 144, 165, 187, 210])
wind_energy = np.array([10, 15, 22, 30, 40, 50, 60, 75, 85, 95, 100, 112, 125, 138, 152, 168, 185, 203, 222, 243, 265])
hydropower = np.array([20, 21, 22, 24, 25, 26, 27, 28, 30, 31, 32, 34, 36, 39, 41, 44, 48, 52, 57, 63, 70])
biomass = np.array([5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 25, 28, 32, 36, 41, 47, 54, 62, 71, 81, 92])
geothermal = np.array([1, 2, 3, 4, 5, 7, 9, 12, 15, 19, 24, 30, 37, 45, 54, 64, 75, 87, 100, 114, 130])

# Calculating emissions reductions (in million tons) as a hypothetical model
emissions_reduction = np.cumsum(np.array([2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15, 18, 21, 25, 29, 34, 40, 47, 55, 64, 74]))

# Plotting
fig, ax1 = plt.subplots(figsize=(16, 10))

# Stacked area chart for energy contributions
ax1.stackplot(years, solar_energy, wind_energy, hydropower, biomass, geothermal,
              labels=['Solar', 'Wind', 'Hydropower', 'Biomass', 'Geothermal'],
              colors=['#FFD700', '#87CEEB', '#1E90FF', '#228B22', '#FF4500'],
              alpha=0.8)

ax1.set_title('Comprehensive Renewable Energy Transition\nAnd Emissions Reduction in Greensville (2015-2035)', fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Total Renewable Energy Supply (GW)', fontsize=12)
ax1.set_xticks(years)
ax1.tick_params(axis='x', rotation=45)
ax1.grid(True, linestyle='--', alpha=0.5, axis='y')
ax1.legend(loc='upper left', title='Energy Sources', fontsize=10)

# Create a secondary axis for carbon emissions reduction
ax2 = ax1.twinx()
ax2.plot(years, emissions_reduction, 'r--', linewidth=2.5, label='Carbon Emissions Reduction')
ax2.set_ylabel('Carbon Emissions Reduction (Million Tons)', fontsize=12, color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Automatically adjust layout to fit all elements comfortably
fig.tight_layout()

# Show the plot
plt.show()