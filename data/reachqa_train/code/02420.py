import matplotlib.pyplot as plt
import numpy as np

# Define regions and sandwich types
regions = ['North America', 'Europe', 'Asia', 'South America']
sandwich_types = ['PB&J', 'BLT', 'Club', 'Cuban', 'Grilled Cheese']

# Popularity data for each region (as a percentage)
popularity = np.array([
    [25, 30, 20, 15, 10],  # North America
    [15, 20, 25, 20, 20],  # Europe
    [10, 15, 30, 25, 20],  # Asia
    [20, 10, 15, 30, 25]   # South America
])

# Define colors for each sandwich type
colors = ['#FFD700', '#FF6347', '#4682B4', '#32CD32', '#9400D3']

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(12, 8))

# Initialize the bottom values for stacking
bottom = np.zeros(len(regions))

# Create stacked bar chart
for idx, (sandwich, color) in enumerate(zip(sandwich_types, colors)):
    ax.bar(regions, popularity[:, idx], bottom=bottom, color=color, label=sandwich, alpha=0.8)
    bottom += popularity[:, idx]

# Title and labels
ax.set_title("Global Appetite for Sandwiches:\nA Stacked Analysis of Regional Preferences", fontsize=16, weight='bold', pad=20)
ax.set_ylabel("Popularity Percentage (%)", fontsize=12)
ax.set_xlabel("Regions", fontsize=12)

# Rotate x-axis labels to prevent overlap
plt.xticks(rotation=45, ha='right')

# Add legend outside of plot
ax.legend(title="Sandwich Types", bbox_to_anchor=(1.05, 1), loc='upper left')

# Automatically adjust the plot to ensure it fits neatly
plt.tight_layout()

# Display the plot
plt.show()