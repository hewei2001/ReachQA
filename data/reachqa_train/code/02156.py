import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define the data: Urban Population Density (people/km²) and Innovation Index (0-100)
population_density = np.array([1000, 2300, 1500, 3000, 1800, 2500, 2000, 3500, 2200, 2750, 3200, 3700, 2700])
innovation_index = np.array([65, 80, 75, 85, 72, 82, 78, 90, 77, 84, 87, 93, 85])

# Define a fitting function (logarithmic)
def fitting_function(x, a, b, c):
    return a * np.log(b * x) + c

# Fit the curve to the data
params, _ = curve_fit(fitting_function, population_density, innovation_index)

# Generate a smooth curve across the range of the data
x_smooth = np.linspace(min(population_density), max(population_density), 500)
y_smooth = fitting_function(x_smooth, *params)

# Create the plot
plt.figure(figsize=(12, 8))

# Scatter plot for the raw data
plt.scatter(population_density, innovation_index, color='blue', edgecolor='black', s=100, label='Cities', alpha=0.7)

# Plot the smooth fitting line
plt.plot(x_smooth, y_smooth, color='red', linewidth=2, label='Trend Line')

# Title and axis labels
plt.title("Visionary Paths:\nMapping the Pulse of Urban Innovation", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Urban Population Density (people/km²)", fontsize=12)
plt.ylabel("Innovation Index (0-100)", fontsize=12)

# Add a legend to distinguish between data points and the fitting line
plt.legend(loc='lower right', fontsize=10)

# Add a grid to improve readability
plt.grid(True, linestyle='--', linewidth=0.6, alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()