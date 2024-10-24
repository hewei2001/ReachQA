import matplotlib.pyplot as plt
import numpy as np

# Define communication methods
communication_methods = ['Emails', 'Instant Messaging', 'Video Calls', 'In-Person Meetings', 'Collaborative Tools']

# Artificial productivity scores for each communication method
# Slightly adjusted for clearer illustration
productivity_scores = [
    [75, 82, 78, 85, 80, 72, 77, 86, 80, 74, 81, 75, 79],  # Emails
    [88, 85, 90, 92, 87, 89, 90, 93, 91, 87, 85, 88, 90],  # Instant Messaging
    [65, 68, 70, 72, 69, 67, 70, 71, 68, 66, 72, 70, 69],  # Video Calls
    [80, 85, 83, 82, 81, 84, 85, 79, 82, 84, 85, 83, 86],  # In-Person Meetings
    [91, 94, 92, 95, 93, 90, 96, 92, 94, 93, 91, 94, 92]   # Collaborative Tools
]

# Create the vertical box plot
plt.figure(figsize=(12, 8))
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
colors = ['#FF9999', '#FFCC99', '#99FF99', '#66B3FF', '#C2C2F0']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add titles and labels
plt.title('Communication Styles and Productivity:\nA Modern Workplace Analysis', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Communication Methods', fontsize=12)
plt.ylabel('Productivity Scores', fontsize=12)

# Add grid for better readability
plt.grid(linestyle='--', alpha=0.6)

# Add legend with custom handles for colors
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
labels = communication_methods
plt.legend(handles, labels, title='Methods', loc='upper left', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()