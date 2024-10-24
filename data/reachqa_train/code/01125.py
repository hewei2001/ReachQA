import numpy as np
import matplotlib.pyplot as plt

# Define the years and regions
years = np.arange(2010, 2020)

# Average temperature data (in degrees Celsius)
antarctic_temps = np.array([-1.8, -2.0, -1.6, -1.5, -2.2, -2.1, -1.9, -2.0, -1.8, -1.7])
arctic_temps = np.array([-1.2, -1.0, -0.8, -0.9, -1.4, -1.5, -1.1, -1.3, -1.0, -0.9])

# Error margins (representing measurement variability)
antarctic_errors = np.array([0.2, 0.3, 0.1, 0.2, 0.4, 0.3, 0.2, 0.3, 0.2, 0.1])
arctic_errors = np.array([0.3, 0.2, 0.3, 0.2, 0.4, 0.3, 0.4, 0.3, 0.2, 0.1])

# Simulated extreme temperature event data for overlay
antarctic_events = np.array([3, 4, 5, 4, 6, 5, 3, 5, 4, 2])
arctic_events = np.array([2, 3, 2, 4, 5, 4, 6, 5, 3, 3])

# Set up the plot
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the temperature data with error bars
ax1.errorbar(years, antarctic_temps, yerr=antarctic_errors, fmt='-o', 
             label='Antarctic Coast Temp', color='royalblue', capsize=5, alpha=0.8)
ax1.errorbar(years, arctic_temps, yerr=arctic_errors, fmt='-s', 
             label='Arctic Ocean Temp', color='forestgreen', capsize=5, alpha=0.8)

# Secondary axis for overlay data (number of extreme events)
ax2 = ax1.twinx()
ax2.bar(years - 0.15, antarctic_events, width=0.3, color='lightsteelblue', 
        label='Antarctic Events', alpha=0.6)
ax2.bar(years + 0.15, arctic_events, width=0.3, color='mediumseagreen', 
        label='Arctic Events', alpha=0.6)

# Customize the main temperature chart
ax1.set_title("Polar Regions Temperature and Extreme Events Overview (2010-2019)",
              fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel("Year", fontsize=12, labelpad=10)
ax1.set_ylabel("Avg Temperature (°C)", fontsize=12, labelpad=10)
ax1.set_xticks(years)
ax1.set_ylim(-2.5, -0.5)

# Customize the overlay axis
ax2.set_ylabel("Extreme Temperature Events", fontsize=12, labelpad=10)
ax2.set_ylim(0, 7)

# Add legends for both plots
ax1_legend = ax1.legend(loc='upper left', fontsize=10, title="Temperature")
ax2_legend = ax2.legend(loc='upper right', fontsize=10, title="Events")
ax1.add_artist(ax1_legend)

# Add grid and optimize layout
ax1.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Display the plot
plt.show()