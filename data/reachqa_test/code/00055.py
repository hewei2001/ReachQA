import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Data for the funnel chart
stages = [
    "People Reached",
    "People Engaged",
    "People Educated",
    "People Acted",
    "People Sustained"
]
values = [10000, 6500, 4200, 2700, 1500]

# Create the funnel chart
fig, ax = plt.subplots(figsize=(10, 8))

# Define colors and gradients
colors = plt.cm.viridis_r(np.linspace(0.1, 0.9, len(stages)))

# Plot the funnel using trapezoids
for i in range(len(stages)):
    width_top = values[i] / max(values) * 0.8
    width_bottom = values[i + 1] / max(values) * 0.8 if i + 1 < len(values) else 0.2
    
    # Add a shadow effect for each trapezoid
    trapezoid = patches.Polygon(
        [[0.1 - width_top / 2, i], [0.1 + width_top / 2, i], 
         [0.1 + width_bottom / 2, i + 1], [0.1 - width_bottom / 2, i + 1]],
        closed=True,
        edgecolor='black',
        linewidth=1.5,
        facecolor=colors[i],
        alpha=0.85
    )
    ax.add_patch(trapezoid)
    
    # Adding arrows between stages
    if i < len(stages) - 1:
        ax.annotate('', xy=(0.1, i + 1), xytext=(0.1, i + 0.7),
                    arrowprops=dict(arrowstyle="->", color='black'))

    # Enhanced text label with better visibility
    ax.text(0.1, i + 0.5, f'{stages[i]}: {values[i]}', 
            fontsize=12, color='white', ha='center', 
            va='center', weight='bold', style='italic', 
            bbox=dict(facecolor='gray', alpha=0.3, boxstyle='round,pad=0.3'))

# Adjust the limits and remove axes
ax.set_xlim(-0.5, 0.7)
ax.set_ylim(0, len(stages))
ax.axis('off')

# Add title with line breaks for better visibility
plt.title("Environmental Campaign Funnel\nAwareness to Sustained Action",
          fontsize=16, fontweight='bold', loc='center')

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()