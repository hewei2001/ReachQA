import matplotlib.pyplot as plt
import numpy as np

# Define decades and average temperatures with potential error margins
decades = np.array(['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s'])
average_temperatures = np.array([15.2, 15.5, 15.8, 16.0, 16.3, 16.8, 17.1])
error_margins = np.array([0.2, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05])

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the average temperatures with error bars
ax.errorbar(decades, average_temperatures, yerr=error_margins, fmt='-o', capsize=5,
            color='teal', ecolor='orange', elinewidth=2, markerfacecolor='navy',
            markersize=8, label='Temperature with Error Margin')

# Customize the plot
ax.set_title('Average Annual Temperature Change\nin Atlantis Isles (1960s-2020s)', 
             fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Decades', fontsize=12)
ax.set_ylabel('Temperature (°C)', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6)

# Adding a legend
ax.legend(title='Data Source:', loc='upper left', fontsize=10)

# Additional plot aesthetics
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot
plt.show()