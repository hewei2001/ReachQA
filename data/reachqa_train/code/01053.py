import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Data representing hours of study and corresponding test scores
study_hours = np.array([2, 3, 4, 5, 6, 6.5, 7, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5,
                        12, 12.5, 13, 13.5, 14, 14.5, 15, 5, 4.5, 3.5, 6.8, 7.5, 9.2, 10.7, 12.3])
test_scores = np.array([55, 58, 62, 65, 67, 69, 70, 75, 78, 80, 82, 85, 87, 90, 92,
                        94, 95, 97, 98, 99, 100, 100, 66, 60, 59, 71, 73, 84, 89, 93])

# Define a quadratic model for fitting
def model(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the model to the data
params, _ = curve_fit(model, study_hours, test_scores)

# Generate smooth data points for the fitted curve
x_smooth = np.linspace(study_hours.min(), study_hours.max(), 500)
y_smooth = model(x_smooth, *params)

# Create the plot
plt.figure(figsize=(10, 6))

# Scatter plot of the original data
plt.scatter(study_hours, test_scores, color='royalblue', label='Student Data', alpha=0.8, edgecolor='white', s=100)

# Plot the smooth fitting curve
plt.plot(x_smooth, y_smooth, color='darkorange', linewidth=2, label='Fitted Trend')

# Title and labels
plt.title('Impact of Study Hours on Mathematics Test Scores', fontsize=16, fontweight='bold', ha='center')
plt.xlabel('Study Hours Per Week', fontsize=12)
plt.ylabel('Test Scores', fontsize=12)

# Adding grid and legend
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='lower right', fontsize=10)

# Adjust layout to avoid clipping
plt.tight_layout()

# Show the plot
plt.show()