import matplotlib.pyplot as plt
import numpy as np

# Days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Hours spent per activity per day (example data)
social_media = [1.5, 1.5, 2, 2.5, 3, 4.5, 5]
online_gaming = [1, 1, 1, 1, 2, 3.5, 4]
video_streaming = [2.5, 3, 2.5, 3, 3.5, 4, 4.5]
work_related = [9, 9, 9, 9, 8, 2, 1]
online_learning = [1, 1, 1.5, 1, 1, 0.5, 0.5]

# Stack the data
activities = np.vstack([social_media, online_gaming, video_streaming, work_related, online_learning])

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Define colors for the different activities
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Stacked area chart
ax.stackplot(days, activities, labels=['Social Media', 'Online Gaming', 'Video Streaming', 'Work Related', 'Online Learning'], colors=colors, alpha=0.8)

# Add title and labels
ax.set_title('Digital Content Consumption\nAcross a Week', fontsize=16, fontweight='bold')
ax.set_xlabel('Days of the Week', fontsize=12)
ax.set_ylabel('Hours Spent', fontsize=12)

# Rotate x-ticks to prevent overlap
plt.xticks(rotation=45)

# Add legend
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title="Activities", fontsize='small', title_fontsize='medium')

# Add grid lines
ax.grid(linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()