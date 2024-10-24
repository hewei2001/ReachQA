import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate, stats

# Define study hours and corresponding GPA values
study_hours = np.array([5, 7, 8, 10, 13, 14, 15, 16, 17, 19, 20, 22, 25, 27, 30])
gpas = np.array([2.0, 2.3, 2.5, 2.7, 3.0, 3.1, 3.2, 3.3, 3.4, 3.6, 3.8, 3.9, 3.9, 4.0, 4.0])

# Create the main figure and axis
fig, ax1 = plt.subplots(figsize=(12, 8))

# Scatter plot for study hours and GPA
ax1.scatter(study_hours, gpas, color='purple', edgecolors='k', s=100, label='Students')

# Fit a smooth spline curve
spline = interpolate.make_interp_spline(study_hours, gpas, k=3)
x_smooth = np.linspace(study_hours.min(), study_hours.max(), 300)
y_smooth = spline(x_smooth)
ax1.plot(x_smooth, y_smooth, color='darkorange', linewidth=2, linestyle='-', label='Spline Trend Line')

# Linear regression line
slope, intercept, _, _, _ = stats.linregress(study_hours, gpas)
ax1.plot(study_hours, slope * study_hours + intercept, color='blue', linewidth=2, linestyle='--', label='Linear Fit')

# Confidence interval for the linear regression
confidence_level = 0.95
t_value = stats.t.ppf((1 + confidence_level) / 2, len(study_hours) - 2)
stderr = stats.linregress(study_hours, gpas).stderr
confidence_interval = t_value * stderr
ax1.fill_between(study_hours, (slope * study_hours + intercept - confidence_interval), 
                 (slope * study_hours + intercept + confidence_interval), color='blue', alpha=0.2, label='95% Confidence Interval')

# Add a secondary axis for a histogram
ax2 = ax1.twinx()
ax2.hist(study_hours, bins=8, color='gray', alpha=0.3, edgecolor='black', label='Study Hour Distribution')
ax2.set_ylabel('Frequency', fontsize=12, color='gray')

# Title, labels, and legend
ax1.set_title('Correlation Between Study Hours and GPA\nAmong High School Students', fontsize=16)
ax1.set_xlabel('Study Hours per Week', fontsize=12)
ax1.set_ylabel('GPA', fontsize=12)
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Enable grid on primary axis
ax1.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()