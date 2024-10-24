import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from matplotlib.patches import FancyArrow

# Define the stages and their respective values
stages = [
    "Manuscript\nSubmission", "Initial\nEditing", "Final\nEditing",
    "Production", "Marketing", "Distribution", "Bestseller\nStatus"
]
values = [1000, 800, 600, 500, 300, 200, 50]

# Calculate the width of each stage for plotting
stage_widths = np.array(values) / np.max(values)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 10))

# Gradient colors for each stage
colors = ['#003f5c', '#2f4b7c', '#665191', '#a05195', '#d45087', '#f95d6a', '#ffa600']
gradients = [np.linspace(0.8, 1.0, 100), np.linspace(1.0, 0.8, 100)]

# Plot each stage of the funnel
for i, (stage, width, color) in enumerate(zip(stages, stage_widths, colors)):
    start_width = width / 2
    end_width = stage_widths[i + 1] / 2 if i < len(stages) - 1 else 0

    # Create gradient effect
    for grad_index, grad in enumerate(gradients):
        ax.fill_betweenx(
            [i + grad_index / 2.0, i + 0.5 + grad_index / 2.0],
            -start_width, start_width,
            color=color, alpha=grad[0]
        )

    # Draw text annotations with arrows
    text_x = 0.6 if i % 2 == 0 else -0.6
    ax.annotate(
        f'{stage}: {values[i]}',
        xy=(0, i + 0.5), xycoords='data',
        xytext=(text_x, i + 0.5), textcoords='data',
        arrowprops=dict(facecolor='grey', shrink=0.05, width=1.5, headwidth=5),
        fontsize=11, fontweight='bold', color='black',
        horizontalalignment='center', verticalalignment='center'
    )

# Set limits and remove unnecessary axes
ax.set_ylim(0, len(stages))
ax.set_xlim(-1, 1)
ax.axis('off')

# Title with two lines for better readability
ax.set_title(
    "Journey of a Book: From Manuscript to Bestseller\nThe Funnel of Publishing Stages",
    fontsize=18, fontweight='bold', pad=20
)

# Ensure that layout is optimized
plt.tight_layout()

# Display the funnel chart
plt.show()