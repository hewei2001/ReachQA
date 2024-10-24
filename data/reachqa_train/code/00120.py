import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Data for funnel steps
steps = [
    "Enrollment",
    "Year 1\nCompletion",
    "Comprehensive\nExams",
    "Proposal\nDefense",
    "Dissertation\nDefense",
    "Graduation"
]

# Number of students at each stage
student_counts = np.array([1000, 750, 600, 400, 300, 250])

# Normalize widths for funnel-like appearance
widths = student_counts / student_counts[0]

# Set colors for each step for visual distinction
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f']

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Define the position and size of each stage of the funnel
for i in range(len(steps)):
    # Calculate the top and bottom widths for the trapezoid
    top_width = widths[i] if i == 0 else widths[i-1]
    bottom_width = widths[i]
    
    # Create trapezoid using Polygon
    trapezoid = patches.Polygon(
        [
            [(1 - top_width) / 2, i], [(1 + top_width) / 2, i], 
            [(1 + bottom_width) / 2, i + 1], [(1 - bottom_width) / 2, i + 1]
        ], closed=True, color=colors[i], edgecolor='black'
    )
    
    ax.add_patch(trapezoid)

    # Add text to the center of each trapezoid
    ax.text(0.5, i + 0.5, f"{steps[i]}\n{student_counts[i]} Students", 
            ha='center', va='center', fontsize=12, color='black', weight='bold')

# Customize the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, len(steps))
ax.axis('off')  # Remove axes for a cleaner look

# Title
ax.set_title(
    'The Path to PhD: Academic Attrition in STEM Disciplines', 
    fontsize=16, weight='bold', ha='center', va='bottom', pad=30
)

# Tight layout
plt.tight_layout()

# Display the plot
plt.show()