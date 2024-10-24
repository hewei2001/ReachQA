import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data: Training hours per week vs. Performance Score in the Galactic Games
training_hours = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
performance_scores = np.array([52, 54, 63, 70, 76, 84, 88, 92, 96, 99])

# Create a smooth curve using spline interpolation
spline_fit = make_interp_spline(training_hours, performance_scores, k=3)
fit_x = np.linspace(min(training_hours), max(training_hours), 200)
fit_y = spline_fit(fit_x)

# Plot configuration
plt.figure(figsize=(14, 8))

# Scatter plot for athlete data points
plt.scatter(training_hours, performance_scores, color='royalblue', edgecolors='black', s=100, label='Athlete Scores')

# Plot the smooth fitted curve
plt.plot(fit_x, fit_y, color='darkorange', linewidth=3, label='Trend Line (Smooth Fit)')

# Customizing plot appearance
plt.title('Impact of Training Hours on Performance\nin the Galactic Games', fontsize=16, fontweight='bold', loc='center')
plt.xlabel('Training Hours per Week', fontsize=13)
plt.ylabel('Performance Score', fontsize=13)
plt.xticks(np.arange(0, 55, step=5))
plt.yticks(np.arange(50, 105, step=5))
plt.legend(loc='lower right', fontsize=11, frameon=True)
plt.grid(alpha=0.4)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()