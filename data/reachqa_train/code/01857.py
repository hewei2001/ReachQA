import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial

# Hypothetical data for the analysis
decades = np.arange(1980, 2030, 5)
average_temperatures = np.array([14.8, 14.9, 15.0, 15.1, 15.3, 15.5, 15.8, 16.0, 16.3, 16.7])
migration_distances = np.array([70000, 69500, 69000, 68500, 67500, 67000, 66000, 65500, 65000, 64500])

# Fit a second-degree polynomial (quadratic) to the data
coefs = Polynomial.fit(average_temperatures, migration_distances, 2).convert().coef

# Generate a range of x values for plotting the fit line
x_fit = np.linspace(min(average_temperatures), max(average_temperatures), 500)
y_fit = np.polyval(coefs[::-1], x_fit)

# Create the scatter plot with a polynomial fitting line
plt.figure(figsize=(12, 7))

# Scatter plot for the data points
plt.scatter(average_temperatures, migration_distances, color='darkcyan', s=100, edgecolor='black', label='Migration Distance')

# Plot the polynomial fit line
plt.plot(x_fit, y_fit, color='darkred', linestyle='-', linewidth=2, label='Polynomial Fit')

# Annotate each point with its respective decade
for i, decade in enumerate(decades):
    plt.annotate(f'{decade}s', (average_temperatures[i], migration_distances[i]),
                 textcoords="offset points", xytext=(5, 5), ha='right', fontsize=9, color='darkblue')

# Title and labels
plt.title('Effects of Rising Temperatures on\nArctic Tern Migration Patterns', fontsize=16, fontweight='bold')
plt.xlabel('Average Yearly Temperature (°C)', fontsize=12)
plt.ylabel('Migration Distance (km)', fontsize=12)

# Add grid and legend for clarity
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper right', fontsize=10)

# Adjust the layout for better readability and to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()