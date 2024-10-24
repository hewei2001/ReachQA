import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Expanded dataset with multiple categories
green_space_percentage = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
aqi_values_region1 = np.array([150, 140, 130, 120, 110, 100, 90, 85, 80, 70, 65, 50])
aqi_values_region2 = np.array([160, 150, 135, 125, 115, 105, 95, 88, 82, 75, 70, 55])

# Scatter plot with two data groups
fig, ax = plt.subplots(figsize=(12, 8))
ax.scatter(green_space_percentage, aqi_values_region1, color='darkgreen', alpha=0.7, s=100, label='Region 1')
ax.scatter(green_space_percentage, aqi_values_region2, color='navy', alpha=0.7, s=100, label='Region 2')

# Smooth line fitting for both regions
x_smooth = np.linspace(green_space_percentage.min(), green_space_percentage.max(), 300)
spline1 = make_interp_spline(green_space_percentage, aqi_values_region1, k=3)
spline2 = make_interp_spline(green_space_percentage, aqi_values_region2, k=3)
y_smooth1 = spline1(x_smooth)
y_smooth2 = spline2(x_smooth)

# Plot smooth fitted lines
ax.plot(x_smooth, y_smooth1, color='limegreen', linestyle='--', linewidth=2, label='Fitted Curve - Region 1')
ax.plot(x_smooth, y_smooth2, color='blue', linestyle='-.', linewidth=2, label='Fitted Curve - Region 2')

# Additional mathematical line (theoretical model)
theory_line = 200 - 3 * x_smooth ** 0.5
ax.plot(x_smooth, theory_line, color='red', linestyle=':', linewidth=2, label='Theoretical Model')

# Add title, labels, and legend
ax.set_title('Impact of Urban Green Spaces on Air Quality\nComparison Between Regions', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Percentage of Green Space (%)', fontsize=12)
ax.set_ylabel('Air Quality Index (AQI)', fontsize=12)
ax.legend(title='Legend', fontsize=10, loc='upper right')

# Invert y-axis to show better air quality (lower AQI) at the top
ax.invert_yaxis()

# Add grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout for better appearance
plt.tight_layout()

# Display the plot
plt.show()