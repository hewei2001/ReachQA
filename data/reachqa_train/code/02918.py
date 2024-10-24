import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])

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

# Plotting the data
fig, ax = plt.subplots(figsize=(14, 8))

# Plot lines with error bars for each ocean
ax.errorbar(years, atlantic_temp, yerr=atlantic_err, label='Atlantic Ocean', fmt='-o', color='navy', capsize=4)
ax.errorbar(years, pacific_temp, yerr=pacific_err, label='Pacific Ocean', fmt='-s', color='teal', capsize=4)
ax.errorbar(years, indian_temp, yerr=indian_err, label='Indian Ocean', fmt='-^', color='maroon', capsize=4)
ax.errorbar(years, arctic_temp, yerr=arctic_err, label='Arctic Ocean', fmt='-d', color='purple', capsize=4)

# Customizing the plot
ax.set_title('Climate Change Impact on Ocean Surface Temperatures\n(2010-2020)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Average Surface Temperature (°C)', fontsize=14, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.7)

# Add a legend to differentiate the lines
ax.legend(loc='upper left', fontsize=11, frameon=False)

# Set x-ticks to be each year and format labels
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right', fontsize=10)

# Automatically adjust the subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()