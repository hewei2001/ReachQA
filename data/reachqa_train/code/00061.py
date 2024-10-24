import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define star temperatures (in Kelvin) and corresponding luminosities (relative to the Sun's luminosity)
star_temperatures = np.array([3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500])
star_luminosities = np.array([0.2, 0.4, 0.6, 0.85, 1.0, 1.3, 1.8, 2.3, 3.2, 5.0])

# Interpolation for the fitting curve
spline = make_interp_spline(star_temperatures, star_luminosities, k=3)
smooth_temps = np.linspace(star_temperatures.min(), star_temperatures.max(), 200)
smooth_luminosities = spline(smooth_temps)

# Create the scatter plot
plt.figure(figsize=(12, 8))
plt.scatter(star_temperatures, star_luminosities, color='navy', s=100, alpha=0.7, edgecolor='black', label='Stars in Aurora')
plt.plot(smooth_temps, smooth_luminosities, color='tomato', linestyle='-', linewidth=2, label='Fitted Curve')

# Adding details to the plot
plt.title("Brightness Variation of Stars in\nConstellation 'Aurora'", fontsize=16, weight='bold')
plt.xlabel("Temperature (K)", fontsize=14, labelpad=10)
plt.ylabel("Luminosity (Relative to Sun)", fontsize=14, labelpad=10)
plt.xlim(2800, 7800)
plt.ylim(0, 5.5)
plt.legend(loc='upper left', fontsize=12, frameon=True, shadow=True)
plt.grid(True, linestyle='--', alpha=0.6)

# Ensure the layout is tidy and adjusted
plt.tight_layout()

# Display the plot
plt.show()