import matplotlib.pyplot as plt
import numpy as np

# Sectors and their respective resource allocations
sectors = ["Energy", "Military", "Technology", "Healthcare", "Education"]
allocations = [30, 25, 20, 15, 10]

# Define colors for each sector using gradient-inspired shades
colors = ['#007acc', '#ff4d4d', '#33cc33', '#ffcc00', '#b266ff']

# Create a doughnut chart
fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    allocations, labels=sectors, colors=colors, startangle=140, explode=(0, 0, 0.1, 0, 0),
    autopct='%1.1f%%', pctdistance=0.75, textprops=dict(color="w", fontsize=10),
    wedgeprops=dict(width=0.3), shadow=True
)

# Enhance text readability
for text in texts:
    text.set_color('black')
    text.set_fontsize(11)

# Add a central annotation summarizing the chart's purpose
plt.gcf().text(0.5, 0.5, 'Galactic\nResource\nAllocation', fontsize=16, fontweight='bold', color='#333333', ha='center')

# Configure the title, using line breaks for better layout
plt.title('Resource Allocation Across Sectors\nin the Galactic Empire (Year 2223)', fontsize=16, fontweight='bold', pad=20)

# Add a legend with customized styling
plt.legend(wedges, sectors, title='Sectors', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10, frameon=False)

# Automatically adjust the layout to prevent overlapping elements
plt.tight_layout()

# Show the chart
plt.show()