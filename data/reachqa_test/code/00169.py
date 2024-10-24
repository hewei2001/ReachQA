import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Define continents and their respective genre streaming percentages
continents = ['North America', 'Europe', 'Asia', 'South America', 'Africa']
genres = ['Pop', 'Rock', 'Hip-Hop', 'Jazz', 'Classical']

# Streaming preference percentages for each continent
streaming_data = {
    'North America': [40, 25, 20, 10, 5],
    'Europe': [30, 30, 15, 15, 10],
    'Asia': [35, 20, 25, 10, 10],
    'South America': [45, 20, 15, 5, 15],
    'Africa': [30, 25, 20, 10, 15]
}

# Create the percentage bar chart
fig, ax = plt.subplots(figsize=(14, 9))
fig.patch.set_facecolor('#f7f7f7')

# Define a sophisticated color palette for different genres
colors = ['#a1d99b', '#6baed6', '#fdae6b', '#fd8d3c', '#9e9ac8']
cmap = LinearSegmentedColormap.from_list('custom_cmap', colors, N=100)

# Starting point for each bar (cumulative percentage)
bottoms = np.zeros(len(continents))

# Plot each genre's percentage for each continent
for idx, genre in enumerate(genres):
    percentages = [streaming_data[continent][idx] for continent in continents]
    bars = ax.barh(continents, percentages, left=bottoms, label=genre, 
                   color=cmap(idx * 20), edgecolor='grey', linewidth=0.5)
    bottoms += percentages

    # Label each segment with its percentage value
    for bar, percent in zip(bars, percentages):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_y() + bar.get_height() / 2,
            f'{percent}%',
            ha='center',
            va='center',
            color='black',
            fontsize=9,
            fontweight='bold'
        )

# Add labels and title
ax.set_xlabel('Percentage of Total Streaming Hours', fontsize=12, fontweight='bold', color='#333333')
ax.set_title('The Evolution of Global Music Streaming Preferences\nAcross Continents', fontsize=16, fontweight='bold', color='#333333', pad=20)

# Set x-axis to 0-100% to ensure consistency
ax.set_xlim(0, 100)

# Add a legend
ax.legend(title='Music Genres', loc='upper center', bbox_to_anchor=(0.5, -0.1), fontsize=10, ncol=5, frameon=False)

# Customize tick labels
plt.xticks(range(0, 101, 10))

# Grid and background enhancements
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.6)
ax.set_facecolor('#f0f0f0')

# Optimize layout
plt.tight_layout(pad=2.0, rect=[0, 0.05, 1, 1])

# Show the plot
plt.show()