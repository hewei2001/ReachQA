import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define the data: depth of excavation (in meters) and corresponding artifact ages (in years)
depths = np.array([0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.5, 9.0, 10.5, 12.0, 14.0, 16.0, 18.0])
artifact_ages = np.array([200, 350, 500, 750, 1300, 1600, 2100, 2700, 3200, 3700, 4200, 4800, 5300, 5900, 6500])

# Define fitting functions
def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

def linear_fit(x, m, b):
    return m * x + b

# Perform curve fitting
quad_params, _ = curve_fit(quadratic_fit, depths, artifact_ages)
lin_params, _ = curve_fit(linear_fit, depths, artifact_ages)

# Generate smooth line data for fitting
depth_range = np.linspace(min(depths), max(depths), 300)
fitted_quadratic = quadratic_fit(depth_range, *quad_params)
fitted_linear = linear_fit(depth_range, *lin_params)

# Plot setup
fig, axs = plt.subplots(2, 1, figsize=(12, 12), sharex=True, gridspec_kw={'height_ratios': [3, 1]})

# Scatter plot and fitting curves
axs[0].scatter(depths, artifact_ages, color='teal', marker='o', label='Artifact Data Points', alpha=0.7, edgecolors='k')
axs[0].plot(depth_range, fitted_quadratic, color='darkorange', linestyle='-', linewidth=2, label='Quadratic Fit')
axs[0].plot(depth_range, fitted_linear, color='navy', linestyle='--', linewidth=2, label='Linear Fit')

# Annotations
for i in range(len(depths)):
    axs[0].annotate(f"{artifact_ages[i]}", (depths[i], artifact_ages[i]), textcoords="offset points", xytext=(5, -10), ha='center', fontsize=8, color='purple')

axs[0].set_title('Depth vs. Age of Artifacts at Anatolia Site\nExploring the Correlation of Excavation', fontsize=16, weight='bold')
axs[0].set_ylabel('Estimated Age of Artifacts (years)', fontsize=12)
axs[0].legend(loc='upper left', fontsize=10)
axs[0].grid(True, linestyle='--', alpha=0.6)

# Subplot for residuals
residuals_quad = artifact_ages - quadratic_fit(depths, *quad_params)
residuals_lin = artifact_ages - linear_fit(depths, *lin_params)

axs[1].scatter(depths, residuals_quad, color='darkorange', label='Quadratic Residuals', edgecolors='k')
axs[1].scatter(depths, residuals_lin, color='navy', label='Linear Residuals', edgecolors='k', marker='x')
axs[1].axhline(0, color='gray', linestyle='-', linewidth=0.8)
axs[1].set_xlabel('Depth of Excavation (meters)', fontsize=12)
axs[1].set_ylabel('Residuals', fontsize=12)
axs[1].legend(loc='upper left', fontsize=10)
axs[1].grid(True, linestyle='--', alpha=0.6)

# Adjust layout to fit elements within the figure
plt.tight_layout()

# Show the plot
plt.show()