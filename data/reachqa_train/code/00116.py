import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

# Define study hours and corresponding GPA values
study_hours = np.array([5, 7, 8, 10, 13, 14, 15, 16, 17, 19, 20, 22, 25, 27, 30])
gpas = np.array([2.0, 2.3, 2.5, 2.7, 3.0, 3.1, 3.2, 3.3, 3.4, 3.6, 3.8, 3.9, 3.9, 4.0, 4.0])

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(study_hours, gpas, color='purple', edgecolors='k', s=100, label='Students')

# Fit a smooth curve using spline interpolation
spline = interpolate.make_interp_spline(study_hours, gpas, k=3)
x_smooth = np.linspace(study_hours.min(), study_hours.max(), 300)
y_smooth = spline(x_smooth)

# Plot the smooth curve
plt.plot(x_smooth, y_smooth, color='darkorange', linewidth=2, linestyle='-', label='Trend Line')

# Configure the plot title and labels
plt.title('Correlation Between Study Hours and GPA\nAmong High School Students', fontsize=16)
plt.xlabel('Study Hours per Week', fontsize=12)
plt.ylabel('GPA', fontsize=12)

# Add legend to distinguish between data points and trend line
plt.legend(loc='lower right')

# Enable grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout for better appearance
plt.tight_layout()

# Show the plot
plt.show()