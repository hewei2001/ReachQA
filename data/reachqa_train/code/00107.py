import matplotlib.pyplot as plt
import numpy as np

# Data representing the biomass proportion of different groups in a rainforest
labels = ['Trees', 'Shrubs', 'Animals', 'Fungi', 'Decomposers']
sizes = [40, 25, 20, 10, 5]

# Colors for each section of the ring chart
colors = ['forestgreen', 'lightgreen', 'gold', 'slategray', 'saddlebrown']

# Create the ring chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(aspect="equal"))

# Wedge properties for the ring chart
wedges, texts, autotexts = ax.pie(
    sizes, colors=colors, wedgeprops=dict(width=0.4, edgecolor='w', linewidth=2, alpha=0.9), 
    startangle=90, autopct='%1.1f%%', pctdistance=0.75
)

# Enhance the auto-generated percentage texts
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)

# Annotate wedges with labels
for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1) / 2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    # Use a fixed connection style for arrows
    ax.annotate(f"{labels[i]}", xy=(x, y), xytext=(1.2 * x, 1.2 * y),
                horizontalalignment=horizontalalignment,
                bbox=dict(boxstyle="round,pad=0.3", fc="lightyellow", ec="gray", lw=0.72),
                arrowprops=dict(arrowstyle="-", connectionstyle="arc3,rad=0.3"))

# Set a central label inside the ring
ax.text(0, 0, "Rainforest\nEcosystem", ha='center', va='center', fontsize=14, fontweight='bold', color='darkblue')

# Set the title of the chart with line breaks for clarity
plt.title("Harmony in Biodiversity:\nThe Ecosystem Symbiosis", fontsize=16, fontweight='bold', color='darkgreen', va='baseline')

# Include a small legend off to the side
ax.legend(wedges, labels, title="Components", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Add a subtle shadow to the wedges to create depth
plt.gca().set_axis_off()  # Remove the axis for a clean look
plt.gca().add_artist(plt.Circle((0, 0), 0.2, color='w', zorder=0))

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()