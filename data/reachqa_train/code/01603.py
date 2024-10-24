import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Define coffee consumption in cups per day
coffee_consumption = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

# Define productivity measured in tasks completed per day
productivity = np.array([3, 5, 8, 10, 11, 12, 11, 9, 6])

# Create smooth lines for the scatter plot using spline interpolation
coffee_spline = make_interp_spline(coffee_consumption, productivity)

# Generate new coffee consumption values for a smooth line
coffee_new = np.linspace(0, 8, 300)
productivity_smooth = coffee_spline(coffee_new)

# Setup the plot
plt.figure(figsize=(12, 7))

# Scatter plot for coffee consumption vs productivity
plt.scatter(coffee_consumption, productivity, color='brown', label='Observed Data', s=100, edgecolor='black')

# Plot the smooth line
plt.plot(coffee_new, productivity_smooth, color='green', linestyle='-', linewidth=2, alpha=0.7, label='Trend Line')

# Add titles and labels
plt.title('Coffee Consumption vs Productivity\nin a Tech Startup', fontsize=16, fontweight='bold')
plt.xlabel('Coffee Consumption (Cups per Day)', fontsize=12)
plt.ylabel('Productivity (Tasks Completed per Day)', fontsize=12)

# Customize ticks and grid for better readability
plt.xticks(np.arange(0, 9, step=1))
plt.yticks(np.arange(2, 14, step=2))
plt.grid(alpha=0.3, linestyle='--')

# Add a legend to differentiate between scatter and trend line
plt.legend(fontsize=10, loc='upper left', edgecolor='gray')

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()