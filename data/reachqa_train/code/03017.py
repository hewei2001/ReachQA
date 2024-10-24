import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Define distances (in km) from residential areas to green spaces and the associated well-being scores
distances = np.array([0.5, 1, 1.5, 2, 3, 4, 5, 6, 7, 8])
wellbeing_small_park = np.array([7, 6.8, 6.5, 6, 5.5, 5, 4.5, 4, 3.8, 3.5])
wellbeing_large_park = np.array([8, 7.8, 7.5, 7, 6.8, 6.3, 5.8, 5, 4.8, 4.5])
wellbeing_botanical_garden = np.array([9, 8.8, 8.5, 8, 7.5, 7, 6.5, 6, 5.5, 5])

# Prepare the plot
plt.figure(figsize=(12, 8))

# Scatter plot
plt.scatter(distances, wellbeing_small_park, color='green', label='Small Park', s=100, alpha=0.7, edgecolor='black')
plt.scatter(distances, wellbeing_large_park, color='blue', label='Large Park', s=100, alpha=0.7, edgecolor='black')
plt.scatter(distances, wellbeing_botanical_garden, color='orange', label='Botanical Garden', s=100, alpha=0.7, edgecolor='black')

# Smooth lines using interpolation
x_smooth = np.linspace(distances.min(), distances.max(), 300)

small_park_smooth = make_interp_spline(distances, wellbeing_small_park, k=3)(x_smooth)
large_park_smooth = make_interp_spline(distances, wellbeing_large_park, k=3)(x_smooth)
botanical_garden_smooth = make_interp_spline(distances, wellbeing_botanical_garden, k=3)(x_smooth)

plt.plot(x_smooth, small_park_smooth, color='green', linewidth=2, linestyle='--', label='Small Park Fit')
plt.plot(x_smooth, large_park_smooth, color='blue', linewidth=2, linestyle='--', label='Large Park Fit')
plt.plot(x_smooth, botanical_garden_smooth, color='orange', linewidth=2, linestyle='--', label='Botanical Garden Fit')

# Customize the chart
plt.title('Impact of Urban Green Spaces\non Resident Well-being', fontsize=16, fontweight='bold')
plt.xlabel('Distance to Green Space (km)', fontsize=14)
plt.ylabel('Well-being Score', fontsize=14)
plt.legend(fontsize=12, loc='upper right', title="Green Space Type")
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(np.arange(0, 9, 1))
plt.yticks(np.arange(3, 10, 0.5))

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()