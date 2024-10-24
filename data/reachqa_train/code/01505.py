import matplotlib.pyplot as plt
import numpy as np

# Days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Hours spent per activity per day
social_media = [1.5, 1.5, 2, 2.5, 3, 4.5, 5]
online_gaming = [1, 1, 1, 1, 2, 3.5, 4]
video_streaming = [2.5, 3, 2.5, 3, 3.5, 4, 4.5]
work_related = [9, 9, 9, 9, 8, 2, 1]
online_learning = [1, 1, 1.5, 1, 1, 0.5, 0.5]
physical_exercise = [0.5, 0.5, 0.5, 1, 1, 1.5, 2]
reading = [0.5, 0.5, 0.5, 0.5, 1, 2, 2.5]

# Stack the data
activities = np.vstack([social_media, online_gaming, video_streaming, work_related, online_learning, physical_exercise, reading])

# Calculate daily totals and averages
daily_totals = np.sum(activities, axis=0)
weekly_avg = np.mean(activities, axis=1)

# Plotting
fig, ax = plt.subplots(figsize=(14, 9))

# Define colors for the different activities
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Stacked area chart
ax.stackplot(days, activities, labels=['Social Media', 'Online Gaming', 'Video Streaming', 'Work Related', 'Online Learning', 'Physical Exercise', 'Reading'], colors=colors, alpha=0.8)

# Overlay total hours line
ax.plot(days, daily_totals, color='black', linestyle='-', linewidth=2, label='Total Hours')

# Add title and labels
ax.set_title('Digital Content and Activity Engagement\nThroughout the Week', fontsize=16, fontweight='bold')
ax.set_xlabel('Days of the Week', fontsize=12)
ax.set_ylabel('Hours Spent', fontsize=12)

# Rotate x-ticks to prevent overlap
plt.xticks(rotation=45)

# Add legend with adjusted location
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title="Activities", fontsize='small', title_fontsize='medium')

# Add grid lines
ax.grid(linestyle='--', alpha=0.7)

# Add secondary y-axis for weekly average per activity
ax2 = ax.twinx()
ax2.set_ylabel('Weekly Average (Hours)', fontsize=12)
ax2.plot(days, weekly_avg, color='gray', linestyle='--', marker='o', linewidth=1.5, label='Weekly Average')
ax2.legend(loc='upper right', bbox_to_anchor=(1, 0.8), title="Weekly Average", fontsize='small', title_fontsize='medium')

# Automatically adjust layout to fit all elements
plt.tight_layout()

# Show the plot
plt.show()