import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define grades and languages
grades = ['Grade 6', 'Grade 8', 'Grade 10']
languages = ['English', 'Mandarin', 'Spanish']

# Proficiency percentages by grade and language for each school
school_A_proficiency = np.array([
    [70, 50, 40],  # Grade 6
    [80, 60, 50],  # Grade 8
    [85, 65, 55]   # Grade 10
])

school_B_proficiency = np.array([
    [60, 55, 45],  # Grade 6
    [70, 65, 55],  # Grade 8
    [80, 75, 65]   # Grade 10
])

school_C_proficiency = np.array([
    [65, 45, 55],  # Grade 6
    [75, 55, 65],  # Grade 8
    [85, 60, 75]   # Grade 10
])

# Set up the figure
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Plot parameters
num_grades = len(grades)
num_languages = len(languages)
dx = dy = 0.25  # Smaller dimensions for better spacing

# Colors for each language
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Plotting for each school
offset = np.array([0.0, 0.3, 0.6])  # Offset for each school
for school_idx, school_data in enumerate([school_A_proficiency, school_B_proficiency, school_C_proficiency]):
    for grade_idx in range(num_grades):
        x_pos = np.full(num_languages, grade_idx) + offset[school_idx]
        y_pos = np.arange(num_languages)
        z_pos = np.zeros(num_languages)
        proficiency = school_data[grade_idx]
        
        ax.bar3d(x_pos, y_pos, z_pos, dx, dy, proficiency, color=colors, alpha=0.8, zsort='average')

# Customizing ticks and labels
ax.set_xticks(np.arange(num_grades))
ax.set_xticklabels(grades, rotation=45, ha='right')
ax.set_yticks(np.arange(num_languages))
ax.set_yticklabels(languages)
ax.set_xlabel('Grades', labelpad=10)
ax.set_ylabel('Languages', labelpad=10)
ax.set_zlabel('Proficiency (%)', labelpad=10)
ax.set_title('Language Proficiency in Multilingual Schools\nAcross Different Grades', pad=40)

# Adjust view angle for better perspective
ax.view_init(elev=25, azim=60)

# Add legends for schools
school_legend = [
    plt.Line2D([0], [0], color='gray', alpha=0.8, lw=4, label='School A'),
    plt.Line2D([0], [0], color='gray', alpha=0.8, lw=4, label='School B'),
    plt.Line2D([0], [0], color='gray', alpha=0.8, lw=4, label='School C')
]
language_legend = [plt.Line2D([0], [0], color=colors[i], lw=4, label=languages[i]) for i in range(num_languages)]

ax.legend(handles=school_legend + language_legend, title='Schools and Languages', loc='upper left', bbox_to_anchor=(1.05, 1))

plt.tight_layout()
plt.show()