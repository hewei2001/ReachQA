import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Crop types and locations
crops = ['Wheat', 'Corn', 'Soybeans']
locations = ['Mars', 'Moon', 'Oasis']

# Yield data in tons per hectare (refined for better visualization)
yields = np.array([
    [1.5, 0.8, 2.2],  # Wheat: Mars, Moon, Oasis
    [1.8, 0.7, 2.5],  # Corn: Mars, Moon, Oasis
    [1.2, 0.6, 2.0]   # Soybeans: Mars, Moon, Oasis
])

# Set up figure and 3D axes
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Create meshgrid for x, y indices
_x = np.arange(len(locations))
_y = np.arange(len(crops))
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

# Flatten yield data and set bar dimensions
top = yields.ravel()
bottom = np.zeros_like(top)
width = depth = 0.4

# Colors for each crop
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Plot each crop with different color
for i in range(len(crops)):
    ax.bar3d(x[i::len(crops)], y[i::len(crops)], bottom[i::len(crops)], width, depth, top[i::len(crops)], 
             shade=True, color=colors[i], alpha=0.9)

# Add labels and title
ax.set_title('Interplanetary Agricultural Experimentation\nCrop Yield Analysis', fontsize=16, fontweight='bold')
ax.set_xlabel('Location', fontsize=12)
ax.set_ylabel('Crop Type', fontsize=12)
ax.set_zlabel('Yield (tons/ha)', fontsize=12)

# Customize tick labels
ax.set_xticks(_x + width / 2)
ax.set_xticklabels(locations, fontsize=11)
ax.set_yticks(_y + depth / 2)
ax.set_yticklabels(crops, fontsize=11)

# Rotate the viewing angle for optimal visibility
ax.view_init(elev=20, azim=45)

# Add a legend for the crops
ax.legend(crops, loc='upper right', title="Crops", fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()