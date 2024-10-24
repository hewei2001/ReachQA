import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Extended data for a full year with multiple pollutants (CO2, NO2, PM2.5)
days = np.arange(1, 366)  # Days in a year
co2_levels = 400 + 20 * np.sin(2 * np.pi * days / 365) + np.random.normal(0, 10, days.size)
no2_levels = 30 + 10 * np.sin(2 * np.pi * days / 180) + np.random.normal(0, 5, days.size)
pm25_levels = 50 + 15 * np.sin(2 * np.pi * days / 90) + np.random.normal(0, 7, days.size)

# Interpolation for smooth curves
days_smooth = np.linspace(days.min(), days.max(), 1000)
spl_co2 = make_interp_spline(days, co2_levels, k=3)
co2_smooth = spl_co2(days_smooth)
spl_no2 = make_interp_spline(days, no2_levels, k=3)
no2_smooth = spl_no2(days_smooth)
spl_pm25 = make_interp_spline(days, pm25_levels, k=3)
pm25_smooth = spl_pm25(days_smooth)

# Plot configuration
plt.figure(figsize=(14, 8))

# Subplot for CO2
plt.subplot(311)
plt.scatter(days, co2_levels, color='red', s=10, label='CO2 Measurements', alpha=0.6, zorder=3)
plt.plot(days_smooth, co2_smooth, color='darkred', linewidth=2, label='CO2 Trend', zorder=2)
plt.title("Yearly Air Quality Analysis\nCO2 Levels Over Time", fontsize=14, weight='bold')
plt.xlabel("Day of the Year")
plt.ylabel("CO2 Levels (ppm)")
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.5)

# Subplot for NO2
plt.subplot(312)
plt.scatter(days, no2_levels, color='green', s=10, label='NO2 Measurements', alpha=0.6, zorder=3)
plt.plot(days_smooth, no2_smooth, color='darkgreen', linewidth=2, label='NO2 Trend', zorder=2)
plt.title("NO2 Levels Over Time", fontsize=14, weight='bold')
plt.xlabel("Day of the Year")
plt.ylabel("NO2 Levels (ppb)")
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.5)

# Subplot for PM2.5
plt.subplot(313)
plt.scatter(days, pm25_levels, color='blue', s=10, label='PM2.5 Measurements', alpha=0.6, zorder=3)
plt.plot(days_smooth, pm25_smooth, color='navy', linewidth=2, label='PM2.5 Trend', zorder=2)
plt.title("PM2.5 Levels Over Time", fontsize=14, weight='bold')
plt.xlabel("Day of the Year")
plt.ylabel("PM2.5 Levels (µg/m³)")
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust subplot parameters for better layout
plt.tight_layout()

# Display the plot
plt.show()