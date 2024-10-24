import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

# Data for the Ancient Wonders
wonders = [
    "Great Pyramid of Giza",
    "Hanging Gardens of Babylon",
    "Statue of Zeus at Olympia",
    "Temple of Artemis at Ephesus",
    "Mausoleum at Halicarnassus",
    "Colossus of Rhodes",
    "Lighthouse of Alexandria"
]

# Estimated construction years
construction_years = [20, 15, 8, 10, 7, 12, 5]

# Colors and patterns for each wonder
colors = [
    '#FFD700',  # Gold for the Pyramid
    '#98FB98',  # Light green for Gardens
    '#4682B4',  # Steel blue for Zeus
    '#FF6347',  # Tomato for Artemis
    '#8B4513',  # Saddle brown for Mausoleum
    '#4169E1',  # Royal blue for Colossus
    '#FF4500'   # Orange red for Lighthouse
]

patterns = ['/', '\\', '|', '-', '+', 'x', 'o']

# Create a horizontal bar chart with gradient effect
fig, ax = plt.subplots(figsize=(16, 9))
y_pos = np.arange(len(wonders))

bars = ax.barh(
    y_pos, construction_years, color=colors, edgecolor='black', height=0.6, hatch=patterns
)

# Adding labels, title, and grid
ax.set_yticks(y_pos)
ax.set_yticklabels(wonders, fontsize=10)
ax.invert_yaxis()  # Highest value at the top
ax.set_xlabel('Estimated Construction Years', fontsize=12)
ax.set_title('Construction Time of the Seven Ancient Wonders\n(Estimated in Years)', fontsize=16, fontweight='bold')
ax.grid(axis='x', linestyle='--', alpha=0.6)

# Annotate bars with their values and additional info
for bar, years in zip(bars, construction_years):
    ax.text(
        bar.get_width() + 0.5, 
        bar.get_y() + bar.get_height() / 2, 
        f'{years} years', 
        va='center', 
        ha='left', 
        fontsize=10, 
        color='black'
    )

# Background decoration
background = FancyBboxPatch(
    (0, 0), 1, 1, boxstyle="round,pad=0.1", color='whitesmoke', transform=ax.transAxes,
    zorder=-1, linewidth=0
)
ax.add_patch(background)

# Subtle Background Image (commented out as a placeholder)
# plt.figimage(plt.imread('ancient_map.jpg'), xo=0, yo=0, alpha=0.1, zorder=-1)

# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout()

# Display the chart
plt.show()