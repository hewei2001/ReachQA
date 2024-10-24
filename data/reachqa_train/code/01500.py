import matplotlib.pyplot as plt

# Data for workshop attendance across various genres
genres = ['Fantasy', 'Science Fiction', 'Mystery', 'Non-fiction', 'Poetry']
attendance = [
    [22, 25, 20, 28, 30, 18, 24],    # Fantasy
    [18, 20, 15, 25, 17, 22, 19],    # Science Fiction
    [30, 28, 35, 32, 26, 31, 29],    # Mystery
    [15, 14, 13, 12, 17, 10, 18],    # Non-fiction
    [20, 18, 22, 19, 25, 21, 24]     # Poetry
]

# Initialize the plot
plt.figure(figsize=(12, 8))

# Create a horizontal boxplot
boxprops = dict(facecolor='lightgrey', color='black')
medianprops = dict(color='red', linewidth=2)
meanprops = dict(marker='o', markerfacecolor='green', markersize=8)
flierprops = dict(marker='s', markerfacecolor='orange', markersize=6, linestyle='none')
whiskerprops = dict(color='black', linewidth=1.5)
capprops = dict(color='black', linewidth=1.5)

plt.boxplot(attendance, vert=False, patch_artist=True, showmeans=True, notch=True,
            boxprops=boxprops, whiskerprops=whiskerprops, capprops=capprops,
            medianprops=medianprops, meanprops=meanprops, flierprops=flierprops)

# Set the y-ticks to genre names
plt.yticks(range(1, len(genres) + 1), genres, fontsize=11, fontweight='bold')

# Add a title and axis labels
plt.title('Creative Writing Workshop Attendance Across Various Genres\n', fontsize=16, fontweight='bold')
plt.xlabel('Number of Participants', fontsize=12, fontweight='bold')
plt.ylabel('Writing Genre', fontsize=12, fontweight='bold')

# Customize the grid
plt.grid(True, linestyle='--', alpha=0.7, axis='x')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()