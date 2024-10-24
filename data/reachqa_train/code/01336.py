import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data: Coffee consumption (cups per day) and corresponding productivity scores
coffee_consumption = np.array([1, 2, 3, 4, 5, 6, 7, 8])
productivity_scores = np.array([45, 55, 65, 72, 78, 80, 76, 70])

# Create the scatter plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(coffee_consumption, productivity_scores, color='brown', alpha=0.7, s=100, label='Survey Data')

# Generate a smooth line fitting using spline interpolation
x_smooth = np.linspace(coffee_consumption.min(), coffee_consumption.max(), 300)
spline = make_interp_spline(coffee_consumption, productivity_scores, k=3)
y_smooth = spline(x_smooth)

# Plot the smooth fitted line
ax.plot(x_smooth, y_smooth, color='sienna', linestyle='-', linewidth=2, label='Fitted Curve')

# Add a title, labels, and a legend
ax.set_title('Impact of Coffee Consumption\non Workplace Productivity', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Coffee Consumption (Cups per Day)', fontsize=12)
ax.set_ylabel('Productivity Score', fontsize=12)
ax.legend(title='Legend', fontsize=10, loc='upper right')

# Customize the plot with grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()