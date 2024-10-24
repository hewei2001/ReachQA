import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the years and corresponding acidity levels (pH) for coffee beans
years = np.array([1990, 1995, 2000, 2005, 2010, 2015, 2020])
acidity_levels = np.array([5.0, 5.1, 5.3, 5.5, 5.4, 5.3, 5.1])

# Define the additional dataset: Average temperature (°C)
avg_temperatures = np.array([22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0])

# Create a smooth curve using spline interpolation for acidity levels
years_new = np.linspace(years.min(), years.max(), 300)
spl = make_interp_spline(years, acidity_levels, k=3)
acidity_smooth = spl(years_new)

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(14, 7))

# Plot the scatter points and trend line for acidity levels
ax1.scatter(years, acidity_levels, color='chocolate', label='Recorded pH Levels', zorder=3)
ax1.plot(years_new, acidity_smooth, color='saddlebrown', linestyle='-', linewidth=2, label='pH Trend Line', zorder=2)

# Set labels and limits for the primary y-axis (acidity levels)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('pH Level', fontsize=12, color='saddlebrown')
ax1.tick_params(axis='y', labelcolor='saddlebrown')
ax1.set_ylim(4.9, 5.6)

# Create a secondary y-axis for temperature data
ax2 = ax1.twinx()
ax2.bar(years, avg_temperatures, width=3, color='skyblue', alpha=0.6, label='Avg Temperature (°C)', zorder=1)
ax2.set_ylabel('Average Temperature (°C)', fontsize=12, color='skyblue')
ax2.tick_params(axis='y', labelcolor='skyblue')
ax2.set_ylim(21, 26)

# Add annotations for recorded pH levels
for i, year in enumerate(years):
    ax1.annotate(f"{acidity_levels[i]}", (year, acidity_levels[i]), textcoords="offset points", xytext=(-10, 10), ha='center')

# Add titles and legends
plt.title('The Evolution of Coffee Bean Acidity Levels and Temperature\nOver Time (1990 - 2020)', fontsize=14, fontweight='bold')
fig.legend(loc='upper left', bbox_to_anchor=(0.15, 0.85), title='Data Points')

# Add grids to improve readability
ax1.grid(True, linestyle='--', alpha=0.6)
ax2.grid(False)  # Disable secondary grid

# Ensure the layout is optimal and elements do not overlap
fig.tight_layout()

# Display the plot
plt.show()