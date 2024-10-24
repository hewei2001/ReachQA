import matplotlib.pyplot as plt
import numpy as np

# Define regions and their corresponding contribution percentages
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Oceania']
contributions = [22, 28, 30, 9, 6, 5]

# Define colors for each region
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Calculate total contributions for percentage annotations
total_contributions = sum(contributions)

# Create the ring chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    contributions, 
    labels=regions, 
    colors=colors, 
    autopct=lambda p: '{:.1f}%'.format(p * total_contributions / 100),
    startangle=140,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Draw a circle at the center to label the chart internally
inner_circle = plt.Circle((0, 0), 0.35, color='white')
ax.add_artist(inner_circle)
ax.text(0, 0, 'Sustainability\nEfforts', horizontalalignment='center', verticalalignment='center', fontsize=12, fontweight='bold')

# Ensure the ring chart is perfectly circular
ax.axis('equal')

# Title and styling
plt.title("Global Contributions to Environmental Sustainability\nRegion-wise Breakdown", fontsize=16, fontweight='bold')
plt.setp(texts, size=10, weight='bold')
plt.setp(autotexts, size=10, weight='bold', color='black')

# Position the legend outside the chart
plt.legend(wedges, regions, title="Regions", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Adjust layout to ensure all elements fit well within the figure
plt.tight_layout()

# Show the chart
plt.show()