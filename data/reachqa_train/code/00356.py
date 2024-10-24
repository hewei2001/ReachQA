import matplotlib.pyplot as plt
import numpy as np

# Simulated average annual temperature data (in °C) over a decade
years = np.arange(2010, 2020)
average_temperatures = np.array([-10.5, -11.0, -9.8, -10.2, -11.3, -9.7, -10.5, -9.9, -10.1, -9.6])
temperature_std_dev = np.array([0.8, 1.1, 0.6, 0.9, 1.0, 0.7, 0.8, 1.2, 0.7, 0.9])

# Simulated average annual snowfall (in cm) over the same decade
average_snowfall = np.array([150, 160, 140, 155, 165, 135, 145, 150, 152, 148])
snowfall_std_dev = np.array([10, 15, 12, 8, 20, 18, 11, 14, 9, 13])

# Set up the subplots
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

# Plot 1: Average Annual Temperature with error bars
ax[0].errorbar(years, average_temperatures, yerr=temperature_std_dev, fmt='-o',
               color='royalblue', ecolor='lightcoral', elinewidth=2, capsize=4, 
               markerfacecolor='white', markeredgecolor='royalblue', markersize=7,
               label='Avg Temperature ± Std Dev')
ax[0].set_title('Temperature Variability\nin the Arctic Region', fontsize=14, fontweight='bold')
ax[0].set_xlabel('Year', fontsize=12)
ax[0].set_ylabel('Avg Annual Temperature (°C)', fontsize=12)
ax[0].set_ylim(min(average_temperatures - temperature_std_dev) - 1, 
               max(average_temperatures + temperature_std_dev) + 1)
ax[0].legend(loc='upper right', fontsize=10)
ax[0].grid(True, linestyle='--', alpha=0.6)

# Plot 2: Average Annual Snowfall with error bars
ax[1].bar(years, average_snowfall, yerr=snowfall_std_dev, color='cadetblue', 
          alpha=0.7, ecolor='saddlebrown', capsize=4, label='Avg Snowfall ± Std Dev')
ax[1].set_title('Snowfall Trends in the Arctic Region', fontsize=14, fontweight='bold')
ax[1].set_xlabel('Year', fontsize=12)
ax[1].set_ylabel('Avg Annual Snowfall (cm)', fontsize=12)
ax[1].set_ylim(0, max(average_snowfall + snowfall_std_dev) + 20)
ax[1].legend(loc='upper right', fontsize=10)
ax[1].grid(True, linestyle='--', alpha=0.6)

# Overall title for the entire figure
plt.suptitle('Climate Trends: Analyzing Arctic Temperature and Snowfall Over a Decade', fontsize=16, fontweight='bold', y=1.02)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()