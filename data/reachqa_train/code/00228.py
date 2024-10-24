import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Define stages and corresponding data
stages = [
    'Initial Awareness',
    'Feasibility Study',
    'Strategic Planning',
    'Pilot Implementation',
    'Full-scale Deployment'
]
counts = [500, 380, 260, 150, 80]

# Calculate the width of each stage to represent its size proportionally
widths = np.array(counts) / max(counts)

# Define colors for each stage
colors = ['#76c7c0', '#4a7c59', '#ffcc29', '#f7a072', '#d9455f']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 10))

# Starting position for the first rectangle
y_position = 0

# Draw each stage of the funnel using rectangles
for i, (stage, count, width, color) in enumerate(zip(stages, counts, widths, colors)):
    # Draw trapezoid-like rectangles with decreasing width
    ax.add_patch(patches.Rectangle((0.5 - width / 2, y_position), width, 1, color=color))
    
    # Annotate with the stage name and count
    ax.text(0.5, y_position + 0.5, f'{stage}\n{count} organizations',
            ha='center', va='center', fontsize=10, color='white', fontweight='bold')
    
    # Update position for the next stage
    y_position += 1.1  # Increase spacing between stages

# Remove axes
ax.set_xlim(0, 1)
ax.set_ylim(0, len(stages))
ax.axis('off')

# Set title
plt.title("Pathway to Sustainability:\nTransition Stages to Renewable Energy", fontsize=14, fontweight='bold', pad=20)

# Use tight layout to avoid clipping text
plt.tight_layout()
plt.show()