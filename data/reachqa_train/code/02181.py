import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2015 to 2025
years = np.arange(2015, 2026)

# Renewable energy contribution in gigawatts (GW)
solar_energy = np.array([5, 8, 12, 16, 20, 24, 28, 35, 40, 46, 52])
wind_energy = np.array([10, 15, 22, 30, 40, 50, 60, 75, 85, 95, 100])
hydropower = np.array([20, 21, 22, 24, 25, 26, 27, 28, 30, 31, 32])
biomass = np.array([5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 25])

# Plotting the stacked area chart
plt.figure(figsize=(14, 8))
plt.stackplot(years, solar_energy, wind_energy, hydropower, biomass,
              labels=['Solar Energy', 'Wind Energy', 'Hydropower', 'Biomass'],
              colors=['#FFD700', '#87CEEB', '#1E90FF', '#228B22'],
              alpha=0.7)

# Add title and labels
plt.title('Renewable Energy Transition in Greensville\nFrom 2015 to 2025', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Renewable Energy Supply (GW)', fontsize=12)

# Customize x-axis ticks
plt.xticks(years, rotation=45, ha='right')

# Add grid lines for better readability
plt.grid(visible=True, linestyle='--', alpha=0.5, axis='y')

# Position legend to avoid obscuring the data
plt.legend(loc='upper left', title='Energy Sources', fontsize=10, bbox_to_anchor=(1, 1))

# Automatically adjust layout to fit all elements comfortably
plt.tight_layout()

# Show the plot
plt.show()