import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Asteroid diameters (in kilometers)
asteroid_diameters = np.array([0.5, 1.2, 0.8, 2.1, 3.5, 1.7, 2.8, 3.0, 4.5, 5.0, 2.9, 3.3, 1.1, 1.5, 4.0])

# Average distance from Earth during close approach (in millions of kilometers)
close_approach_distances = np.array([1.2, 2.4, 1.8, 3.0, 4.5, 2.7, 3.8, 3.9, 5.5, 6.0, 4.0, 3.7, 2.0, 2.8, 5.0])

# Define a polynomial function for fitting
def polynomial_fit(x, a, b, c):
    return a * x**2 + b * x + c

# Perform curve fitting to find the best-fit parameters
params, _ = curve_fit(polynomial_fit, asteroid_diameters, close_approach_distances)

# Generate a range of values for plotting the smooth curve
x_fit = np.linspace(min(asteroid_diameters), max(asteroid_diameters), 500)
y_fit = polynomial_fit(x_fit, *params)

# Create the scatter plot with a smooth fitting curve
plt.figure(figsize=(10, 6))

# Scatter plot of the asteroid data
plt.scatter(asteroid_diameters, close_approach_distances, color='darkcyan', edgecolor='k', s=100, label='Asteroid Data')

# Smooth fitting line
plt.plot(x_fit, y_fit, color='tomato', linewidth=2, linestyle='-', label='Polynomial Fit')

# Add title and labels
plt.title("Asteroid Close Approaches\nSize vs. Distance", fontsize=16, fontweight='bold')
plt.xlabel("Asteroid Diameter (km)", fontsize=12)
plt.ylabel("Average Distance from Earth (Million km)", fontsize=12)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Add legend
plt.legend(loc='upper left', fontsize=10)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Show plot
plt.show()