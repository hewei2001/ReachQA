import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker

# Define months for the x-axis
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Temperature data for each city in degrees Celsius
climatia_temps = np.array([-2, 0, 5, 12, 18, 24, 28, 26, 19, 12, 6, 1])
tempestville_temps = np.array([8, 9, 10, 13, 16, 20, 22, 21, 18, 14, 10, 9])
sunnyvale_temps = np.array([15, 16, 18, 20, 24, 28, 30, 29, 27, 22, 18, 16])

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot data with gradient colors for temperature change visualization
ax.plot(months, climatia_temps, label='Climatia', color='dodgerblue', marker='o', linewidth=2.5)
ax.plot(months, tempestville_temps, label='Tempestville', color='mediumseagreen', marker='s', linestyle='--', linewidth=2)
ax.plot(months, sunnyvale_temps, label='Sunnyvale', color='darkorange', marker='^', linestyle='-.', linewidth=2)

# Fill area under curves for better visual distinction
ax.fill_between(months, climatia_temps, color='dodgerblue', alpha=0.1)
ax.fill_between(months, tempestville_temps, color='mediumseagreen', alpha=0.1)
ax.fill_between(months, sunnyvale_temps, color='darkorange', alpha=0.1)

# Set title and labels
ax.set_title('Urban Temperature Variations in 2023\nClimatia, Tempestville & Sunnyvale', fontsize=16, fontweight='bold')
ax.set_xlabel('Months', fontsize=14)
ax.set_ylabel('Temperature (°C)', fontsize=14)

# Add reference lines
ax.axhline(y=0, color='grey', linewidth=1.5, linestyle='--')
ax.axhline(y=20, color='lightcoral', linewidth=1, linestyle=':')

# Enhanced grid lines
ax.grid(True, linestyle='--', alpha=0.7)

# Annotate peak and low temperatures
for city, temps, color in [('Climatia', climatia_temps, 'dodgerblue'),
                           ('Tempestville', tempestville_temps, 'mediumseagreen'),
                           ('Sunnyvale', sunnyvale_temps, 'darkorange')]:
    max_temp = temps.max()
    min_temp = temps.min()
    ax.annotate(f"Peak: {max_temp}°C", 
                (months[temps.argmax()], max_temp), 
                textcoords="offset points", xytext=(-30, 10), fontsize=10, color=color)
    ax.annotate(f"Low: {min_temp}°C", 
                (months[temps.argmin()], min_temp), 
                textcoords="offset points", xytext=(-30, -20), fontsize=10, color=color)

# Secondary axis to show anomalies (example data)
ax2 = ax.twinx()
anomalies = climatia_temps - np.mean(climatia_temps)
ax2.bar(months, anomalies, color='lightsteelblue', alpha=0.3, width=0.4, label='Anomalies (Climatia)')
ax2.set_ylabel('Temperature Anomaly (°C)', fontsize=12, color='lightsteelblue')
ax2.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))

# Legends
ax.legend(loc='upper left', fontsize=12)
ax2.legend(loc='upper right', fontsize=12)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()