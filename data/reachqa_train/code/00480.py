import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Expanded Data: Reading speed (words per minute) and comprehension score (out of 100)
reading_speeds = np.array([100, 110, 120, 130, 135, 140, 150, 160, 170, 180, 185, 190, 195, 200, 210, 215, 220, 225, 230, 240, 250, 260, 270])
comprehension_scores = np.array([68, 70, 72, 71, 74, 76, 78, 80, 79, 81, 83, 85, 84, 82, 86, 87, 89, 88, 87, 90, 91, 92, 93])

# Additional Data Group for Complexity: Age groups
age_groups = np.array(['Teen'] * 8 + ['Adult'] * 8 + ['Senior'] * 7)

# Higher-Degree Polynomial Fit Function
def polynomial_fit(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d

# Calculate polynomial fit parameters
popt, _ = curve_fit(polynomial_fit, reading_speeds, comprehension_scores)

# Generate a smooth line over the reading speed range
x_line = np.linspace(min(reading_speeds), max(reading_speeds), 200)
y_line = polynomial_fit(x_line, *popt)

# Plot settings
plt.figure(figsize=(14, 8))

# Scatter plot of the data with different age groups
unique_groups = np.unique(age_groups)
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
for group, color in zip(unique_groups, colors):
    idx = age_groups == group
    plt.scatter(reading_speeds[idx], comprehension_scores[idx], color=color, label=f'Students ({group})', s=100, alpha=0.75, edgecolor='black')

# Polynomial fit line
plt.plot(x_line, y_line, color='coral', linestyle='--', linewidth=3, label='Cubic Polynomial Fit')

# Titles and labels
plt.title("Analyzing Reading Speed and Comprehension Across Age Groups\n(Polynomial Fit with Multiple Data Sets)", fontsize=16, pad=20)
plt.xlabel("Reading Speed (words per minute)", fontsize=13)
plt.ylabel("Comprehension Score (out of 100)", fontsize=13)

# Legend placement
plt.legend(loc='lower right', fontsize=12, edgecolor='black')

# Axis limits
plt.xlim(min(reading_speeds) - 20, max(reading_speeds) + 20)
plt.ylim(min(comprehension_scores) - 10, max(comprehension_scores) + 10)

# Display R-squared value for the polynomial fit
residuals = comprehension_scores - polynomial_fit(reading_speeds, *popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((comprehension_scores - np.mean(comprehension_scores))**2)
r_squared = 1 - (ss_res / ss_tot)
plt.text(max(reading_speeds) - 50, min(comprehension_scores) + 5, f'R-squared: {r_squared:.2f}', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

# Grid and layout adjustments
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Show plot
plt.show()