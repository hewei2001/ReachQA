import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the years and corresponding acidity levels (pH) for coffee beans
years = np.array([1990, 1995, 2000, 2005, 2010, 2015, 2020])
acidity_levels = np.array([5.0, 5.1, 5.3, 5.5, 5.4, 5.3, 5.1])

# Create a smooth curve using spline interpolation
years_new = np.linspace(years.min(), years.max(), 300)
spl = make_interp_spline(years, acidity_levels, k=3)
acidity_smooth = spl(years_new)

# Initialize the plot
plt.figure(figsize=(12, 6))

# Plot the scatter points for the recorded pH levels
plt.scatter(years, acidity_levels, color='chocolate', label='Recorded pH Levels', zorder=2)

# Plot the smooth trend line fitting
plt.plot(years_new, acidity_smooth, color='saddlebrown', linestyle='-', linewidth=2, label='Trend Line', zorder=1)

# Annotate significant points on the scatter chart with pH values
for i, year in enumerate(years):
    plt.annotate(f"{acidity_levels[i]}", (year, acidity_levels[i]), textcoords="offset points", xytext=(-10, 10), ha='center')

# Add labels, title, and legend
plt.xlabel('Year', fontsize=12)
plt.ylabel('pH Level', fontsize=12)
plt.title('The Evolution of Coffee Bean Acidity Levels\nOver Time (1990 - 2020)', fontsize=14, fontweight='bold')
plt.legend(loc='upper right', title='Data Points')

# Add a grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Set limits to the y-axis for clarity and better visualization
plt.ylim(4.9, 5.6)

# Automatically adjust layout to prevent overlap and ensure clarity
plt.tight_layout()

# Display the plot
plt.show()