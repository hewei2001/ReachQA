import matplotlib.pyplot as plt
import numpy as np

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

# Define colors for each wonder
colors = [
    '#FFD700',  # Gold for the Pyramid
    '#98FB98',  # Light green for Gardens
    '#4682B4',  # Steel blue for Zeus
    '#FF6347',  # Tomato for Artemis
    '#8B4513',  # Saddle brown for Mausoleum
    '#4169E1',  # Royal blue for Colossus
    '#FF4500'   # Orange red for Lighthouse
]

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(14, 8))
y_pos = np.arange(len(wonders))

# Plot horizontal bars with specified colors
bars = ax.barh(y_pos, construction_years, color=colors, edgecolor='black', height=0.6)

# Adding labels, title, and grid
ax.set_yticks(y_pos)
ax.set_yticklabels(wonders, fontsize=10)
ax.invert_yaxis()  # Highest value at the top
ax.set_xlabel('Estimated Construction Years', fontsize=12)
ax.set_title('Construction Time of the Seven Ancient Wonders\n(Estimated in Years)', fontsize=16, fontweight='bold')
ax.grid(axis='x', linestyle='--', alpha=0.6)

# Annotate bars with their values
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

# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout()

# Display the chart
plt.show()