import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# Define the stages and their respective values
stages = [
    "Manuscript\nSubmission", "Initial\nEditing", "Final\nEditing",
    "Production", "Marketing", "Distribution", "Bestseller\nStatus"
]
values = [1000, 800, 600, 500, 300, 200, 50]

# Calculate the width of each stage for plotting
stage_widths = np.array(values) / np.max(values)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Colors for each stage
colors = ['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600', '#ff7c43', '#ffa500']

# Plot each stage of the funnel
for i, (stage, width, color) in enumerate(zip(stages, stage_widths, colors)):
    # Define the starting and ending width for each funnel section
    start_width = stage_widths[i] / 2
    end_width = stage_widths[i + 1] / 2 if i < len(stages) - 1 else 0

    # Draw a trapezoid representing each stage
    ax.fill_betweenx([i, i + 1], -start_width, start_width, color=color, alpha=0.8)
    ax.fill_betweenx([i, i + 1], -end_width, end_width, color=color, alpha=0.8)

    # Annotate the stage with its name and value
    ax.text(0, i + 0.5, f'{stage}: {values[i]}', va='center', ha='center', fontsize=11, fontweight='bold', color='white')

# Set limits and remove unnecessary axes
ax.set_ylim(0, len(stages))
ax.set_xlim(-0.5, 0.5)
ax.axis('off')

# Title with two lines for better readability
ax.set_title(
    "Journey of a Book: From Manuscript to Bestseller\nThe Funnel of Publishing Stages",
    fontsize=16, fontweight='bold', pad=20
)

# Ensure that layout is optimized
plt.tight_layout()

# Display the funnel chart
plt.show()