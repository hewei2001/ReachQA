import matplotlib.pyplot as plt
import numpy as np

# Data representing the number of students who selected each programming language
languages = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'C#', 'Go', 'Swift']
student_counts = [150, 90, 60, 120, 30, 50, 20, 40]

# Calculate percentages for the pie chart
total_students = sum(student_counts)
percentages = [count / total_students * 100 for count in student_counts]

# Create a 1x2 grid of subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Bar chart subplot
bars = ax1.bar(languages, student_counts, color=['#5DA5DA', '#FAA43A', '#60BD68', '#F17CB0', '#B2912F', '#B276B2', '#DECF3F', '#F15854'])
ax1.set_title("Distribution of Programming Languages\nSelected by Computer Science Students", fontsize=14, weight='bold', pad=20)
ax1.set_xlabel("Programming Languages", fontsize=12)
ax1.set_ylabel("Number of Students", fontsize=12)
ax1.set_xticklabels(languages, fontsize=10, rotation=45, ha='right')
ax1.grid(True, axis='y', linestyle='--', alpha=0.5)

# Display values on top of the bars
for bar, count in zip(bars, student_counts):
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 3, str(count), ha='center', va='bottom', fontsize=10)

# Pie chart subplot
ax2.pie(percentages, labels=languages, autopct='%1.1f%%', startangle=90, colors=['#5DA5DA', '#FAA43A', '#60BD68', '#F17CB0', '#B2912F', '#B276B2', '#DECF3F', '#F15854'])
ax2.set_title("Percentage of Students Selecting Each Language", fontsize=14, weight='bold', pad=20)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()