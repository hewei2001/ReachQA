import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Renewable energy adoption data (in percentage) for four countries
germany_adoption = np.array([15, 18, 21, 24, 28, 31, 34, 38, 42, 45, 48])
usa_adoption = np.array([9, 10, 12, 13, 15, 17, 20, 22, 25, 27, 30])
india_adoption = np.array([5, 6, 7, 9, 11, 14, 17, 19, 23, 27, 30])
brazil_adoption = np.array([40, 42, 43, 45, 47, 50, 52, 55, 58, 60, 63])

# Error margins for each country
germany_error = np.array([2, 2, 3, 3, 4, 3, 4, 3, 3, 2, 2])
usa_error = np.array([1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1])
india_error = np.array([1, 1, 1, 2, 2, 2, 3, 2, 3, 2, 2])
brazil_error = np.array([3, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2])

# Set up the plot
plt.figure(figsize=(14, 8))

# Plot each country's adoption trend with error bars
plt.errorbar(years, germany_adoption, yerr=germany_error, fmt='-o', label='Germany', color='#1f77b4', capsize=5, alpha=0.9)
plt.errorbar(years, usa_adoption, yerr=usa_error, fmt='-s', label='USA', color='#ff7f0e', capsize=5, alpha=0.9)
plt.errorbar(years, india_adoption, yerr=india_error, fmt='-^', label='India', color='#2ca02c', capsize=5, alpha=0.9)
plt.errorbar(years, brazil_adoption, yerr=brazil_error, fmt='-d', label='Brazil', color='#d62728', capsize=5, alpha=0.9)

# Customize the plot
plt.title('Renewable Energy Adoption Trends (2010-2020)\nA Decade of Growth and Variability', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Renewable Energy Adoption (%)', fontsize=14)

# Add grid lines and set ticks
plt.grid(linestyle='--', alpha=0.6)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 71, 10))

# Add legend with a title
plt.legend(loc='upper left', fontsize=10, title="Countries")

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()