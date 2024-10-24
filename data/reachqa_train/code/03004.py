import matplotlib.pyplot as plt
import numpy as np

# Define game genres
genres = ['FPS: First-Person Shooter', 'RPG: Role-Playing Game', 'RTS: Real-Time Strategy', 'Sports Game']

# FPS data for each genre, creatively representing performance variations
fps_data = [
    [58, 61, 59, 62, 70, 65, 56, 60, 63, 67],  # FPS: Tight consistency
    [44, 50, 47, 51, 49, 54, 45, 48, 53, 50],  # RPG: Higher variability due to open environments
    [72, 75, 73, 72, 76, 73, 78, 71, 79, 74],  # RTS: Isometric views, generally high FPS
    [66, 69, 71, 67, 65, 69, 70, 68, 72, 70]   # Sports: Consistent FPS similar to RTS
]

# Initiate a plot
fig, ax = plt.subplots(figsize=(10, 6))

# Generate box plots
boxplots = ax.boxplot(fps_data, vert=True, patch_artist=True, notch=True, showmeans=True)

# Define custom colors for box plot fill
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
for patch, color in zip(boxplots['boxes'], colors):
    patch.set_facecolor(color)

# Configure title and axis labels
ax.set_title('Frame Rate Analysis Across Game Genres\n(Frames Per Second - FPS)', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Game Genres', fontsize=12, labelpad=10)
ax.set_ylabel('Frames Per Second (FPS)', fontsize=12, labelpad=10)

# Customize x-tick labels
ax.set_xticks(np.arange(1, len(genres) + 1))
ax.set_xticklabels(genres, rotation=15, ha='right', fontsize=10, fontweight='bold')

# Legend to explain color coding
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(handles, [genre.split(':')[0] for genre in genres], title="Genre", loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Ensure layout is tight and elements are visible
plt.tight_layout()

# Display the plot
plt.show()