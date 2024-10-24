import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Define months and years
months = np.arange(1, 13)
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Average monthly temperatures (°C) for each year in Fantasica
temps_year_1 = [5, 7, 10, 15, 20, 25, 28, 27, 22, 16, 10, 6]
temps_year_2 = [4, 6, 9, 14, 19, 23, 27, 26, 21, 15, 9, 5]
temps_year_3 = [6, 8, 12, 17, 22, 26, 29, 28, 23, 17, 11, 7]

# Average monthly precipitation (mm) for each year in Fantasica
precip_year_1 = [78, 60, 54, 45, 60, 48, 35, 38, 49, 66, 77, 84]
precip_year_2 = [80, 62, 56, 47, 62, 50, 37, 40, 51, 68, 79, 86]
precip_year_3 = [82, 64, 58, 49, 64, 52, 39, 42, 53, 70, 81, 88]

# Temperature variability (error margin)
error_year_1 = [1, 2, 1.5, 2, 1.8, 1.6, 1.2, 1, 1.5, 1.8, 1.2, 1]
error_year_2 = [1.5, 2.5, 2, 1.8, 2, 1.6, 1.4, 1.2, 1.6, 2, 1.5, 1.3]
error_year_3 = [1, 1.8, 2.5, 2, 2.2, 1.8, 1.5, 1.3, 1.7, 2.1, 1.3, 1]

# Plot setup
fig, ax1 = plt.subplots(figsize=(12, 8))

# Adding shading for seasons (simplified: Winter and Summer)
ax1.axvspan(0.5, 2.5, facecolor='lightblue', alpha=0.3, label='Winter')
ax1.axvspan(6.5, 8.5, facecolor='lightyellow', alpha=0.3, label='Summer')

# Plotting temperatures with error bars
ax1.errorbar(months, temps_year_1, yerr=error_year_1, fmt='-o', capsize=4, 
             color='tab:blue', alpha=0.8, label='Year 1')
ax1.errorbar(months, temps_year_2, yerr=error_year_2, fmt='-s', capsize=4, 
             color='tab:green', alpha=0.8, label='Year 2')
ax1.errorbar(months, temps_year_3, yerr=error_year_3, fmt='-^', capsize=4, 
             color='tab:red', alpha=0.8, label='Year 3')

# Setting title, labels, and limits
ax1.set_title('Average Monthly Temperatures and Precipitation on Fantasica Island\n'
              '(With Temperature Error Margins and Seasonal Indicators)', fontsize=14, pad=20)
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Temperature (°C)', fontsize=12)
ax1.set_xticks(months)
ax1.set_xticklabels(month_labels)
ax1.set_xlim(0.5, 12.5)
ax1.set_ylim(0, 35)
ax1.grid(True, linestyle='--', alpha=0.5)

# Adding secondary y-axis for precipitation
ax2 = ax1.twinx()
ax2.plot(months, precip_year_1, '-.b', label='Precipitation Year 1', alpha=0.5)
ax2.plot(months, precip_year_2, '-.g', label='Precipitation Year 2', alpha=0.5)
ax2.plot(months, precip_year_3, '-.r', label='Precipitation Year 3', alpha=0.5)
ax2.set_ylabel('Precipitation (mm)', fontsize=12)
ax2.set_ylim(30, 100)

# Customizing legends
temp_legend = ax1.legend(loc='upper left', title='Temperature Observations', fontsize=10)

# Seasonal shading legend
season_patch_winter = mpatches.Patch(color='lightblue', alpha=0.3, label='Winter')
season_patch_summer = mpatches.Patch(color='lightyellow', alpha=0.3, label='Summer')
season_legend = ax1.legend(handles=[season_patch_winter, season_patch_summer], loc='lower left', fontsize=10)
ax1.add_artist(temp_legend)

ax2.legend(loc='upper right', title='Precipitation Observations', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()