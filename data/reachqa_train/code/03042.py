import matplotlib.pyplot as plt
import numpy as np

# Data: Energy production (in GWh) for solar and wind in three regions
regions = ['North', 'South', 'Central']
solar_energy = [
    [12, 15, 14, 17, 22, 19, 21, 18],  # North
    [25, 30, 28, 26, 32, 31, 29, 27],  # South
    [18, 20, 17, 21, 23, 22, 20, 19]   # Central
]
wind_energy = [
    [30, 32, 31, 29, 34, 33, 30, 32],  # North
    [40, 42, 39, 45, 43, 41, 44, 40],  # South
    [22, 24, 20, 26, 28, 23, 25, 24]   # Central
]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Create box plots
positions_solar = np.arange(len(regions)) * 2.0 - 0.35
positions_wind = np.arange(len(regions)) * 2.0 + 0.35

bp_solar = ax.boxplot(solar_energy, positions=positions_solar, widths=0.3,
                      patch_artist=True, notch=True,
                      boxprops=dict(facecolor="#FFD700", color="black"),
                      whiskerprops=dict(color="black"),
                      capprops=dict(color="black"),
                      medianprops=dict(color="red"))

bp_wind = ax.boxplot(wind_energy, positions=positions_wind, widths=0.3,
                     patch_artist=True, notch=True,
                     boxprops=dict(facecolor="#00BFFF", color="black"),
                     whiskerprops=dict(color="black"),
                     capprops=dict(color="black"),
                     medianprops=dict(color="blue"))

# Customize plot
ax.set_title('Distribution of Renewable Energy Production in 2023:\nA Regional Analysis of Solar and Wind Energy',
             fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Regions', fontsize=12)
ax.set_ylabel('Energy Production (GWh)', fontsize=12)
ax.set_xticks(np.arange(len(regions)) * 2.0)
ax.set_xticklabels(regions, fontsize=10)
ax.grid(True, linestyle='--', alpha=0.5)

# Add a legend
solar_patch = plt.Line2D([0], [0], color='w', marker='s', markersize=10, markerfacecolor="#FFD700")
wind_patch = plt.Line2D([0], [0], color='w', marker='s', markersize=10, markerfacecolor="#00BFFF")
ax.legend([solar_patch, wind_patch], ['Solar Energy', 'Wind Energy'], loc='upper left', fontsize=10, frameon=True)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()