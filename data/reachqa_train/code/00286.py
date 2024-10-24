import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Define the months
months = np.array([
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
])

# Average temperatures (°C)
average_temperatures = np.array([
    1.5, 3.0, 6.5, 10.5, 14.0, 18.5, 22.0, 21.0, 16.5, 11.0, 6.0, 2.5
])

# Historical average temperatures for comparison (°C)
historical_temperatures = np.array([
    2.0, 2.5, 5.0, 9.0, 13.0, 17.0, 21.5, 20.5, 15.0, 10.0, 5.5, 2.0
])

# Temperature error margins (°C)
temperature_errors = np.array([
    1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9
])

# Plot the line chart with error bars
fig, ax = plt.subplots(figsize=(14, 8))

# Plot current average temperatures
ax.errorbar(
    months, average_temperatures, yerr=temperature_errors, fmt='-o', 
    color='#FF5733', ecolor='lightgray', elinewidth=2, capsize=4, label='Current Avg Temp'
)

# Plot historical average temperatures
ax.plot(months, historical_temperatures, '-s', color='#1f77b4', alpha=0.7, label='Historical Avg Temp')

# Fill area under the current average temperature line
ax.fill_between(months, average_temperatures-temperature_errors, average_temperatures+temperature_errors, 
                color='#FF5733', alpha=0.1)

# Calculate and plot a trend line
slope, intercept, _, _, _ = linregress(range(len(months)), average_temperatures)
trend_line = slope * np.arange(len(months)) + intercept
ax.plot(months, trend_line, 'r--', linewidth=1, label='Trend Line')

# Customize the plot appearance
ax.set_title('Average Monthly Temperatures in Evergreen Valley\nwith Historical Comparison & Trends', 
             fontsize=16, fontweight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Temperature (°C)', fontsize=12)
ax.set_ylim(0, 25)
ax.grid(True, linestyle='--', alpha=0.6)

# Highlight a specific month with annotation
highlight_month = 'July'
highlight_idx = np.where(months == highlight_month)[0][0]
ax.annotate('Peak Temperature', xy=(highlight_month, average_temperatures[highlight_idx]),
            xytext=(highlight_month, average_temperatures[highlight_idx] + 3),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, ha='center')

# Rotate x-axis labels for readability
plt.xticks(rotation=45)

# Add a legend
ax.legend(loc='upper right', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()