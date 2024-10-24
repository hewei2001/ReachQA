import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2013 to 2023
years = np.arange(2013, 2024)

# Define the percentage usage data for each category
video_lectures = np.array([15, 18, 21, 25, 30, 35, 40, 50, 55, 60, 65])
interactive_quizzes = np.array([5, 8, 12, 15, 18, 20, 25, 28, 30, 32, 35])
discussion_forums = np.array([3, 5, 10, 12, 14, 18, 20, 25, 27, 30, 32])

# Stack the data to create cumulative usage values
usage_stack = np.row_stack((video_lectures, interactive_quizzes, discussion_forums))

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(years, usage_stack, labels=['Video Lectures', 'Interactive Quizzes', 'Online Discussion Forums'],
             colors=['#FF9999', '#66B3FF', '#99FF99'], alpha=0.8)

# Customize the title and labels with line breaks and formatting
ax.set_title('Evolution of Digital Learning Tools Usage\n(2013-2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Total Usage (%)', fontsize=12)

# Add a legend outside the plot area for clarity
ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1))

# Customize the grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Adjust layout to avoid any overlap or truncation
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Rotate x-axis labels slightly for better fit
plt.xticks(rotation=45)

# Display the plot
plt.show()