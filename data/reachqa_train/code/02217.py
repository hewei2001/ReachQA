import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Data: Percentage of Green Spaces (%)
green_space_percentage = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])

# Data: PM2.5 levels (micrograms per cubic meter)
pm25_levels = np.array([85, 80, 75, 70, 65, 60, 55, 50, 48, 45, 42, 40])

# Define a function for a smooth fitting line (e.g., exponential decay)
def model(x, a, b):
    return a * np.exp(-b * x) + 35  # 35 as the lower asymptote value

# Perform the curve fitting
popt, pcov = curve_fit(model, green_space_percentage, pm25_levels)

# Generate x values for the fitting curve
x_values = np.linspace(5, 60, 100)
fitting_curve = model(x_values, *popt)

# Create the plot
plt.figure(figsize=(10, 6))
plt.scatter(green_space_percentage, pm25_levels, color='forestgreen', label='City Data Points', s=100, alpha=0.7)
plt.plot(x_values, fitting_curve, color='darkorange', linestyle='--', linewidth=2.5, label='Fitting Curve')

# Add titles and labels
plt.title('Impact of Urban Green Spaces on Air Quality\nCorrelation between Green Space Percentage and PM2.5 Levels', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Percentage of Urban Area as Green Spaces (%)', fontsize=12)
plt.ylabel('PM2.5 Levels (µg/m³)', fontsize=12)

# Add a grid for better readability
plt.grid(visible=True, which='both', linestyle='--', linewidth=0.5)

# Add a legend
plt.legend(title='Legend', fontsize=10, loc='upper right')

# Add annotations for points
for i, txt in enumerate(pm25_levels):
    plt.annotate(txt, (green_space_percentage[i], pm25_levels[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

# Automatically adjust the layout to fit everything
plt.tight_layout()

# Display the plot
plt.show()