import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Enhanced data for light intensity and corresponding growth rates, with additional data points and a new data group
light_intensity = np.linspace(50, 1000, 24)  # more data points
growth_rate_species_1 = np.array([2.1, 2.4, 2.8, 3.0, 3.2, 3.5, 3.8, 3.9, 4.0, 4.2, 4.3, 4.5, 
                                  4.5, 4.3, 4.2, 4.1, 3.9, 3.8, 3.5, 3.3, 3.1, 2.8, 2.5, 2.2])
growth_rate_species_2 = np.array([1.5, 1.8, 2.1, 2.3, 2.5, 2.7, 3.0, 3.2, 3.3, 3.6, 3.9, 4.0, 
                                  4.1, 4.0, 3.8, 3.6, 3.4, 3.1, 2.9, 2.7, 2.5, 2.3, 2.0, 1.7])

# Function for curve fitting (quadratic polynomial as an example)
def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the curve for both species
params_species_1, _ = curve_fit(quadratic, light_intensity, growth_rate_species_1)
params_species_2, _ = curve_fit(quadratic, light_intensity, growth_rate_species_2)

# Create a plot with multiple subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Plot for Species 1
ax1.scatter(light_intensity, growth_rate_species_1, color='forestgreen', s=100, edgecolor='black', alpha=0.7, label='Species 1')
ax1.plot(light_intensity, quadratic(light_intensity, *params_species_1), color='darkgreen', linestyle='--', label='Fit: Species 1')
ax1.set_title("Influence of Light Intensity on Plant Growth Rate\nSpecies 1", fontsize=14, weight='bold')
ax1.set_xlabel("Light Intensity (Lux)", fontsize=12)
ax1.set_ylabel("Growth Rate (cm/week)", fontsize=12)
ax1.legend(loc='upper right')
ax1.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Plot for Species 2
ax2.scatter(light_intensity, growth_rate_species_2, color='royalblue', s=100, edgecolor='black', alpha=0.7, label='Species 2')
ax2.plot(light_intensity, quadratic(light_intensity, *params_species_2), color='navy', linestyle='--', label='Fit: Species 2')
ax2.set_title("Influence of Light Intensity on Plant Growth Rate\nSpecies 2", fontsize=14, weight='bold')
ax2.set_xlabel("Light Intensity (Lux)", fontsize=12)
ax2.set_ylabel("Growth Rate (cm/week)", fontsize=12)
ax2.legend(loc='upper right')
ax2.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Improve the layout
plt.tight_layout()

# Show the complex chart
plt.show()