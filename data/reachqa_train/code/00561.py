import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Original screen time vs GPA data
screen_time = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
gpa = np.array([3.9, 3.7, 3.6, 3.3, 3.1, 2.9, 2.6, 2.4, 2.2, 2.0])

# Hypothetical data for average sleep duration
average_sleep_hours = np.array([8.5, 8.3, 8.0, 7.8, 7.5, 7.3, 7.0, 6.8, 6.5, 6.2])

# Define a quadratic function for curve fitting GPA
def fit_function(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the original GPA data
params, _ = curve_fit(fit_function, screen_time, gpa)
smooth_screen_time = np.linspace(1, 10, 100)
smooth_gpa = fit_function(smooth_screen_time, *params)

# Plot
fig, ax1 = plt.subplots(figsize=(12, 8))

# Scatter plot and curve fit for screen time vs GPA
ax1.scatter(screen_time, gpa, color='blue', label='GPA Data', alpha=0.7, s=80)
ax1.plot(smooth_screen_time, smooth_gpa, color='red', linestyle='--', label='Quadratic Fit')
ax1.set_xlabel('Average Daily Screen Time (hours)', fontsize=12)
ax1.set_ylabel('GPA (4.0 scale)', color='blue', fontsize=12)
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_xticks(np.arange(1, 11, step=1))
ax1.set_yticks(np.arange(2.0, 4.1, step=0.2))
ax1.set_xlim(0.5, 10.5)
ax1.set_ylim(1.8, 4.1)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.set_title('Impact of Screen Time on Academic Performance\nand Sleep Patterns in High School Students', fontsize=14, fontweight='bold')

# Create a secondary y-axis for average sleep duration
ax2 = ax1.twinx()
ax2.plot(screen_time, average_sleep_hours, color='green', marker='o', label='Avg Sleep Duration', linestyle='-', linewidth=2)
ax2.set_ylabel('Average Sleep Duration (hours)', color='green', fontsize=12)
ax2.tick_params(axis='y', labelcolor='green')
ax2.set_yticks(np.arange(6, 9.1, step=0.5))
ax2.set_ylim(5.5, 9.5)

# Combine legends from both axes
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper right')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()