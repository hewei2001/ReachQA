import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the data: exercise duration in minutes and corresponding mood levels
exercise_duration = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
mood_levels = np.array([3, 4, 5, 5.5, 6, 7, 7.5, 8, 8.5, 9])

# Initialize the plot
plt.figure(figsize=(12, 7))
plt.scatter(exercise_duration, mood_levels, color='dodgerblue', label='Mood Levels', edgecolor='black', s=100)

# Create a smooth fitting curve
x_smooth = np.linspace(exercise_duration.min(), exercise_duration.max(), 300)
spl = make_interp_spline(exercise_duration, mood_levels, k=3)
mood_smooth = spl(x_smooth)

# Plot the smooth fitting line
plt.plot(x_smooth, mood_smooth, color='darkorange', linewidth=2, label='Smooth Fit')

# Annotate specific insights
plt.annotate('Moderate Improvement', xy=(45, 6), xytext=(55, 5.5),
             arrowprops=dict(facecolor='green', shrink=0.05),
             fontsize=10, color='green')

plt.annotate('Significant Boost', xy=(85, 8.5), xytext=(75, 7.5),
             arrowprops=dict(facecolor='purple', shrink=0.05),
             fontsize=10, color='purple')

# Set titles and labels
plt.title('The Effect of Exercise on Mood Levels: \nA Visual Correlation Analysis', fontsize=16, weight='bold', pad=20)
plt.xlabel('Exercise Duration (minutes)', fontsize=14)
plt.ylabel('Mood Level (1-10)', fontsize=14)

# Customize axis limits and grid
plt.xlim(0, 110)
plt.ylim(0, 10)
plt.grid(True, linestyle='--', alpha=0.6)

# Add legend and adjust layout
plt.legend(loc='lower right', fontsize=12)
plt.tight_layout()

# Display the plot
plt.show()