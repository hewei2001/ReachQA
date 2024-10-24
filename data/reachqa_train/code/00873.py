import numpy as np
import matplotlib.pyplot as plt

# Artificial data: exam scores for each grade
grade_6_scores = [45, 55, 60, 62, 65, 70, 71, 72, 75, 80, 82, 85, 88, 90, 92]
grade_7_scores = [50, 53, 58, 60, 63, 67, 70, 74, 75, 77, 80, 82, 84, 87, 91]
grade_8_scores = [52, 56, 59, 61, 65, 68, 70, 72, 76, 78, 79, 81, 83, 86, 89]
grade_9_scores = [55, 57, 60, 63, 66, 69, 71, 73, 76, 78, 80, 82, 85, 87, 90]
grade_10_scores = [60, 62, 65, 67, 70, 73, 75, 77, 79, 81, 84, 86, 89, 92, 95]

# Combine the scores into a list
all_scores = [grade_6_scores, grade_7_scores, grade_8_scores, grade_9_scores, grade_10_scores]

# Plotting the Vertical Box Chart
fig, ax = plt.subplots(figsize=(10, 6))

# Create the boxplot
box = ax.boxplot(all_scores, patch_artist=True, notch=True, 
           boxprops=dict(facecolor='#c9c9ff', color='#0000ff'),
           whiskerprops=dict(color='#0000ff'),
           capprops=dict(color='#0000ff'),
           medianprops=dict(color='red'))

# Customize the plot
ax.set_title('Student Performance in Mathematics Exams by Grade', fontsize=14, loc='center', wrap=True)
ax.set_xlabel('Grade Level', fontsize=12)
ax.set_ylabel('Exam Scores', fontsize=12)
ax.set_xticklabels(['Grade 6', 'Grade 7', 'Grade 8', 'Grade 9', 'Grade 10'], fontsize=10)

# Add grid for clarity
ax.yaxis.grid(True, linestyle='--', alpha=0.5)

# Highlight the grade with the most variance
ax.annotate('Highest Variance\nin Scores', xy=(4, 92), xytext=(3.5, 96),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the chart
plt.show()