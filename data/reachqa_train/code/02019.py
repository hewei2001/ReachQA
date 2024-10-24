import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the years and corresponding average travel speeds (in km/h)
years = np.array([2000, 2005, 2010, 2015, 2020, 2025, 2030, 2035, 2040])
travel_speeds = np.array([800, 850, 1000, 2000, 5000, 12000, 20000, 50000, 100000])

# Use a spline to create a smooth curve fitting for the data
years_smooth = np.linspace(years.min(), years.max(), 300)
spl = make_interp_spline(years, travel_speeds, k=3)  # Spline of degree 3
travel_speeds_smooth = spl(years_smooth)

plt.figure(figsize=(12, 8))

# Scatter plot
plt.scatter(years, travel_speeds, color='purple', s=100, alpha=0.7, label='Travel Speed Data')

# Plot smooth curve fitting
plt.plot(years_smooth, travel_speeds_smooth, color='blue', linestyle='-', linewidth=2.5, label='Smooth Fitting Curve')

# Add title and labels
plt.title("Evolution of Teleportation Technology\nImpact on Travel Speed in Technotopia (2000-2040)",
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Average Travel Speed (km/h)", fontsize=12)

# Highlight key milestones in teleportation technology
milestones = {
    2010: '1st Commercial Teleporter',
    2025: 'Quantum Leap Teleporters',
    2035: 'Instant Transport Network'
}

for year, event in milestones.items():
    plt.annotate(event, xy=(year, travel_speeds[years == year]), xytext=(year - 3, travel_speeds[years == year] + 5000),
                 arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, backgroundcolor='w')

# Customize grid and legend
plt.grid(linestyle='--', linewidth=0.7, alpha=0.7)
plt.legend(loc='upper left', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()