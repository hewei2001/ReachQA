import numpy as np
import matplotlib.pyplot as plt

# Original data: exam scores for each grade
grade_6_scores = [45, 55, 60, 62, 65, 70, 71, 72, 75, 80, 82, 85, 88, 90, 92]
grade_7_scores = [50, 53, 58, 60, 63, 67, 70, 74, 75, 77, 80, 82, 84, 87, 91]
grade_8_scores = [52, 56, 59, 61, 65, 68, 70, 72, 76, 78, 79, 81, 83, 86, 89]
grade_9_scores = [55, 57, 60, 63, 66, 69, 71, 73, 76, 78, 80, 82, 85, 87, 90]
grade_10_scores = [60, 62, 65, 67, 70, 73, 75, 77, 79, 81, 84, 86, 89, 92, 95]

# Create a slightly varied dataset for the violin plot
grade_6_scores_v = [x + np.sin(i) * 2 for i, x in enumerate(grade_6_scores)]
grade_7_scores_v = [x + np.cos(i) * 1.5 for i, x in enumerate(grade_7_scores)]
grade_8_scores_v = [x + np.sin(i/2) for i, x in enumerate(grade_8_scores)]
grade_9_scores_v = [x + np.cos(i/3) * 2 for i, x in enumerate(grade_9_scores)]
grade_10_scores_v = [x + np.sin(i/4) for i, x in enumerate(grade_10_scores)]

# Combine the scores into lists for plotting
all_scores = [grade_6_scores, grade_7_scores, grade_8_scores, grade_9_scores, grade_10_scores]
all_scores_v = [grade_6_scores_v, grade_7_scores_v, grade_8_scores_v, grade_9_scores_v, grade_10_scores_v]

# Setup for subplots
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# Plotting the boxplot
box = axs[0].boxplot(all_scores, patch_artist=True, notch=True,
                     boxprops=dict(facecolor='#c9c9ff', color='#0000ff'),
                     whiskerprops=dict(color='#0000ff'),
                     capprops=dict(color='#0000ff'),
                     medianprops=dict(color='red'))

axs[0].set_title('Mathematics Exam Scores by Grade Level\n(Boxplot)', fontsize=12, wrap=True)
axs[0].set_xlabel('Grade Level', fontsize=10)
axs[0].set_ylabel('Exam Scores', fontsize=10)
axs[0].set_xticklabels(['Grade 6', 'Grade 7', 'Grade 8', 'Grade 9', 'Grade 10'], fontsize=9)
axs[0].yaxis.grid(True, linestyle='--', alpha=0.5)
axs[0].annotate('Highest Variance\nin Scores', xy=(4, 92), xytext=(3.5, 96),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=8)

# Plotting the violin plot
violins = axs[1].violinplot(all_scores_v, showmeans=False, showmedians=True)
for pc in violins['bodies']:
    pc.set_facecolor('#ffcccb')
    pc.set_edgecolor('#ff5733')
    pc.set_alpha(0.6)

axs[1].set_title('Mathematics Exam Scores by Grade Level\n(Violin Plot)', fontsize=12, wrap=True)
axs[1].set_xlabel('Grade Level', fontsize=10)
axs[1].set_ylabel('Exam Scores', fontsize=10)
axs[1].set_xticks([1, 2, 3, 4, 5])
axs[1].set_xticklabels(['Grade 6', 'Grade 7', 'Grade 8', 'Grade 9', 'Grade 10'], fontsize=9)
axs[1].yaxis.grid(True, linestyle='--', alpha=0.5)
axs[1].annotate('Interesting Distribution', xy=(3, 85), xytext=(2.5, 89),
                arrowprops=dict(facecolor='green', arrowstyle='->'), fontsize=8)

plt.tight_layout()
plt.show()