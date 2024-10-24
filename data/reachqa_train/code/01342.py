import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Extended Data for the funnel stages
stages = [
    "Manuscripts Received",
    "Initial Screening",
    "Peer Review",
    "Revision Needed",
    "Accepted for Evaluation",
    "Edited",
    "Proofing",
    "Ready for Print",
    "Published",
    "On Bestseller List"
]

counts = [500, 400, 300, 250, 200, 150, 120, 100, 80, 10]

# Colors for each stage with gradient transition
colors = [
    '#A1C4FD', '#89F7FE', '#8CDFD6', '#8ED69B', 
    '#92FE9D', '#FAD7A1', '#FF9A8B', '#FC5C9C', 
    '#F94892', '#C92367'
]

# Create the funnel chart
fig, ax = plt.subplots(figsize=(12, 8))

# Calculate the top and bottom widths and heights of each stage
total_height = len(stages)
funnel_widths = [np.log1p(count) / np.log1p(max(counts)) for count in counts]
stage_heights = [0.8 * (count / max(counts)) for count in counts]

# Plot each stage as a trapezoid with varying heights
for i, (stage, count) in enumerate(zip(stages, counts)):
    top_width = funnel_widths[i]
    bottom_width = funnel_widths[i+1] if i+1 < len(funnel_widths) else 0.1
    height = stage_heights[i]
    x0 = (1 - top_width) / 2
    x1 = (1 - bottom_width) / 2
    y0 = sum(stage_heights[:i])
    y1 = y0 + height

    polygon = patches.Polygon(
        [(x0, y0), (x0 + top_width, y0),
         (x1 + bottom_width, y1),
         (x1, y1)],
        closed=True, color=colors[i], edgecolor='grey'
    )
    ax.add_patch(polygon)

    # Add stage label and count with percentage change
    percentage_change = f"({int((counts[i] / counts[0]) * 100)}%)"
    ax.text(0.5, y0 + height/2, f"{stage}\n{count} Manuscripts {percentage_change}",
            ha='center', va='center', fontsize=9, color='black', fontweight='bold')

# Set plot title with line breaks
ax.set_title("The Elaborate Journey of a Bestselling Novel\nin the Publishing Pipeline",
             fontsize=16, fontweight='bold', va='bottom', ha='center')

# Set limits and hide axes
ax.set_xlim(0, 1)
ax.set_ylim(0, sum(stage_heights))
ax.axis('off')

# Enhance layout
plt.tight_layout()

# Display the plot
plt.show()