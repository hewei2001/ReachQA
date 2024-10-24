import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define green space coverage (%) and corresponding temperature increases (°C)
green_space_percentage = np.array([70, 55, 30, 50, 80])
temperature_increase = np.array([1.5, 3.0, 4.5, 2.8, 1.0])

# Sort the data by green space percentage to ensure it's strictly increasing
sorted_indices = np.argsort(green_space_percentage)
green_space_percentage = green_space_percentage[sorted_indices]
temperature_increase = temperature_increase[sorted_indices]

# Interpolation for the fitting curve using spline
spline = make_interp_spline(green_space_percentage, temperature_increase, k=3)
smooth_gspace = np.linspace(green_space_percentage.min(), green_space_percentage.max(), 200)
smooth_temp = spline(smooth_gspace)

# Create the scatter plot
plt.figure(figsize=(12, 7))
plt.scatter(green_space_percentage, temperature_increase, color='forestgreen', s=120, alpha=0.8, edgecolor='black', label='City Data Points')
plt.plot(smooth_gspace, smooth_temp, color='darkorange', linestyle='-', linewidth=2.5, label='Fitting Curve')

# Adding plot details
plt.title("Urban Growth Analysis:\nGreen Spaces vs. Urban Heat Islands", fontsize=18, weight='bold', ha='center')
plt.xlabel("Green Space Coverage (%)", fontsize=14, labelpad=10)
plt.ylabel("Temperature Increase (°C)", fontsize=14, labelpad=10)
plt.xlim(20, 90)
plt.ylim(0, 5)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(loc='upper right', fontsize=12, frameon=True, shadow=True)
plt.grid(True, linestyle='--', alpha=0.6)

# Annotate data points with city names
city_labels = ['City A', 'City B', 'City C', 'City D', 'City E']
for i, city in enumerate(city_labels):
    plt.annotate(city, (green_space_percentage[i], temperature_increase[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='navy')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()