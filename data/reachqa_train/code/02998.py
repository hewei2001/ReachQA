import matplotlib.pyplot as plt
import numpy as np

# Data for the Seven Wonders of the Ancient World
wonders = [
    "Great Pyramid of Giza",
    "Hanging Gardens of Babylon",
    "Statue of Zeus at Olympia",
    "Temple of Artemis at Ephesus",
    "Mausoleum at Halicarnassus",
    "Colossus of Rhodes",
    "Lighthouse of Alexandria"
]

# Estimated heights (in meters)
heights = np.array([146.6, 25, 12, 18, 45, 33, 100])

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Bar colors
colors = ['#FFD700', '#8FBC8F', '#CD5C5C', '#FFA07A', '#4682B4', '#DAA520', '#FF8C00']

# Plotting the bars
ax.barh(wonders, heights, color=colors, edgecolor='black', height=0.6)

# Title and labels
ax.set_title('Estimated Heights of the Seven Wonders\nof the Ancient World', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Height (meters)', fontsize=14)
ax.set_ylabel('Wonder', fontsize=14)

# Annotating the bars with heights
for i, height in enumerate(heights):
    ax.text(height + 2, i, f'{height:.1f} m', va='center', ha='left', fontsize=12, color='black')

# Customizing the y-axis
ax.set_yticks(np.arange(len(wonders)))
ax.set_yticklabels(wonders, fontsize=12)
ax.tick_params(axis='y', which='major', pad=10)

# Invert the y-axis for better readability
ax.invert_yaxis()

# Adding a vertical grid
ax.xaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.6)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()