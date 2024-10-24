import matplotlib.pyplot as plt
import numpy as np

# Original data for boxplot
reading_hours = [
    [10, 12, 8, 15, 10, 11, 14, 13, 9, 7, 12, 10, 11],  # First Year
    [14, 16, 15, 13, 17, 15, 18, 20, 16, 14, 19, 18, 16],  # Second Year
    [18, 20, 22, 19, 21, 23, 25, 24, 22, 20, 19, 24, 22],  # Third Year
    [12, 15, 14, 13, 18, 17, 16, 15, 14, 15, 17, 19, 14]   # Fourth Year
]

# Construct combined data for histogram subplot
combined_hours = sum(reading_hours, [])

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# First subplot: Box plot
boxplot = axs[0].boxplot(reading_hours, patch_artist=True, notch=True, vert=True, showmeans=True)
colors = ['skyblue', 'lightgreen', 'lightcoral', 'navajowhite']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)
for median in boxplot['medians']:
    median.set(color='purple', linewidth=1.5)
for mean in boxplot['means']:
    mean.set(marker='o', markerfacecolor='black', markeredgecolor='black')

axs[0].set_title("Reading Habits of University Students\nby Year of Study", fontsize=14, fontweight='bold')
axs[0].set_xlabel("Year of Study", fontsize=12)
axs[0].set_ylabel("Hours of Reading per Week", fontsize=12)
axs[0].set_xticklabels(["First Year", "Second Year", "Third Year", "Fourth Year"])
axs[0].yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Second subplot: Histogram
axs[1].hist(combined_hours, bins=10, color='lightcoral', edgecolor='black', alpha=0.7)
axs[1].set_title("Distribution of Reading Hours\nAcross All Cohorts", fontsize=14, fontweight='bold')
axs[1].set_xlabel("Hours of Reading per Week", fontsize=12)
axs[1].set_ylabel("Number of Students", fontsize=12)
axs[1].yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()