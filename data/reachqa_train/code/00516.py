import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy.stats import norm

# Data: Training hours per week vs. Performance Score in the Galactic Games

# Original data for a baseline comparison
training_hours = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
performance_scores = np.array([52, 54, 63, 70, 76, 84, 88, 92, 96, 99])

# Simulated data for different athlete groups (Novice, Intermediate, Advanced)
novice_scores = performance_scores - np.array([5, 8, 7, 10, 6, 10, 12, 14, 12, 10])
intermediate_scores = performance_scores
advanced_scores = performance_scores + np.array([8, 10, 12, 15, 14, 16, 18, 19, 18, 20])

# Create a smooth curve using spline interpolation for each group
fit_x = np.linspace(min(training_hours), max(training_hours), 200)
novice_spline_fit = make_interp_spline(training_hours, novice_scores, k=3)(fit_x)
intermediate_spline_fit = make_interp_spline(training_hours, intermediate_scores, k=3)(fit_x)
advanced_spline_fit = make_interp_spline(training_hours, advanced_scores, k=3)(fit_x)

# Plot configuration
plt.figure(figsize=(14, 10))

# Scatter plot for athlete data points with three groups
plt.scatter(training_hours, novice_scores, color='lightskyblue', edgecolors='black', s=70, label='Novice Scores')
plt.scatter(training_hours, intermediate_scores, color='royalblue', edgecolors='black', s=100, label='Intermediate Scores')
plt.scatter(training_hours, advanced_scores, color='navy', edgecolors='black', s=120, label='Advanced Scores')

# Plot the smooth fitted curves for each group
plt.plot(fit_x, novice_spline_fit, color='lightcoral', linewidth=2.5, linestyle='--', label='Trend Line (Novice)')
plt.plot(fit_x, intermediate_spline_fit, color='darkorange', linewidth=3, label='Trend Line (Intermediate)')
plt.plot(fit_x, advanced_spline_fit, color='green', linewidth=2.5, linestyle=':', label='Trend Line (Advanced)')

# Customizing plot appearance
plt.title('Impact of Training Hours on Performance in the Galactic Games\nAcross Different Athlete Levels', fontsize=16, fontweight='bold')
plt.xlabel('Training Hours per Week', fontsize=13)
plt.ylabel('Performance Score', fontsize=13)
plt.xticks(np.arange(0, 55, step=5))
plt.yticks(np.arange(40, 110, step=10))
plt.legend(loc='lower right', fontsize=11, frameon=True)
plt.grid(alpha=0.4)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()