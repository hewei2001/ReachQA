import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define age groups (in years) and corresponding average coffee consumption
age_groups = np.array([18, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
coffee_consumption = np.array([1.8, 2.5, 3.0, 3.6, 4.2, 3.9, 3.5, 3.0, 2.8, 2.3, 1.9, 1.4])

# Set up the figure and axis
plt.figure(figsize=(12, 7))

# Scatter plot for the data points
plt.scatter(age_groups, coffee_consumption, color='darkblue', s=100, edgecolor='black', label='Observed Data', alpha=0.7)

# Spline interpolation for a smooth fitting line
spline = make_interp_spline(age_groups, coffee_consumption, k=3)  # Cubic spline
age_range = np.linspace(min(age_groups), max(age_groups), 300)
smooth_line = spline(age_range)

# Plot the smooth fitting line
plt.plot(age_range, smooth_line, color='red', linestyle='-', linewidth=2, label='Trend Line')

# Add title and labels
plt.title("Coffee Consumption Trends Across Age Groups", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Age (years)", fontsize=12)
plt.ylabel("Average Cups of Coffee Per Day", fontsize=12)

# Add a legend to the plot
plt.legend(loc='upper right', fontsize=10, frameon=True)

# Add grid lines for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust subplot params for the plot to fit into the figure area
plt.tight_layout()

# Display the plot
plt.show()