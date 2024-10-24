import matplotlib.pyplot as plt
import numpy as np

# Define the months of the year
months = np.arange(1, 13)
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Average monthly temperatures (°C) for three cities
new_york_temps = np.array([0.0, 1.5, 5.0, 11.0, 16.5, 21.0, 25.0, 24.5, 20.0, 14.0, 8.5, 3.0])
moscow_temps = np.array([-6.5, -5.0, 0.0, 8.0, 15.0, 19.5, 22.0, 20.0, 14.0, 7.0, 0.0, -4.0])
tokyo_temps = np.array([5.0, 6.0, 9.5, 15.0, 20.0, 23.5, 27.0, 29.0, 25.0, 19.0, 13.0, 8.0])

# Standard deviations representing the variability in temperatures
new_york_std = np.array([1.0, 1.5, 1.2, 1.0, 1.5, 1.0, 1.5, 1.2, 1.0, 1.5, 1.0, 1.2])
moscow_std = np.array([1.5, 1.7, 1.3, 1.2, 1.6, 1.2, 1.8, 1.5, 1.3, 1.0, 1.5, 1.7])
tokyo_std = np.array([0.8, 1.0, 0.9, 1.1, 0.7, 0.8, 1.0, 0.9, 0.7, 0.8, 0.9, 0.8])

# Create the plot
plt.figure(figsize=(14, 8))

# Plot each city's data with error bars
plt.errorbar(months, new_york_temps, yerr=new_york_std, label='New York', fmt='-o', color='blue', ecolor='lightblue', elinewidth=2, capsize=3)
plt.errorbar(months, moscow_temps, yerr=moscow_std, label='Moscow', fmt='-s', color='red', ecolor='salmon', elinewidth=2, capsize=3)
plt.errorbar(months, tokyo_temps, yerr=tokyo_std, label='Tokyo', fmt='-^', color='green', ecolor='lightgreen', elinewidth=2, capsize=3)

# Add title and labels
plt.title("Climate Science: Monthly Temperature Variability\nAnalysis Across Northern Hemisphere Cities", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=14)
plt.ylabel("Average Temperature (°C)", fontsize=14)

# Customize the x-ticks to show month names
plt.xticks(months, month_names, fontsize=12)
plt.yticks(fontsize=12)

# Show legend
plt.legend(loc='upper left', fontsize=12)

# Enable grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to ensure no overlap
plt.tight_layout()

# Display the plot
plt.show()