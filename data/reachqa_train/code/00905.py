import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial

# Expanded Sleep durations in hours per night
sleep_durations = np.array([3, 4, 5, 6, 7, 8, 9, 10, 11])

# Mean cognitive performance scores for different age groups
mean_scores_youth = np.array([55, 60, 68, 75, 82, 85, 84, 80, 76])
mean_scores_adults = np.array([50, 55, 62, 70, 78, 83, 81, 77, 73])

# Standard deviation indicating variability in scores
std_devs_youth = np.array([6, 5, 4, 3, 3, 2, 3, 4, 5])
std_devs_adults = np.array([5, 4, 3, 2, 2, 3, 4, 5, 6])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot line chart with error bars for youth
ax.errorbar(sleep_durations, mean_scores_youth, yerr=std_devs_youth, fmt='-o', color='royalblue',
            ecolor='lightcoral', elinewidth=2, capsize=5, alpha=0.8, label='Youth Scores ± SD')

# Plot line chart with error bars for adults
ax.errorbar(sleep_durations, mean_scores_adults, yerr=std_devs_adults, fmt='-s', color='darkorange',
            ecolor='lightgray', elinewidth=2, capsize=5, alpha=0.8, label='Adult Scores ± SD')

# Fit a polynomial regression line for youth
p_youth = Polynomial.fit(sleep_durations, mean_scores_youth, deg=3)
ax.plot(*p_youth.linspace(), color='blue', linestyle='--', label='Youth Trend')

# Fit a polynomial regression line for adults
p_adults = Polynomial.fit(sleep_durations, mean_scores_adults, deg=3)
ax.plot(*p_adults.linspace(), color='orange', linestyle='--', label='Adult Trend')

# Highlight peak performance with annotations for both groups
ax.annotate('Peak Performance (Youth)', xy=(8, 85), xytext=(7, 87),
            arrowprops=dict(facecolor='green', arrowstyle='->'),
            fontsize=10, color='darkgreen')

ax.annotate('Peak Performance (Adults)', xy=(8, 83), xytext=(9, 85),
            arrowprops=dict(facecolor='purple', arrowstyle='->'),
            fontsize=10, color='purple')

# Title and labels
ax.set_title("Impact of Sleep Duration on Cognitive Performance\nAcross Different Age Groups",
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Sleep Duration (hours per night)", fontsize=12)
ax.set_ylabel("Cognitive Performance Score", fontsize=12)

# Set limits for clarity
ax.set_ylim(45, 90)
ax.set_xlim(2.5, 11.5)

# Add grid
ax.grid(True, linestyle='--', alpha=0.6)

# Add a legend in a clear area
ax.legend(loc='upper right', fontsize=10)

# Automatically adjust layout for readability
plt.tight_layout()

# Display the plot
plt.show()