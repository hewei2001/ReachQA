import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial

# Latitude data (in degrees, hypothetical locations on Mars)
latitudes = np.array([-70, -50, -30, -10, 10, 30, 50, 70, 85])

# Water trace intensity values (arbitrary units, hypothetical data)
water_intensity = np.array([5, 15, 25, 40, 60, 45, 30, 20, 10])

# Fit a polynomial curve (degree 2) to the data
coefs = np.polyfit(latitudes, water_intensity, 2)
poly_fit = Polynomial(coefs)

# Generate smooth latitude values for the curve
latitudes_fit = np.linspace(-90, 90, 500)
water_intensity_fit = poly_fit(latitudes_fit)

# Create the scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(latitudes, water_intensity, color='deepskyblue', edgecolors='k', s=100, label='Water Trace Observations')
plt.plot(latitudes_fit, water_intensity_fit, color='darkorange', linewidth=2, linestyle='--', label='Trend Curve (2nd Degree Polynomial)')

# Annotate data points
for i, (lat, intensity) in enumerate(zip(latitudes, water_intensity)):
    plt.annotate(f'({lat}, {intensity})', (lat, intensity), textcoords="offset points", xytext=(-10,10), ha='center')

# Set the title and labels
plt.title("Exploration of Mars:\nMapping Water Traces Across Latitudes", fontsize=16, fontweight='bold')
plt.xlabel("Latitude (degrees)", fontsize=12)
plt.ylabel("Water Trace Intensity (arbitrary units)", fontsize=12)

# Add grid and legend
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(loc='upper right', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()