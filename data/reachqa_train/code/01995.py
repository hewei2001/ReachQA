import matplotlib.pyplot as plt
import numpy as np

# Define months for a full year
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Satisfaction scores for five fictional schools with more complex patterns
school_a_scores = [65, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88]
school_b_scores = [60, 61, 63, 66, 67, 69, 71, 73, 75, 77, 78, 80]
school_c_scores = [58, 57, 59, 60, 62, 65, 67, 69, 72, 74, 75, 77]
school_d_scores = [62, 64, 66, 65, 67, 68, 70, 72, 73, 75, 76, 78]
school_e_scores = [55, 56, 57, 59, 61, 63, 66, 67, 69, 70, 73, 75]

# Secondary metric: test scores for each school
test_scores = {
    'School A': [85, 87, 90, 92, 94, 95, 97, 96, 95, 93, 91, 92],
    'School B': [75, 77, 78, 79, 81, 82, 83, 84, 86, 87, 85, 86],
    'School C': [70, 72, 74, 75, 77, 76, 75, 74, 72, 71, 73, 74],
    'School D': [65, 67, 68, 69, 71, 73, 75, 77, 76, 74, 73, 72],
    'School E': [60, 62, 64, 66, 67, 68, 69, 70, 72, 73, 71, 70]
}

# Set up the plotting area
plt.figure(figsize=(14, 8))

# Plot satisfaction scores with trend lines for each school
schools_data = [
    ('School A', school_a_scores, '#FF5733', 'o'),
    ('School B', school_b_scores, '#33FFBD', 's'),
    ('School C', school_c_scores, '#FF33A6', '^'),
    ('School D', school_d_scores, '#3385FF', 'd'),
    ('School E', school_e_scores, '#85FF33', 'p')
]

for school, scores, color, marker in schools_data:
    plt.plot(months, scores, marker=marker, linestyle='-', color=color, linewidth=2, label=school)
    trend = np.poly1d(np.polyfit(range(len(months)), scores, 3))
    plt.plot(months, trend(range(len(months))), color=color, linestyle='--', alpha=0.5)

# Add test scores as a bar plot on a secondary y-axis
ax1 = plt.gca()
ax2 = ax1.twinx()
width = 0.15

for i, (school, scores) in enumerate(test_scores.items()):
    ax2.bar([x + width * i for x in range(len(months))], scores, width=width, alpha=0.3, label=f'{school} Test Score')

# Title and axis labels
plt.title('Annual Impact of Innovative Teaching Methods on Student Metrics\nSatisfaction & Test Scores (2023)', fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Satisfaction Score', fontsize=12)
ax2.set_ylabel('Test Score', fontsize=12)

# Add grid and legends
plt.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper left', fontsize=9)
ax2.legend(loc='upper right', fontsize=9)

# Automatically adjust the layout
plt.tight_layout()

# Show the plot
plt.show()