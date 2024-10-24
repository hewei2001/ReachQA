import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

# Define regions and their corresponding contribution percentages
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Oceania']
contributions = [22, 28, 30, 9, 6, 5]

# Calculate total contributions for percentage annotations
total_contributions = sum(contributions)

# Define gradient color map for a more engaging look
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
fig.subplots_adjust(wspace=0.3)

# Create the ring chart with a subtle 3D effect
wedges, texts, autotexts = ax1.pie(
    contributions, 
    labels=regions, 
    colors=colors, 
    autopct=lambda p: '{:.1f}%'.format(p * total_contributions / 100),
    startangle=140,
    wedgeprops=dict(width=0.3, edgecolor='w', linewidth=2.5)
)

# Inner circle with textured pattern for added depth
inner_circle = Circle((0, 0), 0.35, facecolor='lightgray', edgecolor='black', linewidth=0.5)
ax1.add_artist(inner_circle)

# Enhanced label at the center
ax1.text(0, 0, 'Sustainability\nEfforts', horizontalalignment='center', verticalalignment='center', fontsize=12, fontweight='bold', color='black')

# Ensure the ring chart is perfectly circular
ax1.axis('equal')

# Title and styling
ax1.set_title("Global Contributions to Environmental Sustainability\nRegion-wise Breakdown", fontsize=14, fontweight='bold', loc='center', pad=20)
plt.setp(texts, size=10)
plt.setp(autotexts, size=9, weight='bold', color='white')

# Position the legend outside the chart
ax1.legend(wedges, regions, title="Regions", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Additional subplot: A bar chart to compare contributions
bar_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
ax2.barh(regions, contributions, color=bar_colors)
ax2.set_xlabel('Contributions (%)', fontsize=12)
ax2.set_title('Contribution Comparison', fontsize=14, fontweight='bold')
ax2.set_xlim(0, 35)
for i, v in enumerate(contributions):
    ax2.text(v + 1, i, f"{v}%", color='black', va='center', fontweight='bold')

# Adjust layout to ensure all elements fit well within the figure
plt.tight_layout()

# Show the chart
plt.show()