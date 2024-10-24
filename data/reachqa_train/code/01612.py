import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Create artificial data
exercise_time = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
stress_levels = np.array([9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3])

# Create a smooth curve using spline interpolation
x_smooth = np.linspace(exercise_time.min(), exercise_time.max(), 200)
spl = make_interp_spline(exercise_time, stress_levels, k=3)  # k=3 for cubic spline
y_smooth = spl(x_smooth)

# Plotting the scatter chart
plt.figure(figsize=(10, 6))
plt.scatter(exercise_time, stress_levels, color='skyblue', edgecolor='black', alpha=0.7, s=100, label='Students')

# Plotting the smooth fitting curve
plt.plot(x_smooth, y_smooth, color='darkorange', linestyle='--', linewidth=2, label='Fitting Curve')

# Customize the chart
plt.title('Exercise Time vs. Stress Levels Among University Students', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Exercise Time per Week (Hours)', fontsize=12)
plt.ylabel('Perceived Stress Level (1-10)', fontsize=12)
plt.xlim(0, 13)
plt.ylim(1, 10)
plt.xticks(np.arange(0, 13, 1))
plt.yticks(np.arange(1, 11, 1))
plt.grid(True, linestyle='--', alpha=0.6)

# Adding a legend
plt.legend(loc='upper right', frameon=True)

# Annotate the median data point
median_exercise = np.median(exercise_time)
median_stress = np.median(stress_levels)
plt.annotate(f'Median: {median_exercise} hrs,\nStress: {median_stress}', xy=(median_exercise, median_stress),
             xytext=(median_exercise+2, median_stress+1),
             arrowprops=dict(facecolor='gray', shrink=0.05), fontsize=10, ha='center', bbox=dict(facecolor='white', alpha=0.5))

# Optimize layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()