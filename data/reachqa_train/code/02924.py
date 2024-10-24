import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Internet usage in hours per day and perceived productivity
internet_usage = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
productivity_scores = np.array([3.5, 4, 5, 6, 7, 7.5, 8.1, 8.5, 8.7, 8.8])

# Logistic function for smooth fitting
def logistic(x, L, k, x0):
    return L / (1 + np.exp(-k * (x - x0)))

# Fit the logistic curve to the data
params, _ = curve_fit(logistic, internet_usage, productivity_scores, p0=[10, 1, 5])

# Generate x values for smooth line
x_fit = np.linspace(internet_usage.min(), internet_usage.max(), 500)
# Calculate y values for the logistic curve
y_fit = logistic(x_fit, *params)

# Create the scatter plot with a smooth fitting curve
plt.figure(figsize=(10, 6))
plt.scatter(internet_usage, productivity_scores, color='green', alpha=0.6, edgecolors='black', label='Data Points')
plt.plot(x_fit, y_fit, color='red', linestyle='--', linewidth=2, label='Smooth Fit')

# Titles and labels
plt.title("Correlation Between Internet Usage and WFH Productivity", fontsize=14, weight='bold', pad=15)
plt.xlabel("Internet Usage (Hours/Day)", fontsize=12)
plt.ylabel("Productivity Level (Scale 1-10)", fontsize=12)

# Customizing plot elements for clarity
plt.xlim(0.5, 10.5)
plt.ylim(3, 10)
plt.xticks(np.arange(1, 11, step=1))
plt.yticks(np.arange(3, 11, step=1))

# Add legend and grid
plt.legend(loc='lower right', fontsize=10, frameon=True)
plt.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()