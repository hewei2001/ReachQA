import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

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

# Create the figure and axes
fig, ax = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [2, 1]})

# Boxplot with overlaid violin plot
sns.violinplot(data=data, orient='h', ax=ax[0], inner=None, palette='muted', alpha=0.5)
boxplot = ax[0].boxplot(data, vert=False, patch_artist=True, notch=True,
                        boxprops=dict(facecolor='#D6EAF8', color='black'),
                        whiskerprops=dict(color='black'),
                        capprops=dict(color='black'),
                        flierprops=dict(marker='o', color='red', alpha=0.5),
                        medianprops=dict(color='darkblue', linewidth=2))

# Customize box colors
colors = ['#A9CCE3', '#A3E4D7', '#F9E79F', '#F5B7B1', '#D2B4DE']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

# Overlay data points with jitter
for i, genre_data in enumerate(data):
    y = np.random.normal(loc=i+1, scale=0.05, size=len(genre_data))  # Apply jitter
    ax[0].plot(genre_data, y, 'o', color='gray', alpha=0.6)

# Titles and labels for the main plot
ax[0].set_title('Weekly Reading Habits of College Students by Genre', fontsize=14, fontweight='bold')
ax[0].set_xlabel('Hours per Week', fontsize=12)
ax[0].set_yticks(np.arange(len(genres)))
ax[0].set_yticklabels(genres, fontsize=11)
ax[0].grid(axis='x', linestyle='--', linewidth=0.7, alpha=0.7)

# Subplot: Histogram of total hours per genre
total_hours = [sum(hours) for hours in data]
ax[1].barh(genres, total_hours, color=colors, alpha=0.8)
ax[1].set_title('Total Weekly Hours Spent per Genre', fontsize=12, fontweight='bold')
ax[1].set_xlabel('Total Hours', fontsize=12)
ax[1].grid(axis='x', linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()