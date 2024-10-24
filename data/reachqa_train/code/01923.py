import matplotlib.pyplot as plt
import numpy as np

# Data representing the number of students who selected each programming language
languages = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'C#', 'Go', 'Swift']
student_counts = [150, 90, 60, 120, 30, 50, 20, 40]

# Generate positions for the bars
x_positions = np.arange(len(languages))

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the histogram as a bar chart
bars = ax.bar(x_positions, student_counts, color=['#5DA5DA', '#FAA43A', '#60BD68', '#F17CB0', '#B2912F', '#B276B2', '#DECF3F', '#F15854'])

# Customizing the plot
ax.set_title("Distribution of Programming Languages\nSelected by Computer Science Students", fontsize=14, weight='bold', pad=20)
ax.set_xlabel("Programming Languages", fontsize=12)
ax.set_ylabel("Number of Students", fontsize=12)
ax.set_xticks(x_positions)
ax.set_xticklabels(languages, fontsize=10, rotation=45, ha='right')

# Adding a grid for better readability
ax.grid(True, axis='y', linestyle='--', alpha=0.5)

# Display the values on top of the bars
for bar, count in zip(bars, student_counts):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 3, str(count), ha='center', va='bottom', fontsize=10)

# Automatically adjust subplot params to give specified padding and prevent overlap
plt.tight_layout()

# Display the plot
plt.show()