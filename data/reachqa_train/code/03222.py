import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Define the funnel stages and corresponding values
stages = [
    "Signups",
    "First Week Active",
    "Midterm Active",
    "Final Week Active",
    "Course Completion"
]
values = [10000, 7500, 5000, 3500, 2000]

# Define colors for the funnel stages
colors = ['#4c72b0', '#55a868', '#c44e52', '#8172b3', '#ccb974']

# Create a new figure for the funnel chart
fig, ax = plt.subplots(figsize=(10, 7))

# Define the width reduction factor between each stage
width_reduction = 0.15

# Starting position for the y-coordinate
start_y = np.arange(len(values))

# Draw trapezoids for each stage
for i, (stage, value) in enumerate(zip(stages, values)):
    # Calculate the width for the top and bottom of the trapezoid
    top_width = (1.0 - i * width_reduction)
    bottom_width = (1.0 - (i + 1) * width_reduction)
    
    # Define the corners of the trapezoid
    corners = [(1.0 - top_width) / 2, start_y[i], 
               (1.0 + top_width) / 2, start_y[i],
               (1.0 + bottom_width) / 2, start_y[i] + 0.8, 
               (1.0 - bottom_width) / 2, start_y[i] + 0.8]
    
    # Create a polygon for the trapezoid
    polygon = patches.Polygon(
        [corners[:2], corners[2:4], corners[4:6], corners[6:]], 
        closed=True, 
        color=colors[i], 
        edgecolor='black'
    )
    
    # Add the polygon to the axis
    ax.add_patch(polygon)
    
    # Add text label inside the trapezoid
    ax.text(0.5, start_y[i] + 0.4, f"{stage}: {value:,}", fontsize=12, fontweight='bold',
            color='white', ha='center', va='center')

# Set the limits and aspect of the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, len(stages))
ax.set_aspect('auto')

# Remove axes for a cleaner look
ax.axis('off')

# Add a title
plt.title("EduPlus Student Retention Funnel:\nTracking Engagement Across a Semester", fontsize=16, fontweight='bold', pad=20)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()