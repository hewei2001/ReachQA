import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Define star ages in billions of years
star_ages = np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5])

# Define apparent magnitudes for stars corresponding to the ages
star_brightness = np.array([1.3, 1.7, 2.2, 2.5, 3.0, 3.4, 3.7, 4.1, 4.3, 4.6, 4.8])

# Smooth the scatter plot using a spline interpolation
x_smooth = np.linspace(star_ages.min(), star_ages.max(), 300)
spline = make_interp_spline(star_ages, star_brightness, k=3)
y_smooth = spline(x_smooth)

# Create the scatter plot with smooth fitting
plt.figure(figsize=(10, 6))
plt.scatter(star_ages, star_brightness, color='navy', s=100, edgecolor='white', zorder=5, label='Stars')
plt.plot(x_smooth, y_smooth, color='skyblue', lw=3, zorder=4, label='Smooth Fit')

# Customize the plot with title and labels
plt.title('Mapping the Stars: Stellar Brightness vs. Age\nin a Young Galaxy', fontsize=14, weight='bold', pad=20)
plt.xlabel('Star Age (Billion Years)', fontsize=12)
plt.ylabel('Apparent Magnitude\n(Lower is Brighter)', fontsize=12)
plt.gca().invert_yaxis()  # Invert y-axis since lower magnitude is brighter
plt.grid(True, linestyle='--', alpha=0.6)

# Add a legend
plt.legend(loc='upper left', fontsize=10)

# Automatically adjust layout to fit elements neatly
plt.tight_layout()

# Display the plot
plt.show()