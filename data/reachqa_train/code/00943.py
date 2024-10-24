import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import AnchoredText
# import mplcursors  # Commented out because mplcursors might not be installed

# Data
decades = ['1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
rock = [50, 45, 35, 30, 25, 20]
pop = [20, 25, 30, 35, 40, 45]
hip_hop = [0, 5, 15, 25, 30, 25]
classical = [10, 8, 5, 4, 3, 2]
jazz = [10, 7, 4, 3, 2, 1]
electronic = [5, 5, 5, 10, 15, 20]
country = [5, 5, 6, 6, 5, 7]
total_consumption = np.array(rock) + np.array(pop) + np.array(hip_hop) + \
                    np.array(classical) + np.array(jazz) + np.array(electronic) + np.array(country)

colors = ['#8B0000', '#FF69B4', '#8A2BE2', '#FFD700', '#4682B4', '#32CD32', '#D2691E']

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Stacked area chart
ax.stackplot(decades, rock, pop, hip_hop, classical, jazz, electronic, country,
             labels=['Rock', 'Pop', 'Hip-Hop', 'Classical', 'Jazz', 'Electronic', 'Country'],
             colors=colors, alpha=0.8)

# Highlight specific trends with markers
highlight_points = {'rock': 0, 'hip_hop': 4, 'electronic': 5}  # Indices of interest
for genre, idx in highlight_points.items():
    genre_data = locals()[genre]
    ax.plot(decades[idx], genre_data[idx], marker='o', color='black')
    ax.annotate(f'{genre.capitalize()} Spike', (decades[idx], genre_data[idx]),
                textcoords="offset points", xytext=(-10,10), ha='center')

# Overlay line plot for total music consumption
ax2 = ax.twinx()
ax2.plot(decades, total_consumption, color='black', linestyle='--', linewidth=1.5)
ax2.set_ylabel('Total Music Consumption Index', fontsize=12, color='black')
ax2.yaxis.label.set_color('black')

# Style the plot
ax.set_title("The Evolution of Music Genres Over Time:\nFrom the 1970s to the 2020s", fontsize=16, weight='bold')
ax.set_xlabel("Decade", fontsize=12)
ax.set_ylabel("Percentage of Total Music Consumption", fontsize=12)
ax.set_ylim(0, 100)
ax.grid(True, linestyle='--', alpha=0.5)

# Accessibility improvements
ax.legend(loc='upper left', title="Music Genres", fontsize=10, title_fontsize='13', bbox_to_anchor=(1.15, 1))

# Enhance interactivity
# mplcursors.cursor(hover=True)  # Commented out because mplcursors might not be installed

# Secondary notes
note = AnchoredText("Key Events: \n- 1980s: Rise of MTV\n- 2000s: Streaming Emerges", loc='lower right', frameon=True, pad=0.5)
ax.add_artist(note)

# Final layout adjustments
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()