import matplotlib.pyplot as plt
import numpy as np

concepts = ['Geometry', 'Algebra', 'Data Analysis', 'Measurement', 'Number Sense']
beginner = [20, 25, 15, 30, 22]  # percentage of students with beginner proficiency
intermediate = [40, 35, 45, 25, 38]  # percentage of students with intermediate proficiency
advanced = [40, 40, 40, 45, 40]  # percentage of students with advanced proficiency

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [3, 1]})

# Bar chart
x = np.arange(len(concepts))
width = 0.8

ax1.bar(x, beginner, width, label='Beginner', color='#FFC080')
ax1.bar(x, intermediate, width, bottom=beginner, label='Intermediate', color='#87CEEB')
ax1.bar(x, advanced, width, bottom=[i + j for i, j in zip(beginner, intermediate)], label='Advanced', color='#32CD32')

ax1.set_xlabel('Mathematical Concepts')
ax1.set_ylabel('Proficiency Level (%)')
ax1.set_title("Mathematical Mastery: Proficiency Levels of Students\nin Visual Mathematical Reasoning Ability Test", fontsize=12)

ax1.set_xticks(x)
ax1.set_xticklabels(concepts, rotation=45, ha='right', fontsize=10)
ax1.set_yticks(np.arange(0, 101, 20))
ax1.set_ylim(0, 100)

for i, concept in enumerate(concepts):
    ax1.text(i, beginner[i] / 2, f'{beginner[i]}%', ha='center', va='center', fontsize=10)
    ax1.text(i, beginner[i] + intermediate[i] / 2, f'{intermediate[i]}%', ha='center', va='center', fontsize=10)
    ax1.text(i, beginner[i] + intermediate[i] + advanced[i] / 2, f'{advanced[i]}%', ha='center', va='center', fontsize=10)

ax1.legend(loc='upper right', bbox_to_anchor=(1.05, 1), fontsize=10)

# Pie chart
sizes = [sum(beginner), sum(intermediate), sum(advanced)]
labels = ['Beginner', 'Intermediate', 'Advanced']
colors = ['#FFC080', '#87CEEB', '#32CD32']

ax2.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax2.axis('equal')
ax2.set_title('Total Proficiency Distribution', fontsize=12)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()