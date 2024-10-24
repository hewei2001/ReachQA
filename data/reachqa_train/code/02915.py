import matplotlib.pyplot as plt
import numpy as np

# Define the years and average global salinity levels (in PSU - Practical Salinity Units)
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
average_salinity = np.array([34.5, 34.7, 34.6, 34.8, 34.9, 35.0, 34.8, 34.7, 35.1, 35.2, 35.0])
variability = np.array([0.2, 0.15, 0.25, 0.2, 0.18, 0.1, 0.2, 0.22, 0.15, 0.13, 0.2])

# Create the line chart with error bars
plt.figure(figsize=(12, 6))
plt.errorbar(years, average_salinity, yerr=variability, fmt='-o', color='navy', ecolor='lightblue',
             elinewidth=2, capsize=5, alpha=0.8, label='Average Salinity Level (PSU)')

# Customize the appearance of the plot
plt.xlabel('Year', fontsize=14)
plt.ylabel('Salinity (PSU)', fontsize=14)
plt.title('Temporal Trends and Variability in\nGlobal Ocean Salinity Levels (2010-2020)', 
          fontsize=16, fontweight='bold', pad=15)
plt.xticks(years, rotation=45)

# Add a grid to improve readability
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)

# Add a legend to clarify the chart elements
plt.legend(loc='upper right', fontsize=12)

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()