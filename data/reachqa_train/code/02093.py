import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Original data: Green space increase (% increase) and air quality improvement (Index improvement)
green_space_increase = np.array([5, 12, 18, 24, 30, 35, 40, 45, 50, 55, 60])
air_quality_improvement = np.array([2, 4, 7, 10, 12, 15, 18, 22, 25, 28, 30])

# New data: Investment in green space infrastructure (in million dollars)
investment_infrastructure = np.array([3, 8, 15, 22, 35, 45, 50, 65, 75, 85, 90])

# Generate smooth curve using spline interpolation for the trend line
x_new = np.linspace(green_space_increase.min(), green_space_increase.max(), 300)
spl = make_interp_spline(green_space_increase, air_quality_improvement, k=3)
y_smooth = spl(x_new)

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 8))

# Scatter plot and smooth trend line for air quality improvement
ax1.scatter(green_space_increase, air_quality_improvement, color='forestgreen', s=100, alpha=0.6, edgecolor='black', label='District Data Points')
ax1.plot(x_new, y_smooth, color='dodgerblue', linewidth=2, linestyle='--', label='Smooth Trend Line')

# Bar plot for investment in green space infrastructure
ax2 = ax1.twinx()  # Create a secondary y-axis
ax2.bar(green_space_increase, investment_infrastructure, color='orange', alpha=0.4, width=3, label='Investment in Infrastructure (Million $)')

# Titles and labels
plt.title("Greenfield City's Urban Green Spaces, Air Quality Improvement\nand Infrastructure Investment (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Green Space Increase (%)', fontsize=12, labelpad=10)
ax1.set_ylabel('Air Quality Improvement (Index Points)', fontsize=12, labelpad=10)
ax2.set_ylabel('Investment in Infrastructure (Million $)', fontsize=12, labelpad=10)

# Legend
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=12)

# Annotate a point of interest on the air quality improvement line
highlight_idx = 7
ax1.annotate('Notable Improvement',
             xy=(green_space_increase[highlight_idx], air_quality_improvement[highlight_idx]),
             xytext=(green_space_increase[highlight_idx] - 10, air_quality_improvement[highlight_idx] + 5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, ha='center', va='bottom')

# Annotate a point of interest on the investment bars
investment_highlight_idx = 5
ax2.annotate('Increased Investment',
             xy=(green_space_increase[investment_highlight_idx], investment_infrastructure[investment_highlight_idx]),
             xytext=(green_space_increase[investment_highlight_idx] + 5, investment_infrastructure[investment_highlight_idx] + 10),
             arrowprops=dict(facecolor='darkorange', shrink=0.05),
             fontsize=10, ha='left', va='center')

# Enhance grid for better readability
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()