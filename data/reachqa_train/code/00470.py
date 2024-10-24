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

# Create the stacked area plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, energy_sources, labels=['Solar', 'Wind', 'Hydro', 'Biomass'],
             colors=['#FFD700', '#87CEEB', '#32CD32', '#FF6347'], alpha=0.8)

# Title and labels
ax.set_title('Renewable Energy Growth in Greenville (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Output (TWh)', fontsize=14)

# Add the legend
ax.legend(loc='upper left', fontsize=12, title='Energy Source')

# Customize x and y ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 141, 20))

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Annotate significant points
ax.annotate('Major Solar Investment', xy=(2013, 8), xytext=(2015, 40),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, ha='center', backgroundcolor='white')

ax.annotate('Wind Energy Boost', xy=(2017, 31), xytext=(2018, 70),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, ha='center', backgroundcolor='white')

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()