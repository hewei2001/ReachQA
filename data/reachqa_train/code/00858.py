import numpy as np
import matplotlib.pyplot as plt

# Data: Weekly study hours for students in each subject
study_hours = {
    "Mathematics": [12, 15, 14, 20, 18, 22, 25, 17, 10, 16, 14, 15, 19, 18, 13, 21],
    "Biology": [10, 12, 11, 15, 13, 17, 19, 14, 11, 16, 18, 12, 14, 15, 16, 17],
    "Psychology": [8, 9, 10, 12, 11, 13, 14, 10, 9, 8, 12, 13, 11, 10, 15, 14],
    "Computer Science": [14, 18, 16, 19, 20, 21, 22, 17, 16, 18, 15, 20, 19, 17, 22, 18],
    "English Literature": [7, 9, 10, 8, 9, 12, 13, 11, 9, 8, 10, 12, 11, 8, 9, 10]
}

# Related data: Average test scores for the same subjects
average_scores = {
    "Mathematics": 85,
    "Biology": 78,
    "Psychology": 74,
    "Computer Science": 88,
    "English Literature": 69
}

subjects = list(study_hours.keys())
data = list(study_hours.values())
scores = [average_scores[subject] for subject in subjects]

fig, axes = plt.subplots(1, 2, figsize=(14, 8))

# Plot 1: Horizontal box plot for study hours
axes[0].boxplot(data, vert=False, patch_artist=True, labels=subjects, notch=True,
                boxprops=dict(facecolor='#add8e6', color='black'),
                whiskerprops=dict(color='black'),
                capprops=dict(color='black'),
                flierprops=dict(marker='o', markerfacecolor='red', markersize=8, linestyle='none'),
                medianprops=dict(color='darkblue', linewidth=2))

colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']
for patch, color in zip(axes[0].artists, colors):
    patch.set_facecolor(color)

axes[0].set_title("Distribution of Weekly Study Hours\nAmong College Students", fontsize=12, weight='bold')
axes[0].set_xlabel("Weekly Study Hours", fontsize=10)
axes[0].set_ylabel("Subjects", fontsize=10)
axes[0].grid(axis='x', linestyle='--', alpha=0.7)

# Plot 2: Scatter plot for average scores
axes[1].scatter(subjects, scores, color=colors, s=100)
axes[1].set_title("Average Test Scores by Subject", fontsize=12, weight='bold')
axes[1].set_xlabel("Subjects", fontsize=10)
axes[1].set_ylabel("Average Test Score", fontsize=10)
axes[1].set_ylim(65, 95)

for i, txt in enumerate(scores):
    axes[1].annotate(txt, (subjects[i], scores[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=9)

fig.suptitle("Academic Focus and Performance Analysis", fontsize=14, weight='bold')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()