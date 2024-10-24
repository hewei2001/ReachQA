import matplotlib.pyplot as plt
import numpy as np

# Define years in BC (for easy plotting)
years_bc = np.array([2995, 2994, 2993, 2992, 2991])

# Hypothetical average annual temperatures in degrees Celsius
average_temperatures = np.array([16.1, 15.8, 16.0, 15.7, 16.2])

# Hypothetical error margins (± degrees Celsius)
temperature_errors = np.array([0.4, 0.3, 0.5, 0.3, 0.4])

# Create the line chart with error bars
plt.figure(figsize=(10, 6))

# Plot the average temperature line with error bars
plt.errorbar(years_bc, average_temperatures, yerr=temperature_errors, fmt='-o', linewidth=2, color='royalblue',
             ecolor='lightcoral', elinewidth=2, capsize=5, alpha=0.8, label='Avg Temperature ± Error')

# Annotate data points with the temperature
for i, temp in enumerate(average_temperatures):
    plt.annotate(f'{temp}°C', (years_bc[i], average_temperatures[i]), textcoords="offset points", xytext=(-5, 10),
                 ha='center', fontsize=10, color='royalblue')

# Customize axes labels and title
plt.xlabel('Year (BC)', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.title('Temperature Fluctuations in Atlantis\n(2995 BC - 2991 BC)', fontsize=16, fontweight='bold', pad=20)

# Set limits for better visualization
plt.xlim(2995.5, 2990.5)
plt.ylim(15, 17)

# Add gridlines
plt.grid(True, linestyle='--', alpha=0.6)

# Add legend
plt.legend(loc='upper left', fontsize=12)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()