import matplotlib.pyplot as plt
import numpy as np

# Original Data: Years and projected growth in gigawatts for each region
years = np.array([2020, 2021, 2022, 2023, 2024])
solaria_growth = np.array([20, 30, 45, 60, 80])
windholm_growth = np.array([10, 25, 40, 50, 65])
hydrovia_growth = np.array([15, 20, 30, 35, 55])
geoearth_growth = np.array([5, 15, 25, 30, 50])

# Error margins for each region
solaria_error = np.array([3, 4, 5, 6, 7])
windholm_error = np.array([2, 3, 4, 5, 6])
hydrovia_error = np.array([3, 2, 4, 4, 5])
geoearth_error = np.array([1, 2, 3, 4, 5])

# Cumulative data for overlay plot
cumulative_growth = np.cumsum(solaria_growth + windholm_growth + hydrovia_growth + geoearth_growth)

# Set up the plot
fig, ax1 = plt.subplots(figsize=(14, 9))

# Plot each region's growth with error bars
ax1.errorbar(years, solaria_growth, yerr=solaria_error, fmt='-o', label='Solaria', capsize=5, color='tab:orange', alpha=0.8)
ax1.errorbar(years, windholm_growth, yerr=windholm_error, fmt='-s', label='Windholm', capsize=5, color='tab:green', alpha=0.8)
ax1.errorbar(years, hydrovia_growth, yerr=hydrovia_error, fmt='-^', label='Hydrovia', capsize=5, color='tab:blue', alpha=0.8)
ax1.errorbar(years, geoearth_growth, yerr=geoearth_error, fmt='-d', label='Geoearth', capsize=5, color='tab:red', alpha=0.8)

# Titles and labels for the primary y-axis
ax1.set_title('Projected Renewable Energy Production Growth\nwith Error Margins and Cumulative Overlay (2020-2024)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Additional GW of Renewable Energy Capacity', fontsize=12)
ax1.legend(title='Region', fontsize=10, loc='upper left', frameon=False)
ax1.grid(True, linestyle='--', alpha=0.6)

# Secondary y-axis for cumulative growth
ax2 = ax1.twinx()
ax2.fill_between(years, cumulative_growth, color='lightgrey', alpha=0.5, label='Cumulative Growth')
ax2.plot(years, cumulative_growth, color='grey', linestyle='--', linewidth=2)
ax2.set_ylabel('Cumulative GW', fontsize=12)
ax2.legend(loc='upper right', fontsize=10, frameon=False)

# Adjust layout to prevent overlap
fig.tight_layout()

# Display the plot
plt.show()