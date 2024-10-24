import matplotlib.pyplot as plt
import numpy as np

# Define years of the study
years = np.arange(2010, 2022)

# Constructing average temperature data for three cities (in °C)
atlantis_temp = [15.0, 15.2, 15.4, 15.6, 15.5, 15.7, 15.8, 16.0, 16.1, 16.3, 16.4, 16.5]
eloria_temp = [20.0, 20.1, 20.3, 20.4, 20.3, 20.5, 20.7, 20.8, 21.0, 21.1, 21.2, 21.3]
zephyros_temp = [10.0, 10.1, 10.3, 10.2, 10.4, 10.6, 10.7, 10.9, 11.0, 11.2, 11.3, 11.4]

# Define the standard deviation for each city to represent the error bars
atlantis_err = [0.3] * len(years)
eloria_err = [0.4] * len(years)
zephyros_err = [0.2] * len(years)

# Plotting the line chart with error bars
plt.figure(figsize=(12, 7))

# Plot each city's temperature data with error bars
plt.errorbar(years, atlantis_temp, yerr=atlantis_err, label='Atlantis', fmt='o-', color='#1f77b4', capsize=4, alpha=0.8, linewidth=2)
plt.errorbar(years, eloria_temp, yerr=eloria_err, label='Eloria', fmt='s-', color='#ff7f0e', capsize=4, alpha=0.8, linewidth=2)
plt.errorbar(years, zephyros_temp, yerr=zephyros_err, label='Zephyros', fmt='^-', color='#2ca02c', capsize=4, alpha=0.8, linewidth=2)

# Add titles and labels
plt.title('Climate Trends in Fictional Cities:\nA 12-Year Analysis', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Temperature (°C)', fontsize=12)

# Customize ticks
plt.xticks(years, rotation=45)
plt.yticks(np.arange(10, 22, 2))

# Add grid and legend
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Cities', fontsize=10, loc='upper left')

# Set axes limits to ensure error bars are within the plot area
plt.xlim(2009.5, 2021.5)
plt.ylim(9, 22)

# Ensure layout is optimized for visibility
plt.tight_layout()

# Display the chart
plt.show()