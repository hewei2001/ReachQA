import matplotlib.pyplot as plt
import numpy as np

# Define genres
genres = ['Science Fiction', 'Mystery', 'Romance', 'Non-Fiction', 'Fantasy']

# Generate hypothetical data: hours spent reading each genre per week
data = [
    [5, 6, 7, 8, 6, 5, 9, 10, 7, 8, 6, 7, 8, 6, 7, 5, 12, 14, 5],
    [3, 4, 5, 6, 5, 4, 6, 7, 5, 8, 5, 4, 7, 5, 6, 8, 4, 3, 10, 12],
    [2, 3, 4, 3, 5, 6, 4, 5, 3, 4, 7, 6, 5, 3, 2, 4, 9, 10],
    [6, 7, 8, 9, 6, 5, 7, 8, 5, 6, 9, 10, 8, 7, 6, 10, 12, 11, 13],
    [4, 5, 6, 7, 5, 4, 6, 7, 8, 5, 6, 5, 7, 8, 4, 3, 2, 11, 13, 15]
]

# Create the plot
plt.figure(figsize=(10, 6))
boxplot = plt.boxplot(data, vert=False, patch_artist=True, notch=True,
                      boxprops=dict(facecolor='#D6EAF8', color='black'),
                      whiskerprops=dict(color='black'),
                      capprops=dict(color='black'),
                      flierprops=dict(marker='o', color='red', alpha=0.5),
                      medianprops=dict(color='darkblue', linewidth=2))

# Customizing the boxes with different colors
colors = ['#A9CCE3', '#A3E4D7', '#F9E79F', '#F5B7B1', '#D2B4DE']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

# Titles and labels
plt.title('Weekly Reading Habits of College Students\nby Genre', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Hours per Week', fontsize=12)
plt.yticks(ticks=np.arange(1, len(genres) + 1), labels=genres, fontsize=11)

# Grid for better readability
plt.grid(axis='x', linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust layout for readability
plt.tight_layout()

# Display the plot
plt.show()