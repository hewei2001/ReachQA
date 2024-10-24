import matplotlib.pyplot as plt
import numpy as np

# Data
countries = ['USA', 'China', 'Japan', 'South Korea', 'UK', 'Germany', 'France', 'Australia']
extracurricular_time = [10, 5, 8, 12, 9, 7, 11, 6]
academic_performance = [85, 92, 90, 88, 82, 89, 84, 87]
student_ratio = [0.8, 0.7, 0.9, 0.6, 0.8, 0.7, 0.85, 0.75]

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [2.5, 1]})

# Set the bar positions
bar_positions = np.arange(len(countries))

# Plot the bar chart on the first subplot
ax1.bar(bar_positions, extracurricular_time, label='Extracurricular Time', color='tab:blue', width=0.4)
ax1.bar(bar_positions + 0.4, academic_performance, label='Academic Performance', color='tab:red', width=0.4)

# Add grid lines
ax1.grid(True, linestyle='--', which='major', color='grey', alpha=0.25)

# Set axis labels and title
ax1.set_xlabel('Countries')
ax1.set_ylabel('Time (hours/week) and Score (out of 100)')
ax1.set_title('Balancing Act: Extracurricular Time vs.\nAcademic Performance Across Nations')

# Set x-axis tick labels
ax1.set_xticks(bar_positions + 0.2)
ax1.set_xticklabels(countries, rotation=45, ha='right')

# Add legend
ax1.legend(loc='upper right')

# Add text labels above the bars
for i, (x, y) in enumerate(zip(bar_positions, extracurricular_time)):
    ax1.text(x, y + 0.5, str(y), ha='center', va='bottom')
for i, (x, y) in enumerate(zip(bar_positions + 0.4, academic_performance)):
    ax1.text(x, y + 0.5, str(y), ha='center', va='bottom')

# Plot a pie chart on the second subplot
ax2.pie(student_ratio, labels=countries, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20(np.arange(len(countries))))
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax2.set_title('Student Ratio Across Nations')

# Adjust the layout to prevent overlapping
fig.tight_layout()

# Show the plot
plt.show()