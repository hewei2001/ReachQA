import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Average ocean surface temperatures in °C for each ocean
atlantic_temp = np.array([15.1, 15.3, 15.5, 15.6, 15.7, 15.9, 16.0, 16.1, 16.3, 16.4, 16.5])
pacific_temp = np.array([16.1, 16.2, 16.4, 16.5, 16.7, 16.8, 17.0, 17.1, 17.3, 17.4, 17.6])
indian_temp = np.array([24.1, 24.2, 24.3, 24.5, 24.6, 24.8, 24.9, 25.0, 25.2, 25.3, 25.5])
arctic_temp = np.array([2.0, 2.2, 2.3, 2.5, 2.6, 2.8, 3.0, 3.1, 3.3, 3.4, 3.5])

# Estimated standard deviations (variability) for error bars
atlantic_err = np.array([0.2] * len(years))
pacific_err = np.array([0.3] * len(years))
indian_err = np.array([0.15] * len(years))
arctic_err = np.array([0.25] * len(years))

# Calculate average temperature increase over the decade for each ocean
atlantic_inc = atlantic_temp[-1] - atlantic_temp[0]
pacific_inc = pacific_temp[-1] - pacific_temp[0]
indian_inc = indian_temp[-1] - indian_temp[0]
arctic_inc = arctic_temp[-1] - arctic_temp[0]

increases = [atlantic_inc, pacific_inc, indian_inc, arctic_inc]
oceans = ['Atlantic Ocean', 'Pacific Ocean', 'Indian Ocean', 'Arctic Ocean']

# Set up the 1x2 subplot layout
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# First plot: line plot with error bars
ax1 = axes[0]
ax1.errorbar(years, atlantic_temp, yerr=atlantic_err, label='Atlantic Ocean', fmt='-o', color='navy', capsize=4)
ax1.errorbar(years, pacific_temp, yerr=pacific_err, label='Pacific Ocean', fmt='-s', color='teal', capsize=4)
ax1.errorbar(years, indian_temp, yerr=indian_err, label='Indian Ocean', fmt='-^', color='maroon', capsize=4)
ax1.errorbar(years, arctic_temp, yerr=arctic_err, label='Arctic Ocean', fmt='-d', color='purple', capsize=4)

ax1.set_title('Climate Change Impact on Ocean Surface Temperatures\n(2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Average Surface Temperature (°C)', fontsize=12, fontweight='bold')
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(loc='upper left', fontsize=10)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, ha='right', fontsize=10)

# Second plot: bar chart showing temperature increase
ax2 = axes[1]
bars = ax2.bar(oceans, increases, color=['navy', 'teal', 'maroon', 'purple'])
ax2.set_title('Average Temperature Increase (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax2.set_ylabel('Temperature Increase (°C)', fontsize=12, fontweight='bold')

# Add data labels to each bar
for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 0.1, round(yval, 2), ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()