import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Original data for light exposure in hours and corresponding plant heights in cm
light_exposure = np.array([2, 4, 6, 8, 10, 12, 14, 16])
plant_heights = np.array([20, 35, 45, 60, 58, 55, 50, 40])

# Related dataset for the effect of different soil types on plant heights with constant light exposure
soil_types = ['Sandy', 'Loamy', 'Clayey', 'Peaty']
average_heights = np.array([45, 60, 55, 50])
height_std_dev = np.array([5, 3, 4, 2])

# Polynomial fit for the first subplot
coefficients = np.polyfit(light_exposure, plant_heights, 2)
polynomial = np.poly1d(coefficients)
light_exposure_smooth = np.linspace(light_exposure.min(), light_exposure.max(), 300)
plant_heights_smooth = polynomial(light_exposure_smooth)

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# First subplot: Scatter plot with a polynomial fitting line
axs[0].scatter(light_exposure, plant_heights, color='green', label='Measured Heights', s=100, edgecolors='black', alpha=0.7)
axs[0].plot(light_exposure_smooth, plant_heights_smooth, color='limegreen', linestyle='-', linewidth=2, label='Growth Trend (Fit)')
axs[0].set_title("Impact of Light on Plant Growth", fontsize=14, fontweight='bold', pad=10)
axs[0].set_xlabel('Light Exposure (Hours)', fontsize=12)
axs[0].set_ylabel('Plant Height (cm)', fontsize=12)
axs[0].legend(title="Observations", fontsize=10)
axs[0].grid(True, linestyle='--', alpha=0.6)

# Second subplot: Bar plot of average plant heights for different soil types
axs[1].bar(soil_types, average_heights, yerr=height_std_dev, color=['peru', 'forestgreen', 'steelblue', 'sienna'], alpha=0.8, capsize=5)
axs[1].set_title("Plant Growth Across Different Soil Types", fontsize=14, fontweight='bold', pad=10)
axs[1].set_xlabel('Soil Type', fontsize=12)
axs[1].set_ylabel('Average Plant Height (cm)', fontsize=12)
axs[1].grid(axis='y', linestyle='--', alpha=0.6)

# Shared title for both subplots
plt.suptitle("Urban Farming Experiment\nAnalyzing Environmental Effects on Plant Growth", fontsize=16, fontweight='bold', y=1.02)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()