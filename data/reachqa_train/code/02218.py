import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Original Data: Percentage of Green Spaces (%)
green_space_percentage = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
# PM2.5 levels (micrograms per cubic meter)
pm25_levels = np.array([85, 80, 75, 70, 65, 60, 55, 50, 48, 45, 42, 40])

# Additional Related Data: Population Density (people per square km)
population_density = np.array([1200, 1100, 1000, 950, 920, 890, 870, 850, 840, 830, 820, 810])
# Additional: NO2 levels (micrograms per cubic meter)
no2_levels = np.array([42, 39, 36, 33, 31, 28, 26, 25, 23, 21, 20, 19])

# Model function for fitting (exponential decay)
def model(x, a, b):
    return a * np.exp(-b * x) + 35

# Curve fitting for PM2.5 levels
popt_pm25, _ = curve_fit(model, green_space_percentage, pm25_levels)
x_values_pm25 = np.linspace(5, 60, 100)
fitting_curve_pm25 = model(x_values_pm25, *popt_pm25)

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# First subplot: PM2.5 levels
axs[0].scatter(green_space_percentage, pm25_levels, color='forestgreen', label='City Data Points', s=100, alpha=0.7)
axs[0].plot(x_values_pm25, fitting_curve_pm25, color='darkorange', linestyle='--', linewidth=2.5, label='Fitting Curve')
axs[0].set_title('Impact of Urban Green Spaces on Air Quality\nCorrelation with PM2.5 Levels', fontsize=12, fontweight='bold')
axs[0].set_xlabel('Green Spaces (%)', fontsize=10)
axs[0].set_ylabel('PM2.5 Levels (µg/m³)', fontsize=10)
axs[0].legend(loc='upper right', fontsize=9)
axs[0].grid(visible=True, linestyle='--', linewidth=0.5)
for i, txt in enumerate(pm25_levels):
    axs[0].annotate(txt, (green_space_percentage[i], pm25_levels[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

# Second subplot: NO2 levels vs. Population Density
axs[1].bar(green_space_percentage, no2_levels, color='skyblue', alpha=0.7, label='NO2 Levels')
axs[1].plot(green_space_percentage, population_density / 50, color='crimson', marker='o', linestyle='-', linewidth=2, label='Population Density (scaled)')
axs[1].set_title('Population Density and NO2 Levels', fontsize=12, fontweight='bold')
axs[1].set_xlabel('Green Spaces (%)', fontsize=10)
axs[1].set_ylabel('NO2 Levels (µg/m³)', fontsize=10, color='skyblue')
axs[1].tick_params(axis='y', labelcolor='skyblue')
axs[1].legend(loc='upper right', fontsize=9)
axs[1].grid(visible=True, linestyle='--', linewidth=0.5)

# Align y-axis label colors
secax = axs[1].twinx()
secax.set_ylabel('Population Density (people/km²)', fontsize=10, color='crimson')
secax.plot([], [], color='crimson', marker='o', label='Population Density')
secax.tick_params(axis='y', labelcolor='crimson')
secax.legend(loc='upper left', fontsize=9)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()