import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Extended dataset: Hours of creative and social activities per week
creative_hours = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
social_hours = np.array([2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7])

# Happiness levels corresponding to creative and social hours
happiness_levels = np.array([30, 33, 36, 48, 52, 60, 70, 80, 85, 89, 95])

# Polynomial fitting functions
def cubic_fit(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

# Perform curve fitting for both models
cubic_params, _ = curve_fit(cubic_fit, creative_hours, happiness_levels)
quadratic_params, _ = curve_fit(quadratic_fit, creative_hours, happiness_levels)

# Generate data for fitting curves
hours_range = np.linspace(min(creative_hours), max(creative_hours), 300)
cubic_curve = cubic_fit(hours_range, *cubic_params)
quadratic_curve = quadratic_fit(hours_range, *quadratic_params)

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))
ax.scatter(creative_hours, happiness_levels, color='teal', label='Observed Data',
           alpha=0.8, edgecolors='k', s=100)

# Plot fitting curves
ax.plot(hours_range, cubic_curve, color='orange', linestyle='-', linewidth=2, label='Cubic Fit Curve')
ax.plot(hours_range, quadratic_curve, color='purple', linestyle='--', linewidth=2, label='Quadratic Fit Curve')

# Add error bars to simulate real-world data variability
happiness_std = np.array([3, 4, 5, 5, 6, 5, 4, 3, 4, 3, 3])
ax.errorbar(creative_hours, happiness_levels, yerr=happiness_std, fmt='o', color='gray', alpha=0.5, label='Error Bars')

# Titles and labels
ax.set_title("Impact of Creative and Social Activities on\nHappiness Levels", fontsize=16, pad=20)
ax.set_xlabel("Hours of Creative Activities per Week", fontsize=12)
ax.set_ylabel("Happiness Level (1 to 100)", fontsize=12)
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_xlim(min(creative_hours) - 1, max(creative_hours) + 1)
ax.set_ylim(20, 100)
ax.set_xticks(np.arange(0, 11, 1))
ax.set_yticks(np.arange(20, 101, 10))

# Additional subplot to compare with social hours
ax2 = ax.twinx()
ax2.set_ylabel("Hours of Social Activities per Week", color='blue', fontsize=12)
ax2.plot(creative_hours, social_hours, color='blue', linestyle=':', linewidth=2, marker='s', label='Social Hours')
ax2.tick_params(axis='y', labelcolor='blue')

# Automatically adjust layout
fig.tight_layout()

# Display the plot
plt.show()