import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Define the stages and corresponding data
stages = [
    "Concept Development", 
    "Sketching & Drafting", 
    "Artwork Creation", 
    "Peer Review & Critique",
    "Gallery Submission", 
    "Gallery Exhibition"
]
artwork_counts = np.array([100, 70, 40, 25, 15, 8])

# Define colors for each stage
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Calculate widths of trapezoids based on percentages
max_width = 200  # Maximum width of the funnel
trapezoid_widths = (artwork_counts / artwork_counts[0]) * max_width

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Starting position for the first trapezoid
y_start = 0
height = 1  # Height of each trapezoid

# Plot each stage of the funnel
for i in range(len(stages)):
    width_top = trapezoid_widths[i]
    width_bottom = trapezoid_widths[i+1] if i+1 < len(stages) else 0

    # Create the trapezoid
    trapezoid = patches.Polygon(
        [[(max_width - width_top)/2, y_start], [(max_width + width_top)/2, y_start],
         [(max_width + width_bottom)/2, y_start + height], [(max_width - width_bottom)/2, y_start + height]],
        closed=True,
        facecolor=colors[i],
        edgecolor='darkgrey'
    )

    # Add the trapezoid to the plot
    ax.add_patch(trapezoid)

    # Add text annotations
    ax.text(
        max_width / 2, 
        y_start + height / 2, 
        f"{stages[i]}: {artwork_counts[i]}",
        va='center', 
        ha='center',
        fontsize=10,
        fontweight='bold',
        color='black'
    )

    # Move to the next stage
    y_start += height + 0.3

# Title and labels
ax.set_title("The Artistic Journey:\nFrom Concept to Gallery", fontsize=14, fontweight='bold')
ax.set_xlim(0, max_width)
ax.set_ylim(0, y_start)
ax.axis('off')  # Hide axes

# Automatically adjust the layout
plt.tight_layout()

# Display the funnel chart
plt.show()