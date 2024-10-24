import matplotlib.pyplot as plt
import numpy as np

# Define the years of interest
years = np.array([1977, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020])

# Cumulative data return in gigabytes (hypothetical values)
data_return = np.array([0.1, 0.5, 1.5, 3.0, 4.0, 4.5, 5.0, 5.5, 5.75, 6.0])

# Error values representing uncertainties in transmission (hypothetical)
data_errors = np.array([0.05, 0.1, 0.2, 0.25, 0.2, 0.15, 0.1, 0.1, 0.05, 0.05])

# Create the plot
plt.figure(figsize=(12, 7))

# Plot the data with error bars
plt.errorbar(years, data_return, yerr=data_errors, fmt='-o', ecolor='tomato', capsize=5, 
             capthick=2, elinewidth=2, markerfacecolor='dodgerblue', markersize=7, 
             label='Cumulative Data Return (GB)')

# Customize plot appearance
plt.title("Exploration Trends of the Outer Solar System:\nVoyager Missions", fontsize=16, weight='bold', pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Cumulative Data Return (GB)", fontsize=14)
plt.xticks(years, rotation=45, fontsize=12)
plt.yticks(np.arange(0, 7, 1), fontsize=12)
plt.ylim(0, 6.5)
plt.grid(linestyle='--', alpha=0.6)

# Add a legend
plt.legend(loc='upper left', fontsize=12, frameon=False)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()