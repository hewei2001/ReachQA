import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

# Define years and corresponding data for the number of flowers visited by bumblebees
years = np.arange(2020, 2031)
flowers_visited = np.array([120, 135, 145, 160, 155, 150, 170, 180, 175, 190, 195])

# Environmental index for each year
environmental_index = np.array([8.0, 8.2, 8.5, 8.6, 8.7, 9.0, 9.2, 9.5, 9.3, 9.7, 9.8])

# Sort environmental index and corresponding flowers visited
sorted_indices = np.argsort(environmental_index)
environmental_index_sorted = environmental_index[sorted_indices]
flowers_visited_sorted = flowers_visited[sorted_indices]

# Create a smooth fitting curve using spline interpolation
spline_curve = interpolate.make_interp_spline(environmental_index_sorted, flowers_visited_sorted)
smooth_index = np.linspace(min(environmental_index_sorted), max(environmental_index_sorted), 300)
smooth_flowers_visited = spline_curve(smooth_index)

# Initialize plot
fig, ax = plt.subplots(figsize=(12, 7), dpi=100)

# Plot scatter points
ax.scatter(environmental_index_sorted, flowers_visited_sorted, color='darkorange', edgecolor='black', s=100, label='Observed Data')

# Plot smooth fitting line
ax.plot(smooth_index, smooth_flowers_visited, color='forestgreen', linewidth=2, linestyle='-', label='Smooth Fit Curve')

# Title and labels
ax.set_title("Tracking the Flight of the Bumblebee:\nAnalyzing Pollination Patterns (2020-2030)", fontsize=16, pad=20)
ax.set_xlabel('Environmental Index (Scale 1-10)', fontsize=12)
ax.set_ylabel('Flowers Visited (Thousands)', fontsize=12)

# Customize legend
ax.legend(loc='upper left', fontsize=10)

# Add grid for clarity
ax.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the layout
plt.tight_layout()

# Display the chart
plt.show()