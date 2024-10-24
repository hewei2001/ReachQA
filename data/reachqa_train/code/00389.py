import matplotlib.pyplot as plt
import numpy as np

# Define the days of the week
days = np.array(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

# Artificial NO2 levels in micrograms per cubic meter (µg/m³) for each day
no2_levels = np.array([35, 42, 39, 48, 45, 30, 25])

# Error margins for NO2 levels (± µg/m³)
error_margins = np.array([5, 4, 4, 6, 5, 3, 2])

# Artificial PM2.5 levels for each day
pm25_levels = np.array([22, 30, 28, 35, 32, 20, 15])

# Plotting the line chart with error bars for NO2 levels
fig, ax1 = plt.subplots(figsize=(12, 7))

# NO2 levels with error bars
ax1.errorbar(days, no2_levels, yerr=error_margins, fmt='-o', color='darkred', ecolor='gray',
             elinewidth=2, capsize=5, capthick=2, alpha=0.8, label='NO2 Levels')
ax1.set_xlabel("Day of the Week", fontsize=12)
ax1.set_ylabel("NO2 Levels (µg/m³)", fontsize=12, color='darkred')
ax1.tick_params(axis='y', labelcolor='darkred')

# Overlay bar chart for PM2.5 levels
ax2 = ax1.twinx()
ax2.bar(days, pm25_levels, color='royalblue', alpha=0.5, width=0.3, label='PM2.5 Levels')
ax2.set_ylabel("PM2.5 Levels (µg/m³)", fontsize=12, color='royalblue')
ax2.tick_params(axis='y', labelcolor='royalblue')

# Title and grid
ax1.set_title("Urban Air Quality Monitoring:\nDaily NO2 and PM2.5 Levels Over a Week", fontsize=16, fontweight='bold')
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Legends for each axis
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Automatically adjust the layout to prevent overlaps
plt.tight_layout()

# Display the plot
plt.show()