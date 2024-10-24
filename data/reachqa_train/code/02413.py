import matplotlib.pyplot as plt
import numpy as np

# Define fashion trends and continents
trends = ['Vintage', 'Minimalist', 'Athleisure', 'Bohemian', 'Sustainable', 'Futuristic', 'Streetwear']
continents = ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Oceania']

# Original popularity index data
popularity_index = np.array([
    [80, 65, 70, 75, 60, 85],  # Vintage
    [70, 50, 85, 55, 45, 60],  # Minimalist
    [75, 60, 65, 80, 55, 70],  # Athleisure
    [65, 75, 60, 70, 80, 65],  # Bohemian
    [90, 80, 95, 85, 75, 80],  # Sustainable
    [55, 45, 50, 60, 50, 65],  # Futuristic
    [85, 70, 75, 90, 65, 80]   # Streetwear
])

# Compute average popularity for each trend
average_popularity = popularity_index.mean(axis=1)

# Create subplots
fig, ax = plt.subplots(1, 2, figsize=(18, 8))

# First subplot: Heatmap of popularity indices
cax = ax[0].imshow(popularity_index, cmap='coolwarm', aspect='auto', interpolation='nearest')
ax[0].set_title('Global Popularity of Fashion Trends\nAcross Continents', fontsize=14, fontweight='bold', pad=20)
ax[0].set_xticks(np.arange(len(continents)))
ax[0].set_yticks(np.arange(len(trends)))
ax[0].set_xticklabels(continents, rotation=45, ha='right', fontsize=10)
ax[0].set_yticklabels(trends, fontsize=10)

# Annotate the heatmap
for i in range(len(trends)):
    for j in range(len(continents)):
        color = 'white' if popularity_index[i, j] < 70 else 'black'
        ax[0].text(j, i, popularity_index[i, j], ha='center', va='center', color=color, fontsize=9)

# Correct color bar for the heatmap
cbar = fig.colorbar(cax, ax=ax[0], orientation='vertical')
cbar.set_label('Popularity Index (0 to 100)', fontsize=10)

# Second subplot: Bar chart of average popularity
ax[1].bar(trends, average_popularity, color='skyblue', edgecolor='black')
ax[1].set_title('Average Global Popularity of Fashion Trends', fontsize=14, fontweight='bold', pad=20)
ax[1].set_ylabel('Average Popularity Index', fontsize=12)
ax[1].set_ylim(0, 100)
ax[1].set_xticklabels(trends, rotation=45, ha='right', fontsize=10)

# Layout adjustment
plt.tight_layout()

# Show the plot
plt.show()