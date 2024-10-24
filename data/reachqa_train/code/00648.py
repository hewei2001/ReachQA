import numpy as np
import matplotlib.pyplot as plt

# Years over which the data is distributed
years = np.arange(2010, 2020)

# Energy production data for each renewable source in terawatt-hours (TWh)
# These values are constructed to show incremental growth and changes over time
solar = np.array([5, 12, 19, 25, 30, 38, 45, 50, 58, 65])
wind = np.array([22, 27, 34, 40, 48, 52, 60, 70, 82, 90])
hydro = np.array([55, 55, 57, 60, 64, 68, 73, 78, 85, 92])
biomass = np.array([8, 11, 14, 18, 22, 28, 32, 36, 41, 46])

# Stack the data
data = np.vstack([solar, wind, hydro, biomass])

# Colors for each area
colors = ['gold', 'skyblue', 'lightgreen', 'saddlebrown']

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(years, data, labels=['Solar', 'Wind', 'Hydro', 'Biomass'], colors=colors, alpha=0.8)

# Add labels and title
ax.set_title('A Decade of Green Power: Renewable Energy Production\nin EcoLand', fontsize=14, fontweight='bold', loc='center')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production (TWh)', fontsize=12)

# Configure x-axis ticks and rotate for clarity
ax.set_xticks(years)
ax.tick_params(axis='x', rotation=45)

# Add legend with clear placement
ax.legend(loc='upper left', title='Energy Sources')

# Add grid
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()