import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data for average annual temperature (°C) and number of bird species
temperatures = np.array([10, 12, 15, 18, 21, 24, 26, 30, 34])
bird_species = np.array([20, 25, 32, 40, 45, 47, 50, 49, 45])

# Related data for average annual rainfall (mm) and number of bird species
rainfall = np.array([400, 450, 470, 490, 520, 540, 560, 580, 600])

# Create a 1x2 subplot layout
fig, axes = plt.subplots(1, 2, figsize=(18, 7), constrained_layout=True)

# First subplot: Scatter plot with trend line
axes[0].scatter(temperatures, bird_species, color='royalblue', label='National Parks', s=120, alpha=0.8, edgecolors='w')
x_smooth = np.linspace(temperatures.min(), temperatures.max(), 300)
spl = make_interp_spline(temperatures, bird_species, k=3)
y_smooth = spl(x_smooth)
axes[0].plot(x_smooth, y_smooth, color='forestgreen', label='Trend Line', linestyle='-', linewidth=2.5)
axes[0].set_title("Temperature vs. Bird Species Diversity\nin National Parks", fontsize=14, fontweight='bold')
axes[0].set_xlabel("Average Annual Temperature (°C)", fontsize=12)
axes[0].set_ylabel("Number of Bird Species", fontsize=12)
axes[0].set_xlim(8, 36)
axes[0].set_ylim(15, 55)
axes[0].legend(loc='upper right', fontsize=11, frameon=True, shadow=True)
axes[0].grid(True, linestyle='--', linewidth=0.6, alpha=0.7)

# Second subplot: Bar chart for rainfall vs. bird species
axes[1].bar(temperatures, bird_species, color='slateblue', edgecolor='black', label='Bird Species')
axes[1].set_title("Rainfall Impact on Bird Species Diversity", fontsize=14, fontweight='bold')
axes[1].set_xlabel("Average Annual Rainfall (mm)", fontsize=12)
axes[1].set_ylabel("Number of Bird Species", fontsize=12)
axes[1].set_xlim(8, 36)
axes[1].set_ylim(15, 55)
axes[1].legend(loc='upper right', fontsize=11, frameon=True, shadow=True)
axes[1].grid(axis='y', linestyle='--', linewidth=0.6, alpha=0.7)

# Improve layout automatically to handle text overlap and spacing
fig.tight_layout()

# Show the combined plots
plt.show()