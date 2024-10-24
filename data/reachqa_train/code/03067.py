import matplotlib.pyplot as plt
import numpy as np

# Original satisfaction scores for each department
technology_scores = [7, 8, 6, 9, 8, 7, 9, 8, 8, 7, 10, 8, 7, 6, 8]
marketing_scores = [5, 6, 7, 5, 6, 6, 7, 6, 6, 5, 5, 7, 6, 8, 5]
sales_scores = [6, 7, 6, 5, 8, 7, 6, 5, 6, 7, 5, 8, 6, 7, 6]
finance_scores = [8, 9, 8, 9, 7, 8, 8, 7, 9, 9, 8, 7, 9, 8, 8]
hr_scores = [9, 10, 9, 8, 9, 10, 8, 9, 8, 9, 10, 9, 9, 8, 9]

# Additional satisfaction-related data for departments
technology_engagement = [6, 7, 7, 8, 7, 8, 8, 6, 9, 8, 8, 7, 8, 8, 7]
marketing_engagement = [4, 5, 6, 5, 5, 6, 6, 5, 5, 6, 5, 6, 5, 7, 6]
sales_engagement = [5, 6, 5, 6, 7, 6, 5, 6, 6, 7, 6, 7, 5, 7, 6]
finance_engagement = [7, 8, 7, 8, 8, 8, 7, 8, 9, 8, 8, 7, 8, 9, 8]
hr_engagement = [8, 9, 9, 8, 9, 8, 9, 8, 9, 9, 9, 8, 8, 9, 8]

# Aggregate the data for plots
satisfaction_scores = [technology_scores, marketing_scores, sales_scores, finance_scores, hr_scores]
engagement_scores = [technology_engagement, marketing_engagement, sales_engagement, finance_engagement, hr_engagement]
departments = ['Technology', 'Marketing', 'Sales', 'Finance', 'Human Resources']

# Set up the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [1, 1.5]})

# Plot the original box plot
ax1.boxplot(satisfaction_scores, vert=False, patch_artist=True, notch=True, whis=1.5,
            boxprops=dict(facecolor="lightblue", color="navy"),
            whiskerprops=dict(color="navy"),
            capprops=dict(color="navy"),
            flierprops=dict(marker="o", color="red", alpha=0.5),
            medianprops=dict(color="darkorange"))
ax1.set_title("Employee Satisfaction Scores\nAcross Departments", fontsize=14, fontweight='bold')
ax1.set_xlabel("Satisfaction Score", fontsize=12)
ax1.set_yticklabels(departments, fontsize=12)
ax1.set_xlim(0, 11)
ax1.grid(True, linestyle='--', alpha=0.7)

# Plot the violin plot for engagement scores
violin_parts = ax2.violinplot(engagement_scores, vert=False, showmeans=False, showmedians=True)
for pc in violin_parts['bodies']:
    pc.set_facecolor('lightgreen')
    pc.set_edgecolor('forestgreen')
    pc.set_alpha(0.7)
for partname in ('cbars', 'cmins', 'cmaxes', 'cmedians'):
    vp = violin_parts[partname]
    vp.set_edgecolor('forestgreen')
    vp.set_linewidth(1.5)

ax2.set_title("Employee Engagement Scores\nAcross Departments", fontsize=14, fontweight='bold')
ax2.set_xlabel("Engagement Score", fontsize=12)
ax2.set_xlim(0, 11)
ax2.set_yticks(range(1, len(departments) + 1))
ax2.set_yticklabels(departments, fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.7)

# Adjust layout for better readability
plt.tight_layout()

# Show the plot
plt.show()