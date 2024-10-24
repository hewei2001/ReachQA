import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define screen time data (hours per day)
screen_time = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Define GPA data (on a 4.0 scale) with some realistic patterns
gpa = np.array([3.9, 3.7, 3.6, 3.3, 3.1, 2.9, 2.6, 2.4, 2.2, 2.0])

# Define a quadratic function for curve fitting
def fit_function(x, a, b, c):
    return a * x**2 + b * x + c

# Perform curve fitting to find best-fit parameters
params, _ = curve_fit(fit_function, screen_time, gpa)

# Generate smooth GPA values for a smooth fitting line
smooth_screen_time = np.linspace(1, 10, 100)
smooth_gpa = fit_function(smooth_screen_time, *params)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(screen_time, gpa, color='blue', label='Observed Data', alpha=0.7, s=80)
plt.plot(smooth_screen_time, smooth_gpa, color='red', linestyle='--', label='Quadratic Fit')

# Customize the plot
plt.title('Impact of Screen Time on Academic Performance\nin High School Students', fontsize=14, fontweight='bold')
plt.xlabel('Average Daily Screen Time (hours)', fontsize=12)
plt.ylabel('GPA (4.0 scale)', fontsize=12)
plt.xticks(np.arange(1, 11, step=1))
plt.yticks(np.arange(2.0, 4.1, step=0.2))
plt.xlim(0.5, 10.5)
plt.ylim(1.8, 4.1)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper right')

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()