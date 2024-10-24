import matplotlib.pyplot as plt
import numpy as np

# Define the data
years = np.arange(2010, 2020)
avg_temperatures = np.array([15.2, 15.3, 15.4, 15.7, 16.0, 16.1, 16.2, 16.4, 16.5, 16.8])
temperature_errors = np.array([0.2, 0.3, 0.25, 0.3, 0.2, 0.3, 0.15, 0.2, 0.25, 0.2])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the line chart with error bars
ax.errorbar(
    years, avg_temperatures, yerr=temperature_errors,
    fmt='-o', color='mediumseagreen', ecolor='lightcoral',
    elinewidth=2, capsize=5, capthick=2, alpha=0.8, label='Average Temperature ± Error'
)

# Set labels and title with line breaks for better readability
ax.set_xlabel('Year', fontsize=13, fontweight='bold')
ax.set_ylabel('Average Temperature (°C)', fontsize=13, fontweight='bold')
ax.set_title('Annual Temperature Trends in Coastal City\n(2010-2019)', fontsize=15, fontweight='bold')

# Set grid
ax.grid(True, linestyle='--', alpha=0.7)

# Define axis limits
ax.set_xlim(2009, 2020)
ax.set_ylim(14.5, 17.5)

# Add legend
ax.legend(loc='upper left', fontsize=11)

# Adjust layout for clarity
plt.tight_layout()

# Display the plot
plt.show()