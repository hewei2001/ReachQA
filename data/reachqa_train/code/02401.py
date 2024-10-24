import matplotlib.pyplot as plt
import numpy as np

# Years for the data
years = np.arange(1840, 1850)

# Average annual temperatures (in °C) and associated measurement uncertainties (error margins)
athens_temps = [16.1, 16.3, 16.2, 16.4, 16.5, 16.6, 16.4, 16.5, 16.7, 16.8]
athens_errors = [0.2, 0.3, 0.2, 0.3, 0.4, 0.3, 0.2, 0.3, 0.4, 0.3]

cairo_temps = [20.5, 20.7, 20.6, 20.8, 20.9, 21.0, 20.9, 21.1, 21.3, 21.2]
cairo_errors = [0.3, 0.2, 0.3, 0.4, 0.3, 0.4, 0.3, 0.4, 0.3, 0.2]

beijing_temps = [12.4, 12.5, 12.7, 12.6, 12.9, 13.0, 13.2, 13.3, 13.4, 13.5]
beijing_errors = [0.4, 0.3, 0.2, 0.3, 0.2, 0.4, 0.3, 0.3, 0.2, 0.3]

# Annual precipitation data for each city (mm)
athens_precip = [420, 430, 410, 415, 425, 440, 435, 445, 450, 455]
cairo_precip = [20, 18, 19, 21, 22, 20, 18, 17, 16, 15]
beijing_precip = [520, 530, 525, 540, 535, 545, 550, 560, 570, 575]

# Initialize the plot with dual axes
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot temperature data with error bars
ax1.errorbar(years, athens_temps, yerr=athens_errors, fmt='o-', label='Athens (Temp)', capsize=4, color='blue', ecolor='lightblue', alpha=0.8)
ax1.errorbar(years, cairo_temps, yerr=cairo_errors, fmt='s-', label='Cairo (Temp)', capsize=4, color='orange', ecolor='lightcoral', alpha=0.8)
ax1.errorbar(years, beijing_temps, yerr=beijing_errors, fmt='^-', label='Beijing (Temp)', capsize=4, color='green', ecolor='lightgreen', alpha=0.8)

# Title, labels, and grid
ax1.set_title('19th Century Temperature & Precipitation Data\nfrom Global Observatories (1840-1849)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=13)
ax1.set_ylabel('Average Temperature (°C)', fontsize=13)
ax1.grid(True, linestyle='--', alpha=0.5)

# Create a second y-axis for the precipitation data
ax2 = ax1.twinx()
ax2.bar(years - 0.2, athens_precip, width=0.2, label='Athens (Precip)', color='skyblue', alpha=0.6)
ax2.bar(years, cairo_precip, width=0.2, label='Cairo (Precip)', color='navajowhite', alpha=0.6)
ax2.bar(years + 0.2, beijing_precip, width=0.2, label='Beijing (Precip)', color='palegreen', alpha=0.6)
ax2.set_ylabel('Annual Precipitation (mm)', fontsize=13)

# Combine legends from both axes
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=11)

# Adjust layout
fig.tight_layout()

# Show the plot
plt.show()