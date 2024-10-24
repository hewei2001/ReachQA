import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

# Define the stages of the funnel and corresponding values
stages = [
    "Ideation &\nConceptualization",
    "Initial Research",
    "Detailed R&D",
    "Prototype\nDevelopment",
    "Prototype\nTesting",
    "Focus Group\nAnalysis",
    "Marketing &\nPre-Launch Hype",
    "Product\nLaunch",
    "Initial Sales\nFeedback",
    "Market\nPenetration"
]
values = [10000, 9000, 7500, 5000, 3000, 2500, 2000, 1500, 1200, 1000]

# Calculate percentage drop between stages
percentage_drops = [(values[i] - values[i+1]) / values[i] * 100 for i in range(len(values) - 1)]

# Colors for each stage
colors = ['#FF5733', '#FF6F33', '#FF8D33', '#FFA833', '#FFC733', '#E1FF33', 
          '#8DFF33', '#33FF57', '#33FF8D', '#33FFC7']

# Create the plot
fig, ax = plt.subplots(figsize=(10, 8))

# Start y-position for the first stage
y_start = 0

# Plot each stage as a rectangle with trapezoid appearance
for i, (stage, value, color) in enumerate(zip(stages, values, colors)):
    width = value / float(max(values))
    left = (1 - width) / 2

    # Draw a rectangle
    rect = Rectangle((left, y_start), width, 1, color=color, alpha=0.9)
    ax.add_patch(rect)

    # Add text inside each stage
    ax.text(0.5, y_start + 0.5, f'{stage}\n{value} engagements', 
            fontsize=10, va='center', ha='center', color='black')
    
    # Display percentage drop on the side
    if i < len(percentage_drops):
        ax.text(1.02, y_start + 0.5, f'{percentage_drops[i]:.1f}% drop', 
                fontsize=9, va='center', ha='left', color='gray')
    
    y_start += 1

# Customizations for the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, len(stages))
ax.set_yticks([])
ax.set_xticks([])
ax.set_title("Tech Product Journey:\nA Complex Funnel From Concept to Market Success", 
             fontsize=14, fontweight='bold', pad=15)

# Add grid lines for better readability
ax.yaxis.grid(True, which='major', linestyle='--', linewidth=0.5)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()