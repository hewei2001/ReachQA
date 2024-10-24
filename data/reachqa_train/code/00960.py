import matplotlib.pyplot as plt
import numpy as np

# Data for book lengths in pages for each genre
science_fiction_lengths = [320, 290, 310, 350, 280, 315, 300, 340, 330, 295]
mystery_lengths = [210, 220, 230, 205, 225, 215, 200, 230, 240, 210]
fantasy_lengths = [450, 470, 440, 460, 480, 455, 475, 445, 430, 465]
romance_lengths = [180, 195, 170, 185, 175, 190, 180, 195, 200, 185]
historical_fiction_lengths = [400, 380, 390, 410, 405, 395, 400, 385, 375, 390]

data = [
    science_fiction_lengths, 
    mystery_lengths, 
    fantasy_lengths, 
    romance_lengths, 
    historical_fiction_lengths
]

# Calculate averages and identify outliers
averages = [np.mean(genre) for genre in data]
outliers = [[value for value in genre if value < np.percentile(genre, 25) - 1.5*(np.percentile(genre, 75) - np.percentile(genre, 25)) 
                                 or value > np.percentile(genre, 75) + 1.5*(np.percentile(genre, 75) - np.percentile(genre, 25))]
            for genre in data]

genres = ['Science Fiction', 'Mystery', 'Fantasy', 'Romance', 'Historical Fiction']

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))
box = ax.boxplot(data, labels=genres, patch_artist=True, notch=True, showmeans=True)

# Color setup for boxes
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF6666']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize medians, means, whiskers, and caps
plt.setp(box['medians'], color='black', linewidth=1.5)
plt.setp(box['means'], marker='o', color='blue', markersize=5)
plt.setp(box['whiskers'], linestyle='--', color='gray')
plt.setp(box['caps'], color='gray')

# Overlay line plot for averages
ax.plot(range(1, len(genres) + 1), averages, marker='s', linestyle='-', color='purple', label='Average Length')

# Scatter plot for outliers
for idx, genre_outliers in enumerate(outliers):
    ax.scatter([idx + 1] * len(genre_outliers), genre_outliers, color='red', zorder=3)

# Add grid and labels
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_title('Exploring Book Length Variability\nAcross Popular Genres', fontsize=14, fontweight='bold')
ax.set_xlabel('Genres', fontsize=12)
ax.set_ylabel('Book Length (Pages)', fontsize=12)

# Legend
ax.legend(loc='upper right')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()