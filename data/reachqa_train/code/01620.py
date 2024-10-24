import matplotlib.pyplot as plt
import numpy as np

# Define departments and programming languages
departments = ['CS', 'DS', 'EE', 'ME', 'Math', 'Business', 'Physics', 'Chemistry']
languages = ['Python', 'Java', 'C++', 'R', 'MATLAB', 'JavaScript', 'Swift', 'Go']

# Simulated popularity data (as a percentage)
# Each row corresponds to a language and each column to a department
popularity = np.array([
    [90, 65, 55, 25, 10, 50, 40, 30],   # Python
    [50, 30, 40, 35, 20, 60, 30, 20],   # Java
    [40, 20, 60, 70, 15, 25, 50, 40],   # C++
    [20, 80, 15, 10, 60, 15, 20, 15],   # R
    [10, 5, 10, 60, 90, 10, 5, 10],     # MATLAB
    [60, 70, 30, 20, 30, 80, 40, 50],   # JavaScript
    [30, 45, 55, 40, 35, 25, 60, 45],   # Swift
    [20, 25, 35, 55, 45, 35, 50, 40]    # Go
])

# Colors for each programming language
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']

# Bar width and position settings
bar_width = 0.1
x_indices = np.arange(len(departments))

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot bars for each programming language
for i, (language, color) in enumerate(zip(languages, colors)):
    bars = ax.bar(x_indices + i * bar_width, popularity[i], bar_width, label=language, color=color)
    # Add text labels on top of bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval}%', ha='center', va='bottom', fontsize=7)

# Title and labels
ax.set_title('Programming Language Popularity by University Department in 2023\nExpanded to Include Multiple Departments and Languages', fontsize=14, weight='bold', pad=20)
ax.set_xlabel('Departments', fontsize=12)
ax.set_ylabel('Popularity (%)', fontsize=12)

# Set x-ticks for departments
ax.set_xticks(x_indices + bar_width * (len(languages) - 1) / 2)
ax.set_xticklabels(departments, rotation=45, ha='right')

# Add grid lines along the y-axis
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Add legend with adjusted positioning
ax.legend(title='Languages', fontsize=9, loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=4)

# Adjust layout to prevent clipping and improve appearance
plt.tight_layout()

# Display the plot
plt.show()