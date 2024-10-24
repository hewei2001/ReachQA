import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# New data: Expanded hours spent exercising per week by participants
exercise_hours_expanded = [
    5, 6, 7, 6, 5, 7, 8, 9, 6, 5, 10, 8, 7, 6, 8, 9, 10, 11, 9, 7,
    5, 12, 13, 7, 5, 8, 10, 11, 15, 16, 6, 8, 7, 5, 10, 9, 12, 14, 7, 6,
    9, 11, 9, 8, 10, 6, 12, 13, 5, 14, 17, 8, 9, 7, 10, 8, 6, 10, 11, 12,
    5, 13, 14, 15, 6, 7, 8, 9, 16, 17, 10, 8, 7, 12, 11, 10, 12, 14, 16, 9,
    11, 9, 8, 10, 9, 11, 6, 12, 13, 14, 5, 15, 17, 18, 9, 10, 11, 12, 7, 8
]

# Plot setup
plt.figure(figsize=(14, 8))
bins = np.arange(5, 19, 0.5)  # Refined bin size for complexity
n, bins, patches = plt.hist(exercise_hours_expanded, bins=bins, color='lightgreen', edgecolor='gray', alpha=0.6, histtype='stepfilled', label='Exercise Hours')

# Calculate and overlay a Gaussian fit
(mu, sigma) = norm.fit(exercise_hours_expanded)
y = norm.pdf(bins, mu, sigma) * len(exercise_hours_expanded) * (bins[1] - bins[0])
plt.plot(bins, y, 'r--', linewidth=2, label=f'Gaussian Fit: $\mu={mu:.2f}$, $\sigma={sigma:.2f}$')

# Titles and labels
plt.title('Expanded Distribution of Weekly Exercise Hours\nat the Wellness and Fitness Retreat', fontsize=16, fontweight='bold')
plt.xlabel('Hours Spent Exercising per Week', fontsize=14)
plt.ylabel('Number of Participants', fontsize=14)

# Additional visualization elements
plt.axvline(mu, color='magenta', linestyle='dashed', linewidth=2, label='Mean')
plt.axvline(mu + sigma, color='blue', linestyle='dotted', linewidth=2, label='1 Std Dev')
plt.axvline(mu - sigma, color='blue', linestyle='dotted', linewidth=2)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Annotations
plt.annotate('Peak Exercise Range', xy=(8, 20), xytext=(10, 24),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
             fontsize=12, color='black', ha='center')

# Ensuring layout adjusts to avoid overlap
plt.xticks(np.arange(5, 19, 1), fontsize=12)
plt.yticks(fontsize=12)
plt.legend(loc='upper right', fontsize=12)
plt.tight_layout()

# Display the plot
plt.show()