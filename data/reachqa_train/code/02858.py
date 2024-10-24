import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

# Define the stages of the funnel and the corresponding values
stages = [
    "Ideation &\nConceptualization",
    "Research &\nDevelopment",
    "Prototype\nTesting",
    "Marketing &\nPre-Launch Hype",
    "Product\nLaunch",
    "Market\nPenetration"
]
values = [10000, 6000, 4000, 2000, 1500, 1000]

# Colors for each stage
colors = ['#FF5733', '#FF8D33', '#FFC733', '#33FF57', '#33FF8D', '#33FFC7']

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Start y-position for the first stage
y_start = 0

# Plot each stage as a rectangle with trapezoid appearance
for i, (stage, value, color) in enumerate(zip(stages, values, colors)):
    width = value / float(max(values))
    next_width = values[i + 1] / float(max(values)) if i + 1 < len(values) else width
    left = (1 - width) / 2

    # Draw a trapezoid by adding a rectangle with a width transition to the next stage
    ax.add_patch(Rectangle((left, y_start), width, 1, color=color, alpha=0.9))
    
    # Add text inside each stage
    ax.text(0.5, y_start + 0.5, f'{stage}\n{value} engagements', 
            fontsize=10, va='center', ha='center', color='black')
    
    y_start += 1

# Customizations for the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, len(stages))
ax.set_yticks([])  # Remove y ticks
ax.set_xticks([])  # Remove x ticks
ax.set_title("Tech Product Journey:\nFrom Concept to Market Success", fontsize=16, fontweight='bold', pad=15)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()