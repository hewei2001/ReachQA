import matplotlib.pyplot as plt
import numpy as np

# Define the departments and project types
departments = [
    'Software Dev', 'Marketing', 'Operations', 
    'HR', 'Design', 'Finance'
]
projects = ['Product Launch', 'System Upgrade', 'Market Research']

# Define percentage of task allocation for each department in different projects
task_data = np.array([
    [40, 15, 10, 5, 20, 10],  # Product Launch
    [50, 5, 20, 5, 10, 10],   # System Upgrade
    [20, 25, 15, 15, 15, 10]  # Market Research
])

# Hypothetical project efficiency scores (0 to 100)
efficiency_scores = [75, 85, 65]

# Define positions for each group of bars
x = np.arange(len(projects))
bar_width = 0.7

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot each department's data as a stacked bar chart
bottom_heights = np.zeros(len(projects))
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', 
    '#d62728', '#9467bd', '#8c564b'
]

for idx, department in enumerate(departments):
    ax1.bar(x, task_data[:, idx], bottom=bottom_heights, width=bar_width, label=department, color=colors[idx])
    bottom_heights += task_data[:, idx]

# Add labels and title
ax1.set_title("Task Allocation and Workload Distribution\nwith Project Efficiency Scores", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Project Types", fontsize=12)
ax1.set_ylabel("Task Allocation (%)", fontsize=12)

# Set x-ticks and labels
ax1.set_xticks(x)
ax1.set_xticklabels(projects, fontsize=10)

# Add a legend with title
ax1.legend(title='Departments', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)

# Configure gridlines
ax1.grid(axis='y', linestyle='--', alpha=0.6)

# Display percentage labels on the bars
for i in range(len(projects)):
    cumulative_height = 0
    for j in range(len(departments)):
        percentage = task_data[i, j]
        ax1.text(i, cumulative_height + percentage / 2, f'{percentage}%', ha='center', va='center', color='white', fontsize=8)
        cumulative_height += percentage

# Create a secondary axis for the line plot
ax2 = ax1.twinx()
ax2.plot(x, efficiency_scores, color='darkgreen', marker='o', linewidth=2, markersize=8, label='Project Efficiency')
ax2.set_ylabel("Efficiency Score", fontsize=12)
ax2.set_ylim(0, 100)

# Add a legend for the line plot
ax2.legend(loc='upper right', fontsize=9)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()