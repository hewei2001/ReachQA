import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Latitudes (from equator to poles)
latitudes = np.array([0, 15, 30, 45, 60, 75, 90])

# Light intensity data for each planet
mars_intensity = np.array([120, 110, 90, 70, 55, 40, 30])
venus_intensity = np.array([80, 85, 80, 75, 70, 60, 50])
jupiter_intensity = np.array([70, 65, 60, 55, 50, 40, 30])

# Create smooth lines for the scatter plot using spline interpolation
mars_spline = make_interp_spline(latitudes, mars_intensity)
venus_spline = make_interp_spline(latitudes, venus_intensity)
jupiter_spline = make_interp_spline(latitudes, jupiter_intensity)

# New latitude values for smooth lines
latitudes_new = np.linspace(0, 90, 300)

mars_smooth = mars_spline(latitudes_new)
venus_smooth = venus_spline(latitudes_new)
jupiter_smooth = jupiter_spline(latitudes_new)

# Setup the plot
plt.figure(figsize=(14, 8))

# Scatter plot for each planet
plt.scatter(latitudes, mars_intensity, color='red', label='Mars', s=100, edgecolor='black')
plt.scatter(latitudes, venus_intensity, color='orange', label='Venus', s=100, edgecolor='black')
plt.scatter(latitudes, jupiter_intensity, color='blue', label='Jupiter', s=100, edgecolor='black')

# Smooth line plot
plt.plot(latitudes_new, mars_smooth, color='red', linestyle='-', linewidth=2, alpha=0.7)
plt.plot(latitudes_new, venus_smooth, color='orange', linestyle='-', linewidth=2, alpha=0.7)
plt.plot(latitudes_new, jupiter_smooth, color='blue', linestyle='-', linewidth=2, alpha=0.7)

# Add titles and labels
plt.title('Galactic Habitats: Exploring Light Intensity\nAcross Planetary Surfaces in 2250', fontsize=16, fontweight='bold')
plt.xlabel('Latitude (degrees)', fontsize=12)
plt.ylabel('Light Intensity (arbitrary units)', fontsize=12)

# Customize ticks and grid
plt.xticks(np.arange(0, 91, step=15))
plt.yticks(np.arange(20, 131, step=10))
plt.grid(alpha=0.3, linestyle='--')

# Add a legend
plt.legend(title='Planetary Surfaces', fontsize=10, loc='upper right', edgecolor='gray')

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()