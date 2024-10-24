import matplotlib.pyplot as plt
import numpy as np

# Years for the data
years = np.array([2018, 2019, 2020, 2021, 2022])

# Regions
regions = ["Northern Region", "Coastal Region", "Desert Region", "Urban Region"]

# Average efficiency for each region over the years
efficiency = np.array([
    [15, 17, 18, 20, 22],  # Northern Region
    [18, 19, 20, 21, 22],  # Coastal Region
    [20, 21, 23, 25, 27],  # Desert Region
    [16, 18, 19, 21, 22]   # Urban Region
])

# Variability (standard deviation) for each region
variability = np.array([
    [1.5, 1.6, 1.7, 1.8, 2.0],  # Northern Region
    [1.2, 1.3, 1.4, 1.5, 1.6],  # Coastal Region
    [1.8, 2.0, 2.2, 2.3, 2.5],  # Desert Region
    [1.3, 1.4, 1.5, 1.6, 1.7]   # Urban Region
])

# Setup the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Colors for each region's line
colors = ['blue', 'green', 'orange', 'red']

# Plot the data with error bars
for i, region in enumerate(regions):
    ax.errorbar(
        years, efficiency[i], yerr=variability[i], label=region,
        fmt='-o', color=colors[i], capsize=5, linewidth=2, markersize=6, alpha=0.9
    )

# Title and labels
ax.set_title('Exploration of Renewable Energy Adoption:\n'
             'Analyzing Efficiency and Variability Across Regions (2018-2022)', 
             fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Efficiency (%)', fontsize=12)

# Legend and grid
ax.legend(title='Regions', loc='upper left')
ax.grid(True, linestyle='--', alpha=0.6)

# Ensure the layout is adjusted so nothing overlaps
plt.tight_layout()

# Display the plot
plt.show()