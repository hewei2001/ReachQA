import matplotlib.pyplot as plt
import numpy as np

# Define months and years
months = np.arange(1, 13)
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Average monthly temperatures (°C) for each year in Fantasica
temps_year_1 = [5, 7, 10, 15, 20, 25, 28, 27, 22, 16, 10, 6]
temps_year_2 = [4, 6, 9, 14, 19, 23, 27, 26, 21, 15, 9, 5]
temps_year_3 = [6, 8, 12, 17, 22, 26, 29, 28, 23, 17, 11, 7]

# Temperature variability (error margin)
error_year_1 = [1, 2, 1.5, 2, 1.8, 1.6, 1.2, 1, 1.5, 1.8, 1.2, 1]
error_year_2 = [1.5, 2.5, 2, 1.8, 2, 1.6, 1.4, 1.2, 1.6, 2, 1.5, 1.3]
error_year_3 = [1, 1.8, 2.5, 2, 2.2, 1.8, 1.5, 1.3, 1.7, 2.1, 1.3, 1]

# Plot setup
fig, ax = plt.subplots(figsize=(10, 6))
ax.errorbar(months, temps_year_1, yerr=error_year_1, 
            label='Year 1', fmt='-o', capsize=4, color='tab:blue', alpha=0.8)
ax.errorbar(months, temps_year_2, yerr=error_year_2, 
            label='Year 2', fmt='-s', capsize=4, color='tab:green', alpha=0.8)
ax.errorbar(months, temps_year_3, yerr=error_year_3, 
            label='Year 3', fmt='-^', capsize=4, color='tab:red', alpha=0.8)

# Chart customizations
ax.set_title('Average Monthly Temperatures on Fantasica Island\n(With Error Margins)', fontsize=14, pad=20)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Temperature (°C)', fontsize=12)
ax.set_xticks(months)
ax.set_xticklabels(month_labels)
ax.set_xlim(0.5, 12.5)
ax.set_ylim(0, 35)

# Add gridlines for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Legend
ax.legend(title='Observations', loc='upper left')

# Automatically adjust layout for clarity
plt.tight_layout()

# Show plot
plt.show()