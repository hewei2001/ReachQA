import matplotlib.pyplot as plt
import numpy as np

# Seasons and gardening activities
seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
activities = ['Planting', 'Watering', 'Weeding', 'Pruning', 'Harvesting']

# Hours spent on each activity per season
activity_hours = np.array([
    [8, 18, 20, 10],    # Planting
    [6, 22, 34, 14],    # Watering
    [12, 18, 25, 28],   # Weeding
    [10, 8, 12, 24],    # Pruning
    [0, 12, 22, 32],    # Harvesting
])

# Average tasks completed per activity per season (sample data)
tasks_completed = np.array([
    [2, 5, 6, 3],    # Planting
    [3, 6, 8, 4],    # Watering
    [3, 4, 6, 7],    # Weeding
    [2, 3, 3, 5],    # Pruning
    [0, 4, 6, 8],    # Harvesting
])

# Plotting the charts
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Define colors
colors = ['#8c564b', '#1f77b4', '#2ca02c', '#d62728', '#ff7f0e']

# First subplot: Stacked area chart
ax1.stackplot(seasons, activity_hours, labels=activities, colors=colors, alpha=0.8)
ax1.set_title('Garden Landscaping Activities Through the Seasons', fontsize=14, fontweight='bold')
ax1.set_xlabel('Seasons', fontsize=12)
ax1.set_ylabel('Hours Spent', fontsize=12)
ax1.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title="Gardening Activities", fontsize='small', title_fontsize='medium')
ax1.grid(linestyle='--', alpha=0.7)

# Second subplot: Bar chart of tasks completed
width = 0.15  # Width of the bars
x = np.arange(len(seasons))  # Seasons index
for idx, (activity, color) in enumerate(zip(activities, colors)):
    ax2.bar(x + idx * width, tasks_completed[idx], width, label=activity, color=color, alpha=0.8)

ax2.set_title('Average Tasks Completed per Season', fontsize=14, fontweight='bold')
ax2.set_xlabel('Seasons', fontsize=12)
ax2.set_ylabel('Tasks Completed', fontsize=12)
ax2.set_xticks(x + width * 2)  # Centering the x-ticks
ax2.set_xticklabels(seasons)
ax2.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title="Gardening Activities", fontsize='small', title_fontsize='medium')
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()