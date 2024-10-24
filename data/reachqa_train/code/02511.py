import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Celestial Bodies and Trade Data
celestial_bodies = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
distances = np.array([91, 41, 78, 628, 1275, 2720, 4350, 5900])  # in million km
trade_values = np.array([2.5, 5.0, 7.5, 15.0, 10.0, 4.5, 3.0, 1.0])  # in trillion Galactic Credits

# Sort distances and rearrange trade_values accordingly
sorted_indices = np.argsort(distances)
sorted_distances = distances[sorted_indices]
sorted_trade_values = trade_values[sorted_indices]

# Hypothetical Fleet Traffic Data
fleet_traffic = np.array([10, 15, 12, 20, 18, 14, 11, 8])  # Fleet count (hypothetical)

# Create the figure and primary axis
fig, ax1 = plt.subplots(figsize=(12, 8))

# Scatter plot for Trade Values
ax1.scatter(distances, trade_values, color='cornflowerblue', s=120, edgecolor='black', alpha=0.7, label='Trade Routes')

# Annotate points with celestial body names
for i, body in enumerate(celestial_bodies):
    ax1.annotate(body, (distances[i], trade_values[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, fontweight='bold')

# Smooth fitting using spline interpolation
spline = make_interp_spline(sorted_distances, sorted_trade_values)
smooth_distances = np.linspace(sorted_distances.min(), sorted_distances.max(), 500)
smooth_trade_values = spline(smooth_distances)

# Plot the smooth line
ax1.plot(smooth_distances, smooth_trade_values, color='darkorange', linewidth=2, linestyle='-', label='Trend Line')

# Configure primary axis
ax1.set_title('Galactic Economy and Fleet Management:\nTrading Routes and Fleet Traffic of the Solar System', fontsize=16, fontweight='bold', loc='center')
ax1.set_xlabel('Distance from Earth (million km)', fontsize=14)
ax1.set_ylabel('Trade Value (trillion Galactic Credits)', fontsize=14)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend(loc='upper left', fontsize=10, frameon=False)

# Create secondary axis for Fleet Traffic
ax2 = ax1.twinx()
bar_width = 50  # Width for the bars

# Bar plot for Fleet Traffic
ax2.bar(distances, fleet_traffic, width=bar_width, color='lightcoral', alpha=0.5, label='Fleet Traffic')

# Configure secondary axis
ax2.set_ylabel('Fleet Traffic (count)', fontsize=14)
ax2.legend(loc='upper right', fontsize=10, frameon=False)

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()