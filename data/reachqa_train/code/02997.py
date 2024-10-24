import matplotlib.pyplot as plt
import numpy as np

# Define genres
genres = ['Science Fiction', 'Fantasy', 'Mystery', 'Romance', 'Non-fiction']

# Artificially crafted review score data for each genre
data_science_fiction = [8.5, 9.0, 7.5, 8.0, 9.5, 8.7, 9.1, 7.8, 8.4, 9.2]
data_fantasy = [8.8, 9.0, 8.9, 8.7, 8.6, 9.1, 9.0, 9.3, 8.8, 9.0]
data_mystery = [7.5, 6.8, 7.2, 8.0, 7.9, 7.4, 8.1, 7.7, 6.9, 8.3]
data_romance = [6.0, 5.5, 7.0, 6.8, 5.8, 6.2, 7.1, 6.0, 6.9, 5.9]
data_non_fiction = [8.0, 6.5, 5.9, 7.3, 8.4, 5.7, 9.0, 4.9, 6.7, 8.1]

# Combine data for the box plot
data = [data_science_fiction, data_fantasy, data_mystery, data_romance, data_non_fiction]

# Calculate mean scores for each genre for the bar chart
means = [np.mean(genre_data) for genre_data in data]

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# 1. Box Plot (left)
box = ax1.boxplot(data, vert=False, patch_artist=True, notch=True,
                  boxprops=dict(facecolor='lightgrey', color='black', linewidth=1.5),
                  whiskerprops=dict(color='black', linewidth=1.5),
                  capprops=dict(color='black', linewidth=1.5),
                  medianprops=dict(color='red', linewidth=2),
                  flierprops=dict(marker='o', markerfacecolor='purple', markersize=5, linestyle='none'))

# Add color to the boxes for better distinction
colors = ['lightblue', 'lightcoral', 'lightgreen', 'lightpink', 'lightsalmon']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set labels and title for the box plot
ax1.set_yticklabels(genres, fontsize=12, fontweight='bold')
ax1.set_xlabel('Review Score (out of 10)', fontsize=12)
ax1.set_title("Spectrum of Critical Reviews:\nLiterary Genre Analysis", fontsize=16, fontweight='bold')
ax1.xaxis.grid(True, linestyle='--', alpha=0.7)

# 2. Bar Chart (right)
bars = ax2.bar(genres, means, color=colors, edgecolor='black', linewidth=1.5)

# Add value labels on each bar for clarity
for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), va='bottom', ha='center', fontsize=10, fontweight='bold')

# Set labels and title for the bar chart
ax2.set_ylabel('Average Review Score', fontsize=12)
ax2.set_title("Average Scores by Genre", fontsize=16, fontweight='bold')
ax2.set_ylim(0, 10)  # Ensuring the y-axis ranges from 0 to 10 for context

# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout()

# Display the plot
plt.show()