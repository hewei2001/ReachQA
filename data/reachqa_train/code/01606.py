import matplotlib.pyplot as plt
import numpy as np

# Define the departments and grades for each
departments = ['Computer Science', 'English Literature', 'Mechanical Engineering', 'Biology', 'Economics']

# Student grades for each department
grades_data = [
    [85, 78, 92, 88, 79, 83, 91, 76, 85, 89, 90, 81],  # Computer Science
    [72, 68, 80, 75, 82, 79, 74, 71, 73, 77, 70, 69],  # English Literature
    [81, 85, 88, 89, 86, 84, 87, 90, 83, 82, 86, 85],  # Mechanical Engineering
    [89, 93, 91, 87, 92, 90, 85, 88, 94, 89, 90, 91],  # Biology
    [78, 74, 76, 82, 79, 73, 77, 75, 80, 78, 72, 74],  # Economics
]

# Create a 1x2 subplot layout
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Box Plot
ax1 = axs[0]
boxprops = dict(facecolor='#FFD700', color='darkblue')
whiskerprops = dict(color='darkblue', linestyle='--')
capprops = dict(color='darkblue')
flierprops = dict(markerfacecolor='red', marker='o', markersize=8, linestyle='none')
medianprops = dict(color='green', linewidth=2)

boxes = ax1.boxplot(grades_data, vert=True, patch_artist=True, notch=False,
                    boxprops=boxprops, whiskerprops=whiskerprops,
                    capprops=capprops, flierprops=flierprops,
                    medianprops=medianprops)

colors = ['#87CEEB', '#FFB6C1', '#98FB98', '#FFD700', '#FFA07A']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

ax1.set_xticks(range(1, len(departments) + 1))
ax1.set_xticklabels(departments, fontsize=10, rotation=15)

ax1.set_title("Distribution of Grades Across Departments\nat Greenwood College (2022-2023)", fontsize=14, fontweight='bold')
ax1.set_ylabel("Grade", fontsize=12)
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

legend_handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax1.legend(legend_handles, departments, title='Departments', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Histogram - Overall Grade Distribution
all_grades = [grade for dept_grades in grades_data for grade in dept_grades]
ax2 = axs[1]
bins = np.arange(60, 101, 5)  # Bin ranges from 60 to 100

ax2.hist(all_grades, bins=bins, color='skyblue', edgecolor='black', alpha=0.7)

ax2.set_title("Overall Grade Distribution", fontsize=14, fontweight='bold')
ax2.set_xlabel("Grade", fontsize=12)
ax2.set_ylabel("Frequency", fontsize=12)
ax2.set_xticks(bins)
ax2.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()