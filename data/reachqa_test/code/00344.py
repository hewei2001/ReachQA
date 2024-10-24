import matplotlib.pyplot as plt
import numpy as np

# Data for months, average AQI values, and their uncertainties
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
aqi_values = np.array([55, 58, 60, 65, 70, 75, 80, 82, 78, 72, 66, 60])
errors = np.array([3, 2, 4, 5, 6, 5, 3, 4, 5, 6, 4, 3])

# Calculate monthly AQI change percentages for the second plot
aqi_change_percentage = np.diff(aqi_values) / aqi_values[:-1] * 100

# Create a figure with two subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6), gridspec_kw={'width_ratios': [2, 1]})

# First subplot: Line chart with error bars
axes[0].errorbar(months, aqi_values, yerr=errors, fmt='-o', ecolor='lightgrey', elinewidth=2, capsize=4, 
                 color='#FF4500', marker='s', markersize=8, linestyle='-', linewidth=2, alpha=0.9)
axes[0].set_title('RoboVille Environmental Surveillance\nAverage Monthly Air Quality Index (AQI) - 2043', 
                  fontsize=14, fontweight='bold', pad=20)
axes[0].set_xlabel('Month', fontsize=12)
axes[0].set_ylabel('Average AQI', fontsize=12)
axes[0].grid(linestyle='--', alpha=0.7)

# Annotate the data points on the first plot
for i, (month, aqi, error) in enumerate(zip(months, aqi_values, errors)):
    axes[0].annotate(f'{aqi}±{error}', (month, aqi), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10)

axes[0].legend(['Monthly Average AQI with Error'], loc='upper left', fontsize=10, title="Legend")

# Second subplot: Bar chart for AQI change percentage
axes[1].bar(months[1:], aqi_change_percentage, color='lightgreen', edgecolor='green', alpha=0.7)
axes[1].axhline(0, color='grey', linewidth=0.8, linestyle='--')
axes[1].set_title('Monthly AQI Change Percentage', fontsize=12, fontweight='bold', pad=15)
axes[1].set_xlabel('Month', fontsize=12)
axes[1].set_ylabel('% Change', fontsize=12)
axes[1].grid(linestyle='--', alpha=0.5)

# Annotate the bars with percentage change
for i, change in enumerate(aqi_change_percentage):
    axes[1].annotate(f'{change:.1f}%', (months[i+1], change), textcoords="offset points", xytext=(0,5), ha='center', fontsize=10)

# Adjust layout to prevent overlaps
plt.tight_layout()

# Display the plot
plt.show()