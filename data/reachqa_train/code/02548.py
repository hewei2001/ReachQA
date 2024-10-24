import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

# Original dataset representing green space coverage and corresponding AQI values
green_space_coverage = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
average_aqi = np.array([80, 76, 71, 67, 64, 60, 57, 54, 52, 50])

# Additional data: percentage of urban population with access to green spaces
population_access = np.array([20, 30, 40, 50, 60, 65, 70, 80, 85, 90])

# Create the figure and axes
fig, ax1 = plt.subplots(figsize=(12, 7))

# Scatter plot for the original dataset
sc = ax1.scatter(green_space_coverage, average_aqi, color='forestgreen', edgecolor='black', s=100, alpha=0.7, label='Neighborhoods')

# Smooth curve fitting using spline interpolation
spline = interpolate.make_interp_spline(green_space_coverage, average_aqi)
smooth_curve_x = np.linspace(green_space_coverage.min(), green_space_coverage.max(), 300)
smooth_curve_y = spline(smooth_curve_x)
ax1.plot(smooth_curve_x, smooth_curve_y, color='deepskyblue', linewidth=2, linestyle='-', label='Smooth Fit')

# Invert y-axis for AQI
ax1.invert_yaxis()

# Dual y-axis for the additional bar plot
ax2 = ax1.twinx()
ax2.bar(green_space_coverage, population_access, color='lightcoral', alpha=0.5, width=3, label='Population Access (%)')

# Annotations for significant thresholds
for i in range(len(green_space_coverage)):
    if average_aqi[i] < 60:
        ax1.annotate('Good AQI', (green_space_coverage[i], average_aqi[i]), textcoords="offset points", xytext=(-10,-10), ha='center', fontsize=9, color='darkred')

# Titles and labels
title = "Impact of Urban Green Spaces on Air Quality and Accessibility"
ax1.set_title("\n".join([title[:35], title[35:]]), fontsize=14, fontweight='bold')
ax1.set_xlabel("Green Space Coverage (%)", fontsize=12)
ax1.set_ylabel("Average Air Quality Index (AQI)", fontsize=12)
ax2.set_ylabel("Population Access to Green Spaces (%)", fontsize=12)

# Grid and legends
ax1.grid(True, linestyle='--', alpha=0.6)
fig.legend(loc='upper left', bbox_to_anchor=(0.12, 0.95), fontsize=10, ncol=2)

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plot
plt.show()