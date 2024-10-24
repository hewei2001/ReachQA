import numpy as np
import matplotlib.pyplot as plt

# Time segments of the day
time_segments = ['Early Morning', 'Morning', 'Afternoon', 'Evening', 'Night']

# Artificial screen time data in hours for each device category
smartphones = np.array([1, 2.5, 3, 2, 1.5])
tablets = np.array([0.5, 1, 1.5, 1, 0.5])
laptops = np.array([0.5, 1.5, 2, 2.5, 1])
desktops = np.array([0.2, 0.5, 1, 1.5, 0.8])

# Calculate cumulative values for stacking the areas
cumulative_tablets = smartphones + tablets
cumulative_laptops = cumulative_tablets + laptops
cumulative_desktops = cumulative_laptops + desktops

# Total screen time irrespective of device
total_screen_time = cumulative_desktops

# Average screen time per device category (example data)
avg_device_usage = np.array([
    np.mean(smartphones),
    np.mean(tablets),
    np.mean(laptops),
    np.mean(desktops)
])
device_labels = ['Smartphones', 'Tablets', 'Laptops', 'Desktops']

# Creating subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

# Plotting the area chart
ax1 = axes[0]
ax1.fill_between(time_segments, smartphones, label='Smartphones', color='#ff9999', alpha=0.7)
ax1.fill_between(time_segments, smartphones, cumulative_tablets, label='Tablets', color='#66b3ff', alpha=0.7)
ax1.fill_between(time_segments, cumulative_tablets, cumulative_laptops, label='Laptops', color='#99ff99', alpha=0.7)
ax1.fill_between(time_segments, cumulative_laptops, cumulative_desktops, label='Desktops', color='#ffcc99', alpha=0.7)
ax1.set_title('The Digital Landscape:\nScreen Time Across Devices in 2023', fontsize=16, fontweight='bold')
ax1.set_xlabel('Time of Day', fontsize=12)
ax1.set_ylabel('Hours of Screen Time', fontsize=12)
ax1.legend(loc='upper left', fontsize=10, title='Devices')
ax1.set_xticks(np.arange(len(time_segments)))
ax1.set_xticklabels(time_segments, rotation=30, ha='right', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.5)

# Plotting the bar chart for average device usage
ax2 = axes[1]
ax2.bar(device_labels, avg_device_usage, color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'], alpha=0.7)
ax2.set_title('Average Device Usage', fontsize=16, fontweight='bold')
ax2.set_xlabel('Device Category', fontsize=12)
ax2.set_ylabel('Average Hours', fontsize=12)
ax2.set_ylim(0, max(avg_device_usage) + 1)
for i, value in enumerate(avg_device_usage):
    ax2.text(i, value + 0.1, f"{value:.1f}", ha='center', va='bottom', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()