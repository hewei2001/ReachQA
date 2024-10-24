import numpy as np
import matplotlib.pyplot as plt

# Define decades and genres
decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
genres = ['Rock', 'Pop', 'Jazz', 'Hip-Hop', 'Electronic', 'Classical', 'Metal']

# Construct data for genre popularity across decades
popularity_scores = np.array([
    [90, 70, 40, 10, 20, 30, 50],  # 1960s
    [85, 75, 35, 20, 25, 25, 55],  # 1970s
    [80, 85, 30, 30, 40, 20, 60],  # 1980s
    [75, 90, 25, 50, 60, 15, 70],  # 1990s
    [70, 80, 20, 70, 75, 10, 65],  # 2000s
    [65, 90, 15, 80, 85, 10, 60],  # 2010s
    [60, 85, 10, 85, 90, 5, 55],   # 2020s
])

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))

# Create the heat map using 'magma' color map
cax = ax.imshow(popularity_scores.T, cmap='magma', aspect='auto', interpolation='nearest')

# Set title and labels
ax.set_title('Music Genre Popularity Evolution\nfrom 1960s to 2020s', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decades', fontsize=12, fontweight='bold')
ax.set_ylabel('Music Genres', fontsize=12, fontweight='bold')

# Configure ticks
ax.set_xticks(np.arange(len(decades)))
ax.set_yticks(np.arange(len(genres)))
ax.set_xticklabels(decades, fontsize=10)
ax.set_yticklabels(genres, fontsize=10)

# Annotate the heatmap with the data values
for i in range(popularity_scores.shape[1]):
    for j in range(popularity_scores.shape[0]):
        ax.text(i, j, f'{popularity_scores[j, i]}', ha='center', va='center', color='white', fontsize=8)

# Add a color bar
cbar = fig.colorbar(cax, pad=0.01)
cbar.set_label('Popularity Score', fontsize=12, fontweight='bold')

# Adjust layout for better display and avoid overlaps
plt.tight_layout()

# Display the plot
plt.show()