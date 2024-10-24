import matplotlib.pyplot as plt
import numpy as np

# Define artificial data representing screen time distribution in hours
screen_time_data = {
    "Software Developers": [9, 10, 10, 11, 8, 9, 10, 11, 12, 9, 10, 11, 9, 10],
    "Data Scientists": [8, 9, 9, 10, 11, 9, 8, 9, 10, 8, 9, 10, 9, 8],
    "Graphic Designers": [7, 8, 9, 10, 8, 7, 8, 9, 10, 8, 9, 7, 8],
    "Project Managers": [6, 7, 6, 7, 8, 7, 6, 7, 6, 6, 7, 8, 6],
    "HR Professionals": [5, 6, 5, 5, 6, 5, 4, 5, 6, 5, 5, 6, 4]
}

# Extract data for plotting
role_labels = list(screen_time_data.keys())
data = list(screen_time_data.values())

# Create a horizontal box plot
fig, ax = plt.subplots(figsize=(12, 7))
box = ax.boxplot(data, vert=False, patch_artist=True, notch=True)

# Customize the appearance of the boxes
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add annotations for median values inside each box
for i, line in enumerate(box['medians']):
    x, y = line.get_xydata()[1]  # Median x and y values
    ax.text(x, y, f'{x:.1f}', horizontalalignment='center', verticalalignment='center', 
            fontweight='bold', fontsize=9, color='white')

# Set y-tick labels
ax.set_yticklabels(role_labels, fontsize=11)

# Add labels and title with line breaks for clarity
ax.set_title("Technological Workspaces:\nDistribution of Screen Time Across Different Roles",
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Screen Time (Hours)", fontsize=12)
ax.set_ylabel("Roles", fontsize=12)

# Customize grid
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Add a legend indicating roles with matching colors
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(handles, role_labels, title="Roles", loc='upper right', bbox_to_anchor=(1.3, 1.0), fontsize='small')

# Automatically adjust layout for better appearance
plt.tight_layout()

# Display the plot
plt.show()