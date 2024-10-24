import matplotlib.pyplot as plt
import numpy as np

# Data: Album lengths in minutes for each genre
rock_album_lengths = [42, 48, 55, 47, 50, 53, 60, 45, 40, 52, 58, 46, 49, 51]
pop_album_lengths = [35, 37, 40, 42, 38, 39, 41, 45, 44, 36, 39, 43, 46, 47]
jazz_album_lengths = [50, 55, 52, 57, 54, 60, 58, 63, 62, 55, 51, 56, 61, 59]
hiphop_album_lengths = [45, 48, 50, 47, 52, 49, 51, 53, 46, 49, 50, 52, 48, 47]
classical_album_lengths = [65, 70, 72, 75, 68, 66, 71, 73, 69, 74, 70, 67, 72, 75]

# Combine all data into a single list
all_album_lengths = [
    rock_album_lengths,
    pop_album_lengths,
    jazz_album_lengths,
    hiphop_album_lengths,
    classical_album_lengths
]

# Genre names
genres = ['Rock', 'Pop', 'Jazz', 'Hip-Hop', 'Classical']

# Create the boxplot
plt.figure(figsize=(10, 6))
box = plt.boxplot(all_album_lengths, labels=genres, patch_artist=True, notch=True)

# Customizing the box plot
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFD700', '#FFCC99']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize whiskers, caps, and medians
plt.setp(box['whiskers'], color='gray', linestyle='-')
plt.setp(box['caps'], color='gray')
plt.setp(box['medians'], color='black', linewidth=2)

# Add titles and labels
plt.title('Distribution of Album Lengths by Genre\n(2013-2023)', fontsize=14, weight='bold')
plt.xlabel('Music Genre', fontsize=12)
plt.ylabel('Album Length (minutes)', fontsize=12)

# Adding grid lines for clarity
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()