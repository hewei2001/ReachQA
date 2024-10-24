import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# Define stages in the sustainable fashion production process
stages = [
    "Concept and Design",
    "Material Sourcing",
    "Eco-friendly Manufacturing",
    "Quality Assurance",
    "Distribution and Retail",
    "Sold to Consumers"
]

# Define the number of pieces at each stage
pieces = np.array([1000, 800, 600, 450, 300, 200])

# Calculate the width of each funnel section relative to the maximum
max_width = 1.0  # Max width of the funnel at the top
widths = max_width * (pieces / pieces[0])

# Setup figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Plot funnel sections using rectangles
y_position = np.arange(len(stages))
colors = ['#76c7c0', '#66b3ff', '#ffcccb', '#ffdd57', '#9acd32', '#8b0000']
for i, (width, color) in enumerate(zip(widths, colors)):
    ax.add_patch(Rectangle(
        (0.5 - width / 2, i),  # Center the rectangle
        width, 1, color=color, edgecolor='grey'
    ))

# Invert the y-axis to have the first stage at the top
ax.invert_yaxis()

# Annotate the pieces and percentages on the chart
percentages = (pieces / pieces[0]) * 100
for i, (piece, perc) in enumerate(zip(pieces, percentages)):
    ax.text(0.5, i + 0.5, f"{stages[i]}: {piece} pieces\n({perc:.1f}%)", va='center', ha='center', fontsize=9, color='black')

# Set limits and remove axes
ax.set_xlim(0, 1)
ax.set_ylim(0, len(stages))
ax.axis('off')

# Add a title with line breaks for better readability
plt.title("The Stages of Sustainable\nFashion Production Funnel", fontsize=14, fontweight='bold')

# Adjust layout to prevent overlaps
plt.tight_layout()

# Display the plot
plt.show()