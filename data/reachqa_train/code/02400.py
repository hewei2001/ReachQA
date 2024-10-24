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

# Initialize the plot
plt.figure(figsize=(12, 7))

# Plot the data with error bars
plt.errorbar(years, athens_temps, yerr=athens_errors, fmt='o-', label='Athens (Greece)', capsize=4, color='blue', ecolor='lightblue', alpha=0.8)
plt.errorbar(years, cairo_temps, yerr=cairo_errors, fmt='s-', label='Cairo (Egypt)', capsize=4, color='orange', ecolor='lightcoral', alpha=0.8)
plt.errorbar(years, beijing_temps, yerr=beijing_errors, fmt='^-', label='Beijing (China)', capsize=4, color='green', ecolor='lightgreen', alpha=0.8)

# Chart title and axis labels
plt.title('Decadal Temperature Records\nfrom 19th Century Global Observatories (1840-1849)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Temperature (°C)', fontsize=12)

# Add legend
plt.legend(loc='upper left', fontsize=10, title='Observatories')

# Customize the plot grid
plt.grid(True, linestyle='--', alpha=0.5)

# Adjust layout for clarity
plt.tight_layout()

# Display the plot
plt.show()