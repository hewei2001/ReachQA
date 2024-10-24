import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Data for CO2 levels (ppm) and corresponding plant growth rates (g/m²)
co2_levels = np.array([300, 320, 340, 360, 380, 400, 420, 440, 460, 480])
growth_rates = np.array([5, 10, 15, 20, 28, 35, 42, 47, 50, 52])

# Define a quadratic function for fitting
def poly_fit(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the data using the polynomial function
params, _ = curve_fit(poly_fit, co2_levels, growth_rates)

# Create a smooth line for the fitted curve
x_fit = np.linspace(min(co2_levels), max(co2_levels), 500)
y_fit = poly_fit(x_fit, *params)

# Set up the plot
plt.figure(figsize=(10, 6))

# Plot the scatter chart for observed data points
plt.scatter(co2_levels, growth_rates, color='green', label='Observed Growth Rates', s=100, alpha=0.8, edgecolor='k')

# Plot the smooth fitting curve
plt.plot(x_fit, y_fit, color='blue', linestyle='-', linewidth=2, label='Polynomial Fit')

# Configure plot title and axis labels
plt.title('CO2 Levels vs. Plant Growth Rates\nUnderstanding Atmospheric Effects on Photosynthesis', fontsize=14, fontweight='bold')
plt.xlabel('CO2 Levels (ppm)', fontsize=12)
plt.ylabel('Growth Rates (g/m²)', fontsize=12)

# Add a legend to distinguish data and fit
plt.legend(loc='upper left', fontsize=10)

# Annotate a significant trend in the plot
plt.annotate('Notable increase in growth efficiency', xy=(380, 28), xytext=(320, 35),
             arrowprops=dict(facecolor='red', arrowstyle='->', lw=1.5), fontsize=10, color='red')

# Enable grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the layout for optimal space usage
plt.tight_layout()

# Display the plot
plt.show()