import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial

# Original data
soil_carbon_content = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plant_growth_height = np.array([10, 13, 21, 25, 33, 35, 38, 45, 50, 58])

# Additional related data (Hypothetical data for photosynthesis rate)
photosynthesis_rate = np.array([15, 22, 32, 44, 51, 60, 68, 75, 85, 93])

# Fit a polynomial of degree 2 to the original data
coefs_growth = np.polyfit(soil_carbon_content, plant_growth_height, 2)
polynomial_fit_growth = Polynomial(coefs_growth[::-1])

# Smooth values for the fitting line
x_smooth = np.linspace(soil_carbon_content.min(), soil_carbon_content.max(), 200)
y_smooth_growth = polynomial_fit_growth(x_smooth)

# Set up the subplot layout
fig, axs = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Analysis in the Greenbelt Zone\nComparative Study of Soil Impact on Growth and Photosynthesis", fontsize=16, fontweight='bold')

# Plot the first subplot: Scatter plot with polynomial fit
axs[0].scatter(soil_carbon_content, plant_growth_height, color='forestgreen', s=100, label='Sample Plots', edgecolor='black', alpha=0.7)
axs[0].plot(x_smooth, y_smooth_growth, color='darkorange', linewidth=2, label='Polynomial Fit', linestyle='-')
axs[0].set_title('Soil Carbon vs Plant Growth', fontsize=14)
axs[0].set_xlabel("Soil Carbon Content (%)", fontsize=12)
axs[0].set_ylabel("Plant Growth (Height in cm)", fontsize=12)
axs[0].legend(title='Legend', fontsize=10)
axs[0].grid(True, linestyle='--', alpha=0.7)

# Plot the second subplot: Bar plot for photosynthesis rate
axs[1].bar(soil_carbon_content, photosynthesis_rate, color='slateblue', alpha=0.7, label='Photosynthesis Rate')
axs[1].set_title('Soil Carbon vs Photosynthesis Rate', fontsize=14)
axs[1].set_xlabel("Soil Carbon Content (%)", fontsize=12)
axs[1].set_ylabel("Photosynthesis Rate (Units)", fontsize=12)
axs[1].legend(loc='upper left', fontsize=10)
axs[1].grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plot
plt.show()