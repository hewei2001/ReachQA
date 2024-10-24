import matplotlib.pyplot as plt
import numpy as np

# Data for mythical creature sightings
creatures = ['Dragon', 'Unicorn', 'Phoenix', 'Mermaid', 'Griffin', 'Centaur']
sightings = [150, 120, 80, 100, 60, 90]
characteristics = [
    "Fiery and Majestic", 
    "Graceful and Magical", 
    "Rebirth from Ashes", 
    "Mysterious and Alluring", 
    "Guardian of Treasures", 
    "Dual Natured and Wise"
]

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create the bar chart
bar_positions = np.arange(len(creatures))
colors = ['#FF6347', '#FFD700', '#FF4500', '#1E90FF', '#8A2BE2', '#7FFF00']
bars = ax.bar(bar_positions, sightings, color=colors, width=0.6)

# Title and labels
ax.set_title('Enchanted Encounters:\nMythical Creature Sightings by Country', fontsize=16, weight='bold')
ax.set_xlabel('Mythical Creatures', fontsize=12)
ax.set_ylabel('Number of Sightings', fontsize=12)

# Set x-axis labels
ax.set_xticks(bar_positions)
ax.set_xticklabels(creatures, rotation=45, ha='right')

# Add grid lines
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adding annotations
for bar, characteristic in zip(bars, characteristics):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 2, characteristic, ha='center', va='bottom', fontsize=10, style='italic')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()