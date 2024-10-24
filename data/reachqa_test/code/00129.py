import matplotlib.pyplot as plt
import numpy as np

# City names
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

# PM2.5 levels (µg/m³) for each city over a year (24 time points)
pm25_levels = [
    [12, 14, 15, 20, 18, 22, 30, 32, 28, 18, 16, 19, 23, 25, 22, 15, 14, 10, 9, 12, 16, 14, 15, 20],  # New York
    [22, 18, 19, 25, 30, 28, 25, 27, 29, 30, 32, 30, 28, 25, 22, 21, 19, 17, 16, 14, 16, 20, 25, 28],  # Los Angeles
    [18, 15, 16, 20, 25, 24, 22, 26, 28, 27, 23, 20, 19, 18, 16, 15, 13, 12, 11, 14, 19, 20, 18, 17],  # Chicago
    [25, 28, 30, 32, 35, 30, 28, 26, 29, 27, 28, 29, 25, 22, 20, 18, 19, 21, 22, 24, 28, 30, 31, 35],  # Houston
    [16, 18, 19, 21, 23, 25, 24, 22, 20, 18, 17, 19, 20, 22, 21, 19, 17, 15, 14, 13, 16, 18, 19, 20]   # Phoenix
]

# Monthly average temperatures for each city (24 time points)
avg_temperatures = [
    [30, 32, 35, 42, 50, 60, 70, 75, 65, 55, 45, 35, 32, 33, 36, 43, 51, 62, 72, 78, 67, 56, 46, 37],  # New York
    [58, 60, 62, 66, 70, 75, 80, 85, 83, 77, 65, 60, 59, 62, 65, 67, 72, 77, 82, 86, 84, 80, 70, 62],  # Los Angeles
    [25, 28, 32, 40, 50, 60, 70, 75, 68, 55, 45, 30, 28, 30, 34, 42, 51, 61, 71, 76, 69, 56, 46, 32],  # Chicago
    [55, 60, 65, 72, 78, 85, 92, 95, 89, 78, 65, 60, 58, 63, 68, 74, 80, 87, 94, 97, 91, 80, 66, 60],  # Houston
    [50, 55, 60, 68, 75, 82, 90, 96, 90, 77, 65, 55, 52, 56, 61, 69, 76, 84, 92, 97, 90, 78, 66, 56]   # Phoenix
]

# Create subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 7))

# Box plot for PM2.5 levels
box = axes[0].boxplot(pm25_levels, labels=cities, patch_artist=True, notch=True,
                      boxprops=dict(facecolor='lightblue', color='blue', linewidth=1.5),
                      whiskerprops=dict(color='darkblue', linewidth=1.5),
                      capprops=dict(color='darkblue', linewidth=1.5),
                      medianprops=dict(color='darkred', linewidth=2),
                      flierprops=dict(marker='o', color='red', alpha=0.5))

# Color customization for each box
colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightcoral', 'lightgrey']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Titles and labels for box plot
axes[0].set_title("PM2.5 Concentration Levels Across Cities\nVisualizing Urban Air Quality", fontsize=12, fontweight='bold')
axes[0].set_xlabel("Cities", fontsize=10)
axes[0].set_ylabel("PM2.5 (µg/m³)", fontsize=10)
axes[0].grid(axis='y', linestyle='--', alpha=0.6)

# Line plot for average temperatures
for i, city in enumerate(cities):
    axes[1].plot(range(1, 25), avg_temperatures[i], label=city, linewidth=1.5)

# Titles and labels for line plot
axes[1].set_title("Monthly Average Temperatures\nClimate Patterns in Major Cities", fontsize=12, fontweight='bold')
axes[1].set_xlabel("Month", fontsize=10)
axes[1].set_ylabel("Temperature (°F)", fontsize=10)
axes[1].legend(loc='upper left')
axes[1].grid(linestyle='--', alpha=0.6)

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()