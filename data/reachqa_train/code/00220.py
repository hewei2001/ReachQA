import matplotlib.pyplot as plt
import numpy as np

# Define study hours data for each department
engineering_hours = [25, 35, 40, 45, 50, 30, 55, 60, 65, 48, 53, 56]
humanities_hours = [20, 25, 30, 22, 28, 30, 32, 34, 29, 40, 18, 37]
sciences_hours = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 30, 55]
business_hours = [10, 15, 20, 25, 15, 20, 22, 18, 24, 26, 23, 28]
arts_hours = [5, 10, 15, 20, 25, 30, 5, 10, 15, 40, 35, 20, 25, 45]

# Define average grades for each department
engineering_grades = [85, 88, 90, 95, 80, 75, 92, 89, 91, 86, 87, 93]
humanities_grades = [78, 82, 85, 79, 80, 84, 86, 87, 81, 89, 75, 83]
sciences_grades = [76, 80, 85, 88, 84, 90, 92, 91, 95, 98, 99, 85, 94]
business_grades = [70, 75, 80, 82, 78, 81, 79, 74, 77, 79, 76, 82]
arts_grades = [68, 72, 74, 76, 79, 82, 69, 71, 75, 81, 80, 77, 78, 84]

# Combine data
hours_data = [engineering_hours, humanities_hours, sciences_hours, business_hours, arts_hours]
grades_data = [np.mean(data) for data in [engineering_grades, humanities_grades, sciences_grades, business_grades, arts_grades]]

departments = ['Engineering', 'Humanities', 'Sciences', 'Business', 'Arts']

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(15, 7))

# Plotting the horizontal box plot for study hours
box = ax1.boxplot(hours_data, vert=False, patch_artist=True, labels=departments, notch=True, whis=[5, 95])
colors = ['lightblue', 'lightgreen', 'salmon', 'khaki', 'plum']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
for whisker, cap, median, flier in zip(box['whiskers'], box['caps'], box['medians'], box['fliers']):
    whisker.set(color='gray', linewidth=1.2, linestyle='--')
    cap.set(color='gray', linewidth=1.2)
    median.set(color='darkred', linewidth=2)
    flier.set(marker='o', color='orange', alpha=0.5)

ax1.set_title('Study Hours per Week by University Department\nA Comparative Insight', fontsize=14, fontweight='bold')
ax1.set_xlabel('Study Hours per Week', fontsize=12)
ax1.set_ylabel('Department', fontsize=12)
ax1.xaxis.grid(True, linestyle='--', color='grey', alpha=0.7)

# Plotting the bar chart for average grades
ax2.bar(departments, grades_data, color=colors)
ax2.set_title('Average Grades by Department', fontsize=14, fontweight='bold')
ax2.set_xlabel('Department', fontsize=12)
ax2.set_ylabel('Average Grade', fontsize=12)
ax2.set_ylim(65, 100)  # Assuming grades are out of 100

# Optimize layout
plt.tight_layout()

# Show the plot
plt.show()