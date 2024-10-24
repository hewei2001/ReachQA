import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2050, 2061)

# Define data for each component (in arbitrary units)
solar_farms = [20, 25, 30, 35, 40, 50, 55, 60, 65, 70, 75]
vertical_forests = [15, 20, 25, 30, 35, 38, 40, 45, 50, 55, 60]
autonomous_transport = [10, 15, 20, 25, 30, 35, 37, 40, 42, 45, 50]
smart_water_systems = [8, 10, 15, 20, 25, 28, 30, 35, 40, 45, 50]

# Stack the data
data = np.vstack([solar_farms, vertical_forests, autonomous_transport, smart_water_systems])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, data, labels=['Solar Farms', 'Vertical Forests', 'Autonomous Transport', 'Smart Water Systems'],
             colors=['gold', 'forestgreen', 'dodgerblue', 'darkcyan'], alpha=0.85)

# Add titles and labels
ax.set_title('Biocities Evolution (2050-2060):\nIntegration of Nature and Technology', fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Contribution to Biocity Ecosystem (Arbitrary Units)', fontsize=12)

# Customize the legend
ax.legend(loc='upper left', title='Ecosystem Components', fontsize=10)

# Add grid for readability
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()