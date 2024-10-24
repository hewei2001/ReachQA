import matplotlib.pyplot as plt
import numpy as np

# Define years for the x-axis
years = np.arange(2020, 2031)

# Artificial data for average ocean temperatures (in Celsius)
# Assume a gradual increase in temperature over the decade
average_temperatures = [16.2, 16.3, 16.5, 16.6, 16.8, 17.0, 17.2, 17.3, 17.5, 17.7, 17.8]

# Simulated errors (standard deviation) in measurement
measurement_errors = [0.15, 0.13, 0.14, 0.12, 0.16, 0.14, 0.13, 0.15, 0.12, 0.14, 0.13]

# Create the line chart with error bars
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the data
ax.errorbar(years, average_temperatures, yerr=measurement_errors, fmt='o-', 
            color='b', ecolor='r', elinewidth=2, capsize=4, alpha=0.8, label='Avg Temperature ± Error')

# Add titles and labels
ax.set_title("Monitoring Ocean Temperature Changes\nand Measurement Accuracy (2020-2030)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Temperature (°C)", fontsize=14)

# Add a legend
ax.legend(loc='upper left', fontsize=12)

# Enhance the grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Add annotation for the first and last data point
ax.annotate(f'{average_temperatures[0]:.1f}°C', xy=(2020, average_temperatures[0]), 
            xytext=(2019.3, average_temperatures[0] - 0.3),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, fontweight='bold', color='darkgreen')

ax.annotate(f'{average_temperatures[-1]:.1f}°C', xy=(2030, average_temperatures[-1]), 
            xytext=(2030.7, average_temperatures[-1] + 0.2),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, fontweight='bold', color='darkred')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()