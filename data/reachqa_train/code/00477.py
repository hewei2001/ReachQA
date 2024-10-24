import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Months and data expansion
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Simulated data for different parameters across months
altitude = np.array([900, 950, 1100, 1200, 1400, 1500, 1600, 1550, 1450, 1300, 1100, 950])
speed = np.array([20, 22, 24, 26, 28, 30, 32, 31, 29, 26, 24, 22])
temperature = np.array([5, 6, 9, 15, 20, 25, 30, 29, 24, 18, 11, 6])
wind_speed = np.array([5, 6, 8, 10, 12, 11, 10, 9, 8, 7, 6, 5])

# Numeric representation for months
months_numeric = np.arange(len(months))

# Spline interpolation for smooth curves
def smooth_curve(data):
    spline = make_interp_spline(months_numeric, data, k=3)
    return spline(np.linspace(months_numeric.min(), months_numeric.max(), 300))

altitude_smooth = smooth_curve(altitude)
speed_smooth = smooth_curve(speed)
temperature_smooth = smooth_curve(temperature)
wind_speed_smooth = smooth_curve(wind_speed)

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Altitude vs. Months
axs[0, 0].scatter(months_numeric, altitude, color='skyblue', label='Altitude (m)', s=100)
axs[0, 0].plot(np.linspace(months_numeric.min(), months_numeric.max(), 300), altitude_smooth, color='skyblue', linewidth=2)
axs[0, 0].set_title("Altitude over Months", fontsize=14)
axs[0, 0].set_xticks(months_numeric)
axs[0, 0].set_xticklabels(months, rotation=45, ha='right')
axs[0, 0].set_ylabel("Altitude (m)")
axs[0, 0].grid(True, linestyle='--', alpha=0.6)

# Speed vs. Months
axs[0, 1].scatter(months_numeric, speed, color='darkorange', label='Speed (km/h)', s=100)
axs[0, 1].plot(np.linspace(months_numeric.min(), months_numeric.max(), 300), speed_smooth, color='darkorange', linewidth=2)
axs[0, 1].set_title("Speed over Months", fontsize=14)
axs[0, 1].set_xticks(months_numeric)
axs[0, 1].set_xticklabels(months, rotation=45, ha='right')
axs[0, 1].set_ylabel("Speed (km/h)")
axs[0, 1].grid(True, linestyle='--', alpha=0.6)

# Temperature vs. Months
axs[1, 0].scatter(months_numeric, temperature, color='lightgreen', label='Temperature (°C)', s=100)
axs[1, 0].plot(np.linspace(months_numeric.min(), months_numeric.max(), 300), temperature_smooth, color='lightgreen', linewidth=2)
axs[1, 0].set_title("Temperature over Months", fontsize=14)
axs[1, 0].set_xticks(months_numeric)
axs[1, 0].set_xticklabels(months, rotation=45, ha='right')
axs[1, 0].set_ylabel("Temperature (°C)")
axs[1, 0].grid(True, linestyle='--', alpha=0.6)

# Wind Speed vs. Months
axs[1, 1].scatter(months_numeric, wind_speed, color='purple', label='Wind Speed (m/s)', s=100)
axs[1, 1].plot(np.linspace(months_numeric.min(), months_numeric.max(), 300), wind_speed_smooth, color='purple', linewidth=2)
axs[1, 1].set_title("Wind Speed over Months", fontsize=14)
axs[1, 1].set_xticks(months_numeric)
axs[1, 1].set_xticklabels(months, rotation=45, ha='right')
axs[1, 1].set_ylabel("Wind Speed (m/s)")
axs[1, 1].grid(True, linestyle='--', alpha=0.6)

# Overall Title and Layout
fig.suptitle("Complex Interplay of Atmospheric Conditions Across Months", fontsize=16, y=1.02)
plt.tight_layout()
plt.show()