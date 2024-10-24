import matplotlib.pyplot as plt
import numpy as np

# Programming Languages
languages = ["Python", "JavaScript", "Java", "C++", "Ruby", "Go"]

# Satisfaction levels (1 to 10 scale) for each programming language
satisfaction_levels = [
    [8, 9, 7, 8, 10, 7, 9, 8, 7, 9, 8, 6, 9, 10, 8, 7, 8, 8],  # Python
    [7, 6, 7, 8, 9, 5, 6, 8, 7, 6, 8, 9, 7, 6, 5, 7, 6, 8],   # JavaScript
    [7, 7, 6, 8, 7, 6, 8, 7, 9, 6, 8, 7, 8, 6, 5, 7, 9, 6],   # Java
    [5, 5, 4, 6, 7, 4, 5, 5, 6, 6, 7, 5, 6, 4, 5, 4, 6, 4],   # C++
    [9, 8, 9, 10, 8, 7, 9, 8, 8, 9, 10, 7, 8, 9, 8, 9, 10, 9], # Ruby
    [8, 7, 8, 9, 7, 8, 8, 9, 7, 8, 9, 8, 9, 8, 7, 8, 8, 7]    # Go
]

# Mean Satisfaction Levels for Bar Chart
mean_satisfaction = [np.mean(level) for level in satisfaction_levels]

# Create the subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))

# Box Plot
box = ax1.boxplot(satisfaction_levels, labels=languages, patch_artist=True, notch=True, vert=False,
                  boxprops=dict(color='blue'),
                  whiskerprops=dict(color='darkblue'),
                  capprops=dict(color='darkblue'),
                  medianprops=dict(color='darkred', linewidth=2),
                  flierprops=dict(marker='o', color='red', alpha=0.5))

# Color customization for each box
colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightcoral', 'lightgrey', 'lightpink']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Titles and labels for the box plot
ax1.set_title("User Satisfaction Levels in Software Development\n(Box Plot Analysis)", fontsize=14, fontweight='bold')
ax1.set_xlabel("Satisfaction Level (1 to 10)", fontsize=12)
ax1.set_ylabel("Programming Languages", fontsize=12)
ax1.grid(axis='x', linestyle='--', alpha=0.6)

# Bar Chart
ax2.barh(languages, mean_satisfaction, color='lightblue', edgecolor='black')
ax2.set_title("Average Satisfaction Levels Across Programming Languages\n(Bar Chart Analysis)", fontsize=14, fontweight='bold')
ax2.set_xlabel("Average Satisfaction Level (1 to 10)", fontsize=12)
ax2.set_ylabel("Programming Languages", fontsize=12)
ax2.set_xlim(0, 10)

# Tight layout to prevent overlapping
plt.tight_layout()
plt.show()