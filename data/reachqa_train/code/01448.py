import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

# Define the stages and their respective manuscript/book counts
stages = [
    "Manuscript\nSubmissions",
    "Manuscripts\nReviewed",
    "Initial\nAcceptance",
    "Editing and\nRevisions",
    "Final Approval\nfor Publication",
    "Books\nPublished",
    "Bestsellers"
]

counts = [10000, 5000, 2500, 1000, 500, 250, 50]
percentages = [f"{(c / counts[0]) * 100:.1f}%" for c in counts]

# Related but different data: Average processing times (in days)
processing_times = [30, 25, 20, 18, 15, 10, 5]

# Set up figure and axis
fig, ax1 = plt.subplots(figsize=(10, 8))

# Define colors for each stage
colors = [
    '#FF6F61', '#FFA177', '#FFD081', 
    '#C3DD8D', '#8DC3DE', '#8EA4D2', 
    '#A098B6'
]

# Plot each stage as a trapezoid-like shape
for i in range(len(stages)):
    upper_width = 1 - (i / len(stages) * 0.4)
    lower_width = 1 - ((i + 1) / len(stages) * 0.4)
    left_offset = (1 - upper_width) / 2
    height = 1
    
    points = [
        (left_offset, i * height), 
        (1 - left_offset, i * height),
        ((1 - lower_width) / 2, (i + 1) * height), 
        (1 - (1 - lower_width) / 2, (i + 1) * height)
    ]
    
    polygon = Polygon(points, closed=True, facecolor=colors[i], edgecolor='white', lw=2)
    ax1.add_patch(polygon)
    
    ax1.text(0.5, i + 0.5, f"{stages[i]}: {counts[i]}\n({percentages[i]})",
             ha='center', va='center', color='black', fontsize=11)

# Line plot overlay for processing times
ax2 = ax1.twinx()
ax2.plot(processing_times, range(len(stages)), marker='o', color='grey', linewidth=2, label='Avg Processing Time (days)')
ax2.set_ylim(0, len(stages))
ax2.invert_yaxis()  # Invert y-axis to match the funnel direction
ax2.set_ylabel('Average Processing Time (days)', fontsize=12, color='grey')
ax2.tick_params(axis='y', labelcolor='grey')

# Customize layout and aesthetics
ax1.set_xlim(0, 1)
ax1.set_ylim(0, len(stages))
ax1.set_yticks([])
ax1.set_xticks([])
ax1.axis('off')
ax1.set_title("The Publishing Process: Manuscript to Bestseller\nA Journey of Aspiring Authors",
              fontsize=16, fontweight='bold', pad=20)

# Add legend for the line plot
ax2.legend(loc='upper right')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()