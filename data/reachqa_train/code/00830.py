import matplotlib.pyplot as plt
import numpy as np

# Define the years for the plot
years = np.array([2015, 2016, 2017, 2018, 2019, 2020])

# Data: Number of breweries in each region (fictional data)
northland = np.array([120, 135, 150, 165, 180, 195])
eastwood = np.array([80, 90, 105, 120, 130, 140])
westlake = np.array([60, 75, 85, 95, 110, 125])
south_valley = np.array([50, 60, 70, 85, 100, 110])

# Error margins representing uncertainty or variance in the data
northland_error = np.array([5, 6, 4, 5, 7, 6])
eastwood_error = np.array([4, 5, 3, 4, 6, 5])
westlake_error = np.array([3, 4, 5, 4, 6, 4])
south_valley_error = np.array([2, 3, 3, 5, 4, 5])

# Plotting the line chart with error bars
plt.figure(figsize=(12, 8))
plt.errorbar(years, northland, yerr=northland_error, label='Northland', fmt='-o', capsize=5, color='tab:blue', alpha=0.8)
plt.errorbar(years, eastwood, yerr=eastwood_error, label='Eastwood', fmt='-^', capsize=5, color='tab:orange', alpha=0.8)
plt.errorbar(years, westlake, yerr=westlake_error, label='Westlake', fmt='-s', capsize=5, color='tab:green', alpha=0.8)
plt.errorbar(years, south_valley, yerr=south_valley_error, label='South Valley', fmt='-d', capsize=5, color='tab:red', alpha=0.8)

# Customizing the plot
plt.title('Growth of Breweries in the Craft Beer Industry\n(2015-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Breweries', fontsize=14)
plt.xticks(years)
plt.yticks(np.arange(40, 210, 20))
plt.legend(title='Regions', loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)

# Annotations for significant growth
plt.annotate('Rapid Growth\nin Westlake', xy=(2019, 110), xytext=(2017.5, 130),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='center')
plt.annotate('Consistent Rise\nin Northland', xy=(2020, 195), xytext=(2018.5, 180),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='center')

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Show plot
plt.show()