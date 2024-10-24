import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Hours of creative activities per week
creative_hours = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Happiness levels corresponding to creative hours
# These represent a trend where happiness increases with more creative activity
happiness_levels = np.array([30, 35, 40, 50, 55, 60, 68, 75, 82, 88, 90])

# Define a cubic fitting function to model the relationship
def cubic_fit(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

# Perform curve fitting to find the best-fit parameters
cubic_params, _ = curve_fit(cubic_fit, creative_hours, happiness_levels)

# Generate data for the smooth fitting curve
hours_range = np.linspace(min(creative_hours), max(creative_hours), 300)
fitting_curve = cubic_fit(hours_range, *cubic_params)

# Plotting the scatter chart with the fitting curve
plt.figure(figsize=(10, 6))
plt.scatter(
    creative_hours, happiness_levels,
    color='teal', label='Observed Data',
    alpha=0.8, edgecolors='k', s=100
)
plt.plot(
    hours_range, fitting_curve,
    color='orange', linestyle='-', linewidth=2, label='Cubic Fit Curve'
)
plt.title(
    "Impact of Creative Activities on\nHappiness Levels",
    fontsize=16, pad=20
)
plt.xlabel("Hours of Creative Activities per Week", fontsize=12)
plt.ylabel("Happiness Level (1 to 100)", fontsize=12)
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlim(min(creative_hours) - 1, max(creative_hours) + 1)
plt.ylim(20, 100)
plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.arange(20, 101, 10))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()