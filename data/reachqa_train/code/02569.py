import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# Define genres and their corresponding number of new titles
genres = ['Sci-Fi', 'Fantasy', 'Mystery', 'Romance', 'Horror', 'Non-Fiction']
new_titles = [120, 145, 160, 180, 90, 200]

# Define positions for each genre on the x-axis
x_positions = np.arange(len(genres))

# Create the bar chart
fig, ax = plt.subplots(figsize=(14, 8))

# Set bar width
bar_width = 0.6

# Gradient colors for bars
gradient_colors = [mcolors.to_rgba('#1f77b4'), mcolors.to_rgba('#ff7f0e'),
                   mcolors.to_rgba('#2ca02c'), mcolors.to_rgba('#d62728'),
                   mcolors.to_rgba('#9467bd'), mcolors.to_rgba('#8c564b')]

# Plot the bars with gradient colors
bars = ax.bar(x_positions, new_titles, width=bar_width, color=gradient_colors, edgecolor='grey', linewidth=1.5)

# Add annotations for each bar with percentage
total_titles = sum(new_titles)
for bar, genre, value in zip(bars, genres, new_titles):
    height = bar.get_height()
    percentage = f"{(value/total_titles)*100:.1f}%"
    ax.annotate(f'{height}\n({percentage})',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 4),  # Offset for text
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

# Set x-ticks and labels
ax.set_xticks(x_positions)
ax.set_xticklabels(genres, fontsize=11, rotation=30, ha='right')

# Add titles and labels with multi-line title
ax.set_title('Independent Book Publishing Growth in 2023\n(Genre-wise Analysis)', fontsize=16, fontweight='bold')
ax.set_xlabel('Genres', fontsize=12)
ax.set_ylabel('New Book Titles Released', fontsize=12)

# Add grid lines with differentiation
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7, which='major')
ax.yaxis.grid(True, linestyle=':', linewidth=0.5, alpha=0.5, which='minor')
ax.yaxis.set_minor_locator(plt.MultipleLocator(10))

# Highlight the genre with the highest number of new titles
max_titles_index = np.argmax(new_titles)
max_titles_genre = genres[max_titles_index]
ax.annotate(f'Top Genre: {max_titles_genre}',
            xy=(max_titles_index, new_titles[max_titles_index]),
            xytext=(max_titles_index + 0.5, new_titles[max_titles_index] + 10),
            arrowprops=dict(facecolor='darkred', arrowstyle='->'),
            fontsize=11, color='darkblue')

# Add a trend line for average number of titles
average_titles = np.mean(new_titles)
ax.axhline(y=average_titles, color='green', linestyle='-.', linewidth=1.5, label=f'Average Titles: {average_titles:.2f}')
ax.legend(fontsize=10, loc='upper left')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()