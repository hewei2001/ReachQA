import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Original Data
sensor_range = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180, 200])
processing_power = np.array([15, 25, 50, 70, 95, 105, 130, 150, 175, 190])
development_speed = np.array([48, 44, 40, 37, 35, 34, 33, 31, 30, 28])

# Additional Data for Energy Efficiency
energy_efficiency = 100 - (0.1 * sensor_range + 0.05 * processing_power)

# Smooth Curve for Development Speed
x_smooth = np.linspace(sensor_range.min(), sensor_range.max(), 300)
z_smooth = make_interp_spline(sensor_range, development_speed, k=3)(x_smooth)

# Setup subplots
fig, ax = plt.subplots(1, 2, figsize=(16, 8))
plt.subplots_adjust(wspace=0.4)

# Subplot 1: Original Scatter Plot with Smooth Curve
scatter = ax[0].scatter(sensor_range, processing_power, c=development_speed, cmap='viridis', s=100, edgecolor='k')
ax[0].plot(x_smooth, z_smooth, 'r-', linewidth=2, label='Smooth Fit Curve')

ax[0].set_title('Autonomous Vehicle Development:\nImpact of Sensor and Processing Features', fontsize=14, fontweight='bold')
ax[0].set_xlabel('Sensor Range (meters)', fontsize=12)
ax[0].set_ylabel('Processing Power (GFLOPS)', fontsize=12)

cbar = plt.colorbar(scatter, ax=ax[0])
cbar.set_label('Development Speed (hours)', fontsize=12)
ax[0].legend(loc='upper right', fontsize=10)
ax[0].grid(True, linestyle='--', alpha=0.6)

# Subplot 2: Bar Chart for Energy Efficiency
ax[1].bar(sensor_range, energy_efficiency, color='c', width=8, edgecolor='k', alpha=0.7)
ax[1].set_title('Energy Efficiency vs Sensor Range', fontsize=14, fontweight='bold')
ax[1].set_xlabel('Sensor Range (meters)', fontsize=12)
ax[1].set_ylabel('Energy Efficiency (%)', fontsize=12)

# Enhance visibility and prevent overlapping text
plt.tight_layout()

# Display the plots
plt.show()