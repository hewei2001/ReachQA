import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define a function for the polynomial fit
def polynomial_fit(x, a, b, c):
    return a * x**2 + b * x + c

# Synthetic data: Green space per capita (sqm) vs. AQI improvement
cities = [
    'City A', 'City B', 'City C', 'City D', 'City E',
    'City F', 'City G', 'City H', 'City I', 'City J'
]
green_space_per_capita = np.array([5, 12, 18, 22, 29, 33, 37, 42, 46, 50])
aqi_improvement = np.array([2, 8, 15, 20, 28, 34, 40, 48, 55, 63])

# Fit the data with a polynomial function
params, _ = curve_fit(polynomial_fit, green_space_per_capita, aqi_improvement)

# Generate data for the fit line
x_fit = np.linspace(min(green_space_per_capita), max(green_space_per_capita), 100)
y_fit = polynomial_fit(x_fit, *params)

# Create the scatter plot and fit line
plt.figure(figsize=(10, 6))
plt.scatter(green_space_per_capita, aqi_improvement, color='forestgreen', s=100, label='Cities', edgecolors='black')
plt.plot(x_fit, y_fit, color='darkblue', linewidth=2, label='Trend Line', linestyle='--')

# Annotate each point with city names
for i, city in enumerate(cities):
    plt.annotate(city, (green_space_per_capita[i], aqi_improvement[i]), textcoords="offset points", xytext=(5, 5), ha='right')

# Add title and labels
plt.title('Impact of Urban Green Spaces\non Air Quality Improvement', fontsize=14, fontweight='bold')
plt.xlabel('Green Space per Capita (sqm)', fontsize=12)
plt.ylabel('AQI Improvement', fontsize=12)
plt.legend(loc='upper left', fontsize=10)

# Add grid
plt.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout for better readability
plt.tight_layout()

# Show the plot
plt.show()