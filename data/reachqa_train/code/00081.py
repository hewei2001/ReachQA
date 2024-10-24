import matplotlib.pyplot as plt
import numpy as np

# Define hours of the day (0 to 23)
hours = np.array(range(24))

# Define time spent (in minutes) on each activity during these hours
social_media = np.array([10, 8, 6, 5, 5, 6, 12, 15, 18, 22, 25, 28, 30, 35, 30, 28, 25, 20, 15, 10, 8, 10, 15, 12])
online_shopping = np.array([2, 2, 1, 1, 1, 1, 1, 3, 5, 8, 12, 15, 20, 25, 30, 35, 40, 50, 45, 40, 30, 25, 20, 15])
streaming = np.array([5, 4, 3, 2, 2, 3, 5, 7, 10, 12, 15, 20, 22, 25, 28, 30, 40, 50, 55, 60, 55, 50, 40, 30])

# Plotting the scatter chart
fig, ax = plt.subplots(figsize=(12, 6))

# Create scatter plots for each activity
ax.scatter(hours, social_media, color='blue', label='Social Media', alpha=0.6, edgecolors='w', s=100)
ax.scatter(hours, online_shopping, color='green', label='Online Shopping', alpha=0.6, edgecolors='w', s=100)
ax.scatter(hours, streaming, color='red', label='Streaming', alpha=0.6, edgecolors='w', s=100)

# Set titles and labels
ax.set_title('Smartphone Usage Patterns\nAcross Daily Activities', fontsize=16)
ax.set_xlabel('Hour of the Day', fontsize=12)
ax.set_ylabel('Time Spent (minutes)', fontsize=12)

# Customize x-ticks to display every hour
ax.set_xticks(hours)
ax.set_xticklabels([f'{h}:00' for h in hours], rotation=45)

# Add grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Add legend to differentiate activities
ax.legend(title='Activity', loc='upper left')

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()