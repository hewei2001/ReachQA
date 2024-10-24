import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2021)

# Original adoption rates for each continent
europe_adoption = np.array([12, 14, 17, 20, 24, 28, 33, 39, 45, 51, 56])
asia_adoption = np.array([5, 7, 9, 12, 16, 20, 23, 27, 31, 34, 38])
africa_adoption = np.array([3, 5, 7, 9, 11, 15, 18, 21, 24, 28, 30])

# Error margins for each continent
europe_errors = [1.5, 1.2, 1.0, 1.3, 1.1, 1.4, 1.6, 1.5, 1.3, 1.2, 1.1]
asia_errors = [1.0, 1.3, 1.2, 1.1, 1.5, 1.7, 1.6, 1.4, 1.3, 1.5, 1.2]
africa_errors = [0.8, 0.9, 1.0, 1.1, 1.2, 1.5, 1.3, 1.4, 1.5, 1.6, 1.2]

# Calculate annual growth rates as percentage change from previous year
def growth_rate(data):
    return np.round(100 * np.diff(data) / data[:-1], 1)

europe_growth = growth_rate(europe_adoption)
asia_growth = growth_rate(asia_adoption)
africa_growth = growth_rate(africa_adoption)

# Plot the data
fig, ax1 = plt.subplots(figsize=(14, 9))

# Line plot with error bars
ax1.errorbar(years, europe_adoption, yerr=europe_errors, fmt='o-', 
             label='Europe', color='blue', capsize=5, linewidth=2, alpha=0.8)
ax1.errorbar(years, asia_adoption, yerr=asia_errors, fmt='s-', 
             label='Asia', color='green', capsize=5, linewidth=2, alpha=0.8)
ax1.errorbar(years, africa_adoption, yerr=africa_errors, fmt='^-', 
             label='Africa', color='orange', capsize=5, linewidth=2, alpha=0.8)

# Secondary y-axis for growth rate bar plot
ax2 = ax1.twinx()
bar_width = 0.2
ax2.bar(years[:-1] - bar_width, europe_growth, width=bar_width, label='Europe Growth', color='skyblue', alpha=0.6)
ax2.bar(years[:-1], asia_growth, width=bar_width, label='Asia Growth', color='lightgreen', alpha=0.6)
ax2.bar(years[:-1] + bar_width, africa_growth, width=bar_width, label='Africa Growth', color='peachpuff', alpha=0.6)

# Titles and labels
ax1.set_title("Renewable Energy Adoption Rates and Growth\nAcross Continents: 2010-2020", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Adoption Rate (%)", fontsize=14)
ax2.set_ylabel("Annual Growth Rate (%)", fontsize=14)

# Legends
ax1.legend(loc='upper left', fontsize=12)
ax2.legend(loc='upper right', fontsize=12)

# Grid and limits
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_xlim(2009, 2021)
ax1.set_ylim(0, 60)
ax2.set_ylim(0, np.max([europe_growth, asia_growth, africa_growth]) + 5)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()