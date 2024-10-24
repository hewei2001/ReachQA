import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the percentage of green space in various urban areas
green_space_percentage = np.array([5, 10, 15, 20, 25, 30, 35, 40, 50, 60])

# Define the corresponding Air Quality Index (AQI) values for these urban areas
# Lower AQI indicates better air quality
aqi_values = np.array([150, 140, 120, 110, 100, 90, 85, 75, 65, 50])

# Scatter plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(green_space_percentage, aqi_values, color='darkgreen', alpha=0.7, s=100, label='Observed Data')

# Smooth line fitting
x_smooth = np.linspace(green_space_percentage.min(), green_space_percentage.max(), 300)
spline = make_interp_spline(green_space_percentage, aqi_values, k=3)
y_smooth = spline(x_smooth)

# Plot the smooth fitted line
ax.plot(x_smooth, y_smooth, color='limegreen', linestyle='--', linewidth=2, label='Fitted Curve')

# Add title, labels, and legend
ax.set_title('Impact of Urban Green Spaces on Air Quality', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Percentage of Green Space (%)', fontsize=12)
ax.set_ylabel('Air Quality Index (AQI)', fontsize=12)
ax.legend(title='Legend', fontsize=10, loc='upper right')

# Invert the y-axis to show better air quality (lower AQI) at the top
ax.invert_yaxis()

# Add grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout for better appearance
plt.tight_layout()

# Display the plot
plt.show()