import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Original Data
languages_spoken = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10])
satisfaction_level = np.array([4, 5, 5, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 9, 10])

# Remove duplicates by averaging the satisfaction levels for duplicate languages spoken
unique_languages = np.unique(languages_spoken)
avg_satisfaction = [satisfaction_level[languages_spoken == lang].mean() for lang in unique_languages]

# Convert to NumPy arrays for plotting
unique_languages = np.array(unique_languages)
avg_satisfaction = np.array(avg_satisfaction)

# Prepare Spline Interpolation Data
x_new = np.linspace(unique_languages.min(), unique_languages.max(), 300)
spline = make_interp_spline(unique_languages, avg_satisfaction, k=3)
y_smooth = spline(x_new)

# Additional Data for Subplot: Frequency of Satisfaction Levels
unique_levels, frequency = np.unique(satisfaction_level, return_counts=True)

# Setting up the subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))

# Plot 1: Scatter and Spline Curve
axes[0].scatter(unique_languages, avg_satisfaction, color='dodgerblue', s=80, alpha=0.8, edgecolor='k')
axes[0].plot(x_new, y_smooth, color='orange', linewidth=2)
axes[0].set_title('Impact of Multilingual Abilities on\nCommunication Satisfaction', fontsize=14, color='darkblue')
axes[0].set_xlabel('Number of Languages Spoken', fontsize=12)
axes[0].set_ylabel('Communication Satisfaction Level', fontsize=12)
axes[0].set_xticks(np.arange(1, 11, 1))
axes[0].set_yticks(np.arange(1, 11, 1))
axes[0].grid(True, linestyle='--', alpha=0.7)
highlight_points = [(2, 5), (5, 8), (9, 9)]
for (x, y) in highlight_points:
    axes[0].annotate(f'({x}, {y})', xy=(x, y), xytext=(-30, 10),
                     textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'),
                     fontsize=9, color='darkred')

# Plot 2: Bar Chart of Satisfaction Level Frequency
axes[1].bar(unique_levels, frequency, color='seagreen', alpha=0.7, edgecolor='black')
axes[1].set_title('Frequency of Communication Satisfaction Levels', fontsize=14, color='darkblue')
axes[1].set_xlabel('Satisfaction Level', fontsize=12)
axes[1].set_ylabel('Frequency', fontsize=12)
axes[1].set_xticks(unique_levels)
axes[1].set_yticks(np.arange(0, max(frequency) + 1, 1))
axes[1].grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()