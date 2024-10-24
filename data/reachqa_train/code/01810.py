import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.colors import LinearSegmentedColormap

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
max_width = 1.0
widths = max_width * (pieces / pieces[0])

# Setup figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Create a gradient color map from teal to dark red
cmap = LinearSegmentedColormap.from_list("funnel_cmap", ['#76c7c0', '#8b0000'])

# Plot funnel sections using rectangles with gradient colors
y_position = np.arange(len(stages))
for i in range(len(stages)):
    color = cmap(i / (len(stages) - 1))
    ax.add_patch(Rectangle(
        (0.5 - widths[i] / 2, i), 
        widths[i], 1, color=color, edgecolor='grey'
    ))

# Invert the y-axis to have the first stage at the top
ax.invert_yaxis()

# Annotate the pieces and percentages on the chart with dynamic alignment to avoid overlaps
percentages = (pieces / pieces[0]) * 100
for i, (piece, perc) in enumerate(zip(pieces, percentages)):
    ax.text(0.5, i + 0.5, f"{stages[i]}\n{piece} pieces ({perc:.1f}%)", 
            va='center', ha='center', fontsize=9, color='black')

# Add arrows between sections to indicate flow
for i in range(len(stages) - 1):
    ax.annotate('', xy=(0.5, i + 0.9), xytext=(0.5, i + 0.1),
                arrowprops=dict(facecolor='grey', shrink=0.05))

# Set limits and remove axes
ax.set_xlim(0, 1)
ax.set_ylim(0, len(stages))
ax.axis('off')

# Add a thematic background pattern using a subtle gradient or watermark
fig.patch.set_facecolor('whitesmoke')

# Title with line breaks for readability
plt.title("The Stages of Sustainable\nFashion Production Funnel", 
          fontsize=16, fontweight='bold', color='darkgreen')

# Adjust layout to prevent overlaps
plt.tight_layout()

# Display the plot
plt.show()