import matplotlib.pyplot as plt
import numpy as np

# Define genres and their corresponding number of new titles
genres = ['Sci-Fi', 'Fantasy', 'Mystery', 'Romance', 'Horror', 'Non-Fiction']
new_titles = [120, 145, 160, 180, 90, 200]

# Define positions for each genre on the x-axis
x_positions = np.arange(len(genres))

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 7))

# Set bar width and colors
bar_width = 0.6
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Plot the bars with colors
bars = ax.bar(x_positions, new_titles, width=bar_width, color=colors, edgecolor='black')

# Add annotations for each bar
for bar in bars:
    height = bar.get_height()
    ax.annotate(
        f'{height}',
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 4),  # Offset for text
        textcoords="offset points",
        ha='center', va='bottom', fontsize=10, fontweight='bold', color='black'
    )

# Set x-ticks and labels
ax.set_xticks(x_positions)
ax.set_xticklabels(genres, fontsize=11, rotation=30, ha='right')

# Add titles and labels
ax.set_title('Independent Book Publishing Growth in 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Genres', fontsize=12)
ax.set_ylabel('New Book Titles Released', fontsize=12)

# Add grid lines for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Highlight the genre with the highest number of new titles
max_titles_index = np.argmax(new_titles)
max_titles_genre = genres[max_titles_index]
ax.annotate(
    f'Top Genre: {max_titles_genre}',
    xy=(max_titles_index, new_titles[max_titles_index]),
    xytext=(max_titles_index + 0.5, new_titles[max_titles_index] + 10),
    arrowprops=dict(facecolor='black', arrowstyle='->'),
    fontsize=11, color='darkblue'
)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()