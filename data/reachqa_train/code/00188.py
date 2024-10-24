import matplotlib.pyplot as plt
import numpy as np

# Data for the first plot: Average battery life over the years
years = np.arange(2010, 2021)
battery_life = np.array([6, 6.5, 7, 7.8, 8.5, 9.3, 9.8, 10.2, 10.5, 11, 11.5])
variability = np.array([0.5, 0.6, 0.7, 0.9, 1.0, 1.2, 1.3, 1.1, 1.2, 1.3, 1.4])

# Hypothetical data for the second plot: Battery capacity in mAh
battery_capacity = np.array([1200, 1300, 1400, 1550, 1700, 1800, 2000, 2100, 2200, 2300, 2500])

# Create a 1x2 subplot layout
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# First subplot: Line plot for battery life with error bars
axs[0].errorbar(years, battery_life, yerr=variability, fmt='-o', ecolor='gray', capsize=5,
                capthick=2, color='green', alpha=0.8, label='Battery Life Trends')
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].set_title("Evolution of Smartphone Battery Life\n(2010-2020)", fontsize=13, fontweight='bold', pad=10)
axs[0].set_xlabel("Year", fontsize=11)
axs[0].set_ylabel("Average Battery Life (hours)", fontsize=11)
axs[0].set_ylim(5, 13)
axs[0].set_xlim(2009, 2021)
axs[0].legend(loc='upper left', fontsize=9)

# Second subplot: Bar plot for battery capacity
axs[1].bar(years, battery_capacity, color='blue', alpha=0.7, label='Battery Capacity')
axs[1].set_title("Battery Capacity Enhancements\n(2010-2020)", fontsize=13, fontweight='bold', pad=10)
axs[1].set_xlabel("Year", fontsize=11)
axs[1].set_ylabel("Battery Capacity (mAh)", fontsize=11)
axs[1].set_ylim(1000, 2600)
axs[1].set_xlim(2009, 2021)
axs[1].legend(loc='upper left', fontsize=9)

# Enhancing layout
plt.tight_layout()

# Show the plot
plt.show()