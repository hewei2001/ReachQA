import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# NO2 and PM2.5 data points
no2_levels = np.array([15, 18, 21, 22, 24, 30, 35, 40, 43, 45, 50, 55, 60, 65, 70])
pm25_levels = np.array([10, 12, 14, 15, 17, 22, 26, 30, 32, 33, 37, 42, 46, 50, 55])

# Sort data by no2_levels for smooth fitting line
sorted_indices = np.argsort(no2_levels)
no2_levels = no2_levels[sorted_indices]
pm25_levels = pm25_levels[sorted_indices]

# Create a smooth line using interpolation
spl = make_interp_spline(no2_levels, pm25_levels, k=3)
no2_smooth = np.linspace(no2_levels.min(), no2_levels.max(), 300)
pm25_smooth = spl(no2_smooth)

# Plotting the scatter chart
plt.figure(figsize=(10, 6))
plt.scatter(no2_levels, pm25_levels, color='blue', label='Data Points', alpha=0.6)

# Plotting the smooth fitting line
plt.plot(no2_smooth, pm25_smooth, color='red', linestyle='-', linewidth=2, label='Smooth Fitting Line')

# Adding title and labels
plt.title('Correlational Study of NO2 and PM2.5 Concentrations in Smogville', fontsize=16, fontweight='bold', wrap=True)
plt.xlabel('Nitrogen Dioxide (NO2) Concentration (μg/m³)', fontsize=12)
plt.ylabel('Particulate Matter (PM2.5) Concentration (μg/m³)', fontsize=12)

# Add a legend to the plot
plt.legend(loc='upper left', fontsize=10)

# Add grid lines for visual aid
plt.grid(linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()