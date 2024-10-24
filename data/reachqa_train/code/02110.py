import numpy as np
import matplotlib.pyplot as plt

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Define population data for each species
blue_ridge_lynx = np.array([15, 18, 22, 27, 32, 40, 50, 65, 80, 95, 110])
golden_eagle = np.array([25, 28, 26, 30, 27, 29, 31, 28, 30, 32, 33])
river_dolphin = np.array([50, 48, 45, 42, 38, 35, 32, 30, 27, 24, 21])

# Define related but different data for the overlay plot: Habitat areas
lynx_habitat = np.array([30, 32, 35, 40, 50, 60, 75, 90, 100, 110, 120])
eagle_habitat = np.array([55, 52, 54, 53, 55, 58, 60, 63, 65, 67, 68])
dolphin_habitat = np.array([70, 68, 65, 60, 55, 50, 48, 45, 42, 40, 38])

# Create the figure and primary axis
fig, ax1 = plt.subplots(figsize=(14, 9))

# Plot the population data
ax1.plot(years, blue_ridge_lynx, label='Blue Ridge Lynx', color='dodgerblue', marker='o', linewidth=2, linestyle='-')
ax1.plot(years, golden_eagle, label='Golden Eagle', color='gold', marker='s', linewidth=2, linestyle='--')
ax1.plot(years, river_dolphin, label='River Dolphin', color='salmon', marker='^', linewidth=2, linestyle='-.')

# Enhance the plot with titles and labels
ax1.set_title('Decade of Change:\nWildlife Populations and Habitats in Green Haven Sanctuary (2010-2020)', fontsize=16, fontweight='bold', loc='center', pad=30)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Population Count', fontsize=12)

# Add secondary y-axis for habitat data
ax2 = ax1.twinx()
ax2.bar(years - 0.2, lynx_habitat, width=0.2, color='lightblue', alpha=0.6, label='Lynx Habitat Area')
ax2.bar(years, eagle_habitat, width=0.2, color='khaki', alpha=0.6, label='Eagle Habitat Area')
ax2.bar(years + 0.2, dolphin_habitat, width=0.2, color='lightcoral', alpha=0.6, label='Dolphin Habitat Area')
ax2.set_ylabel('Habitat Area (in sq km)', fontsize=12)

# Position the legends to avoid overlap
ax1.legend(loc='upper left', fontsize=10, frameon=True)
ax2.legend(loc='upper right', fontsize=10, frameon=True)

# Add grid lines and annotations
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, ha='right')
ax1.annotate('Lynx Breeding Success', xy=(2018, 80), xytext=(2016, 90),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, backgroundcolor='white')
ax1.annotate('Eagle Population Stabilizes', xy=(2015, 29), xytext=(2012, 35),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, backgroundcolor='white')
ax1.annotate('Dolphin Habitat Loss', xy=(2020, 21), xytext=(2017, 25),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, backgroundcolor='white')

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()