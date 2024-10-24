import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Define the genres and decades
genres = ['Jazz', 'Rock', 'Pop', 'Hip-hop', 'Electronic']
decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s']

# Define the prominence scores for each genre across the decades
prominence_scores = np.array([
    [80, 40, 30, 10, 5],   # 1960s
    [70, 60, 40, 10, 5],   # 1970s
    [60, 80, 70, 20, 10],  # 1980s
    [40, 75, 90, 50, 30],  # 1990s
    [30, 70, 85, 60, 50],  # 2000s
    [20, 60, 80, 70, 65]   # 2010s
])

# Calculate average scores for additional line plot
average_scores = np.mean(prominence_scores, axis=1)

# Create the main figure and the grid for subplots
fig, (ax_heatmap, ax_lineplot) = plt.subplots(2, 1, figsize=(12, 14), gridspec_kw={'height_ratios': [3, 1]})

# Heatmap
cax = ax_heatmap.imshow(prominence_scores, cmap='Spectral', aspect='auto', interpolation='nearest')

# Color bar with improved positioning
cbar = fig.colorbar(cax, ax=ax_heatmap, fraction=0.046, pad=0.04)
cbar.set_label('Prominence Score', rotation=270, labelpad=20)

# Set labels and title for heatmap
ax_heatmap.set_xticks(np.arange(len(genres)))
ax_heatmap.set_yticks(np.arange(len(decades)))
ax_heatmap.set_xticklabels(genres, rotation=45, ha='right', fontsize=10)
ax_heatmap.set_yticklabels(decades, fontsize=10)
ax_heatmap.set_title('Musical Notes:\nThe Sonic Landscape of Musical Genres (1960s to 2010s)', fontsize=16, fontweight='bold', pad=20)

# Annotate the heatmap cells with the prominence scores with styling
for i in range(len(decades)):
    for j in range(len(genres)):
        score = prominence_scores[i, j]
        ax_heatmap.text(j, i, str(score), va='center', ha='center',
                        color='white' if score < 50 else 'black',
                        fontweight='bold' if score >= 80 else 'normal',
                        fontsize=12 if score >= 80 else 10)

# Additional Line Plot for Average Scores
ax_lineplot.plot(decades, average_scores, marker='o', linestyle='-', color='teal', linewidth=2, markersize=8)
ax_lineplot.set_title('Average Genre Prominence Across Decades', fontsize=14, fontweight='bold')
ax_lineplot.set_xlabel('Decades')
ax_lineplot.set_ylabel('Average Score')
ax_lineplot.grid(True)

# Improve layout
plt.tight_layout()

# Show the plot
plt.show()