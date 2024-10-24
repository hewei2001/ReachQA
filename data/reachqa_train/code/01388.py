import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define traffic density and travel time for three different times of the day
traffic_density_morning = np.array([50, 100, 150, 200, 250])
travel_time_morning = np.array([10, 15, 20, 35, 45])

traffic_density_midday = np.array([30, 70, 120, 160, 210])
travel_time_midday = np.array([8, 12, 18, 25, 33])

traffic_density_evening = np.array([40, 90, 140, 180, 230])
travel_time_evening = np.array([9, 14, 22, 30, 40])

# Generate smooth lines using spline interpolation
density_smooth = np.linspace(30, 250, 300)
spline_morning = make_interp_spline(traffic_density_morning, travel_time_morning, k=3)
spline_midday = make_interp_spline(traffic_density_midday, travel_time_midday, k=3)
spline_evening = make_interp_spline(traffic_density_evening, travel_time_evening, k=3)

time_morning_smooth = spline_morning(density_smooth)
time_midday_smooth = spline_midday(density_smooth)
time_evening_smooth = spline_evening(density_smooth)

# Set up the plot
plt.figure(figsize=(12, 8))

# Scatter plot for raw data points
plt.scatter(traffic_density_morning, travel_time_morning, color='red', label='Morning Rush Hour', edgecolor='black', s=100, zorder=2)
plt.scatter(traffic_density_midday, travel_time_midday, color='green', label='Midday', edgecolor='black', s=100, zorder=2)
plt.scatter(traffic_density_evening, travel_time_evening, color='blue', label='Evening Rush Hour', edgecolor='black', s=100, zorder=2)

# Smooth line plot for trends
plt.plot(density_smooth, time_morning_smooth, color='red', linestyle='-', label='Trend - Morning', zorder=1)
plt.plot(density_smooth, time_midday_smooth, color='green', linestyle='-', label='Trend - Midday', zorder=1)
plt.plot(density_smooth, time_evening_smooth, color='blue', linestyle='-', label='Trend - Evening', zorder=1)

# Customize the plot
plt.title('Analyzing Traffic Patterns in Metroville:\nDensity vs. Travel Time', fontsize=16)
plt.xlabel('Traffic Density (vehicles per kilometer)', fontsize=14)
plt.ylabel('Average Travel Time (minutes)', fontsize=14)
plt.xticks(np.arange(30, 251, 40))
plt.yticks(np.arange(0, 51, 10))
plt.grid(True, linestyle='--', alpha=0.5)

# Add legend and adjust layout
plt.legend(title='Time of Day', loc='upper left', fontsize=10, frameon=False)
plt.tight_layout()

# Display the plot
plt.show()