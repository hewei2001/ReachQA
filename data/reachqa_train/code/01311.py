import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.arange(2010, 2021)

# Energy production in terawatt-hours (TWh)
asia_solar = [10, 15, 22, 35, 50, 70, 95, 130, 170, 220, 290]
asia_wind = [20, 30, 40, 55, 70, 90, 115, 140, 175, 200, 230]
asia_hydro = [120, 125, 130, 136, 142, 148, 155, 161, 168, 175, 182]
asia_biomass = [5, 8, 12, 16, 21, 27, 33, 40, 48, 57, 65]

# Combine data for stacked area plotting
asia_data = np.array([asia_solar, asia_wind, asia_hydro, asia_biomass])

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))

# Define colors for each energy source
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Stacked Area Chart for Asia
ax.stackplot(years, asia_data, labels=['Solar', 'Wind', 'Hydro', 'Biomass'], colors=colors, alpha=0.8)

# Title and labels
ax.set_title('Renewable Energy Production Growth in Asia\n(2010-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Production (TWh)', fontsize=14)

# Customize x-ticks to enhance readability
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Energy Source', fontsize=12, frameon=False)

# Grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()