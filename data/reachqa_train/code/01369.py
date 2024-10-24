import matplotlib.pyplot as plt
import numpy as np

# Extended list of community engagement activities
activities = [
    'Community Workshops', 'Volunteer Tree Planting', 'Educational Programs',
    'Public Consultations', 'Social Media Campaigns', 'Local Business Collaborations',
    'Neighborhood Clean-Ups', 'Recycling Drives', 'Community Art Projects',
    'Local Festivals', 'Public Health Awareness', 'Historical Tours'
]

# Percentage breakdown of each activity (sub-categories for stacked bars)
engagement_data = {
    'Participation': [10, 7, 6, 5, 4, 3, 3, 2, 1, 1, 2, 1],
    'Organizing': [5, 5, 4, 3, 3, 2, 2, 1, 1, 2, 1, 2],
    'Funding': [10, 8, 8, 7, 5, 5, 4, 3, 3, 1, 1, 1]
}

# Colors for the stacked bars
colors = ['#8dd3c7', '#ffffb3', '#bebada']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 10))

# Create stacked bar chart
bottom_values = np.zeros(len(activities))
for idx, (category, percentages) in enumerate(engagement_data.items()):
    bars = ax.barh(activities, percentages, left=bottom_values, color=colors[idx], label=category)
    bottom_values += percentages

    # Annotate each segment
    for bar in bars:
        width = bar.get_width()
        if width > 0:  # Add labels only for non-zero segments
            ax.annotate(f'{width}%',
                        xy=(bar.get_x() + width / 2, bar.get_y() + bar.get_height() / 2),
                        xytext=(0, 0),  # Center the text within each bar segment
                        textcoords='offset points',
                        ha='center', va='center', fontsize=8, color='black')

# Set fixed x-axis range to account for the total of sub-categories
ax.set_xlim(0, 35)

# Title and labels
ax.set_title('2023 Urban Green Space Development Initiatives:\nDetailed Community Engagement Breakdown',
             fontsize=16, color='darkgreen', pad=20)
ax.set_xlabel('Percentage (%)', fontsize=12)
ax.set_ylabel('Community Engagement Activities', fontsize=12)

# Invert y-axis to have the first item at the top
ax.invert_yaxis()

# Add a legend to clarify each bar section
ax.legend(loc='upper right', fontsize=10, title='Activity Components')

# Customize tick appearance
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Add grid lines only on x-axis
ax.xaxis.grid(True, linestyle='--', color='grey', alpha=0.7)

# Adjust layout to prevent any cut-off
plt.tight_layout()

# Display the chart
plt.show()