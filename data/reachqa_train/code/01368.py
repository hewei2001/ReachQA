import matplotlib.pyplot as plt
import numpy as np

# Community engagement activities
activities = [
    'Community Workshops',
    'Volunteer Tree Planting',
    'Educational Programs',
    'Public Consultations',
    'Social Media Campaigns',
    'Local Business Collaborations'
]

# Percentage breakdown of each activity (sum to 100)
engagement_percentages = [25, 20, 18, 15, 12, 10]

# Colors for each activity
colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot horizontal percentage bar chart
bars = ax.barh(activities, engagement_percentages, color=colors)

# Adding data labels
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(3, 0),  # Offset the text slightly to the right
                textcoords='offset points',
                ha='left', va='center', fontsize=10)

# Set fixed x-axis range to 100%
ax.set_xlim(0, 100)

# Title and labels
ax.set_title('2023 Urban Green Space Development Initiatives:\nCommunity Engagement Breakdown',
             fontsize=16, color='darkgreen', pad=20)
ax.set_xlabel('Percentage (%)', fontsize=12)
ax.set_ylabel('Community Engagement Activities', fontsize=12)

# Invert y-axis to have the first item at the top
ax.invert_yaxis()

# Customize tick appearance
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Add grid lines only on x-axis
ax.xaxis.grid(True, linestyle='--', color='grey', alpha=0.7)

# Adjust layout to prevent any cut-off
plt.tight_layout()

# Display the chart
plt.show()