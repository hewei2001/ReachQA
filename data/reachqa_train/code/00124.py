import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Extended generational data points (age, tech-savviness score)
ages = np.array([
    75, 80, 85, 60, 65, 70, 50, 55, 30, 35, 40, 45, 20, 22, 25, 8, 10, 15
])
tech_savviness_scores = np.array([
    20, 18, 15, 32, 35, 28, 55, 58, 78, 75, 70, 65, 85, 88, 82, 50, 55, 60
])

# Define multiple fitting functions
def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

def cubic_fit(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

# Perform curve fitting for both quadratic and cubic
quad_params, _ = curve_fit(quadratic_fit, ages, tech_savviness_scores)
cubic_params, _ = curve_fit(cubic_fit, ages, tech_savviness_scores)

# Generate smooth line data for fitting
age_range = np.linspace(min(ages), max(ages), 300)
quad_scores = quadratic_fit(age_range, *quad_params)
cubic_scores = cubic_fit(age_range, *cubic_params)

# Plotting the scatter chart with subplots
fig, ax = plt.subplots(1, 2, figsize=(18, 8))

# Scatter plot with quadratic fit
ax[0].scatter(ages, tech_savviness_scores, color='purple', label='Scores', alpha=0.7, edgecolors='k')
ax[0].plot(age_range, quad_scores, color='orange', linestyle='--', linewidth=2, label='Quadratic Fit')
ax[0].set_title("Tech Savviness: Quadratic Fit Analysis", fontsize=14)
ax[0].set_xlabel("Age")
ax[0].set_ylabel("Tech-Savviness Score")
ax[0].legend(loc='upper left')
ax[0].grid(True, linestyle='--', alpha=0.6)

# Scatter plot with cubic fit
ax[1].scatter(ages, tech_savviness_scores, color='green', label='Scores', alpha=0.7, edgecolors='k')
ax[1].plot(age_range, cubic_scores, color='blue', linestyle='--', linewidth=2, label='Cubic Fit')
ax[1].set_title("Tech Savviness: Cubic Fit Analysis", fontsize=14)
ax[1].set_xlabel("Age")
ax[1].set_ylabel("Tech-Savviness Score")
ax[1].legend(loc='upper left')
ax[1].grid(True, linestyle='--', alpha=0.6)

# Annotate the plots with generational labels
generations = ['Silent', 'Silent', 'Silent', 'Boomers', 'Boomers', 'Boomers',
               'Gen X', 'Gen X', 'Millennials', 'Millennials', 'Millennials',
               'Millennials', 'Gen Z', 'Gen Z', 'Gen Z', 'Gen Alpha', 'Gen Alpha', 'Gen Alpha']

for age, score, gen in zip(ages, tech_savviness_scores, generations):
    ax[0].text(age + 0.5, score + 0.5, gen, fontsize=8)
    ax[1].text(age + 0.5, score + 0.5, gen, fontsize=8)

# Additional subplot layout adjustments
plt.tight_layout()

# Show the plots
plt.show()