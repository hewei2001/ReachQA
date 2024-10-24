import numpy as np
import matplotlib.pyplot as plt

# Define the years and regions
years = np.arange(2010, 2020)
regions = ['Antarctic Coast', 'Arctic Ocean']

# Average temperature data (in degrees Celsius)
antarctic_temps = np.array([-1.8, -2.0, -1.6, -1.5, -2.2, -2.1, -1.9, -2.0, -1.8, -1.7])
arctic_temps = np.array([-1.2, -1.0, -0.8, -0.9, -1.4, -1.5, -1.1, -1.3, -1.0, -0.9])

# Error margins (representing measurement variability)
antarctic_errors = np.array([0.2, 0.3, 0.1, 0.2, 0.4, 0.3, 0.2, 0.3, 0.2, 0.1])
arctic_errors = np.array([0.3, 0.2, 0.3, 0.2, 0.4, 0.3, 0.4, 0.3, 0.2, 0.1])

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the temperature data with error bars
ax.errorbar(years, antarctic_temps, yerr=antarctic_errors, fmt='-o', 
            label='Antarctic Coast', color='royalblue', capsize=5, alpha=0.8)
ax.errorbar(years, arctic_temps, yerr=arctic_errors, fmt='-s', 
            label='Arctic Ocean', color='forestgreen', capsize=5, alpha=0.8)

# Customize the chart
ax.set_title("Climate Science Expedition:\nYearly Temperature Fluctuations in Polar Regions", 
             fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel("Year", fontsize=12, labelpad=10)
ax.set_ylabel("Average Temperature (°C)", fontsize=12, labelpad=10)
ax.set_xticks(years)
ax.set_ylim(-2.5, -0.5)

# Add legend
ax.legend(loc='upper left', fontsize=10, title="Research Areas")

# Add a grid for easier comparison
ax.grid(True, linestyle='--', alpha=0.7)

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()