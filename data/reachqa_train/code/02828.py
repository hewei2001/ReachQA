import matplotlib.pyplot as plt
import numpy as np

# Months of the year
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Artificial AQI data for each month
aqi_levels = np.array([50, 45, 60, 70, 65, 55, 80, 85, 75, 60, 55, 50])

# Uncertainties in AQI measurements
aqi_error = np.array([5, 7, 4, 6, 5, 4, 7, 5, 6, 5, 4, 5])

# Create the plot
plt.figure(figsize=(12, 6))

# Plot the line chart with error bars
plt.errorbar(months, aqi_levels, yerr=aqi_error, fmt='-o', ecolor='red', 
             linestyle='-', color='blue', capsize=5, label='Measured AQI', alpha=0.8)

# Highlight the maximum AQI month
max_aqi_index = np.argmax(aqi_levels)
plt.annotate('Peak AQI', xy=(months[max_aqi_index], aqi_levels[max_aqi_index]), 
             xytext=(months[max_aqi_index], aqi_levels[max_aqi_index] + 10),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=10, color='darkred', ha='center')

# Title and labels
plt.title('Monthly Air Quality Index (AQI) Fluctuations in Ecohaven - 2023\nIncluding Measurement Uncertainties', 
          fontsize=14, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Air Quality Index (AQI)', fontsize=12)

# Customize the grid
plt.grid(True, linestyle=':', linewidth=0.5, color='grey', alpha=0.7)

# Add legend
plt.legend(loc='upper right', fontsize=10)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()