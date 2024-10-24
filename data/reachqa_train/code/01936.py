import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Expanded data for Internet speed (in Mbps)
internet_speeds = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])

# Corresponding productivity indices and another influencing factor
productivity_indices = np.array([55, 60, 63, 65, 67, 70, 72, 75, 76, 78, 80, 82, 84, 85, 87, 89, 90, 92, 94, 95])
video_call_hours = np.array([10, 9, 8.5, 8, 7.5, 7, 6.5, 6, 5.5, 5, 4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1, 0.5, 0])

# Define a polynomial fitting function
def poly_fitting_func(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

# Perform curve fitting
params, _ = curve_fit(poly_fitting_func, internet_speeds, productivity_indices)

# Generate smooth line data for fitting
speed_range = np.linspace(min(internet_speeds), max(internet_speeds), 300)
smooth_productivity = poly_fitting_func(speed_range, *params)

# Create a plot with subplots for a comprehensive view
fig, ax1 = plt.subplots(figsize=(14, 8))

# First plot: Internet Speed vs Productivity with fit
ax1.scatter(internet_speeds, productivity_indices, color='teal', label='Observed Productivity', alpha=0.8, edgecolors='k')
ax1.plot(speed_range, smooth_productivity, color='salmon', linestyle='--', linewidth=2, label='Polynomial Fit')

ax1.set_title("Analysis of Internet Speed's Effect on Productivity", fontsize=16, fontweight='bold')
ax1.set_xlabel("Internet Speed (Mbps)", fontsize=12)
ax1.set_ylabel("Productivity Index", fontsize=12)

# Second plot: Video Call Hours vs Internet Speed
ax2 = ax1.twinx()
ax2.plot(internet_speeds, video_call_hours, color='green', linestyle='-', linewidth=2, marker='o', label='Video Call Hours')
ax2.set_ylabel("Video Call Hours", fontsize=12, color='green')
ax2.tick_params(axis='y', labelcolor='green')

fig.tight_layout()
fig.subplots_adjust(right=0.8)  # Ensure space for dual axis labels

# Legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Annotations for specific insights
for speed, productivity, call_hours in zip(internet_speeds, productivity_indices, video_call_hours):
    ax1.annotate(f"{productivity}", (speed, productivity), textcoords="offset points", xytext=(0, -10), ha='center', fontsize=9, color='darkblue')
    ax2.annotate(f"{call_hours}", (speed, call_hours), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, color='green')

# Adding grid to the first plot
ax1.grid(True, linestyle='--', alpha=0.6)

# Show the plot
plt.show()