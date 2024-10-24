import matplotlib.pyplot as plt
import numpy as np

# Data setup
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
average_temperatures = np.array([5, 7, 10, 15, 18, 22, 25, 24, 20, 15, 10, 6])
temperature_variability = np.array([1.5, 1.3, 1.7, 2.0, 2.5, 1.8, 2.2, 2.0, 1.9, 1.4, 1.2, 1.6])

# Secondary data: Average daylight hours in Solara (fabricated for illustration)
average_daylight_hours = np.array([8, 9, 11, 13, 15, 16, 15, 14, 12, 10, 9, 8])

# Create figure and axis
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the average temperature with error shading
ax1.plot(months, average_temperatures, color='mediumblue', marker='s', linestyle='-', linewidth=2.5, markersize=7, label='Average Temperature')
ax1.fill_between(months, average_temperatures - temperature_variability, average_temperatures + temperature_variability, color='skyblue', alpha=0.3, label='Temperature Variability')

# Highlight the maximum and minimum temperature months
max_month_idx = np.argmax(average_temperatures)
min_month_idx = np.argmin(average_temperatures)
ax1.scatter(months[max_month_idx], average_temperatures[max_month_idx], color='darkred', s=100, edgecolors='black', zorder=5, label='Max Temperature')
ax1.scatter(months[min_month_idx], average_temperatures[min_month_idx], color='navy', s=100, edgecolors='black', zorder=5, label='Min Temperature')

# Second y-axis for daylight hours
ax2 = ax1.twinx()
ax2.plot(months, average_daylight_hours, color='forestgreen', marker='o', linestyle='--', linewidth=2, markersize=6, label='Average Daylight Hours')

# Titles and labels
ax1.set_title('Average Monthly Temperatures and Daylight in Solara\nWith Temperature Variability (°C)', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Temperature (°C)', fontsize=12, color='mediumblue')
ax2.set_ylabel('Daylight Hours', fontsize=12, color='forestgreen')

# Axes ticks customization
ax1.tick_params(axis='y', labelcolor='mediumblue')
ax2.tick_params(axis='y', labelcolor='forestgreen')
ax1.set_ylim(0, 30)
ax2.set_ylim(0, 20)

# Grid lines
ax1.grid(visible=True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Legends
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize=10)

# Annotation for peak summer month
ax1.annotate('Peak summer month', xy=('Jul', 25), xytext=('Aug', 27),
             arrowprops=dict(facecolor='darkred', shrink=0.05, width=1.5),
             fontsize=10, color='darkred', ha='center')

# Layout adjustment and plot display
plt.tight_layout()
plt.show()