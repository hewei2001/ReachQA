import matplotlib.pyplot as plt
import numpy as np

# Define companies and their employee satisfaction scores
companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Company E']
satisfaction_scores = [
    [7, 8, 9, 6, 8, 9, 7, 8, 10, 7],  # Company A
    [5, 6, 5, 7, 6, 8, 5, 7, 6, 7],  # Company B
    [9, 8, 10, 7, 9, 8, 10, 9, 8, 9], # Company C
    [6, 7, 6, 5, 7, 6, 8, 7, 5, 6],  # Company D
    [8, 9, 8, 9, 7, 9, 8, 10, 8, 9]  # Company E
]

# Modify data for the new plot (slightly altered scores for diversity)
satisfaction_scores_2 = [
    [6.5, 8, 9.5, 6, 8.2, 9, 7.1, 8, 10, 7.5],  # Company A
    [5.2, 6.3, 5.1, 7, 6.1, 8, 5.6, 7.3, 6.5, 7],  # Company B
    [9, 8.1, 10, 7.5, 9.3, 8.5, 10.2, 9, 8.3, 9.1], # Company C
    [6.2, 7, 6.5, 5.3, 7.1, 6.8, 8, 7.4, 5.5, 6],  # Company D
    [8.1, 9.3, 8.5, 9, 7.2, 9.1, 8, 10, 8.2, 9]   # Company E
]

# Create subplots: 1 row, 2 columns
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Plot the horizontal box plot
boxplot = ax1.boxplot(satisfaction_scores, vert=False, patch_artist=True, notch=True, whis=1.5)
colors = ['skyblue', 'lightgreen', 'salmon', 'lightcoral', 'plum']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)
for whisker in boxplot['whiskers']:
    whisker.set(color='black', linewidth=1.5)
for median in boxplot['medians']:
    median.set(color='blue', linewidth=2)
ax1.set_yticklabels(companies)
ax1.set_xlabel('Satisfaction Score', fontsize=12)
ax1.set_title('Employee Satisfaction Scores\nAcross Leading Tech Companies', fontsize=14, fontweight='bold', pad=15)
ax1.grid(True, linestyle='--', alpha=0.6)

# Plot the violin plot
parts = ax2.violinplot(satisfaction_scores_2, vert=False, showmeans=False, showmedians=True)
for pc, color in zip(parts['bodies'], colors):
    pc.set_facecolor(color)
    pc.set_alpha(0.7)
parts['cmedians'].set_edgecolor('blue')
parts['cmedians'].set_linewidth(2)
ax2.set_yticks(np.arange(1, len(companies) + 1))
ax2.set_yticklabels(companies)
ax2.set_xlabel('Satisfaction Score', fontsize=12)
ax2.set_title('Distribution of Satisfaction Scores\nwith Enhanced Detail', fontsize=14, fontweight='bold', pad=15)
ax2.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to fit elements well
plt.tight_layout()

# Display the chart
plt.show()