import matplotlib.pyplot as plt
import numpy as np

# Define the days of the week
days = np.array(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

# Artificial NO2 levels in micrograms per cubic meter (µg/m³) for each day
no2_levels = np.array([35, 42, 39, 48, 45, 30, 25])

# Error margins representing potential measurement inaccuracies (± µg/m³)
error_margins = np.array([5, 4, 4, 6, 5, 3, 2])

# Plotting the line chart with error bars
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the NO2 levels with error bars
ax.errorbar(days, no2_levels, yerr=error_margins, fmt='-o', color='darkred', ecolor='gray', 
            elinewidth=2, capsize=5, capthick=2, alpha=0.8, label='NO2 Levels')

# Title and labels
ax.set_title("Urban Air Quality Monitoring: Daily NO2 Levels Over a Week", fontsize=16, fontweight='bold')
ax.set_xlabel("Day of the Week", fontsize=12)
ax.set_ylabel("NO2 Levels (µg/m³)", fontsize=12)

# Adding a grid for better readability
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adding a legend
ax.legend(loc='upper right', fontsize=10)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Automatically adjust the layout to prevent overlaps
plt.tight_layout()

# Display the plot
plt.show()