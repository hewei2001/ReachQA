import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Years representing each decade
years = np.array([1850, 1860, 1870, 1880, 1890, 1900])

# Synthetic data for brush stroke styles in Impressionist paintings
# Metrics for two different painting techniques
stroke_boldness_A = np.array([60, 65, 70, 75, 78, 80])
light_capture_A = np.array([55, 58, 62, 68, 72, 75])

stroke_boldness_B = np.array([50, 54, 60, 67, 73, 78])
light_capture_B = np.array([45, 49, 56, 61, 66, 71])

# Create smooth lines using spline interpolation
years_smooth = np.linspace(years.min(), years.max(), 300)

# Spline fits for the data
smooth_boldness_A = make_interp_spline(years, stroke_boldness_A, k=3)(years_smooth)
smooth_capture_A = make_interp_spline(years, light_capture_A, k=3)(years_smooth)

smooth_boldness_B = make_interp_spline(years, stroke_boldness_B, k=3)(years_smooth)
smooth_capture_B = make_interp_spline(years, light_capture_B, k=3)(years_smooth)

# Set up the plot
plt.figure(figsize=(12, 8))

# Scatter plots for the actual data points
plt.scatter(years, stroke_boldness_A, color='blue', label='Technique A - Boldness', alpha=0.6, marker='o')
plt.scatter(years, light_capture_A, color='cyan', label='Technique A - Capture', alpha=0.6, marker='s')
plt.scatter(years, stroke_boldness_B, color='red', label='Technique B - Boldness', alpha=0.6, marker='^')
plt.scatter(years, light_capture_B, color='orange', label='Technique B - Capture', alpha=0.6, marker='D')

# Smooth lines for the trends
plt.plot(years_smooth, smooth_boldness_A, color='blue', linestyle='-', linewidth=2)
plt.plot(years_smooth, smooth_capture_A, color='cyan', linestyle='-', linewidth=2)
plt.plot(years_smooth, smooth_boldness_B, color='red', linestyle='-', linewidth=2)
plt.plot(years_smooth, smooth_capture_B, color='orange', linestyle='-', linewidth=2)

# Customize the plot
plt.title("The Evolution of Brush Stroke Styles in Impressionist Paintings\n(1850-1900)",
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Metric Value", fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlim(1845, 1905)
plt.ylim(40, 85)

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()