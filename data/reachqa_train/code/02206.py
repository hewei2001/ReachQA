import matplotlib.pyplot as plt
import numpy as np

# Expanded data for manuscript review time in hours
fiction_times = [30, 45, 40, 55, 60, 50, 65, 70, 55, 45, 60, 50, 72, 66, 55, 40, 47, 58, 52, 43]
non_fiction_times = [40, 35, 45, 50, 55, 65, 60, 70, 55, 45, 50, 65, 62, 56, 63, 59, 51, 66, 64, 48]
mystery_times = [20, 25, 15, 30, 35, 40, 25, 30, 20, 15, 28, 24, 18, 21, 22, 26, 32, 31, 19, 23]
fantasy_times = [50, 55, 60, 70, 65, 75, 80, 85, 70, 60, 72, 78, 81, 74, 67, 66, 69, 77, 79, 68]
historical_times = [45, 50, 55, 60, 50, 55, 60, 65, 70, 75, 56, 58, 54, 57, 61, 63, 59, 62, 67, 69]
science_fiction_times = [35, 40, 45, 38, 50, 42, 47, 43, 39, 36, 44, 49, 48, 41, 46, 53, 51, 52, 37, 50]
romance_times = [25, 30, 35, 28, 27, 31, 33, 29, 34, 32, 30, 36, 38, 26, 29, 37, 39, 35, 32, 33]

# Combine data into a list
data = [
    fiction_times, non_fiction_times, mystery_times, fantasy_times,
    historical_times, science_fiction_times, romance_times
]

# Define genre labels
genres = [
    'Fiction', 'Non-fiction', 'Mystery', 'Fantasy', 'Historical', 
    'Science Fiction', 'Romance'
]

# Define box colors
colors = ['#98abc5', '#8a89a6', '#7b6888', '#6b486b', '#a05d56', '#d0743c', '#ff8c00']

# Create a horizontal box plot
fig, ax = plt.subplots(figsize=(14, 9))

# Plot with custom colors and box styles
bp = ax.boxplot(
    data, vert=False, patch_artist=True, labels=genres,
    boxprops=dict(facecolor='lightgray', color='black', linewidth=1.5),
    whiskerprops=dict(color='black', linewidth=1.5),
    capprops=dict(color='black', linewidth=1.5),
    medianprops=dict(color='red', linewidth=2),
    flierprops=dict(marker='o', color='black', alpha=0.5)
)

# Customize the color of each box
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Add mean lines
means = [np.mean(times) for times in data]
for mean, y_pos in zip(means, range(1, len(data) + 1)):
    ax.plot(mean, y_pos, 'D', markerfacecolor='cyan', markersize=8, label='Mean' if y_pos == 1 else "")

# Add chart title and labels
ax.set_title(
    "Literary Masterpieces Under the Editorial Lens:\nTime Allocation for Manuscript Review Across Genres", 
    fontsize=16, pad=20
)
ax.set_xlabel("Time Spent (Hours)", fontsize=12)
ax.set_ylabel("Literary Genres", fontsize=12)

# Add sum annotations
for i, times in enumerate(data):
    total_time = sum(times)
    ax.annotate(f'Total: {total_time}h', xy=(max(times) + 5, i + 1),
                xytext=(max(times) + 5, i + 1), fontsize=9, color='green')

# Customize the grid and layout for better readability
ax.grid(axis='x', linestyle='--', alpha=0.7)
ax.legend(loc='upper right', fontsize=10)
plt.tight_layout()

# Display the chart
plt.show()