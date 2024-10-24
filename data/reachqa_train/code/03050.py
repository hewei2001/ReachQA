import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data representing average tree heights (in meters)
tree_heights = np.array([3.2, 4.1, 5.3, 6.5, 5.8, 6.2, 7.1, 8.0, 7.4, 8.5, 9.1, 9.5])

# Corresponding environmental index values
environmental_index = np.array([40, 42, 45, 48, 50, 53, 56, 60, 58, 63, 65, 68])

# Sort the environmental_index and tree_heights based on environmental_index
sorted_indices = np.argsort(environmental_index)
environmental_index_sorted = environmental_index[sorted_indices]
tree_heights_sorted = tree_heights[sorted_indices]

# Create a smooth fitting line using spline interpolation
spline_model = make_interp_spline(environmental_index_sorted, tree_heights_sorted)
x_smooth = np.linspace(environmental_index_sorted.min(), environmental_index_sorted.max(), 300)
y_smooth = spline_model(x_smooth)

# Initialize the plot
plt.figure(figsize=(12, 8))

# Scatter plot of tree heights against environmental index
plt.scatter(environmental_index_sorted, tree_heights_sorted, color='forestgreen', s=100, label='Measured Tree Heights')

# Plot the smooth fitting curve
plt.plot(x_smooth, y_smooth, color='royalblue', linewidth=2.5, label='Trend Line (Spline Fit)')

# Add title and labels
plt.title('Impact of Environmental Conditions\non Tree Growth in a Forest Ecosystem', fontsize=16, fontweight='bold')
plt.xlabel('Environmental Index', fontsize=14)
plt.ylabel('Average Tree Height (meters)', fontsize=14)

# Add a legend and grid
plt.legend(loc='upper left', fontsize=12, frameon=True)
plt.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()