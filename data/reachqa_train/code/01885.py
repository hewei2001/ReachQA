import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Years representing each decade
years = np.array([1850, 1860, 1870, 1880, 1890, 1900])

# Synthetic data for brush stroke styles in Impressionist paintings
stroke_boldness_A = np.array([60, 65, 70, 75, 78, 80])
light_capture_A = np.array([55, 58, 62, 68, 72, 75])

stroke_boldness_B = np.array([50, 54, 60, 67, 73, 78])
light_capture_B = np.array([45, 49, 56, 61, 66, 71])

# Additional synthetic data for texture complexity
texture_complexity_A = np.array([70, 72, 75, 78, 82, 85])
texture_complexity_B = np.array([65, 67, 69, 72, 76, 80])

# Smooth lines using spline interpolation
years_smooth = np.linspace(years.min(), years.max(), 300)

smooth_boldness_A = make_interp_spline(years, stroke_boldness_A, k=3)(years_smooth)
smooth_capture_A = make_interp_spline(years, light_capture_A, k=3)(years_smooth)
smooth_boldness_B = make_interp_spline(years, stroke_boldness_B, k=3)(years_smooth)
smooth_capture_B = make_interp_spline(years, light_capture_B, k=3)(years_smooth)

# Set up the plot with an additional bar chart overlay
fig, ax1 = plt.subplots(figsize=(12, 8))

# Scatter plots for the actual data points
ax1.scatter(years, stroke_boldness_A, color='blue', label='Technique A - Boldness', alpha=0.6, marker='o')
ax1.scatter(years, light_capture_A, color='cyan', label='Technique A - Capture', alpha=0.6, marker='s')
ax1.scatter(years, stroke_boldness_B, color='red', label='Technique B - Boldness', alpha=0.6, marker='^')
ax1.scatter(years, light_capture_B, color='orange', label='Technique B - Capture', alpha=0.6, marker='D')

# Smooth lines for the trends
ax1.plot(years_smooth, smooth_boldness_A, color='blue', linestyle='-', linewidth=2)
ax1.plot(years_smooth, smooth_capture_A, color='cyan', linestyle='-', linewidth=2)
ax1.plot(years_smooth, smooth_boldness_B, color='red', linestyle='-', linewidth=2)
ax1.plot(years_smooth, smooth_capture_B, color='orange', linestyle='-', linewidth=2)

# Create a bar chart overlay
width = 4  # Bar width for simplicity
ax2 = ax1.twinx()
ax2.bar(years - width/2, texture_complexity_A, width=width, color='purple', alpha=0.4, label='Technique A - Texture')
ax2.bar(years + width/2, texture_complexity_B, width=width, color='green', alpha=0.4, label='Technique B - Texture')

# Customize the plot
ax1.set_title("The Evolution of Brush Stroke Styles and Texture Complexity\nin Impressionist Paintings (1850-1900)",
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Stroke & Light Capture Metrics", fontsize=12)
ax2.set_ylabel("Texture Complexity", fontsize=12)

# Legends for both line plot and bar chart
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Grid, axis limits, and tight layout
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.set_xlim(1845, 1905)
ax1.set_ylim(40, 90)
ax2.set_ylim(60, 90)

plt.tight_layout()
plt.show()