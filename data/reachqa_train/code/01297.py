import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define age groups (in years) and corresponding average coffee consumption
age_groups = np.array([18, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
coffee_consumption = np.array([1.8, 2.5, 3.0, 3.6, 4.2, 3.9, 3.5, 3.0, 2.8, 2.3, 1.9, 1.4])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Scatter plot with colormap
scatter = ax.scatter(age_groups, coffee_consumption, c=coffee_consumption, cmap='viridis', s=100, edgecolor='black', label='Observed Data', alpha=0.8)

# Spline interpolation for a smooth fitting line
spline = make_interp_spline(age_groups, coffee_consumption, k=3)  # Cubic spline
age_range = np.linspace(min(age_groups), max(age_groups), 300)
smooth_line = spline(age_range)

# Plot the smooth fitting line with a gradient
ax.plot(age_range, smooth_line, color='red', linestyle='-', linewidth=2, label='Trend Line')

# Add title and labels, breaking title into lines if necessary
ax.set_title("Coffee Consumption Trends\nAcross Age Groups", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Age (years)", fontsize=12)
ax.set_ylabel("Average Cups of Coffee Per Day", fontsize=12)

# Add annotations for peak and minimum
max_idx = np.argmax(coffee_consumption)
min_idx = np.argmin(coffee_consumption)
ax.annotate('Peak', xy=(age_groups[max_idx], coffee_consumption[max_idx]), xytext=(age_groups[max_idx]+2, coffee_consumption[max_idx]+0.5),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkgreen')
ax.annotate('Minimum', xy=(age_groups[min_idx], coffee_consumption[min_idx]), xytext=(age_groups[min_idx]+2, coffee_consumption[min_idx]-0.5),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkred')

# Customize grid lines and tick marks
ax.grid(True, which='both', linestyle='--', alpha=0.6)
ax.minorticks_on()
ax.tick_params(axis='both', which='major', labelsize=10)

# Add a color bar
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Coffee Consumption Intensity', rotation=270, labelpad=15)

# Add a legend
ax.legend(loc='upper right', fontsize=10, frameon=True)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()