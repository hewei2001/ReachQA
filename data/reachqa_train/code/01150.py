import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data for squirrel sightings in Greenhaven parks
hours = np.array([6, 7, 8, 9, 12, 15, 18, 19, 20])  # observation times in hours
sightings = np.array([20, 35, 55, 60, 25, 15, 40, 45, 30])  # number of squirrel sightings

# Smooth curve fitting using spline interpolation
x_smooth = np.linspace(hours.min(), hours.max(), 300)
spl = make_interp_spline(hours, sightings, k=3)
sightings_smooth = spl(x_smooth)

# Create plot
plt.figure(figsize=(12, 6))
plt.scatter(hours, sightings, color='orange', edgecolors='k', s=100, label='Sighting Observations')
plt.plot(x_smooth, sightings_smooth, color='green', linewidth=2, label='Smooth Trend')

# Titles and labels
plt.title('Squirrel Activity in Greenhaven Parks:\nA Study of Urban Wildlife Movement', fontsize=16, fontweight='bold')
plt.xlabel('Time of Day (Hours)', fontsize=12)
plt.ylabel('Number of Squirrel Sightings', fontsize=12)

# Enhance plot appearance
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper right')
plt.xticks(np.arange(6, 21, 1), labels=[f'{h}:00' for h in range(6, 21)], rotation=45)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()