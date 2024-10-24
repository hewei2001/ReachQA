import matplotlib.pyplot as plt
import numpy as np

# Data representing the biomass proportion of different groups in a rainforest
labels = ['Trees', 'Shrubs', 'Animals', 'Fungi', 'Decomposers']
sizes = [40, 25, 20, 10, 5]

# Colors for each section of the ring chart
colors = ['forestgreen', 'lightgreen', 'gold', 'slategray', 'saddlebrown']

# Create the ring chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))

# Wedge properties for the ring chart
wedges, texts = ax.pie(
    sizes, colors=colors, wedgeprops=dict(width=0.4, edgecolor='w'), startangle=90, pctdistance=0.85
)

# Annotating the wedges with labels
for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1) / 2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    ax.annotate(f"{labels[i]}: {sizes[i]}%", xy=(x, y), xytext=(1.2*x, 1.2*y),
                horizontalalignment=horizontalalignment,
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", lw=0.72),
                arrowprops=dict(arrowstyle="-", connectionstyle="arc3,rad=0.1"))

# Set a central label inside the ring
ax.text(0, 0, "Rainforest\nEcosystem", ha='center', va='center', fontsize=12, fontweight='bold')

# Set the title of the chart with line breaks for clarity
plt.title("Harmony in Biodiversity:\nThe Ecosystem Symbiosis", fontsize=16, fontweight='bold')

# Ensure the layout is tight and non-overlapping
plt.tight_layout()

# Display the plot
plt.show()