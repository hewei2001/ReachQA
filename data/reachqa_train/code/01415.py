import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Original data for CO2 levels (ppm) and corresponding plant growth rates (g/m²)
co2_levels = np.array([300, 320, 340, 360, 380, 400, 420, 440, 460, 480])
growth_rates = np.array([5, 10, 15, 20, 28, 35, 42, 47, 50, 52])

# New related data: assumed average temperature (°C) influencing growth rates
temperatures = np.array([15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

# Define a quadratic function for fitting
def poly_fit(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the original data using the polynomial function
params, _ = curve_fit(poly_fit, co2_levels, growth_rates)

# Create a smooth line for the fitted curve
x_fit = np.linspace(min(co2_levels), max(co2_levels), 500)
y_fit = poly_fit(x_fit, *params)

# Set up the plot with two subplots
fig, ax = plt.subplots(1, 2, figsize=(16, 6))

# First subplot: Scatter plot with polynomial fit
ax[0].scatter(co2_levels, growth_rates, color='green', label='Observed Growth Rates', s=100, alpha=0.8, edgecolor='k')
ax[0].plot(x_fit, y_fit, color='blue', linestyle='-', linewidth=2, label='Polynomial Fit')

# Configure first subplot title and axis labels
ax[0].set_title('CO2 Levels vs. Plant Growth Rates\nUnderstanding Atmospheric Effects on Photosynthesis', fontsize=14, fontweight='bold')
ax[0].set_xlabel('CO2 Levels (ppm)', fontsize=12)
ax[0].set_ylabel('Growth Rates (g/m²)', fontsize=12)
ax[0].legend(loc='upper left', fontsize=10)
ax[0].annotate('Notable increase in growth efficiency', xy=(380, 28), xytext=(320, 35),
               arrowprops=dict(facecolor='red', arrowstyle='->', lw=1.5), fontsize=10, color='red')
ax[0].grid(True, linestyle='--', alpha=0.7)

# Second subplot: Bar chart for temperatures
ax[1].bar(temperatures, growth_rates, color='orange', alpha=0.8, label='Growth Rates by Temp')

# Configure second subplot title and axis labels
ax[1].set_title('Temperature Effects on Growth Rates', fontsize=14, fontweight='bold')
ax[1].set_xlabel('Average Temperature (°C)', fontsize=12)
ax[1].set_ylabel('Growth Rates (g/m²)', fontsize=12)
ax[1].legend(loc='upper left', fontsize=10)
ax[1].grid(True, linestyle='--', alpha=0.7)

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()