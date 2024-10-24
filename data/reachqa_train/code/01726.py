import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data: Sleep Duration (hours) vs. Productivity Index
sleep_duration = np.array([5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9])
productivity_index = np.array([55, 60, 65, 70, 80, 85, 90, 85, 75])

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(sleep_duration, productivity_index, color='royalblue', edgecolors='black', s=100, label='Observed Productivity')

# Smooth fitting curve using B-Spline interpolation
x_smooth = np.linspace(sleep_duration.min(), sleep_duration.max(), 300)
spl = make_interp_spline(sleep_duration, productivity_index, k=3)  # B-spline of degree 3
y_smooth = spl(x_smooth)
plt.plot(x_smooth, y_smooth, color='darkorange', linewidth=2.5, label='Trend Line')

# Titles and labels
plt.title("Impact of Sleep Duration on Creative Productivity:\nInsights from the SomniTech Study", fontsize=14, fontweight='bold')
plt.xlabel("Average Sleep Duration (hours)", fontsize=12)
plt.ylabel("Productivity Index", fontsize=12)

# Add grid for improved readability
plt.grid(visible=True, linestyle='--', alpha=0.6)

# Add legend
plt.legend(loc='upper right')

# Automatically adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()