import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Celestial Bodies and Trade Data
celestial_bodies = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
distances = np.array([91, 41, 78, 628, 1275, 2720, 4350, 5900])  # in million km
trade_values = np.array([2.5, 5.0, 7.5, 15.0, 10.0, 4.5, 3.0, 1.0])  # in trillion Galactic Credits

# Sort distances and trade values in tandem
sorted_indices = np.argsort(distances)
distances = distances[sorted_indices]
trade_values = trade_values[sorted_indices]
celestial_bodies = [celestial_bodies[i] for i in sorted_indices]

# Create the figure and axis
plt.figure(figsize=(12, 8))

# Scatter plot
plt.scatter(distances, trade_values, color='cornflowerblue', s=120, edgecolor='black', alpha=0.7, label='Trade Routes')

# Annotate points with celestial body names
for i, body in enumerate(celestial_bodies):
    plt.annotate(body, (distances[i], trade_values[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, fontweight='bold')

# Smooth fitting using spline interpolation
spline = make_interp_spline(distances, trade_values)
smooth_distances = np.linspace(distances.min(), distances.max(), 500)
smooth_trade_values = spline(smooth_distances)

# Plot the smooth line
plt.plot(smooth_distances, smooth_trade_values, color='darkorange', linewidth=2, linestyle='-', label='Trend Line')

# Title and labels
plt.title('Galactic Economy:\nTrading Routes of the Solar System', fontsize=16, fontweight='bold', loc='center')
plt.xlabel('Distance from Earth (million km)', fontsize=14)
plt.ylabel('Trade Value (trillion Galactic Credits)', fontsize=14)

# Grid, legend, and layout
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper right', fontsize=10, frameon=False)

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()