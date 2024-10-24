import matplotlib.pyplot as plt

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

# Create the box plot
fig, ax = plt.subplots(figsize=(12, 8))
boxprops = dict(facecolor='#FFD700', color='darkblue')
whiskerprops = dict(color='darkblue', linestyle='--')
capprops = dict(color='darkblue')
flierprops = dict(markerfacecolor='red', marker='o', markersize=8, linestyle='none')
medianprops = dict(color='green', linewidth=2)

boxes = ax.boxplot(grades_data, vert=True, patch_artist=True, notch=False,
                   boxprops=boxprops, whiskerprops=whiskerprops,
                   capprops=capprops, flierprops=flierprops,
                   medianprops=medianprops)

# Colors for each department
colors = ['#87CEEB', '#FFB6C1', '#98FB98', '#FFD700', '#FFA07A']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

# Customize the x-axis to reflect departments
ax.set_xticks(range(1, len(departments) + 1))
ax.set_xticklabels(departments, fontsize=12, rotation=15)

# Titles and labels
plt.title("Distribution of Academic Performance Across Departments\nat Greenwood College (2022-2023)", fontsize=16, fontweight='bold', pad=20)
plt.ylabel("Grade", fontsize=12)

# Add grid lines for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Add a legend with custom handles
legend_handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(legend_handles, departments, title='Departments', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()