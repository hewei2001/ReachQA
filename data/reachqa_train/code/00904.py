import matplotlib.pyplot as plt
import numpy as np

# Sleep durations in hours per night
sleep_durations = np.array([4, 5, 6, 7, 8, 9, 10])

# Mean cognitive performance scores
mean_scores = np.array([60, 65, 70, 80, 85, 83, 78])

# Standard deviation indicating variability in scores
std_devs = np.array([5, 4, 3, 2, 2, 3, 4])

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot line chart with error bars
ax.errorbar(sleep_durations, mean_scores, yerr=std_devs, fmt='-o', color='royalblue', ecolor='lightcoral',
            elinewidth=2, capsize=5, alpha=0.8, label='Mean Cognitive Score ± SD')

# Highlight peak performance with annotation
ax.annotate('Peak Performance', xy=(8, 85), xytext=(7, 88),
            arrowprops=dict(facecolor='green', arrowstyle='->'),
            fontsize=10, color='darkgreen')

# Title and labels
ax.set_title("Influence of Sleep Duration on Cognitive Performance:\nA Study Overview",
             fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel("Sleep Duration (hours per night)", fontsize=12)
ax.set_ylabel("Cognitive Performance Score", fontsize=12)

# Set limits for clarity
ax.set_ylim(50, 90)
ax.set_xlim(3.5, 10.5)

# Add grid
ax.grid(True, linestyle='--', alpha=0.6)

# Add a legend in a clear area
ax.legend(loc='upper left', fontsize=10)

# Automatically adjust layout for readability
plt.tight_layout()

# Display the plot
plt.show()