import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define years and PM2.5 data for three cities
years = np.array([1990, 2000, 2010, 2020])
pm25_city_a = np.array([35, 45, 55, 50])
pm25_city_b = np.array([50, 60, 65, 60])
pm25_city_c = np.array([40, 38, 35, 30])

# Generate smooth lines using spline interpolation
years_smooth = np.linspace(years.min(), years.max(), 300)
spline_a = make_interp_spline(years, pm25_city_a, k=3)
spline_b = make_interp_spline(years, pm25_city_b, k=3)
spline_c = make_interp_spline(years, pm25_city_c, k=3)

pm25_city_a_smooth = spline_a(years_smooth)
pm25_city_b_smooth = spline_b(years_smooth)
pm25_city_c_smooth = spline_c(years_smooth)

# Set up the plot
plt.figure(figsize=(12, 8))

# Scatter plot for raw data points
plt.scatter(years, pm25_city_a, color='green', label='City A', edgecolor='black', s=100, zorder=2)
plt.scatter(years, pm25_city_b, color='blue', label='City B', edgecolor='black', s=100, zorder=2)
plt.scatter(years, pm25_city_c, color='red', label='City C', edgecolor='black', s=100, zorder=2)

# Smooth line plot for trends
plt.plot(years_smooth, pm25_city_a_smooth, color='green', linestyle='--', label='Trend A', zorder=1)
plt.plot(years_smooth, pm25_city_b_smooth, color='blue', linestyle='--', label='Trend B', zorder=1)
plt.plot(years_smooth, pm25_city_c_smooth, color='red', linestyle='--', label='Trend C', zorder=1)

# Customize the plot
plt.title('Changes in PM2.5 Levels Over Time\nin Three Major Cities (1990-2020)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('PM2.5 Concentration (µg/m³)', fontsize=14)
plt.xticks(years)
plt.yticks(np.arange(0, 81, 10))
plt.grid(True, linestyle='--', alpha=0.5)

# Add legend and tight layout to avoid overlap
plt.legend(title='City Data & Trends', loc='upper right', fontsize=10)
plt.tight_layout()

# Display the plot
plt.show()