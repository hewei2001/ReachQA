import matplotlib.pyplot as plt
import numpy as np

# Simulated average annual temperature data (in °C) over a decade
years = np.arange(2010, 2020)
average_temperatures = np.array([-10.5, -11.0, -9.8, -10.2, -11.3, -9.7, -10.5, -9.9, -10.1, -9.6])

# Simulated standard deviation values for each year representing variability
temperature_std_dev = np.array([0.8, 1.1, 0.6, 0.9, 1.0, 0.7, 0.8, 1.2, 0.7, 0.9])

# Set up the plot
plt.figure(figsize=(12, 7))

# Plot the line chart with error bars
plt.errorbar(years, average_temperatures, yerr=temperature_std_dev, fmt='-o',
             color='royalblue', ecolor='lightcoral', elinewidth=2, capsize=4, 
             markerfacecolor='white', markeredgecolor='royalblue', markersize=7,
             label='Avg Temperature ± Std Dev')

# Adding titles and labels
plt.title('Climate Trends: Analyzing Temperature Variability\nOver a Decade in the Arctic Region', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Annual Temperature (°C)', fontsize=14)

# Setting the limits for y-axis to ensure all error bars fit comfortably
plt.ylim(min(average_temperatures - temperature_std_dev) - 1, 
         max(average_temperatures + temperature_std_dev) + 1)

# Adding legend
plt.legend(loc='upper right', fontsize=12)

# Adding grid
plt.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()