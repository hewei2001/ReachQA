import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Data: Number of green spaces and well-being index for various cities
green_spaces = np.array([15, 18, 22, 28, 32, 35, 40, 43, 45, 50])
well_being_index = np.array([68, 70, 72, 75, 78, 80, 82, 85, 87, 90])

# Function to fit (quadratic for smooth fitting)
def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the curve
params, _ = curve_fit(quadratic, green_spaces, well_being_index)

# Create smooth x-values for the fitting curve
x_fit = np.linspace(min(green_spaces), max(green_spaces), 100)
y_fit = quadratic(x_fit, *params)

# Create the scatter plot
plt.figure(figsize=(12, 8))
plt.scatter(green_spaces, well_being_index, color='green', label='Cities', s=100, alpha=0.7, edgecolors='black')
plt.plot(x_fit, y_fit, color='blue', label='Quadratic Fit', linestyle='--')

# Add titles and labels
plt.title('The Impact of Urban Green Spaces on Well-being\nA Study of Different Cities', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Number of Urban Green Spaces', fontsize=12)
plt.ylabel('Well-being Index', fontsize=12)

# Customize the grid and legend
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=10, loc='upper left')

# Annotate a specific point
plt.annotate('High Well-being in Green Cities', xy=(50, 90), xytext=(40, 85),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10)

# Enhance plot aesthetics
plt.tight_layout()

# Display the plot
plt.show()