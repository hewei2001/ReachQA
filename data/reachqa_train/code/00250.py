import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define green space coverage (%) and corresponding temperature increases (°C)
green_space_percentage = np.array([70, 55, 30, 50, 80])
temperature_increase = np.array([1.5, 3.0, 4.5, 2.8, 1.0])

# Sort the data to ensure the x-values for interpolation are strictly increasing
sorted_indices = np.argsort(green_space_percentage)
green_space_percentage_sorted = green_space_percentage[sorted_indices]
temperature_increase_sorted = temperature_increase[sorted_indices]

# Interpolation for the fitting curve using spline
spline = make_interp_spline(green_space_percentage_sorted, temperature_increase_sorted, k=3)
smooth_gspace = np.linspace(green_space_percentage_sorted.min(), green_space_percentage_sorted.max(), 200)
smooth_temp = spline(smooth_gspace)

# Creating the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Scatter plot with varied marker styles based on temperature threshold
colors = ['forestgreen' if t < 3 else 'darkred' for t in temperature_increase_sorted]
sizes = [120, 150, 180, 130, 110]  # Vary the size for visual interest
ax.scatter(green_space_percentage_sorted, temperature_increase_sorted, color=colors, s=sizes, alpha=0.8, edgecolor='black', label='City Data Points')

# Plot the fitting curve
ax.plot(smooth_gspace, smooth_temp, color='darkorange', linestyle='-', linewidth=2.5, label='Fitting Curve')

# Fill the area under the curve to highlight it
ax.fill_between(smooth_gspace, smooth_temp, color='orange', alpha=0.1)

# Title and labels with enhanced styling
ax.set_title("Urban Growth Analysis:\nGreen Spaces vs. Urban Heat Islands", fontsize=18, weight='bold', ha='center')
ax.set_xlabel("Green Space Coverage (%)", fontsize=14, labelpad=10)
ax.set_ylabel("Temperature Increase (°C)", fontsize=14, labelpad=10)

# Axis customization
ax.set_xlim(20, 90)
ax.set_ylim(0, 5)
ax.set_xticks(np.arange(20, 91, 10))
ax.set_yticks(np.arange(0, 6, 1))
ax.grid(True, linestyle='--', alpha=0.6)

# Enhanced annotations with connectors
city_labels = ['City A', 'City B', 'City C', 'City D', 'City E']
for i, city in enumerate(city_labels):
    ax.annotate(city, (green_space_percentage_sorted[i], temperature_increase_sorted[i]), textcoords="offset points", xytext=(0,10),
                ha='center', fontsize=10, color='navy', arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

# Adding legend
ax.legend(loc='upper right', fontsize=12, frameon=True, shadow=True)

# Adjust layout
fig.tight_layout()

# Show the plot
plt.show()