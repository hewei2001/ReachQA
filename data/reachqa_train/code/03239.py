import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.arange(2000, 2051, 5)

# Contributions of different energy sources (in arbitrary units for simplicity)
solar = [1, 2, 4, 8, 15, 25, 35, 45, 60, 75, 90]
wind = [2, 4, 7, 12, 20, 30, 40, 50, 65, 80, 95]
hydropower = [30, 32, 33, 34, 35, 35, 36, 36, 37, 37, 38]
biomass = [5, 6, 7, 9, 12, 15, 20, 25, 30, 35, 40]

# Calculate cumulative contributions
cumulative_solar = np.cumsum(solar)
cumulative_wind = np.cumsum(wind)
cumulative_hydropower = np.cumsum(hydropower)
cumulative_biomass = np.cumsum(biomass)

# Create a 1x2 subplot layout
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))

# Plot stacked area chart on the first subplot
ax1.stackplot(years, solar, wind, hydropower, biomass, labels=['Solar', 'Wind', 'Hydropower', 'Biomass'],
              colors=['#ffa600', '#bc5090', '#003f5c', '#58508d'], alpha=0.8)
ax1.set_title("The Rise of Renewables:\nEnergy Landscape Transformation (2000-2050)", 
              fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Energy Production (Arbitrary Units)", fontsize=12)
ax1.set_xticks(years)
ax1.xaxis.set_tick_params(rotation=45)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.legend(loc='upper left', title="Renewable Sources", fontsize=10, bbox_to_anchor=(1, 1))
ax1.annotate('Significant Solar Surge', xy=(2040, 190), xytext=(2025, 200),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')

# Plot cumulative line chart on the second subplot
ax2.plot(years, cumulative_solar, label='Cumulative Solar', color='#ffa600', linewidth=2)
ax2.plot(years, cumulative_wind, label='Cumulative Wind', color='#bc5090', linewidth=2)
ax2.plot(years, cumulative_hydropower, label='Cumulative Hydropower', color='#003f5c', linewidth=2)
ax2.plot(years, cumulative_biomass, label='Cumulative Biomass', color='#58508d', linewidth=2)
ax2.set_title("Cumulative Energy Contribution Over Time", fontsize=14, fontweight='bold', pad=15)
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Cumulative Contribution (Arbitrary Units)", fontsize=12)
ax2.set_xticks(years)
ax2.xaxis.set_tick_params(rotation=45)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Adjust layout for better fit
plt.tight_layout()

# Display the plot
plt.show()