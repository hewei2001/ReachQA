import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial

# Generate contextual data
soil_carbon_content = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plant_growth_height = np.array([10, 13, 21, 25, 33, 35, 38, 45, 50, 58])

# Fit a polynomial of degree 2 to the data
coefs = np.polyfit(soil_carbon_content, plant_growth_height, 2)
polynomial_fit = Polynomial(coefs[::-1])

# Smooth values for the fitting line
x_smooth = np.linspace(soil_carbon_content.min(), soil_carbon_content.max(), 200)
y_smooth = polynomial_fit(x_smooth)

# Plot setup
plt.figure(figsize=(10, 6))
plt.scatter(soil_carbon_content, plant_growth_height, color='forestgreen', s=100, label='Sample Plots', edgecolor='black', alpha=0.7)
plt.plot(x_smooth, y_smooth, color='darkorange', linewidth=2, label='Polynomial Fit', linestyle='-')

# Customizing plot title and labels
plt.title("Soil Carbon Content vs Plant Growth\nAnalysis in the Greenbelt Zone", fontsize=16, fontweight='bold')
plt.xlabel("Soil Carbon Content (%)", fontsize=12)
plt.ylabel("Plant Growth (Height in cm)", fontsize=12)

# Add a legend with a title
plt.legend(title='Legend', fontsize=10, loc='upper left')

# Display a grid
plt.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the final plot
plt.show()