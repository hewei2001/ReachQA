import matplotlib.pyplot as plt
import numpy as np

# Define days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Define average traffic speeds (km/h) for each day
average_speeds = np.array([45, 50, 47, 46, 40, 55, 52])

# Set up the figure and plot the line chart
plt.figure(figsize=(12, 7))
plt.plot(days, average_speeds, marker='o', linestyle='-', color='teal', linewidth=2, markersize=8, label='Avg Speed')

# Annotate data points with average speeds
for i, speed in enumerate(average_speeds):
    plt.annotate(f'{speed} km/h', (days[i], speed), textcoords="offset points", xytext=(0, 10), ha='center')

# Title and labels
plt.title('Traffic Flow Analysis in Green City\nAverage Speed During Peak Hours', fontsize=14, fontweight='bold')
plt.xlabel('Days of the Week', fontsize=12)
plt.ylabel('Average Speed (km/h)', fontsize=12)

# Adding a grid
plt.grid(True, linestyle='--', alpha=0.7)

# Customize the y-axis limits
plt.ylim(35, 60)

# Add legend to the plot
plt.legend(loc='upper right', fontsize=10)

# Improve layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()