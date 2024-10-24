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

# Estimated percentages for 2030
ai_integration_2030 = [75, 85, 90, 60, 80, 70, 50, 65, 55, 95]

# Hypothetical data for 2020
ai_integration_2020 = [30, 40, 50, 25, 35, 30, 20, 25, 15, 40]

# Colors assigned to each sector for better visual distinction
colors = plt.cm.viridis(np.linspace(0, 1, len(sectors)))

# Create a horizontal bar chart
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the bars for 2030 data
bars = ax1.barh(sectors, ai_integration_2030, color=colors, edgecolor='black', label='2030 AI Integration')
ax1.set_xlabel("Percentage of Tasks Performed by AI", fontsize=14)
ax1.set_xlim(0, 100)
ax1.set_yticks(range(len(sectors)))
ax1.set_yticklabels(sectors, fontsize=12)

# Add percentage labels to the end of each bar
ax1.bar_label(bars, fmt='%.0f%%', padding=5)

# Create a secondary y-axis for the line plot
ax2 = ax1.twiny()
ax2.plot(ai_integration_2020, range(len(sectors)), 'r-o', label='2020 AI Integration', markersize=8)
ax2.set_xlim(0, 100)

# Title and labels
plt.title("AI Integration Across Sectors\n2020 vs 2030", fontsize=18, fontweight='bold', pad=20)

# Vertical grid lines for easier value estimation
ax1.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Annotations highlighting key insights in top sectors
annotations = [
    ("Entertainment leads with 95%", 95, 'r'),
    ("Transforming Manufacturing", 90, 'g'),
    ("Finance: A strong AI foothold", 85, 'b')
]

for annotation, value, color in annotations:
    sector_index = ai_integration_2030.index(value)
    ax1.annotate(annotation, xy=(value, sector_index),
                xytext=(value - 20, sector_index + 0.4),
                arrowprops=dict(arrowstyle="->", color='black'),
                fontsize=10, color=color)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Add legends
ax1.legend(loc='upper left', bbox_to_anchor=(0, 1), fontsize=12, title="Year", title_fontsize='13')
ax2.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=12)

# Display the plot
plt.show()