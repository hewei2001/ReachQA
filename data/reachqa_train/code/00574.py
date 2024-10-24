import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data: Average weekly exercise hours and corresponding wellness scores
exercise_hours = np.array([
    1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 
    6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 
    11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16
])
wellness_scores = np.array([
    50, 52, 55, 58, 60, 63, 66, 68, 71, 73, 
    75, 78, 80, 83, 85, 87, 89, 90, 92, 93, 
    94, 95, 95, 96, 96, 97, 97, 98, 98, 99
])

# Create scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(exercise_hours, wellness_scores, color='teal', edgecolor='black', alpha=0.7, s=100, label='Participants')

# Fit a smooth curve using cubic spline
x_smooth = np.linspace(exercise_hours.min(), exercise_hours.max(), 300)
spl = make_interp_spline(exercise_hours, wellness_scores, k=3)
y_smooth = spl(x_smooth)

# Plot the smooth curve
plt.plot(x_smooth, y_smooth, color='orange', linewidth=2.5, label='Trend Curve')

# Configure title and labels
plt.title("Effect of Weekly Exercise on Wellness Scores\nAcross Health Program Participants", fontsize=16, fontweight='bold')
plt.xlabel("Weekly Exercise Hours", fontsize=14)
plt.ylabel("Wellness Score", fontsize=14)

# Add legend
plt.legend(loc='lower right', fontsize=12)

# Add grid for clarity
plt.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()