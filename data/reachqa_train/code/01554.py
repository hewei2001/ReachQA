import matplotlib.pyplot as plt
import numpy as np

# Define years from 2010 to 2020
years = np.arange(2010, 2021)

# Artificial data representing percentage of time spent on different devices
desktops = np.array([50, 48, 45, 42, 38, 35, 32, 30, 28, 26, 24])
laptops = np.array([30, 32, 35, 38, 41, 43, 45, 46, 47, 48, 49])
tablets = np.array([5, 5, 5, 6, 7, 8, 10, 11, 12, 13, 14])
smartphones = 100 - (desktops + laptops + tablets)

# Additional data for average screen time per day in hours
average_screen_time = np.array([6, 6.2, 6.5, 6.8, 7.1, 7.4, 7.8, 8.2, 8.6, 9, 9.5])

# Set up the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Stack plot for device usage
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFDEAD']
ax1.stackplot(years, desktops, laptops, tablets, smartphones, labels=['Desktops', 'Laptops', 'Tablets', 'Smartphones'], colors=colors, alpha=0.85)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Percentage of Time Spent', fontsize=12, color='k')
ax1.set_title('Evolution of Device Usage and Average Screen Time\nin Remote Work Environments (2010-2020)', fontsize=16, weight='bold')

# Add grid for better readability
ax1.grid(alpha=0.3)

# Add a legend for the stack plot
ax1.legend(loc='upper left', title='Devices', fontsize=10)

# Secondary Y-axis for average screen time
ax2 = ax1.twinx()
ax2.plot(years, average_screen_time, color='purple', marker='o', linestyle='--', linewidth=2.5, label='Average Screen Time per Day')
ax2.set_ylabel('Average Screen Time (hours)', fontsize=12, color='purple')
ax2.tick_params(axis='y', labelcolor='purple')

# Add legend for the line plot
ax2.legend(loc='upper right', fontsize=10)

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()