import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.arange(2010, 2021)

# Energy data (in terawatt-hours) for each renewable source
solar = np.array([1, 2, 4, 8, 12, 18, 25, 32, 40, 50, 60])
wind = np.array([5, 8, 11, 15, 20, 25, 31, 37, 45, 52, 60])
hydro = np.array([20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32])
biomass = np.array([2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 16])

# Aggregate the energy sources for the stacked area plot
energy_sources = np.vstack([solar, wind, hydro, biomass])

# Simulated GDP growth rate data (in percent)
gdp_growth = np.array([2.5, 2.8, 3.1, 3.3, 3.6, 3.9, 4.1, 4.4, 4.7, 5.0, 5.3])

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Stacked area plot for renewable energy
ax1.stackplot(years, energy_sources, labels=['Solar', 'Wind', 'Hydro', 'Biomass'],
              colors=['#FFD700', '#87CEEB', '#32CD32', '#FF6347'], alpha=0.7)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Energy Output (TWh)', fontsize=12, color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.set_title('Renewable Energy Growth in Greenville (2010-2020)\nCompared to GDP Growth Rate', 
              fontsize=16, fontweight='bold', pad=20)

# Annotate significant points
ax1.annotate('Major Solar Investment', xy=(2013, 8), xytext=(2015, 40),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, ha='center', backgroundcolor='white')

ax1.annotate('Wind Energy Boost', xy=(2017, 31), xytext=(2018, 70),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, ha='center', backgroundcolor='white')

# Add legend
ax1.legend(loc='upper left', fontsize=10, title='Energy Source')

# Add grid
ax1.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Secondary y-axis for GDP growth rate
ax2 = ax1.twinx()
ax2.plot(years, gdp_growth, color='darkgrey', marker='o', linestyle='-', linewidth=2)
ax2.set_ylabel('GDP Growth Rate (%)', fontsize=12, color='darkgrey')
ax2.tick_params(axis='y', labelcolor='darkgrey')

# Customize ticks
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 141, 20))
ax2.set_yticks(np.arange(2, 6.1, 0.5))

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()