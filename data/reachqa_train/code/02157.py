import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Expanded data: Urban Population Density (people/km²) and Innovation Index (0-100)
# Grouping data into two hypothetical regions for added complexity
population_density_region1 = np.array([1000, 1300, 1500, 2000, 2200, 2500, 2700, 3000])
innovation_index_region1 = np.array([65, 68, 75, 78, 77, 82, 85, 85])
population_density_region2 = np.array([1800, 1900, 2300, 2750, 3200, 3500, 3700])
innovation_index_region2 = np.array([72, 74, 80, 84, 87, 90, 93])

# Define a more complex fitting function (quadratic)
def fitting_function(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the curve to the data for each region
params1, _ = curve_fit(fitting_function, population_density_region1, innovation_index_region1)
params2, _ = curve_fit(fitting_function, population_density_region2, innovation_index_region2)

# Generate smooth curves across the range of the data for each region
x_smooth1 = np.linspace(min(population_density_region1), max(population_density_region1), 500)
y_smooth1 = fitting_function(x_smooth1, *params1)

x_smooth2 = np.linspace(min(population_density_region2), max(population_density_region2), 500)
y_smooth2 = fitting_function(x_smooth2, *params2)

# Create the plot with subplots for regions
fig, ax = plt.subplots(1, 2, figsize=(14, 7), sharey=True)

# Plot for Region 1
ax[0].scatter(population_density_region1, innovation_index_region1, color='blue', edgecolor='black', s=80, alpha=0.7, label='Region 1 Cities')
ax[0].plot(x_smooth1, y_smooth1, color='darkblue', linewidth=2, label='Trend Line Region 1')
ax[0].set_title("Region 1: Innovation vs Density", fontsize=12, fontweight='bold', pad=10)
ax[0].set_xlabel("Population Density (people/km²)", fontsize=10)
ax[0].set_ylabel("Innovation Index (0-100)", fontsize=10)
ax[0].grid(True, linestyle='--', linewidth=0.6, alpha=0.7)
ax[0].legend(loc='lower right', fontsize=8)

# Plot for Region 2
ax[1].scatter(population_density_region2, innovation_index_region2, color='green', edgecolor='black', s=80, alpha=0.7, label='Region 2 Cities')
ax[1].plot(x_smooth2, y_smooth2, color='darkgreen', linewidth=2, label='Trend Line Region 2')
ax[1].set_title("Region 2: Innovation vs Density", fontsize=12, fontweight='bold', pad=10)
ax[1].set_xlabel("Population Density (people/km²)", fontsize=10)
ax[1].grid(True, linestyle='--', linewidth=0.6, alpha=0.7)
ax[1].legend(loc='lower right', fontsize=8)

# Main title for the entire figure
fig.suptitle("Visionary Paths:\nMapping the Pulse of Urban Innovation Across Regions", fontsize=16, fontweight='bold')

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plot
plt.show()