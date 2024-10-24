import matplotlib.pyplot as plt
import numpy as np

# Define months, visibility data, and error
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
average_visibility = np.array([5, 7, 9, 8, 12, 10, 11, 13, 14, 12, 9, 7])
error = np.array([0.5, 0.7, 1.0, 0.8, 1.2, 1.0, 0.9, 1.1, 1.3, 1.0, 0.8, 0.6])

# New related data: Average Cloud Cover Percentage
average_cloud_cover = np.array([70, 65, 60, 55, 50, 45, 40, 35, 30, 50, 65, 75])

# Create figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the line with error bars for Average Visibility
ax1.errorbar(months, average_visibility, yerr=error, fmt='-o',
             ecolor='gray', elinewidth=2, capsize=5, color='blue', alpha=0.8,
             label='Average Visibility with Error')

# Set titles and labels for the primary axis
ax1.set_title("Galactic Watch Observatory:\nComet Lux Visibility and Cloud Cover Over a Year", 
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Month", fontsize=12)
ax1.set_ylabel("Visibility (arbitrary units)", fontsize=12, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Annotate interesting points on the visibility plot
ax1.annotate('Peak Visibility', xy=('September', 14), xytext=('August', 15),
             arrowprops=dict(facecolor='darkred', arrowstyle='->'), fontsize=10, color='darkred')
ax1.annotate('Lowest Visibility', xy=('January', 5), xytext=('February', 4),
             arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=10, color='blue')

# Create secondary y-axis for Average Cloud Cover
ax2 = ax1.twinx()
ax2.bar(months, average_cloud_cover, alpha=0.3, color='green', label='Average Cloud Cover (%)')
ax2.set_ylabel("Cloud Cover (%)", fontsize=12, color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Enhance readability
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
ax1.tick_params(axis='x', rotation=45)

# Add legends
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()