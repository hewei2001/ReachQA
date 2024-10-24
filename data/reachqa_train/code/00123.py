import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Generational data points (age, tech-savviness score)
ages = np.array([60, 65, 70, 50, 55, 30, 35, 20, 22, 8])
tech_savviness_scores = np.array([30, 32, 28, 55, 58, 75, 78, 85, 88, 50])

# Define a smooth fitting function, e.g., a quadratic
def fitting_func(x, a, b, c):
    return a * x**2 + b * x + c

# Perform curve fitting
params, _ = curve_fit(fitting_func, ages, tech_savviness_scores)

# Generate smooth line data for fitting
age_range = np.linspace(min(ages), max(ages), 300)
smooth_scores = fitting_func(age_range, *params)

# Plotting the scatter chart
plt.figure(figsize=(12, 7))
plt.scatter(ages, tech_savviness_scores, color='purple', label='Individual Scores', alpha=0.7, edgecolors='k')
plt.plot(age_range, smooth_scores, color='orange', linestyle='--', linewidth=2, label='Trend Line')

# Annotate the plot with generational labels
for age, score, label in zip(ages, tech_savviness_scores, ['Boomers', 'Boomers', 'Boomers', 'Gen X', 'Gen X', 'Millennials', 'Millennials', 'Gen Z', 'Gen Z', 'Gen Alpha']):
    plt.text(age + 0.5, score + 0.5, label, fontsize=9)

# Title and labels
plt.title("Digital Footprints: The Evolution of Tech Savviness\nThrough Generations")
plt.xlabel("Age")
plt.ylabel("Tech-Savviness Score")
plt.legend(loc='upper left')

# Adding grid for clarity
plt.grid(True, linestyle='--', alpha=0.6)

# Ensure the layout fits well within the plot window
plt.tight_layout()

# Show the plot
plt.show()