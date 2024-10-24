import matplotlib.pyplot as plt
import numpy as np

# Define the board games and their play counts
games = [
    'Catan', 'Ticket to Ride', 'Pandemic', 'Carcassonne', 
    'Codenames', 'Dominion', 'Terraforming Mars', 'Gloomhaven',
    'Wingspan', 'Azul'
]

play_counts = np.array([125, 98, 114, 75, 135, 85, 95, 110, 145, 90])

# Generate colors using a colormap
colors = plt.cm.plasma(np.linspace(0.2, 0.8, len(games)))

# Create the bar chart
fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.barh(games, play_counts, color=colors, edgecolor='black')

# Add title and axis labels
ax.set_title('Top 10 Most Played Board Games\nat Meeple Haven Club (Past Year)', fontsize=16, fontweight='bold')
ax.set_xlabel('Number of Plays', fontsize=12)
ax.set_ylabel('Board Games', fontsize=12)

# Annotate bars with the play count
for bar in bars:
    width = bar.get_width()
    ax.text(width + 2, bar.get_y() + bar.get_height() / 2, f'{int(width)}', 
            va='center', fontsize=10, color='black', weight='bold')

# Customize the grid
ax.xaxis.grid(True, linestyle='--', alpha=0.6)
ax.set_axisbelow(True)

# Ensure labels are clear and readable
plt.xticks(rotation=0)

# Automatically adjust layout to prevent text from clipping
plt.tight_layout()

# Show the plot
plt.show()