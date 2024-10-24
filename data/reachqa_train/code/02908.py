import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Data representing the number of novels read and corresponding creativity scores
novels_read = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
creativity_scores = np.array([50, 52, 58, 63, 68, 74, 79, 85, 89, 93, 97])

# Create a scatter plot
plt.figure(figsize=(10, 7))
plt.scatter(novels_read, creativity_scores, color='purple', s=100, edgecolor='k', alpha=0.7, label='Data Points')

# Create a smooth fitting line using spline interpolation
x_smooth = np.linspace(novels_read.min(), novels_read.max(), 300)
spl = make_interp_spline(novels_read, creativity_scores, k=3)  # B-spline of degree 3
y_smooth = spl(x_smooth)

plt.plot(x_smooth, y_smooth, color='orange', linestyle='-', linewidth=2, label='Smooth Fit')

# Add titles and labels
plt.title('Impact of Reading on Creativity\nAmong Budding Authors', fontsize=16, fontweight='bold')
plt.xlabel('Number of Novels Read', fontsize=12)
plt.ylabel('Creativity Score', fontsize=12)

# Set limits for better visibility
plt.xlim(0, 55)
plt.ylim(45, 100)

# Add legend
plt.legend(loc='lower right', fontsize=12)

# Customize grid
plt.grid(visible=True, linestyle='--', alpha=0.5)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()