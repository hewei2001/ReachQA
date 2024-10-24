import matplotlib.pyplot as plt
import numpy as np

# Sample satisfaction data for each department (scale: 0-10)
engineering_scores = np.array([8, 7, 9, 6, 7, 9, 8, 8, 6, 7, 7, 8, 9, 5, 9])
marketing_scores = np.array([7, 6, 5, 8, 6, 7, 7, 5, 6, 8, 9, 6, 5, 7, 6])
sales_scores = np.array([6, 5, 5, 7, 6, 4, 5, 6, 4, 5, 5, 7, 8, 5, 5])
hr_scores = np.array([9, 8, 9, 9, 8, 9, 10, 8, 9, 8, 10, 9, 9, 8, 10])
it_support_scores = np.array([5, 6, 5, 6, 5, 5, 5, 6, 6, 5, 6, 6, 5, 5, 4])

# New data for average scores
average_scores = [
    engineering_scores.mean(), marketing_scores.mean(),
    sales_scores.mean(), hr_scores.mean(), it_support_scores.mean()
]

# Create a figure with 1x2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Box plot on the first axis
data = [engineering_scores, marketing_scores, sales_scores, hr_scores, it_support_scores]
labels = ['Engineering', 'Marketing', 'Sales', 'HR', 'IT Support']
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']

box = ax1.boxplot(data, patch_artist=True, labels=labels, notch=True, vert=True)
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.setp(box['whiskers'], color='black', linestyle='--')
plt.setp(box['caps'], color='black')
plt.setp(box['medians'], color='red', linewidth=2)

ax1.set_title('Employee Satisfaction by Department\nInnovatech Solutions Annual Survey', fontsize=14, fontweight='bold')
ax1.set_ylabel('Satisfaction Score (0-10)', fontsize=12)
ax1.yaxis.grid(True, linestyle='--', color='grey', alpha=0.5)
ax1.set_xticklabels(labels, rotation=45, fontsize=10)

ax1.annotate('Notably High\nSatisfaction in HR', xy=(4, 10), xytext=(3.5, 9.5),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='right', va='bottom')

# Bar plot for average satisfaction scores on the second axis
bars = ax2.bar(labels, average_scores, color=colors, alpha=0.7)
ax2.set_title('Average Satisfaction Score by Department', fontsize=14, fontweight='bold')
ax2.set_ylabel('Average Satisfaction Score', fontsize=12)
ax2.set_ylim(0, 10)
ax2.yaxis.grid(True, linestyle='--', color='grey', alpha=0.5)
ax2.set_xticklabels(labels, rotation=45, fontsize=10)

# Annotate bars with the average score
for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 0.2, round(yval, 1), ha='center', va='bottom', fontsize=10)

# Layout adjustment
plt.tight_layout()

# Display the plots
plt.show()