import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Define years (2015 to 2025) and corresponding data
years = np.arange(2015, 2026)
wellness_breaks = np.array([10, 12, 15, 18, 21, 23, 26, 28, 30, 32, 35])
satisfaction_scores = np.array([60, 62, 66, 70, 73, 75, 78, 81, 83, 85, 87])

# Create a smooth line using B-spline interpolation
x_smooth = np.linspace(wellness_breaks.min(), wellness_breaks.max(), 300)
spl = make_interp_spline(wellness_breaks, satisfaction_scores, k=3)
y_smooth = spl(x_smooth)

# Set up the plot
plt.figure(figsize=(12, 8))

# Plot the scatter points with improved styling
plt.scatter(wellness_breaks, satisfaction_scores, color='steelblue', label='Observed Data', edgecolor='navy', alpha=0.8, s=100)

# Plot the smooth fitting line
plt.plot(x_smooth, y_smooth, color='crimson', linestyle='-', linewidth=2.5, label='Smooth Fit')

# Enhance axes with minor ticks and labels
plt.xticks(np.arange(8, 38, 2))
plt.yticks(np.arange(55, 91, 5))
plt.xlim(8, 37)
plt.ylim(55, 90)

# Add vertical and horizontal lines for emphasis
plt.axhline(y=80, color='gray', linestyle='--', linewidth=1.2, label='High Satisfaction Threshold')
plt.axvline(x=25, color='green', linestyle='--', linewidth=1.2, label='Ideal Break Minutes')

# Add annotations for specific data points
plt.annotate('Start of Trend', xy=(10, 60), xytext=(12, 58), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Peak Satisfaction', xy=(35, 87), xytext=(31, 85), arrowprops=dict(facecolor='black', shrink=0.05))

# Customize plot title and labels
plt.title('Wellness Breaks and Employee Satisfaction:\nA Decade of Improvement (2015-2025)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Wellness Breaks (Minutes Per Day)', fontsize=14, labelpad=10)
plt.ylabel('Employee Satisfaction Score (out of 100)', fontsize=14, labelpad=10)

# Add legend
plt.legend(loc='lower right', fontsize=11)

# Add grid lines for better readability
plt.grid(visible=True, linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()