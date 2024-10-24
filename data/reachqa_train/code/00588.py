import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Data for the funnel stages
stages = ["Initial Interest", "Inquiry", "Booking", "Pre-Launch Training", "Launch"]
customers = np.array([10000, 7500, 4500, 3000, 1200])

# Normalize data for funnel width
funnel_widths = customers / float(max(customers))

# Reverse data order for plotting from top to bottom
stages = stages[::-1]
funnel_widths = funnel_widths[::-1]

# Define colors for the stages
colors = ['#0066cc', '#3399ff', '#66ccff', '#99ccff', '#cceeff']

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 7))

# Plotting the funnel using trapezoids
for i in range(len(stages)):
    # Calculate the position for each stage
    x1 = -funnel_widths[i] / 2
    x2 = funnel_widths[i] / 2
    y1 = i
    y2 = i + 1
    ax.add_patch(patches.Rectangle((x1, y1), funnel_widths[i], 1, color=colors[i], alpha=0.8))

    # Annotate the stage name and customer count
    ax.text(0, i + 0.5, f"{stages[i]}: {customers[::-1][i]}", fontsize=12, va='center', ha='center', color='white')

# Title and labels
plt.title("Galactic Adventures Customer Journey\nSpace Travel Experience", fontsize=16, fontweight='bold')
plt.xlabel('Proportion of Customers', fontsize=12)
plt.ylabel('Stages', fontsize=12)

# Adjust y-ticks
plt.yticks(np.arange(0.5, len(stages) + 0.5), stages)

# Hide x-ticks and set limits
plt.xticks([])
plt.xlim([-0.5, 0.5])

# Ensure layout is optimal
plt.tight_layout()

# Show plot
plt.show()