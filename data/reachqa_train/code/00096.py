import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from matplotlib.gridspec import GridSpec

# Define years and PM2.5 data for three cities
years = np.array([1990, 2000, 2010, 2020])
pm25_city_a = np.array([35, 45, 55, 50])
pm25_city_b = np.array([50, 60, 65, 60])
pm25_city_c = np.array([40, 38, 35, 30])

# Additional data: Average PM2.5 levels
average_pm25 = (pm25_city_a + pm25_city_b + pm25_city_c) / 3

# Generate smooth lines using spline interpolation
years_smooth = np.linspace(years.min(), years.max(), 300)
spline_a = make_interp_spline(years, pm25_city_a, k=3)
spline_b = make_interp_spline(years, pm25_city_b, k=3)
spline_c = make_interp_spline(years, pm25_city_c, k=3)

pm25_city_a_smooth = spline_a(years_smooth)
pm25_city_b_smooth = spline_b(years_smooth)
pm25_city_c_smooth = spline_c(years_smooth)

# Set up the figure and grid specification
fig = plt.figure(figsize=(16, 8))
gs = GridSpec(1, 2, figure=fig)

# First Subplot: Line and Scatter Plot
ax1 = fig.add_subplot(gs[0, 0])
ax1.scatter(years, pm25_city_a, color='green', label='City A', edgecolor='black', s=100, zorder=3)
ax1.scatter(years, pm25_city_b, color='blue', label='City B', edgecolor='black', s=100, zorder=3)
ax1.scatter(years, pm25_city_c, color='red', label='City C', edgecolor='black', s=100, zorder=3)
ax1.plot(years_smooth, pm25_city_a_smooth, color='green', linestyle='--', label='Trend A', zorder=2)
ax1.plot(years_smooth, pm25_city_b_smooth, color='blue', linestyle='--', label='Trend B', zorder=2)
ax1.plot(years_smooth, pm25_city_c_smooth, color='red', linestyle='--', label='Trend C', zorder=2)

ax1.set_title('Changes in PM2.5 Levels Over Time\nin Three Major Cities (1990-2020)', fontsize=14)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('PM2.5 Concentration (µg/m³)', fontsize=12)
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 81, 10))
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(title='City Data & Trends', loc='upper right', fontsize=10)

# Second Subplot: Bar Chart of Average PM2.5 Levels
ax2 = fig.add_subplot(gs[0, 1])
ax2.bar(years - 2, pm25_city_a, width=4, label='City A', color='green', alpha=0.7)
ax2.bar(years, pm25_city_b, width=4, label='City B', color='blue', alpha=0.7)
ax2.bar(years + 2, pm25_city_c, width=4, label='City C', color='red', alpha=0.7)

ax2.set_title('Average PM2.5 Levels\nAcross All Cities (1990-2020)', fontsize=14)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('PM2.5 Concentration (µg/m³)', fontsize=12)
ax2.set_xticks(years)
ax2.set_yticks(np.arange(0, 81, 10))
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(title='Average Levels', loc='upper right', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()