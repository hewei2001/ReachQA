import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Define latitudes from equator to poles
latitudes = np.array([0, 15, 30, 45, 60, 75, 90])

# Light intensity data for each planet with varying patterns
mars_intensity = 120 * np.exp(-0.03 * latitudes) + 10 * np.cos(np.radians(latitudes))
venus_intensity = 90 + 5 * np.sin(np.radians(latitudes)) - 0.5 * latitudes
jupiter_intensity = 85 - 0.4 * latitudes + 15 * np.exp(-0.05 * latitudes)
saturn_intensity = 100 * np.exp(-0.02 * latitudes) + 20 * np.sin(np.radians(latitudes / 2))

# Include error bars
errors = np.array([5, 4, 3, 3, 2, 2, 1])

# Smooth lines using spline interpolation
latitudes_new = np.linspace(0, 90, 300)
mars_spline = make_interp_spline(latitudes, mars_intensity)(latitudes_new)
venus_spline = make_interp_spline(latitudes, venus_intensity)(latitudes_new)
jupiter_spline = make_interp_spline(latitudes, jupiter_intensity)(latitudes_new)
saturn_spline = make_interp_spline(latitudes, saturn_intensity)(latitudes_new)

# Setup the plot
plt.figure(figsize=(16, 10))

# Scatter plot with error bars
plt.errorbar(latitudes, mars_intensity, yerr=errors, fmt='o', color='red', label='Mars', markersize=8, capsize=5)
plt.errorbar(latitudes, venus_intensity, yerr=errors, fmt='o', color='orange', label='Venus', markersize=8, capsize=5)
plt.errorbar(latitudes, jupiter_intensity, yerr=errors, fmt='o', color='blue', label='Jupiter', markersize=8, capsize=5)
plt.errorbar(latitudes, saturn_intensity, yerr=errors, fmt='o', color='green', label='Saturn', markersize=8, capsize=5)

# Smooth line plots
plt.plot(latitudes_new, mars_spline, color='red', linestyle='-', linewidth=2, alpha=0.7)
plt.plot(latitudes_new, venus_spline, color='orange', linestyle='-', linewidth=2, alpha=0.7)
plt.plot(latitudes_new, jupiter_spline, color='blue', linestyle='-', linewidth=2, alpha=0.7)
plt.plot(latitudes_new, saturn_spline, color='green', linestyle='-', linewidth=2, alpha=0.7)

# Add titles and labels
plt.title('Galactic Habitats: Exploring Light Intensity Across Planetary Surfaces\n A Comparative Study in 2250', fontsize=18, fontweight='bold')
plt.xlabel('Latitude (degrees)', fontsize=14)
plt.ylabel('Light Intensity (arbitrary units)', fontsize=14)

# Customize ticks and grid
plt.xticks(np.arange(0, 91, step=15))
plt.yticks(np.arange(20, 131, step=10))
plt.grid(alpha=0.3, linestyle='--')

# Add a legend
plt.legend(title='Planetary Surfaces', fontsize=12, loc='upper right', edgecolor='gray')

# Add annotations for significant features
max_mars_intensity = mars_intensity.max()
max_mars_latitude = latitudes[mars_intensity.argmax()]
plt.annotate('Mars Max', xy=(max_mars_latitude, max_mars_intensity), xytext=(max_mars_latitude+5, max_mars_intensity+5),
             arrowprops=dict(facecolor='red', shrink=0.05), fontsize=10)

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()