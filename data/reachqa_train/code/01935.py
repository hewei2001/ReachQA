import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Internet speed (in Mbps)
internet_speeds = np.array([10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100])

# Productivity index corresponding to internet speeds
productivity_indices = np.array([60, 63, 65, 68, 70, 75, 78, 82, 85, 89, 92, 95])

# Define a smooth fitting function, e.g., logarithmic
def fitting_func(x, a, b, c):
    return a * np.log(b * x) + c

# Perform curve fitting
params, _ = curve_fit(fitting_func, internet_speeds, productivity_indices)

# Generate smooth line data for fitting
speed_range = np.linspace(min(internet_speeds), max(internet_speeds), 300)
smooth_productivity = fitting_func(speed_range, *params)

# Plotting the scatter chart
plt.figure(figsize=(12, 7))
plt.scatter(internet_speeds, productivity_indices, color='teal', label='Observed Productivity', alpha=0.8, edgecolors='k')
plt.plot(speed_range, smooth_productivity, color='salmon', linestyle='--', linewidth=2, label='Trend Line')

# Title and labels
plt.title("Internet Speed vs. Remote Work Productivity\nin TechCity", fontsize=16, fontweight='bold')
plt.xlabel("Internet Speed (Mbps)", fontsize=12)
plt.ylabel("Productivity Index", fontsize=12)
plt.legend(loc='upper left')

# Add annotations for specific insights
for speed, productivity in zip(internet_speeds, productivity_indices):
    plt.text(speed, productivity - 0.8, f"{productivity}", fontsize=9, ha='center', color='darkblue')

# Adding grid for clarity
plt.grid(True, linestyle='--', alpha=0.6)

# Ensure the layout fits well within the plot window
plt.tight_layout()

# Show the plot
plt.show()