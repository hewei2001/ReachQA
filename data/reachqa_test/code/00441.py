import matplotlib.pyplot as plt
import numpy as np

# Adjusted data for plotting
years = np.arange(2000, 2026)
average_temperatures = np.array([
    14.5, 14.7, 14.8, 14.9, 15.0, 15.1, 15.2, 15.3, 15.4, 15.6, 
    15.0, 15.2, 15.3, 15.1, 15.5, 15.6, 15.8, 16.0, 16.1, 16.3, 
    16.5, 16.7, 16.8, 16.9, 17.0, 17.1
])
high_temperatures = average_temperatures + np.array([
    1.8, 2.0, 1.9, 2.0, 2.0, 2.1, 2.0, 2.1, 2.1, 2.2, 
    2.3, 2.4, 2.3, 2.5, 2.4, 2.5, 2.6, 2.8, 2.9, 3.1, 
    3.0, 3.2, 3.3, 3.4, 3.5, 3.6
])
low_temperatures = average_temperatures - np.array([
    1.3, 1.2, 1.1, 1.3, 1.1, 1.2, 1.0, 1.3, 1.2, 1.1, 
    1.1, 1.0, 0.9, 1.1, 0.8, 0.9, 1.0, 1.2, 0.9, 0.8, 
    0.7, 0.6, 0.5, 0.4, 0.3, 0.4
])
temperature_variability = np.array([
    0.22, 0.18, 0.28, 0.22, 0.20, 0.25, 0.21, 0.28, 0.24, 0.22, 
    0.25, 0.28, 0.24, 0.27, 0.30, 0.32, 0.35, 0.37, 0.40, 0.42, 
    0.44, 0.46, 0.48, 0.50, 0.52, 0.54
])

# Setup for multiple plots
fig, ax = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# First subplot for temperature trends with variability
ax[0].errorbar(
    years, average_temperatures, yerr=temperature_variability, fmt='-o',
    color='teal', ecolor='coral', elinewidth=1.5, capsize=3, label='Avg Temperature',
    alpha=0.8, markerfacecolor='white', markeredgewidth=1, markersize=6
)
ax[0].set_title("Temperature Trends and Variability\nin Greenvale (2000-2025)", fontsize=14, fontweight='bold', pad=15)
ax[0].set_ylabel("Temperature (°C)", fontsize=12)
ax[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax[0].legend(loc='upper left', fontsize=10, frameon=False)
ax[0].annotate('Notable Increase in 2018', xy=(2018, 16.0), xytext=(2015, 17.0),
               arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, color='black')

# Second subplot for high and low temperatures
ax[1].plot(years, high_temperatures, 'r--', label='High Temperature', alpha=0.7)
ax[1].plot(years, low_temperatures, 'b--', label='Low Temperature', alpha=0.7)
ax[1].fill_between(years, high_temperatures, low_temperatures, color='gray', alpha=0.2, label='Temperature Range')
ax[1].set_title("High and Low Temperature Trends", fontsize=12, pad=10)
ax[1].set_xlabel("Year", fontsize=12)
ax[1].set_ylabel("Temperature (°C)", fontsize=12)
ax[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax[1].legend(loc='upper left', fontsize=10, frameon=False)

# Adjust layout and display
plt.tight_layout()
plt.show()
