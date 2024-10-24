import matplotlib.pyplot as plt
import numpy as np

# Define months
months = np.arange(1, 13)
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Average temperatures (°C) for each city
sunville_temps = [25, 27, 30, 32, 35, 38, 37, 36, 34, 31, 28, 26]
rainytown_temps = [18, 19, 21, 24, 26, 27, 26, 25, 23, 20, 19, 18]
snowy_peaks_temps = [-5, -3, 1, 5, 10, 15, 14, 12, 8, 3, -1, -4]

# Temperature variability (errors)
sunville_errors = [1.5, 1.5, 2, 2, 2.5, 2.5, 2, 2, 1.5, 1.5, 1, 1]
rainytown_errors = [1, 1.2, 1.3, 1.5, 1.7, 1.8, 1.5, 1.3, 1.1, 1, 1, 1]
snowy_peaks_errors = [3, 3, 3.5, 4, 4.5, 4, 4, 3.5, 3, 3, 3.5, 3]

# Average precipitation (mm) for each city
sunville_precip = [12, 14, 18, 20, 8, 2, 4, 3, 5, 9, 14, 16]
rainytown_precip = [100, 120, 140, 160, 150, 130, 110, 100, 90, 95, 110, 120]
snowy_peaks_precip = [30, 35, 40, 45, 50, 60, 55, 50, 40, 30, 35, 25]

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 7))

# Plot temperatures with error bars
axes[0].errorbar(months, sunville_temps, yerr=sunville_errors, fmt='-o', capsize=4,
                 label='Sunville', color='orange', alpha=0.8)
axes[0].errorbar(months, rainytown_temps, yerr=rainytown_errors, fmt='-^', capsize=4,
                 label='Rainytown', color='blue', alpha=0.8)
axes[0].errorbar(months, snowy_peaks_temps, yerr=snowy_peaks_errors, fmt='-s', capsize=4,
                 label='Snowy Peaks', color='purple', alpha=0.8)

axes[0].set_title('Average Monthly Temperatures with Variability\nSunville, Rainytown, and Snowy Peaks', 
                  fontsize=12, fontweight='bold')
axes[0].set_xlabel('Month', fontsize=10)
axes[0].set_ylabel('Temperature (°C)', fontsize=10)
axes[0].set_xticks(months)
axes[0].set_xticklabels(month_names)
axes[0].legend(title='Cities')
axes[0].grid(True, linestyle='--', alpha=0.6)
axes[0].set_ylim(-10, 40)

# Plot precipitation with bar chart
axes[1].bar(months - 0.2, sunville_precip, width=0.2, label='Sunville', color='orange', alpha=0.8)
axes[1].bar(months, rainytown_precip, width=0.2, label='Rainytown', color='blue', alpha=0.8)
axes[1].bar(months + 0.2, snowy_peaks_precip, width=0.2, label='Snowy Peaks', color='purple', alpha=0.8)

axes[1].set_title('Average Monthly Precipitation\nSunville, Rainytown, and Snowy Peaks', 
                  fontsize=12, fontweight='bold')
axes[1].set_xlabel('Month', fontsize=10)
axes[1].set_ylabel('Precipitation (mm)', fontsize=10)
axes[1].set_xticks(months)
axes[1].set_xticklabels(month_names)
axes[1].legend(title='Cities')
axes[1].grid(True, linestyle='--', alpha=0.6)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()