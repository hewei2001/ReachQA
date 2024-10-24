import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define ocean depths (in meters) and corresponding jellyfish population density
depths = np.array([10, 30, 50, 100, 150, 200, 300, 400, 500, 600, 700, 800, 900])
jellyfish_density = np.array([15, 40, 55, 70, 45, 30, 20, 25, 35, 45, 40, 30, 20])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Scatter plot with a colormap that reflects population density
scatter = ax.scatter(depths, jellyfish_density, c=jellyfish_density, cmap='ocean', s=100, edgecolor='black', alpha=0.8, label='Observed Data')

# Spline interpolation for a smooth fitting line
spline = make_interp_spline(depths, jellyfish_density, k=3)  # Cubic spline for smoothness
depth_range = np.linspace(min(depths), max(depths), 300)
smooth_line = spline(depth_range)

# Plot the smooth fitting line
ax.plot(depth_range, smooth_line, color='blue', linestyle='-', linewidth=2, label='Density Trend Line')

# Add title and labels with multi-line title for better fit
ax.set_title("Jellyfish Population Density\nAcross Ocean Depths", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Ocean Depth (meters)", fontsize=12)
ax.set_ylabel("Jellyfish Population Density\n(per cubic meter)", fontsize=12)

# Customize grid lines and tick marks
ax.grid(True, which='both', linestyle='--', alpha=0.6)
ax.minorticks_on()
ax.tick_params(axis='both', which='major', labelsize=10)

# Add a color bar to represent jellyfish density
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Population Density', rotation=270, labelpad=15)

# Add a legend
ax.legend(loc='upper right', fontsize=10, frameon=True)

# Automatically adjust layout for optimal display
plt.tight_layout()

# Display the plot
plt.show()