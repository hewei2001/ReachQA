import matplotlib.pyplot as plt
import numpy as np

# Define days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Define average traffic speeds for each day for multiple cities
average_speeds_city1 = np.array([45, 50, 47, 46, 40, 55, 52])
average_speeds_city2 = np.array([48, 53, 49, 47, 42, 57, 54])
average_speeds_city3 = np.array([44, 49, 46, 45, 39, 54, 51])

# Calculate speed ranges as an example of variance or potential standard deviation-like representation
speed_range_city1 = np.array([5, 4, 6, 5, 7, 4, 3])
speed_range_city2 = np.array([4, 5, 3, 6, 8, 5, 4])
speed_range_city3 = np.array([6, 3, 5, 6, 7, 6, 5])

# Set up the figure and subplots
fig, ax = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# Plot average speed for each city with error bars representing variability
ax[0].errorbar(days, average_speeds_city1, yerr=speed_range_city1, marker='o', linestyle='-', color='teal', linewidth=2, markersize=6, label='Green City', capsize=5)
ax[0].errorbar(days, average_speeds_city2, yerr=speed_range_city2, marker='s', linestyle='-', color='coral', linewidth=2, markersize=6, label='Blue City', capsize=5)
ax[0].errorbar(days, average_speeds_city3, yerr=speed_range_city3, marker='^', linestyle='-', color='olive', linewidth=2, markersize=6, label='Red City', capsize=5)

# Title and labels for the first subplot
ax[0].set_title('Traffic Flow Analysis: Speed and Variability\nAcross Multiple Cities', fontsize=14, fontweight='bold')
ax[0].set_ylabel('Average Speed (km/h)', fontsize=12)
ax[0].grid(True, linestyle='--', alpha=0.7)
ax[0].legend(loc='upper right', fontsize=10)

# Create synthetic data for traffic volume (hypothetical data for demonstration)
traffic_volume_city1 = np.array([3000, 3200, 3100, 3050, 2900, 3500, 3300])
traffic_volume_city2 = np.array([3100, 3300, 3150, 3100, 2950, 3600, 3400])
traffic_volume_city3 = np.array([3050, 3250, 3120, 3075, 2920, 3550, 3350])

# Plot traffic volume for each city
ax[1].plot(days, traffic_volume_city1, marker='o', linestyle='--', color='teal', linewidth=2, markersize=6, label='Green City')
ax[1].plot(days, traffic_volume_city2, marker='s', linestyle='--', color='coral', linewidth=2, markersize=6, label='Blue City')
ax[1].plot(days, traffic_volume_city3, marker='^', linestyle='--', color='olive', linewidth=2, markersize=6, label='Red City')

# Title and labels for the second subplot
ax[1].set_title('Traffic Volume Analysis During Peak Hours', fontsize=14, fontweight='bold')
ax[1].set_xlabel('Days of the Week', fontsize=12)
ax[1].set_ylabel('Traffic Volume (vehicles/hour)', fontsize=12)
ax[1].grid(True, linestyle='--', alpha=0.7)
ax[1].legend(loc='upper right', fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()