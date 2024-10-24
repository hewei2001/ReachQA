import matplotlib.pyplot as plt

# Subjects and corresponding student scores
subjects = ['Mathematics', 'Science', 'English', 'History', 'Art']
scores = {
    'Mathematics': [78, 85, 82, 90, 76, 88, 95, 91, 73, 80, 77, 92, 81, 74, 86],
    'Science': [83, 78, 85, 90, 88, 74, 89, 91, 84, 77, 72, 86, 93, 79, 76],
    'English': [80, 75, 85, 88, 82, 79, 91, 87, 83, 78, 81, 77, 89, 92, 84],
    'History': [70, 76, 80, 68, 74, 77, 82, 85, 88, 78, 81, 83, 90, 79, 86],
    'Art': [85, 88, 89, 92, 95, 86, 82, 88, 91, 84, 83, 89, 90, 87, 92]
}

# Collect the scores data
data = [scores[subject] for subject in subjects]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the box plot
box = ax.boxplot(data, patch_artist=True, notch=True, vert=True, 
                 boxprops=dict(facecolor='#cfe2f3', color='black'),
                 whiskerprops=dict(color='black'),
                 capprops=dict(color='black'),
                 medianprops=dict(color='red'),
                 flierprops=dict(markerfacecolor='orange', marker='o', markersize=5))

# Customize and annotate the plot
ax.set_title('Distribution of Student Scores Across Subjects\n(Spring Semester Assessment)', fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Subjects', fontsize=12)
ax.set_ylabel('Scores', fontsize=12)
ax.set_xticks(range(1, len(subjects) + 1))
ax.set_xticklabels(subjects, fontsize=11)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adding a legend
handles = [plt.Line2D([0], [0], color='red', lw=2, label='Median'),
           plt.Line2D([0], [0], marker='o', color='w', label='Outliers', 
                      markerfacecolor='orange', markersize=5)]
ax.legend(handles=handles, loc='upper right', fontsize=10)

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()