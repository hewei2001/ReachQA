import matplotlib.pyplot as plt
import numpy as np

# Define types of youth engagement activities
activities = ['Volunteering', 'Fundraising', 'Advocacy', 'Education', 'Digital Activism']

# Percentage distribution for each activity type
percentages = np.array([25, 15, 20, 30, 10])  # Total should be 100%

# Colors for each activity
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create a horizontal bar chart
bars = ax.barh(activities, percentages, color=colors, edgecolor='black')

# Set the title and labels
ax.set_title('Youth Engagement in Social Causes:\nPercentage Distribution by Activity Type (2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Percentage (%)', fontsize=14)
ax.set_xlim(0, 100)

# Adding percentage labels next to each bar
for bar in bars:
    ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2, f'{bar.get_width()}%', 
            va='center', ha='center', fontsize=12, color='black')

# Add legend outside the plot area
ax.legend(bars, activities, title='Activity Type', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12)

# Add grid lines for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.yaxis.grid(False)  # Disable y-axis grid for clarity

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Show the plot
plt.show()