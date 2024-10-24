import matplotlib.pyplot as plt
import numpy as np

# Define years of study
years = np.arange(2010, 2021)

# Migration distances (in km) for each whale species
blue_whale_distances = np.array([4200, 4400, 4550, 4700, 4650, 4800, 4900, 4850, 4950, 5100, 5000])
humpback_whale_distances = np.array([3700, 3850, 3950, 4000, 4100, 4200, 4300, 4350, 4400, 4450, 4600])
orca_distances = np.array([2200, 2300, 2350, 2450, 2500, 2600, 2550, 2700, 2750, 2800, 2900])

# Estimated errors (in km) for each species
blue_whale_errors = np.array([150, 120, 100, 130, 110, 140, 120, 115, 105, 135, 125])
humpback_whale_errors = np.array([100, 90, 85, 95, 100, 90, 95, 80, 75, 85, 95])
orca_errors = np.array([70, 65, 60, 55, 70, 75, 80, 65, 60, 70, 75])

# Plotting
plt.figure(figsize=(12, 8))

# Plot Blue Whale migrations
plt.errorbar(years, blue_whale_distances, yerr=blue_whale_errors, fmt='-o', linestyle='-', 
             linewidth=2, capsize=5, label='Blue Whale', color='dodgerblue', alpha=0.7)

# Plot Humpback Whale migrations
plt.errorbar(years, humpback_whale_distances, yerr=humpback_whale_errors, fmt='-^', linestyle='-', 
             linewidth=2, capsize=5, label='Humpback Whale', color='seagreen', alpha=0.7)

# Plot Orca migrations
plt.errorbar(years, orca_distances, yerr=orca_errors, fmt='-s', linestyle='-', 
             linewidth=2, capsize=5, label='Orca', color='black', alpha=0.7)

# Add titles and labels
plt.title('Decadal Migration Patterns of Whale Species\n(2010-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Migration Distance (km)', fontsize=12)

# Customize x-ticks and y-ticks
plt.xticks(years, rotation=45)
plt.yticks(np.arange(2000, 5500, 500))

# Enable grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Add a legend
plt.legend(title='Whale Species', title_fontsize='13', fontsize=11, loc='upper left')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()