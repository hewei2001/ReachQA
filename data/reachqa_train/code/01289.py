import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Original Data: Define star ages and corresponding apparent magnitudes
star_ages = np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5])
star_brightness = np.array([1.3, 1.7, 2.2, 2.5, 3.0, 3.4, 3.7, 4.1, 4.3, 4.6, 4.8])

# Smoothing the data using a spline interpolation
x_smooth = np.linspace(star_ages.min(), star_ages.max(), 300)
spline = make_interp_spline(star_ages, star_brightness, k=3)
y_smooth = spline(x_smooth)

# Theoretical Model Data: Exponential decay representing a hypothetical model
model_ages = np.linspace(star_ages.min(), star_ages.max(), 300)
model_brightness = 5 * np.exp(-0.2 * model_ages) + 1

# Plot Setup
plt.figure(figsize=(12, 8))

# Scatter plot with smooth fitting
plt.scatter(star_ages, star_brightness, color='navy', s=100, edgecolor='white', zorder=5, label='Observed Stars')
plt.plot(x_smooth, y_smooth, color='skyblue', lw=3, linestyle='-', zorder=4, label='Smooth Fit')

# Overlay line plot for the theoretical model
plt.plot(model_ages, model_brightness, color='tomato', lw=2, linestyle='--', zorder=3, label='Theoretical Model')

# Customize the plot
plt.title('Mapping the Stars: Stellar Brightness vs. Age in a Young Galaxy\nWith Theoretical Model', 
          fontsize=14, weight='bold', pad=20, ha='center')
plt.xlabel('Star Age (Billion Years)', fontsize=12)
plt.ylabel('Apparent Magnitude\n(Lower is Brighter)', fontsize=12)
plt.gca().invert_yaxis()  # Invert y-axis to show brighter stars at the top
plt.grid(True, linestyle='--', alpha=0.6)

# Annotations for special points where data and model diverge/converge
plt.annotate('Notable Divergence', xy=(5, 3.4), xytext=(6, 3.9), 
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

# Add a legend
plt.legend(loc='upper left', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()