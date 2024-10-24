import matplotlib.pyplot as plt

# Manuscript review times in weeks for different genres
fiction = [4, 5, 6, 8, 10, 12, 6, 7, 9, 11, 7, 8]
non_fiction = [5, 6, 8, 9, 11, 13, 10, 11, 7, 9]
mystery = [3, 4, 6, 7, 10, 12, 3, 4, 5, 9]
sci_fi = [4, 5, 7, 8, 11, 12, 8, 6, 9, 10]
fantasy = [6, 7, 9, 11, 14, 15, 10, 12, 8, 9, 13]

# Collect all the data for the horizontal box chart
data = [fiction, non_fiction, mystery, sci_fi, fantasy]

# Genre labels for the chart
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Science Fiction', 'Fantasy']

# Plotting the horizontal box chart
plt.figure(figsize=(12, 8))

# Create the horizontal boxplot
box = plt.boxplot(data, vert=False, patch_artist=True, notch=True, whis=1.5,
                  boxprops=dict(facecolor='#add8e6', color='darkblue', alpha=0.6),
                  whiskerprops=dict(color='darkblue'),
                  capprops=dict(color='darkblue'),
                  medianprops=dict(color='darkred', linewidth=1.5),
                  flierprops=dict(marker='o', color='green', alpha=0.5))

# Add different colors to each box
colors = ['#add8e6', '#ffcccb', '#c3e6cb', '#fdd835', '#9575cd']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Adding titles and labels
plt.title('Publishing House Insights:\nManuscript Review Time Variability Across Genres', fontsize=16, fontweight='bold')
plt.xlabel('Review Time (weeks)', fontsize=12)
plt.yticks(range(1, len(genres) + 1), genres, fontsize=10)

# Adding grid for readability
plt.grid(visible=True, axis='x', linestyle='--', alpha=0.5)

# Automatically adjust the subplot params so that the subplot(s) fits in to the figure area
plt.tight_layout()

# Show the plot
plt.show()