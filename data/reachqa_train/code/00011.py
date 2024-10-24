import matplotlib.pyplot as plt
import numpy as np

# Days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Average PM2.5 concentrations for each day (µg/m³) and their variability
pm25_concentrations = np.array([55, 60, 52, 45, 50, 65, 70])
pm25_variability = np.array([5, 7, 4, 6, 5, 8, 7])

# Constructed average daily temperatures (°C) for each day
avg_temperatures = np.array([22, 21, 24, 23, 22, 26, 25])

# Create the plot
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot PM2.5 concentration with error bars
ax1.errorbar(days, pm25_concentrations, yerr=pm25_variability, fmt='-o',
             ecolor='red', capsize=5, capthick=2, color='blue', alpha=0.8, label='PM2.5 Levels')

# Adding plot details for ax1
ax1.set_title("Air Quality & Weather Overview:\nPM2.5 Concentration and Temperature Trends", fontsize=14)
ax1.set_xlabel("Day of the Week", fontsize=12)
ax1.set_ylabel("PM2.5 Concentration (µg/m³)", fontsize=12, color='blue')
ax1.set_ylim(35, 80)
ax1.set_yticks(np.arange(35, 85, 5))
ax1.tick_params(axis='y', labelcolor='blue')
ax1.grid(True, linestyle='--', alpha=0.6)

# Create a second y-axis for average daily temperatures
ax2 = ax1.twinx()
ax2.bar(days, avg_temperatures, color='orange', alpha=0.5, width=0.4, label='Average Temperature')
ax2.set_ylabel("Average Temperature (°C)", fontsize=12, color='orange')
ax2.set_ylim(20, 30)
ax2.tick_params(axis='y', labelcolor='orange')

# Combine legends from both axes
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()