import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the years for the analysis
years = np.arange(2023, 2033)

# Data for writers using AI tools (in thousands)
ai_writers = np.array([5, 12, 30, 70, 120, 200, 320, 500, 700, 1000])

# Data for productivity (average words written per month)
productivity = np.array([1200, 1500, 1800, 2300, 3000, 3700, 4400, 5000, 5800, 6500])

# Smoothing the scatter plot
years_smooth = np.linspace(years.min(), years.max(), 300)
ai_writers_smooth = make_interp_spline(years, ai_writers)(years_smooth)
productivity_smooth = make_interp_spline(years, productivity)(years_smooth)

# Create figure and axis
fig, ax1 = plt.subplots(figsize=(12, 6))

# Scatter plot for AI users
scatter1 = ax1.scatter(years, ai_writers, color='blue', label='Writers Using AI Tools (Thousands)', zorder=5, marker='o', s=100)
ax1.plot(years_smooth, ai_writers_smooth, color='blue', linestyle='--', alpha=0.7, zorder=4)
ax1.fill_between(years_smooth, 0, ai_writers_smooth, color='lightblue', alpha=0.3)

# Twin the axis for productivity
ax2 = ax1.twinx()
scatter2 = ax2.scatter(years, productivity, color='orange', label='Average Monthly Productivity (Words)', zorder=5, marker='^', s=100)
ax2.plot(years_smooth, productivity_smooth, color='orange', linestyle='--', alpha=0.7, zorder=4)
ax2.fill_between(years_smooth, 0, productivity_smooth, color='lightcoral', alpha=0.3)

# Set titles and labels
ax1.set_title("The Rise of AI in Creative Writing\nA Decade of Transformation", fontsize=16, weight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Writers Using AI Tools (in thousands)", fontsize=12, color='blue')
ax2.set_ylabel("Average Monthly Productivity (Words)", fontsize=12, color='orange')

# Customize ticks
ax1.tick_params(axis='y', labelcolor='blue')
ax2.tick_params(axis='y', labelcolor='orange')

# Annotations for key points
ax1.annotate('Major Increase', xy=(2030, 500), xytext=(2028, 600),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='blue')
ax2.annotate('High Productivity', xy=(2032, 6500), xytext=(2030, 6800),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='orange')

# Enhanced grid and legends
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
ax2.legend(loc='upper right', bbox_to_anchor=(0.9, 0.9))

# Adjust layout for clarity
plt.tight_layout()

# Show the plot
plt.show()