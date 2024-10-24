import matplotlib.pyplot as plt
import numpy as np

# Define the months of the year and their names
months = np.arange(1, 13)
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Average monthly temperatures (°C) for three cities
new_york_temps = np.array([0.0, 1.5, 5.0, 11.0, 16.5, 21.0, 25.0, 24.5, 20.0, 14.0, 8.5, 3.0])
moscow_temps = np.array([-6.5, -5.0, 0.0, 8.0, 15.0, 19.5, 22.0, 20.0, 14.0, 7.0, 0.0, -4.0])
tokyo_temps = np.array([5.0, 6.0, 9.5, 15.0, 20.0, 23.5, 27.0, 29.0, 25.0, 19.0, 13.0, 8.0])

# Precipitation data (mm) for each city
new_york_precip = np.array([78, 71, 82, 99, 96, 87, 101, 90, 80, 89, 92, 84])
moscow_precip = np.array([35, 31, 34, 44, 50, 75, 95, 77, 65, 60, 45, 40])
tokyo_precip = np.array([48, 56, 117, 124, 137, 160, 154, 168, 209, 197, 92, 51])

# Standard deviations representing temperature variability
new_york_std = np.array([1.0, 1.5, 1.2, 1.0, 1.5, 1.0, 1.5, 1.2, 1.0, 1.5, 1.0, 1.2])
moscow_std = np.array([1.5, 1.7, 1.3, 1.2, 1.6, 1.2, 1.8, 1.5, 1.3, 1.0, 1.5, 1.7])
tokyo_std = np.array([0.8, 1.0, 0.9, 1.1, 0.7, 0.8, 1.0, 0.9, 0.7, 0.8, 0.9, 0.8])

# Create the plot
plt.figure(figsize=(14, 10))

# Plot each city's temperature data with error bars
plt.errorbar(months, new_york_temps, yerr=new_york_std, label='New York Temp', fmt='-o', color='blue', ecolor='lightblue', elinewidth=2, capsize=3)
plt.errorbar(months, moscow_temps, yerr=moscow_std, label='Moscow Temp', fmt='-s', color='red', ecolor='salmon', elinewidth=2, capsize=3)
plt.errorbar(months, tokyo_temps, yerr=tokyo_std, label='Tokyo Temp', fmt='-^', color='green', ecolor='lightgreen', elinewidth=2, capsize=3)

# Add precipitation data using a bar chart
bar_width = 0.2
opacity = 0.6

plt.bar(months - bar_width, new_york_precip, bar_width, alpha=opacity, color='blue', label='New York Precip', edgecolor='darkblue')
plt.bar(months, moscow_precip, bar_width, alpha=opacity, color='red', label='Moscow Precip', edgecolor='darkred')
plt.bar(months + bar_width, tokyo_precip, bar_width, alpha=opacity, color='green', label='Tokyo Precip', edgecolor='darkgreen')

# Add title and labels with appropriate formatting
plt.title("Climate Science: Monthly Temperature and Precipitation\nAcross Northern Hemisphere Cities", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=14)
plt.ylabel("Temperature (°C) / Precipitation (mm)", fontsize=14)

# Customize the x-ticks to show month names
plt.xticks(months, month_names, fontsize=12)
plt.yticks(fontsize=12)

# Extend the legend to include precipitation data
plt.legend(loc='upper right', fontsize=12, frameon=False)

# Enable grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Adjust layout to ensure no overlap
plt.tight_layout()

# Display the plot
plt.show()