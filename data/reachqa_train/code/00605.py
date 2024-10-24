import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define the data: depth of excavation (in meters) and corresponding artifact ages (in years)
depths = np.array([0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.5, 9.0, 10.5, 12.0, 14.0, 16.0, 18.0])
artifact_ages = np.array([200, 350, 500, 750, 1300, 1600, 2100, 2700, 3200, 3700, 4200, 4800, 5300, 5900, 6500])

# Define a quadratic fitting function
def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

# Perform curve fitting
params, _ = curve_fit(quadratic_fit, depths, artifact_ages)

# Generate smooth line data for fitting
depth_range = np.linspace(min(depths), max(depths), 300)
fitted_ages = quadratic_fit(depth_range, *params)

# Plotting the scatter chart with smooth fitting
plt.figure(figsize=(12, 8))

# Scatter plot
plt.scatter(depths, artifact_ages, color='teal', label='Artifact Data Points', alpha=0.7, edgecolors='k')

# Plotting the fitted curve
plt.plot(depth_range, fitted_ages, color='darkorange', linestyle='-', linewidth=2, label='Quadratic Fit')

# Customize the plot with titles and labels
plt.title('Depth vs. Age of Artifacts at Anatolia Site\nExploring the Correlation of Excavation', fontsize=16, weight='bold', pad=15)
plt.xlabel('Depth of Excavation (meters)', fontsize=12)
plt.ylabel('Estimated Age of Artifacts (years)', fontsize=12)
plt.legend(loc='upper left', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

# Ensure layout is adjusted to fit elements within the figure
plt.tight_layout()

# Show the plot
plt.show()