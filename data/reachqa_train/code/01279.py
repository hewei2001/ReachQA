import matplotlib.pyplot as plt
import numpy as np

# Define extended communication methods including subcategories
communication_methods = [
    'Emails', 'Instant Messaging', 'Video Calls', 'In-Person Meetings', 
    'Collaborative Tools', 'Phone Calls', 'Group Video Calls', 'One-on-One Video Calls'
]

# Artificial productivity scores with increased data points and variability
productivity_scores = [
    [72, 75, 78, 80, 83, 85, 87, 78, 80, 82, 79, 81, 84, 76, 80, 83, 79],  # Emails
    [88, 89, 90, 92, 87, 91, 90, 93, 91, 87, 85, 88, 86, 89, 91, 90, 88],  # Instant Messaging
    [62, 65, 68, 71, 69, 67, 70, 73, 68, 66, 70, 67, 69, 68, 72, 70, 69],  # Video Calls
    [77, 80, 82, 83, 81, 84, 85, 79, 82, 84, 78, 81, 80, 83, 85, 84, 82],  # In-Person Meetings
    [91, 92, 94, 95, 93, 90, 96, 92, 94, 93, 91, 94, 95, 92, 94, 92, 93],  # Collaborative Tools
    [78, 80, 82, 81, 85, 83, 79, 80, 82, 81, 84, 85, 78, 80, 79, 81, 83],  # Phone Calls
    [65, 68, 70, 74, 69, 66, 73, 71, 69, 66, 70, 67, 72, 70, 68, 69, 73],  # Group Video Calls
    [68, 71, 73, 76, 72, 70, 75, 74, 72, 69, 71, 69, 74, 72, 76, 75, 71]   # One-on-One Video Calls
]

# Create the vertical box plot
plt.figure(figsize=(14, 10))
box = plt.boxplot(
    productivity_scores,
    patch_artist=True,
    labels=communication_methods,
    notch=True,
    vert=True,
    showmeans=True,
    meanprops={"marker": "o", "markerfacecolor": "white", "markeredgecolor": "black", "markersize": 8}
)

# Customizing the boxplot
colors = ['#FF9999', '#FFCC99', '#99FF99', '#66B3FF', '#C2C2F0', '#FFB6C1', '#ADD8E6', '#90EE90']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add titles and labels
plt.title(
    'Communication Styles and Productivity:\nA Comprehensive Workplace Analysis', 
    fontsize=18, fontweight='bold', pad=20
)
plt.xlabel('Communication Methods', fontsize=14)
plt.ylabel('Productivity Scores', fontsize=14)

# Add grid for better readability
plt.grid(linestyle='--', alpha=0.7)

# Add legend with custom handles for colors
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
plt.legend(handles, communication_methods, title='Methods', loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1))

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()