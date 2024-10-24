import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Define years (2015 to 2025)
years = np.arange(2015, 2026)

# Number of wellness break minutes per day
wellness_breaks = np.array([10, 12, 15, 18, 21, 23, 26, 28, 30, 32, 35])

# Corresponding employee satisfaction scores (out of 100)
satisfaction_scores = np.array([60, 62, 66, 70, 73, 75, 78, 81, 83, 85, 87])

# Create a smooth line using B-spline interpolation
x_smooth = np.linspace(wellness_breaks.min(), wellness_breaks.max(), 300)
spl = make_interp_spline(wellness_breaks, satisfaction_scores, k=3)  # B-spline with degree 3
y_smooth = spl(x_smooth)

# Set up the plot
plt.figure(figsize=(10, 6))

# Plot the scatter points
plt.scatter(wellness_breaks, satisfaction_scores, color='mediumorchid', label='Observed Data', edgecolor='black', alpha=0.7, s=100)

# Plot the smooth fitting line
plt.plot(x_smooth, y_smooth, color='darkorange', linestyle='-', linewidth=2, label='Smooth Fit')

# Customize the plot
plt.title('Wellness Breaks and Employee Satisfaction:\nA Decade of Improvement (2015-2025)', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Wellness Breaks (Minutes Per Day)', fontsize=12, labelpad=10)
plt.ylabel('Employee Satisfaction Score (out of 100)', fontsize=12, labelpad=10)
plt.xlim(8, 37)
plt.ylim(55, 90)

# Add a legend
plt.legend(loc='lower right', fontsize=10)

# Add grid lines
plt.grid(visible=True, linestyle='--', alpha=0.5)

# Adjust layout to fit elements
plt.tight_layout()

# Display the plot
plt.show()