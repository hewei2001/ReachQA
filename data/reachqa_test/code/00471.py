import matplotlib.pyplot as plt
import numpy as np

# Data for online creative communities
platforms = ['DeviantArt', 'ArtStation', 'Behance', 'Instagram', 'Twitter']
number_of_artists = [500, 800, 600, 1000, 300]
average_likes = [2500, 4000, 3500, 6000, 1200]
average_shares = [300, 500, 400, 700, 100]

# New metric for the bar plot: Average Likes per Artist
likes_per_artist = [likes / artists if artists > 0 else 0 for likes, artists in zip(average_likes, number_of_artists)]

# Create a figure with subplots
fig, ax = plt.subplots(1, 2, figsize=(16, 7))

# Scatter Plot
scatter = ax[0].scatter(average_likes, average_shares, s=[size / 2 for size in number_of_artists], 
                        alpha=0.6, edgecolors="w", linewidth=0.5, c=number_of_artists, cmap='viridis', 
                        marker='o')

# Annotate each point with the platform names
for i, platform in enumerate(platforms):
    ax[0].annotate(platform,
                   (average_likes[i], average_shares[i]),
                   textcoords="offset points",
                   xytext=(0, 10),
                   ha='center', fontsize=9)

# Title and labels for scatter plot
ax[0].set_title('Digital Art Adoption Trends:\nOnline Creative Communities in 2023', fontsize=16)
ax[0].set_xlabel('Average Likes', fontsize=12)
ax[0].set_ylabel('Average Shares', fontsize=12)
ax[0].set_xlim(0, 6500)
ax[0].set_ylim(0, 800)
ax[0].grid(True, linestyle='--', alpha=0.6)

# Add a color bar based on the size of the circles representing the number of artists
cbar = plt.colorbar(scatter, ax=ax[0])
cbar.set_label('Number of Artists', rotation=270, labelpad=15)
cbar.ax.invert_yaxis()

# Legend for scatter plot
ax[0].scatter([], [], c='black', alpha=0.6, s=100, label='More Artists')
ax[0].scatter([], [], c='black', alpha=0.6, s=50, label='Fewer Artists')
ax[0].legend(loc='upper left', fontsize=10)

# Bar Plot
ax[1].bar(platforms, likes_per_artist, color='teal', alpha=0.7)
ax[1].set_title('Average Likes per Artist by Platform', fontsize=16)
ax[1].set_xlabel('Platforms', fontsize=12)
ax[1].set_ylabel('Likes per Artist', fontsize=12)
ax[1].set_ylim(0, max(likes_per_artist) + 1)  # Set the limit slightly above max for clarity
ax[1].grid(axis='y', linestyle='--', alpha=0.6)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()