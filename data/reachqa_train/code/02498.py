import matplotlib.pyplot as plt
import numpy as np

# Expanded dataset: hours spent on various leisure activities per week
sports_hours = [3, 6, 9, 12, 1, 5, 11, 14, 10, 9, 2, 8, 12, 6, 7, 5, 3, 12, 11, 7, 4, 6, 8, 9, 10, 12, 14, 15, 3, 4, 8, 5, 7, 2, 10, 11, 13, 15, 5, 6, 9, 7, 6, 5, 4]
reading_hours = [2, 4, 3, 6, 3, 5, 7, 6, 8, 2, 1, 4, 3, 6, 4, 5, 3, 0, 2, 6, 5, 4, 3, 1, 8, 7, 9, 6, 5, 3, 2, 4, 5, 3, 6, 7, 5, 4, 3, 2, 1]
socializing_hours = [12, 14, 16, 18, 15, 17, 13, 20, 19, 11, 14, 16, 13, 15, 17, 19, 20, 18, 15, 13, 14, 16, 18, 19, 17, 15, 14, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7]
watching_tv_hours = [25, 28, 26, 30, 29, 27, 24, 23, 21, 22, 30, 28, 25, 24, 23, 29, 27, 26, 25, 24, 23, 22, 21, 20, 29, 30, 28, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14]
others_hours = [1, 2, 1, 3, 4, 2, 5, 1, 3, 2, 4, 1, 2, 3, 1, 4, 5, 2, 1, 2, 3, 1, 4, 5, 2, 3, 4, 0, 1, 2, 3]
gaming_hours = [10, 11, 12, 9, 8, 7, 6, 5, 4, 3, 10, 11, 12, 8, 9, 11, 14, 13, 12, 9, 10, 8, 7, 6, 5, 3, 4, 2]

# Creating figure and subplots
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('Leisure Time Allocation in Leisureville', fontsize=18, fontweight='bold')

# Histogram of hours spent on each activity
activity_hours = [sports_hours, reading_hours, socializing_hours, watching_tv_hours, others_hours, gaming_hours]
activity_labels = ['Sports', 'Reading', 'Socializing', 'Watching TV', 'Others', 'Gaming']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Shared bin setup for consistency
bins = np.arange(0, 35, 5)

for ax, hours, label, color in zip(axes.flatten(), activity_hours, activity_labels, colors):
    ax.hist(hours, bins=bins, color=color, edgecolor='black', alpha=0.7, label=label)
    ax.set_title(label, fontsize=14)
    ax.set_xlabel('Hours Spent', fontsize=10)
    ax.set_ylabel('Number of Participants', fontsize=10)
    ax.legend(loc='upper right')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to avoid overlapping
fig.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plot
plt.show()