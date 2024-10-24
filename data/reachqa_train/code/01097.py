import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the data: Soil nitrogen levels and corn biomass
soil_nitrogen_levels = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
corn_biomass = np.array([150, 250, 350, 420, 460, 490, 500, 510, 515, 515])

# Logistic function for curve fitting
def logistic(x, a, b, c):
    return c / (1 + np.exp(-(x - b) / a))

# Fit a logistic curve to the data
popt, _ = curve_fit(logistic, soil_nitrogen_levels, corn_biomass, p0=[1, 25, 515])

# Generate a smooth curve for visualization
x_fitted = np.linspace(min(soil_nitrogen_levels), max(soil_nitrogen_levels), 100)
y_fitted = logistic(x_fitted, *popt)

# Plotting setup
plt.figure(figsize=(10, 6))

# Scatter plot for the observed data
plt.scatter(soil_nitrogen_levels, corn_biomass, color='darkgreen', label='Observed Data', marker='o', s=100, edgecolor='black', zorder=5)

# Plot the fitted logistic curve
plt.plot(x_fitted, y_fitted, color='navy', linestyle='-', linewidth=2, label='Logistic Fit', zorder=4)

# Enhancing the plot with titles and labels
plt.title("Impact of Soil Nitrogen Levels on Corn Biomass\nA Field Study", fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Soil Nitrogen Level (mg/kg)", fontsize=12)
plt.ylabel("Corn Biomass (g/m²)", fontsize=12)

# Adding a legend to distinguish between data and fit
plt.legend(loc='upper right', fontsize=10, frameon=False)

# Add a grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()