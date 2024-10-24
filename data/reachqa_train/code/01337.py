import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy.stats import linregress

# Data: Coffee consumption (cups per day) and corresponding productivity scores
coffee_consumption = np.array([1, 2, 3, 4, 5, 6, 7, 8])
productivity_scores = np.array([45, 55, 65, 72, 78, 80, 76, 70])

# Set a consistent color palette
scatter_color = 'chocolate'
line_color = 'saddlebrown'
linear_fit_color = 'forestgreen'
highlight_color = 'gold'

# Create the scatter plot
fig, ax = plt.subplots(figsize=(12, 7))
ax.scatter(coffee_consumption, productivity_scores, color=scatter_color, alpha=0.8, s=100, label='Survey Data')

# Generate a smooth line fitting using spline interpolation
x_smooth = np.linspace(coffee_consumption.min(), coffee_consumption.max(), 300)
spline = make_interp_spline(coffee_consumption, productivity_scores, k=3)
y_smooth = spline(x_smooth)
ax.plot(x_smooth, y_smooth, color=line_color, linestyle='-', linewidth=2.5, label='Spline Fit')

# Add a linear regression line for comparison
slope, intercept, _, _, _ = linregress(coffee_consumption, productivity_scores)
linear_fit = slope * x_smooth + intercept
ax.plot(x_smooth, linear_fit, color=linear_fit_color, linestyle='--', linewidth=2, label='Linear Regression')

# Annotate the maximum productivity score
max_idx = np.argmax(productivity_scores)
ax.annotate('Peak Productivity', xy=(coffee_consumption[max_idx], productivity_scores[max_idx]), 
            xytext=(coffee_consumption[max_idx]+0.5, productivity_scores[max_idx]-10),
            arrowprops=dict(facecolor=highlight_color, arrowstyle='->'), fontsize=11, color=highlight_color)

# Add a title, labels, and a legend
ax.set_title('Impact of Coffee Consumption\non Workplace Productivity', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Coffee Consumption (Cups per Day)', fontsize=13)
ax.set_ylabel('Productivity Score', fontsize=13)
ax.legend(title='Legend', fontsize=11, loc='upper right')

# Customize the plot with grid lines
ax.grid(True, linestyle='--', linewidth=0.7, alpha=0.5)

# Add a background color to the plot area to improve focus
ax.set_facecolor('#f9f9f9')

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()