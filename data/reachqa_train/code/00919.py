import matplotlib.pyplot as plt
import numpy as np

# Years for the X-axis
years = np.array([2020, 2021, 2022, 2023, 2024])

# Projected growth in gigawatts for each region
solaria_growth = np.array([20, 30, 45, 60, 80])
windholm_growth = np.array([10, 25, 40, 50, 65])
hydrovia_growth = np.array([15, 20, 30, 35, 55])
geoearth_growth = np.array([5, 15, 25, 30, 50])

# Error margins for each region, representing uncertainty in predictions
solaria_error = np.array([3, 4, 5, 6, 7])
windholm_error = np.array([2, 3, 4, 5, 6])
hydrovia_error = np.array([3, 2, 4, 4, 5])
geoearth_error = np.array([1, 2, 3, 4, 5])

# Set up the plot
plt.figure(figsize=(12, 8))

# Plot each region's growth with error bars
plt.errorbar(years, solaria_growth, yerr=solaria_error, fmt='-o', label='Solaria', capsize=5, color='tab:orange', alpha=0.8)
plt.errorbar(years, windholm_growth, yerr=windholm_error, fmt='-s', label='Windholm', capsize=5, color='tab:green', alpha=0.8)
plt.errorbar(years, hydrovia_growth, yerr=hydrovia_error, fmt='-^', label='Hydrovia', capsize=5, color='tab:blue', alpha=0.8)
plt.errorbar(years, geoearth_growth, yerr=geoearth_error, fmt='-d', label='Geoearth', capsize=5, color='tab:red', alpha=0.8)

# Titles and labels
plt.title('Projected Renewable Energy Production Growth\nwith Error Margins (2020-2024)', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Additional GW of Renewable Energy Capacity', fontsize=12)

# Add legend and customize
plt.legend(title='Region', fontsize=10, loc='upper left', frameon=False)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()