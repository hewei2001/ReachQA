import matplotlib.pyplot as plt
import numpy as np

# Data Setup
decades = ['1980s', '1990s', '2000s', '2010s']
genres = ['Rock', 'Pop', 'Hip-Hop', 'Jazz', 'Classical', 'Electronic']
popularity_data = np.array([
    [75, 72, 70, 68],  # Rock
    [60, 65, 85, 80],  # Pop
    [30, 40, 85, 90],  # Hip-Hop
    [70, 60, 45, 40],  # Jazz
    [40, 35, 30, 30],  # Classical
    [10, 50, 70, 75]   # Electronic
])

# Calculate average popularity across genres for each decade
average_popularity = popularity_data.mean(axis=0)

# Create main plot with heatmap
fig, ax1 = plt.subplots(figsize=(10, 7))
cax = ax1.imshow(popularity_data, cmap='viridis', aspect='auto')

# Color bar
cbar = plt.colorbar(cax)
cbar.set_label('Popularity Score', rotation=270, labelpad=15)

# Axes labels
ax1.set_xticks(np.arange(len(decades)))
ax1.set_yticks(np.arange(len(genres)))
ax1.set_xticklabels(decades)
ax1.set_yticklabels(genres)
plt.xticks(rotation=45)

# Title with a line break
ax1.set_title('Music Genres Popularity\nAcross the Decades', pad=20)

# Annotate heatmap cells
for i in range(len(genres)):
    for j in range(len(decades)):
        ax1.text(j, i, popularity_data[i, j], ha='center', va='center', color='white')

# Secondary axis for overlay
ax2 = ax1.twinx()
ax2.plot(np.arange(len(decades)), average_popularity, color='red', marker='o', linestyle='-', linewidth=2)
ax2.set_yticks([])
ax2.set_ylim(ax1.get_ylim())

# Legend for overlay
ax2.legend(['Avg Popularity'], loc='upper left', bbox_to_anchor=(1.05, 1))

# Layout adjustment
plt.tight_layout()

# Display plot
plt.show()