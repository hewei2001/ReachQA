import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

# Data representing green space coverage and corresponding AQI values
green_space_coverage = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
average_aqi = np.array([80, 76, 71, 67, 64, 60, 57, 54, 52, 50])

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(green_space_coverage, average_aqi, color='forestgreen', edgecolor='black', s=100, alpha=0.7, label='Neighborhoods')

# Fit a smooth curve using spline interpolation
spline = interpolate.make_interp_spline(green_space_coverage, average_aqi)
smooth_curve_x = np.linspace(green_space_coverage.min(), green_space_coverage.max(), 300)
smooth_curve_y = spline(smooth_curve_x)

# Plot the smooth fitting curve
plt.plot(smooth_curve_x, smooth_curve_y, color='deepskyblue', linewidth=2, linestyle='-', label='Smooth Fit')

# Title and axis labels
plt.title("Impact of Urban Green Spaces on Air Quality in Metropolis City", fontsize=14, fontweight='bold', ha='center')
plt.xlabel("Green Space Coverage (%)", fontsize=12)
plt.ylabel("Average Air Quality Index (AQI)", fontsize=12)

# Adjust the y-axis to show lower AQI (better quality) at the top
plt.gca().invert_yaxis()

# Grid and legend
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper right', fontsize=10)

# Ensure the layout is neat
plt.tight_layout()

# Display the plot
plt.show()