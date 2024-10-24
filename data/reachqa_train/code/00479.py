import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Data: Reading speed (words per minute) and comprehension score (out of 100)
reading_speeds = np.array([100, 120, 135, 150, 160, 170, 185, 190, 195, 200, 210, 215, 225, 230, 240])
comprehension_scores = np.array([70, 72, 74, 78, 80, 79, 83, 84, 85, 82, 86, 85, 88, 87, 89])

# Polynomial fit function
def polynomial_fit(x, a, b, c):
    return a * x ** 2 + b * x + c

# Calculate polynomial fit parameters
popt, _ = curve_fit(polynomial_fit, reading_speeds, comprehension_scores)

# Generate a smooth line over the reading speed range
x_line = np.linspace(min(reading_speeds), max(reading_speeds), 100)
y_line = polynomial_fit(x_line, *popt)

# Plot settings
plt.figure(figsize=(10, 6))

# Scatter plot of the data
plt.scatter(reading_speeds, comprehension_scores, color='teal', label='Students', s=100, alpha=0.75, edgecolor='black')

# Smooth fit line
plt.plot(x_line, y_line, color='coral', linestyle='--', linewidth=2, label='Trend Line (Polynomial Fit)')

# Titles and labels
plt.title("Correlation between Reading Speed and Comprehension", fontsize=14, pad=20)
plt.xlabel("Reading Speed (words per minute)", fontsize=12)
plt.ylabel("Comprehension Score (out of 100)", fontsize=12)

# Legend placement
plt.legend(loc='lower right', fontsize=10)

# Axis limits
plt.xlim(min(reading_speeds) - 10, max(reading_speeds) + 10)
plt.ylim(min(comprehension_scores) - 5, max(comprehension_scores) + 5)

# Grid and layout adjustments
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Show plot
plt.show()