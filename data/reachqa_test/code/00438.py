import matplotlib.pyplot as plt
import numpy as np

# Define the subjects for performance analysis
subjects = ['Mathematics', 'Science', 'English', 'History']

# Artificial student score data for each subject
math_scores = [72, 85, 78, 92, 88, 95, 62, 89, 75, 94, 77, 84, 91, 79, 82]
science_scores = [65, 78, 82, 72, 69, 85, 80, 77, 91, 76, 74, 88, 70, 83, 79]
english_scores = [88, 92, 95, 83, 87, 79, 85, 90, 76, 81, 82, 93, 89, 86, 94]
history_scores = [73, 68, 74, 85, 79, 78, 91, 84, 77, 80, 82, 69, 70, 76, 75]

# Combine the scores into a list for the box plot
data = [math_scores, science_scores, english_scores, history_scores]

# Calculate mean scores for each subject for the bar plot
mean_scores = [np.mean(scores) for scores in data]

# Creating the figure and axis for the plots
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# Plot the box plot on the first subplot
axs[0].boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.6,
               boxprops=dict(facecolor='lightblue', color='navy', linewidth=1.5),
               whiskerprops=dict(color='black', linewidth=1.5),
               capprops=dict(color='black', linewidth=1.5),
               medianprops=dict(color='red', linewidth=2),
               flierprops=dict(marker='o', color='orange', markersize=8, alpha=0.6))

axs[0].set_title('Student Performance Across\nCore Subjects', fontsize=14, fontweight='bold', color='darkblue')
axs[0].set_xticklabels(subjects, fontsize=12)
axs[0].set_ylabel('Scores', fontsize=12, fontweight='bold', color='darkblue')
axs[0].yaxis.grid(True, linestyle='--', alpha=0.7)
axs[0].set_facecolor('#f7f7f7')

# Explanation of plot elements for the box plot
axs[0].text(0.5, -0.1, 'Notches show median variability\nRed lines indicate median scores',
            ha='center', va='center', transform=axs[0].transAxes, fontsize=10, color='grey')

# Plot the bar plot on the second subplot
bars = axs[1].bar(subjects, mean_scores, color='skyblue', edgecolor='navy', linewidth=1.5)
axs[1].set_title('Average Scores Per Subject', fontsize=14, fontweight='bold', color='darkblue')
axs[1].set_ylabel('Average Score', fontsize=12, fontweight='bold', color='darkblue')
axs[1].set_ylim(0, 100)
axs[1].set_facecolor('#f7f7f7')

# Annotate each bar with its mean value
for bar, mean in zip(bars, mean_scores):
    axs[1].text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 5,
                f'{mean:.1f}', ha='center', va='bottom', color='darkblue', fontsize=11)

# Adjust layout to prevent overlapping and ensure the plots are well-aligned
plt.tight_layout()

# Display the plots
plt.show()