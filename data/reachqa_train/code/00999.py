import matplotlib.pyplot as plt
import numpy as np

# Define years in BC (for easy plotting)
years_bc = np.array([2995, 2994, 2993, 2992, 2991])

# Hypothetical average annual temperatures in degrees Celsius
average_temperatures = np.array([16.1, 15.8, 16.0, 15.7, 16.2])

# Hypothetical error margins (± degrees Celsius)
temperature_errors = np.array([0.4, 0.3, 0.5, 0.3, 0.4])

# Hypothetical atmospheric CO2 levels in parts per million (ppm)
co2_levels = np.array([280, 282, 279, 283, 281])

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the average temperature line with error bars on the primary y-axis
ax1.errorbar(years_bc, average_temperatures, yerr=temperature_errors, fmt='-o', linewidth=2, color='royalblue',
             ecolor='lightcoral', elinewidth=2, capsize=5, alpha=0.8, label='Avg Temperature ± Error')
ax1.set_xlabel('Year (BC)', fontsize=12)
ax1.set_ylabel('Temperature (°C)', fontsize=12, color='royalblue')
ax1.tick_params(axis='y', labelcolor='royalblue')

# Annotate data points with the temperature
for i, temp in enumerate(average_temperatures):
    ax1.annotate(f'{temp}°C', (years_bc[i], average_temperatures[i]), textcoords="offset points", xytext=(-5, 10),
                 ha='center', fontsize=10, color='royalblue')

# Create a secondary y-axis for CO2 levels
ax2 = ax1.twinx()
ax2.bar(years_bc, co2_levels, width=0.3, alpha=0.5, color='forestgreen', label='CO2 Levels (ppm)')
ax2.set_ylabel('CO2 Levels (ppm)', fontsize=12, color='forestgreen')
ax2.tick_params(axis='y', labelcolor='forestgreen')

# Title and grid customization
plt.title('Environmental Changes in Atlantis\nTemperature and CO2 Levels (2995 BC - 2991 BC)', fontsize=16, fontweight='bold', pad=20)
ax1.grid(True, linestyle='--', alpha=0.6)

# Add legends
fig.legend(loc='upper left', bbox_to_anchor=(0.15, 0.85), fontsize=12)

# Automatically adjust the layout
fig.tight_layout()

# Display the plot
plt.show()