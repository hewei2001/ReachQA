import matplotlib.pyplot as plt
import numpy as np

# Data: Sectors and the estimated percentage of tasks performed by AI in 2030
sectors = [
    "Healthcare",
    "Finance",
    "Manufacturing",
    "Education",
    "Transport",
    "Retail",
    "Agriculture",
    "Energy",
    "Legal",
    "Entertainment"
]

# Estimated percentages
ai_integration = [75, 85, 90, 60, 80, 70, 50, 65, 55, 95]

# Colors assigned to each sector for better visual distinction
colors = plt.cm.viridis(np.linspace(0, 1, len(sectors)))

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the bars
bars = ax.barh(sectors, ai_integration, color=colors, edgecolor='black')

# Add percentage labels to the end of each bar
ax.bar_label(bars, fmt='%.0f%%', padding=5)

# Title and labels
ax.set_title("AI Integration Across Sectors by 2030", fontsize=18, fontweight='bold', pad=15)
ax.set_xlabel("Percentage of Tasks Performed by AI", fontsize=14)
ax.set_xlim(0, 100)

# Customize y-tick labels to avoid overlap and ensure clarity
ax.set_yticks(range(len(sectors)))
ax.set_yticklabels(sectors, fontsize=12)

# Vertical grid lines for easier value estimation
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Annotations highlighting key insights in top sectors
annotations = [
    ("Entertainment leads with 95%", 95),
    ("Transforming Manufacturing", 90),
    ("Finance: A strong AI foothold", 85)
]

for annotation, value in annotations:
    sector_index = ai_integration.index(value)
    ax.annotate(annotation, xy=(value, sector_index), 
                xytext=(value - 20, sector_index + 0.4),
                arrowprops=dict(arrowstyle="->", color='black'),
                fontsize=10, color='black')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()