import matplotlib.pyplot as plt
import numpy as np

# Data for Climatopia
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
average_temperatures = np.array([5, 7, 10, 15, 20, 25, 30, 29, 24, 18, 10, 6])
temperature_variability = np.array([1.5, 1.3, 1.0, 1.2, 1.8, 2.0, 
                                    1.9, 1.7, 1.6, 1.2, 1.0, 1.4])
# Assume hypothetical average monthly precipitation (in mm)
average_precipitation = np.array([78, 62, 55, 47, 66, 84, 92, 110, 85, 74, 80, 90])

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Line chart with error bars for temperature
ax1.errorbar(months, average_temperatures, yerr=temperature_variability, 
             label='Avg Temp (°C)', color='royalblue', fmt='-o', 
             capsize=5, elinewidth=2, markeredgewidth=2, alpha=0.85)
ax1.set_title('Climatopia Temperature Observation\nMonthly Average with Variability (2023)',
              fontsize=14, fontweight='bold')
ax1.set_xlabel('Month')
ax1.set_ylabel('Temperature (°C)')
ax1.legend(loc='upper left')
ax1.grid(True, linestyle='--', alpha=0.6)

# Bar chart for precipitation
ax2.bar(months, average_precipitation, color='lightseagreen', alpha=0.8)
ax2.set_title('Monthly Average Precipitation (2023)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Month')
ax2.set_ylabel('Precipitation (mm)')
ax2.grid(axis='y', linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()