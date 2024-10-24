import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Define the activities and their corresponding hours
activities = ["Hiking", "Bird Watching", "Camping", "Gardening", "Mountain Biking"]
hours_spent = np.array([120, 90, 75, 110, 95])  # Average annual hours spent

# Additional data: Satisfaction level (out of 5)
satisfaction_levels = np.array([4.5, 4.2, 3.8, 4.0, 4.3])

# Set up the colors and patterns for each activity
colors = ["#8dd3c7", "#ffffb3", "#bebada", "#fb8072", "#80b1d3"]
patterns = ['/', '\\', '|', '-', '+']

# Create the horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot horizontal bars with patterns
bars = ax.barh(activities, hours_spent, color=colors, edgecolor='grey', alpha=0.7, hatch=patterns[0])

# Add data labels for hours spent and satisfaction level
for idx, bar in enumerate(bars):
    ax.text(bar.get_width() - 5, bar.get_y() + bar.get_height()/2,
            f'{int(bar.get_width())} hrs', va='center', ha='right',
            color='black', weight='bold')
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
            f'Sat: {satisfaction_levels[idx]}', va='center', ha='left',
            color='darkgrey', fontsize=10)

# Title and labels
ax.set_title("Balancing Nature: Annual Hours Spent on Outdoor Activities\nAmong Outdoor Enthusiasts",
             fontsize=16, weight='bold', pad=15)
ax.set_xlabel("Average Annual Hours", fontsize=12)
ax.set_ylabel("Outdoor Activities", fontsize=12)

# Add a legend
legend_elements = [Patch(facecolor=colors[i], edgecolor='grey', hatch=patterns[0], label=activities[i]) 
                   for i in range(len(activities))]
ax.legend(handles=legend_elements, title="Activities", loc='upper right', bbox_to_anchor=(1.15, 1))

# Add average line
average_hours = np.mean(hours_spent)
ax.axvline(average_hours, color='red', linestyle='--', linewidth=1)
ax.text(average_hours + 5, len(activities) - 1, f'Avg: {int(average_hours)} hrs',
        color='red', va='center', fontsize=10, fontweight='bold')

# Customize the grid and spines
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.spines['right'].set_color('darkgrey')
ax.spines['top'].set_visible(False)

# Set layout for better visual spacing
plt.tight_layout()

# Display the plot
plt.show()