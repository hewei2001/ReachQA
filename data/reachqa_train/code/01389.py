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

# Calculate derived data: Average Speed (density/time)
avg_speed_morning = traffic_density_morning / travel_time_morning
avg_speed_midday = traffic_density_midday / travel_time_midday
avg_speed_evening = traffic_density_evening / travel_time_evening

# Generate smooth lines using spline interpolation
density_smooth = np.linspace(30, 250, 300)
spline_morning = make_interp_spline(traffic_density_morning, travel_time_morning, k=3)
spline_midday = make_interp_spline(traffic_density_midday, travel_time_midday, k=3)
spline_evening = make_interp_spline(traffic_density_evening, travel_time_evening, k=3)

time_morning_smooth = spline_morning(density_smooth)
time_midday_smooth = spline_midday(density_smooth)
time_evening_smooth = spline_evening(density_smooth)

# Set up the plots
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Density vs Travel Time with smooth trends
ax[0].scatter(traffic_density_morning, travel_time_morning, color='red', label='Morning Rush Hour', edgecolor='black', s=100, zorder=2)
ax[0].scatter(traffic_density_midday, travel_time_midday, color='green', label='Midday', edgecolor='black', s=100, zorder=2)
ax[0].scatter(traffic_density_evening, travel_time_evening, color='blue', label='Evening Rush Hour', edgecolor='black', s=100, zorder=2)

ax[0].plot(density_smooth, time_morning_smooth, color='red', linestyle='-', label='Trend - Morning', zorder=1)
ax[0].plot(density_smooth, time_midday_smooth, color='green', linestyle='-', label='Trend - Midday', zorder=1)
ax[0].plot(density_smooth, time_evening_smooth, color='blue', linestyle='-', label='Trend - Evening', zorder=1)

ax[0].set_title('Traffic Density vs. Travel Time\nin Metroville', fontsize=14)
ax[0].set_xlabel('Traffic Density (vehicles/km)', fontsize=12)
ax[0].set_ylabel('Travel Time (minutes)', fontsize=12)
ax[0].legend(title='Time of Day', loc='upper left', fontsize=9, frameon=False)
ax[0].grid(True, linestyle='--', alpha=0.5)

# Plot 2: Traffic Density vs. Average Speed
ax[1].plot(traffic_density_morning, avg_speed_morning, 'o-', color='red', label='Morning Rush Hour', linewidth=2)
ax[1].plot(traffic_density_midday, avg_speed_midday, 'o-', color='green', label='Midday', linewidth=2)
ax[1].plot(traffic_density_evening, avg_speed_evening, 'o-', color='blue', label='Evening Rush Hour', linewidth=2)

ax[1].set_title('Traffic Density vs. Average Speed', fontsize=14)
ax[1].set_xlabel('Traffic Density (vehicles/km)', fontsize=12)
ax[1].set_ylabel('Average Speed (km/min)', fontsize=12)
ax[1].legend(title='Time of Day', loc='upper right', fontsize=9, frameon=False)
ax[1].grid(True, linestyle='--', alpha=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()