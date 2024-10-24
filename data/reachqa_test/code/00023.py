import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Data: Average daily screen time (in hours) and academic performance score (out of 100)
screen_time = np.array([0.5, 1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9, 10])
academic_scores = np.array([85, 88, 87, 85, 83, 80, 75, 70, 68, 65, 60, 58])

# Polynomial function for fitting
def poly_fit(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

# Fit the polynomial model to the data
popt, _ = curve_fit(poly_fit, screen_time, academic_scores)
x_smooth = np.linspace(0, 10, 100)
smooth_fit = poly_fit(x_smooth, *popt)

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Scatter plot with color gradient
colors = np.linspace(0.2, 1, len(screen_time))
scatter = ax.scatter(screen_time, academic_scores, c=colors, cmap='viridis', edgecolor='black', s=100, label='Observed Data', zorder=3)

# Polynomial fit curve with style modification
ax.plot(x_smooth, smooth_fit, color='darkblue', linestyle='--', linewidth=2, label='Polynomial Fit', zorder=2)

# Highlight key points on the polynomial curve
max_idx = np.argmax(smooth_fit)
min_idx = np.argmin(smooth_fit)
ax.annotate('Max Fit', xy=(x_smooth[max_idx], smooth_fit[max_idx]), xytext=(x_smooth[max_idx] + 0.5, smooth_fit[max_idx] + 5),
            arrowprops=dict(facecolor='red', shrink=0.05), fontsize=10, color='red', zorder=4)
ax.annotate('Min Fit', xy=(x_smooth[min_idx], smooth_fit[min_idx]), xytext=(x_smooth[min_idx] + 0.5, smooth_fit[min_idx] - 10),
            arrowprops=dict(facecolor='green', shrink=0.05), fontsize=10, color='green', zorder=4)

# Setting labels and title
ax.set_title("The Digital Learning Curve:\nImpact of Screen Time on Academic Performance", fontsize=16, pad=20)
ax.set_xlabel("Average Daily Screen Time (hours)", fontsize=12)
ax.set_ylabel("Academic Performance Score (out of 100)", fontsize=12)

# Customizing grid and legend
ax.legend(loc='upper right', fontsize=10)
ax.grid(True, which='both', linestyle='--', alpha=0.7, zorder=1)
ax.minorticks_on()  # Add minor ticks for more granularity

# Automatically adjust the layout
plt.tight_layout()

# Show plot
plt.show()