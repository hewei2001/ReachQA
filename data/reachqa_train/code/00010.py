import matplotlib.pyplot as plt
import numpy as np

# Days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Average PM2.5 concentrations for each day (µg/m³)
pm25_concentrations = np.array([55, 60, 52, 45, 50, 65, 70])

# Standard deviation of PM2.5 concentrations to represent variability
pm25_variability = np.array([5, 7, 4, 6, 5, 8, 7])

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.errorbar(days, pm25_concentrations, yerr=pm25_variability, fmt='-o', ecolor='red', capsize=5, capthick=2, color='blue', alpha=0.8, label='PM2.5 Levels')

# Adding plot details
ax.set_title("Daily Air Pollution Levels:\nPM2.5 Concentration Over a Week", fontsize=14)
ax.set_xlabel("Day of the Week", fontsize=12)
ax.set_ylabel("PM2.5 Concentration (µg/m³)", fontsize=12)
ax.set_ylim(35, 80)
ax.set_yticks(np.arange(35, 85, 5))
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='upper left', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()