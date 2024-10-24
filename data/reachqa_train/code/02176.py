import matplotlib.pyplot as plt
import numpy as np

# Define Tech Sectors and the number of Start-Ups in each
tech_sectors = ['FinTech', 'HealthTech', 'EdTech', 'AgriTech', 'CleanTech']
start_ups = [150, 90, 120, 60, 110]

# Assign colors for each sector for distinction
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create the bar chart
bars = ax.bar(np.arange(len(tech_sectors)), start_ups, color=colors, edgecolor='black', alpha=0.8)

# Title and axis labels
ax.set_title("Silicon Valley's Tech Sector Boom:\nStart-Up Distribution Over the Past Year", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Tech Sectors", fontsize=12)
ax.set_ylabel("Number of Start-Ups", fontsize=12)

# Set x-ticks and labels, with rotation for clarity
ax.set_xticks(np.arange(len(tech_sectors)))
ax.set_xticklabels(tech_sectors, fontsize=10, rotation=25)

# Add value labels above each bar
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 5, int(yval), ha='center', va='bottom', fontsize=10, fontweight='bold')

# Add horizontal grid lines only on y-axis for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Adjust the layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()