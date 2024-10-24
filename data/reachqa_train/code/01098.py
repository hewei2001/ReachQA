import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Original data: Soil nitrogen levels and corn biomass
soil_nitrogen_levels = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
corn_biomass_nitrogen = np.array([150, 250, 350, 420, 460, 490, 500, 510, 515, 515])

# New data: Soil phosphorus levels and corn biomass
soil_phosphorus_levels = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
corn_biomass_phosphorus = np.array([130, 220, 310, 385, 430, 470, 480, 490, 495, 495])

# Logistic function for curve fitting
def logistic(x, a, b, c):
    return c / (1 + np.exp(-(x - b) / a))

# Fit logistic curves to the data
popt_nitrogen, _ = curve_fit(logistic, soil_nitrogen_levels, corn_biomass_nitrogen, p0=[1, 25, 515])
popt_phosphorus, _ = curve_fit(logistic, soil_phosphorus_levels, corn_biomass_phosphorus, p0=[1, 25, 495])

# Generate smooth curves for visualization
x_fitted = np.linspace(5, 50, 100)
y_fitted_nitrogen = logistic(x_fitted, *popt_nitrogen)
y_fitted_phosphorus = logistic(x_fitted, *popt_phosphorus)

# Plotting setup
plt.figure(figsize=(12, 7))

# Scatter plot and logistic fit for nitrogen
plt.scatter(soil_nitrogen_levels, corn_biomass_nitrogen, color='darkgreen', label='Nitrogen Observed', marker='o', s=100, edgecolor='black', zorder=5)
plt.plot(x_fitted, y_fitted_nitrogen, color='navy', linestyle='-', linewidth=2, label='Nitrogen Logistic Fit', zorder=4)

# Bar plot for phosphorus data
bar_width = 0.4
plt.bar(soil_phosphorus_levels + bar_width / 2, corn_biomass_phosphorus, bar_width, color='lightcoral', alpha=0.7, label='Phosphorus Observed')

# Adding logistic fit for phosphorus
plt.plot(x_fitted, y_fitted_phosphorus, color='darkred', linestyle='--', linewidth=2, label='Phosphorus Logistic Fit', zorder=3)

# Enhance the plot with titles, labels, and legends
plt.title("Impact of Soil Nutrients on Corn Biomass\nComparative Analysis of Nitrogen vs. Phosphorus", fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Soil Nutrient Level (mg/kg)", fontsize=12)
plt.ylabel("Corn Biomass (g/m²)", fontsize=12)

# Adding legend
plt.legend(loc='upper left', fontsize=10)

# Adding a grid
plt.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()