import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# NO2 and PM2.5 data points
no2_levels = np.array([15, 18, 21, 22, 24, 30, 35, 40, 43, 45, 50, 55, 60, 65, 70])
pm25_levels = np.array([10, 12, 14, 15, 17, 22, 26, 30, 32, 33, 37, 42, 46, 50, 55])

# Sort data by no2_levels for smooth fitting line
sorted_indices = np.argsort(no2_levels)
no2_levels = no2_levels[sorted_indices]
pm25_levels = pm25_levels[sorted_indices]

# Create a smooth line using interpolation
spl = make_interp_spline(no2_levels, pm25_levels, k=3)
no2_smooth = np.linspace(no2_levels.min(), no2_levels.max(), 300)
pm25_smooth = spl(no2_smooth)

# Related data for an additional subplot (e.g., Ozone levels)
ozone_levels = np.array([20, 22, 25, 27, 28, 33, 38, 42, 44, 48, 52, 58, 63, 68, 72])

# Plotting the charts
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# First subplot: Scatter plot with smooth fitting line
ax1.scatter(no2_levels, pm25_levels, color='blue', label='Data Points', alpha=0.6)
ax1.plot(no2_smooth, pm25_smooth, color='red', linestyle='-', linewidth=2, label='Smooth Fitting Line')
ax1.set_title('Correlation of NO2 and PM2.5\nConcentrations in Smogville', fontsize=14, fontweight='bold')
ax1.set_xlabel('NO2 Concentration (μg/m³)', fontsize=12)
ax1.set_ylabel('PM2.5 Concentration (μg/m³)', fontsize=12)
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(linestyle='--', linewidth=0.5, alpha=0.7)

# Second subplot: Bar chart of Ozone levels
months = np.arange(1, 16)  # Representing data points as different time intervals or categories
ax2.bar(months, ozone_levels, color='green', alpha=0.7)
ax2.set_title('Ozone Levels Across Time Intervals', fontsize=14, fontweight='bold')
ax2.set_xlabel('Time Interval', fontsize=12)
ax2.set_ylabel('Ozone Concentration (μg/m³)', fontsize=12)
ax2.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()