import matplotlib.pyplot as plt
import numpy as np

# Define more complex data with 10 categories and 2 sets of data
categories = ['Mathematics', 'Physics', 'Computer Science', 'Electrical Engineering', 'Mechanical Engineering', 
              'Civil Engineering', 'Chemical Engineering', 'Aerospace Engineering', 'Biomedical Engineering', 'Industrial Engineering']
data_set1 = [20, 18, 22, 15, 25, 19, 21, 17, 23, 16]
data_set2 = [18, 22, 20, 17, 24, 20, 23, 19, 26, 18]

# Create a figure and axis with a larger size
fig, ax = plt.subplots(figsize=(12, 8))

# Define the bar positions and width
bar_positions = np.arange(len(categories))
bar_width = 0.35

# Create bars for the two data sets
ax.bar(bar_positions - bar_width/2, data_set1, width=bar_width, label='Engineering Students', 
       color=plt.cm.tab20(np.arange(len(categories)) / len(categories)))
ax.bar(bar_positions + bar_width/2, data_set2, width=bar_width, label='Science Students', 
       color=plt.cm.tab20((np.arange(len(categories)) + 0.5) / len(categories)))

# Set the title and labels
ax.set_title("Average Time Spent on Different Subjects\nby Engineering and Science Students", fontsize=14)
ax.set_xticks(bar_positions)
ax.set_xticklabels(categories, rotation=45, ha='right', fontsize=10)
ax.set_ylabel("Average Time Spent (hours)", fontsize=12)
ax.set_xlabel("Subjects", fontsize=12)

# Add text labels above the bars
for i, value in enumerate(data_set1):
    ax.text(i - bar_width/2, value + 0.5, f"{value} hours", ha='center', va='bottom', fontsize=10)
for i, value in enumerate(data_set2):
    ax.text(i + bar_width/2, value + 0.5, f"{value} hours", ha='center', va='bottom', fontsize=10)

# Add grid lines along the y-axis and a legend
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.legend(fontsize=12)

# Automatically adjust the layout to avoid occlusion
plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.show()