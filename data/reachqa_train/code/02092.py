import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data: Green space increase (% increase) and air quality improvement (Index improvement)
green_space_increase = np.array([5, 12, 18, 24, 30, 35, 40, 45, 50, 55, 60])
air_quality_improvement = np.array([2, 4, 7, 10, 12, 15, 18, 22, 25, 28, 30])

# Generate smooth curve using spline interpolation
x_new = np.linspace(green_space_increase.min(), green_space_increase.max(), 300)
spl = make_interp_spline(green_space_increase, air_quality_improvement, k=3)
y_smooth = spl(x_new)

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))
ax.scatter(green_space_increase, air_quality_improvement, color='forestgreen', s=100, alpha=0.6, edgecolor='black', label='District Data Points')
ax.plot(x_new, y_smooth, color='dodgerblue', linewidth=2, linestyle='--', label='Smooth Trend Line')

# Add labels and title
plt.title("Greenfield City's Urban Green Spaces and\nAir Quality Improvement (2010-2020)", fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Green Space Increase (%)', fontsize=12, labelpad=10)
plt.ylabel('Air Quality Improvement (Index Points)', fontsize=12, labelpad=10)

# Add legend
plt.legend(loc='upper left', fontsize=12)

# Enhance grid for better readability
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Annotate a point of interest
highlight_idx = 7
ax.annotate('Notable Improvement',
            xy=(green_space_increase[highlight_idx], air_quality_improvement[highlight_idx]),
            xytext=(green_space_increase[highlight_idx] - 10, air_quality_improvement[highlight_idx] + 5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, ha='center', va='bottom')

# Adjust layout for better visibility and avoid overlap
plt.tight_layout()

# Display the chart
plt.show()