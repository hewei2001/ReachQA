import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Data: Number of languages spoken and corresponding communication satisfaction levels
languages_spoken = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10])
satisfaction_level = np.array([4, 5, 5, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 9, 10])

# Remove duplicates by averaging the satisfaction levels for each number of languages spoken
unique_languages, indices = np.unique(languages_spoken, return_inverse=True)
avg_satisfaction = np.zeros_like(unique_languages, dtype=float)
for i in range(len(unique_languages)):
    avg_satisfaction[i] = satisfaction_level[indices == i].mean()

# Define a spline interpolation to create a smooth curve
x_new = np.linspace(unique_languages.min(), unique_languages.max(), 300)
spline = make_interp_spline(unique_languages, avg_satisfaction, k=3)  # Cubic spline
y_smooth = spline(x_new)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(languages_spoken, satisfaction_level, color='dodgerblue', label='Observed Data', s=80, alpha=0.8, edgecolor='k')
plt.plot(x_new, y_smooth, color='orange', label='Smooth Fitting Curve', linewidth=2)

# Customizing the plot
plt.title('Impact of Multilingual Abilities on Communication\nSatisfaction', fontsize=16, color='darkblue')
plt.xlabel('Number of Languages Spoken', fontsize=12)
plt.ylabel('Communication Satisfaction Level', fontsize=12)
plt.xticks(np.arange(1, 11, 1))
plt.yticks(np.arange(1, 11, 1))
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='lower right', fontsize=10)

# Annotate some key points for clarity
highlight_points = [(2, 5), (5, 8), (9, 9)]
for (x, y) in highlight_points:
    plt.annotate(f'({x}, {y})', xy=(x, y), xytext=(-30, 10),
                 textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'),
                 fontsize=9, color='darkred')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()