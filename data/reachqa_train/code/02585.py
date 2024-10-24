import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2021)

# Average coffee consumption per capita (kg/person/year) for each region
north_america = np.array([4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.3, 5.4, 5.5, 5.7])
europe = np.array([7.0, 7.1, 7.3, 7.5, 7.7, 7.8, 8.0, 8.2, 8.3, 8.5, 8.7])
asia = np.array([1.2, 1.3, 1.5, 1.6, 1.7, 1.9, 2.0, 2.1, 2.3, 2.5, 2.7])

# Error margins representing variability (hypothetical factors)
north_america_error = np.array([0.1, 0.1, 0.15, 0.2, 0.2, 0.25, 0.3, 0.3, 0.35, 0.4, 0.4])
europe_error = np.array([0.2, 0.2, 0.25, 0.3, 0.3, 0.35, 0.4, 0.4, 0.45, 0.5, 0.5])
asia_error = np.array([0.05, 0.1, 0.1, 0.15, 0.15, 0.2, 0.2, 0.25, 0.3, 0.35, 0.35])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot with error bars for each region
ax.errorbar(years, north_america, yerr=north_america_error, fmt='-o', color='#4C72B0', capsize=4, label='North America', alpha=0.8)
ax.errorbar(years, europe, yerr=europe_error, fmt='-s', color='#55A868', capsize=4, label='Europe', alpha=0.8)
ax.errorbar(years, asia, yerr=asia_error, fmt='-^', color='#C44E52', capsize=4, label='Asia', alpha=0.8)

# Customize the plot
ax.set_title("Sip Trends: Coffee Consumption Patterns\nAcross Regions (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12, labelpad=10)
ax.set_ylabel("Coffee Consumption (kg/person/year)", fontsize=12, labelpad=10)
ax.legend(loc='upper left', fontsize=11, title='Regions')
ax.grid(True, linestyle='--', alpha=0.7)

# Setting x and y limits to ensure all points are visible
ax.set_xlim(2009, 2021)
ax.set_ylim(0, 10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()