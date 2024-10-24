import matplotlib.pyplot as plt
import numpy as np

# Increased number of subjects and scores for more complexity
subjects = ['Mathematics', 'Science', 'English', 'History', 'Art', 'Physics', 'Chemistry', 'Geography', 'Music']
scores = {
    'Mathematics': np.random.normal(80, 10, 40).tolist(),
    'Science': np.random.normal(75, 12, 40).tolist(),
    'English': np.random.normal(82, 8, 40).tolist(),
    'History': np.random.normal(78, 15, 40).tolist(),
    'Art': np.random.normal(90, 5, 40).tolist(),
    'Physics': np.random.normal(70, 20, 40).tolist(),
    'Chemistry': np.random.normal(68, 18, 40).tolist(),
    'Geography': np.random.normal(85, 7, 40).tolist(),
    'Music': np.random.normal(88, 6, 40).tolist()
}

# Collect the scores data
data = [scores[subject] for subject in subjects]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(16, 9))

# Plot the box plot
box = ax.boxplot(data, patch_artist=True, notch=True, vert=True, 
                 boxprops=dict(facecolor='lightblue', color='navy'),
                 whiskerprops=dict(color='navy'),
                 capprops=dict(color='navy'),
                 medianprops=dict(color='red'),
                 flierprops=dict(markerfacecolor='yellow', marker='D', markersize=6))

# Customize and annotate the plot
ax.set_title('Student Scores Distribution Across Subjects\nfor the Spring Semester Assessment', fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Subjects', fontsize=14)
ax.set_ylabel('Scores', fontsize=14)
ax.set_xticks(range(1, len(subjects) + 1))
ax.set_xticklabels(subjects, fontsize=12, rotation=15)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adding a legend for clarity
handles = [plt.Line2D([0], [0], color='red', lw=2, label='Median'),
           plt.Line2D([0], [0], marker='D', color='w', label='Outliers', 
                      markerfacecolor='yellow', markersize=6)]
ax.legend(handles=handles, loc='upper right', fontsize=10)

# Additional annotations and calculations
means = [np.mean(scores[subject]) for subject in subjects]
std_devs = [np.std(scores[subject]) for subject in subjects]
for i, (mean, std) in enumerate(zip(means, std_devs), start=1):
    ax.text(i, 105, f'Mean: {mean:.1f}\nSD: {std:.1f}', ha='center', va='bottom', fontsize=10, color='darkgreen')

# Swarm plot overlay
for i, subject_scores in enumerate(data, start=1):
    y = subject_scores
    x = np.random.normal(i, 0.04, size=len(y))
    ax.scatter(x, y, alpha=0.5, color='orange', edgecolor='w', s=15, label='Individual Scores' if i == 1 else "")

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()