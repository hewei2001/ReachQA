import numpy as np
import matplotlib.pyplot as plt

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Data representing the percentage share of each energy source in total renewable energy supply
solar = np.array([5, 6, 7, 9, 12, 15, 18, 22, 26, 30, 35, 40, 45, 50, 55, 60, 62, 64, 66, 68, 70])
wind = np.array([15, 17, 19, 22, 24, 27, 29, 31, 33, 35, 36, 37, 38, 39, 40, 40, 40, 41, 42, 43, 43])
biomass = np.array([30, 29, 28, 26, 25, 23, 22, 21, 20, 18, 17, 16, 15, 14, 13, 12, 12, 12, 11, 10, 10])
hydropower = 100 - (solar + wind + biomass)  # Ensure the total adds up to 100%

# Calculate average contributions
average_contributions = np.mean([solar, wind, biomass, hydropower], axis=1)
energy_sources = ['Solar', 'Wind', 'Biomass', 'Hydropower']

# Set up the subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Stacked Area Chart
ax1.stackplot(years, solar, wind, biomass, hydropower, 
              labels=energy_sources, 
              colors=['#FFD700', '#87CEEB', '#32CD32', '#A9A9A9'], alpha=0.8)
ax1.set_title('Evolution of Renewable Energy Sources in Urban Areas\n(2000-2020)', fontsize=12)
ax1.set_xlabel('Year', fontsize=10)
ax1.set_ylabel('Percentage of Total Renewable Energy Supply', fontsize=10)
ax1.legend(loc='upper left', fontsize=8)
ax1.set_xlim(years.min(), years.max())
ax1.set_ylim(0, 100)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.annotate('Rise of Solar Energy', xy=(2015, 35), xytext=(2005, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9)

# Plot 2: Horizontal Bar Chart for Average Contribution
ax2.barh(energy_sources, average_contributions, color=['#FFD700', '#87CEEB', '#32CD32', '#A9A9A9'])
ax2.set_title('Average Contribution of Energy Sources (2000-2020)', fontsize=12)
ax2.set_xlabel('Average Percentage', fontsize=10)
ax2.set_yticks(range(len(energy_sources)))
ax2.set_yticklabels(energy_sources, fontsize=10)
ax2.grid(axis='x', linestyle='--', alpha=0.5)
ax2.set_xlim(0, 100)

# Tight layout to prevent overlap
plt.tight_layout()

# Display the charts
plt.show()