import matplotlib.pyplot as plt
import numpy as np

# Data inputs for the bar chart
study_strategies = ['Standard Reading', 'Summary Notes', 'Group Discussions', 'Online Quizzes', 'Educational Videos']
average_scores = [72.3, 76.1, 79.9, 82.8, 85.5]

# Additional data for the line plot: Simulate average scores improvement over time for each strategy
average_scores_over_time = {
    'Standard Reading': [65.0, 68.5, 70.3, 72.0, 72.3],
    'Summary Notes': [69.1, 72.3, 74.6, 75.9, 76.1],
    'Group Discussions': [74.3, 76.9, 78.8, 79.7, 79.9],
    'Online Quizzes': [77.5, 79.6, 81.1, 82.3, 82.8],
    'Educational Videos': [79.1, 81.4, 83.2, 84.6, 85.5],
}

# Time periods (e.g., semesters)
time_periods = ['Semester 1', 'Semester 2', 'Semester 3', 'Semester 4', 'Semester 5']

# Create a 1x2 grid of subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Plot the bar chart with adjusted colors and styling
bar_positions = np.arange(len(study_strategies))
bars = ax1.bar(bar_positions, average_scores, color=['#8B0000', '#FF8C00', '#FFFF00', '#2E8B57', '#1E90FF'], width=0.7)

# Annotate bars with data
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval, f"{yval:.1f}", va='bottom', ha='center', rotation=45, fontsize=10, color='black')

# Adjust x-axis labels
ax1.set_xticks(bar_positions)
ax1.set_xticklabels(study_strategies, rotation=30, ha='right')

# Set title and labels with custom styling
ax1.set_title('Average Final Exam Scores by Study Strategy', fontsize=14, fontweight='bold')
ax1.set_xlabel('Study Strategy', fontsize=12)
ax1.set_ylabel('Average Score (%)', fontsize=12)

# Enhance grid lines for better readability
ax1.grid(True, linestyle='--', alpha=0.5, axis='y')

# Plot the line chart with different colors for each strategy
for strategy, scores in average_scores_over_time.items():
    ax2.plot(time_periods, scores, marker='o', label=strategy)

# Set title and labels for the line plot
ax2.set_title('Trend of Average Scores Over Time by Study Strategy', fontsize=14, fontweight='bold')
ax2.set_xlabel('Time Period', fontsize=12)
ax2.set_ylabel('Average Score (%)', fontsize=12)

# Adjust layout and legend for the line plot
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(loc='upper left')

# Adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()