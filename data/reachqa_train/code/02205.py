import matplotlib.pyplot as plt
import numpy as np

# Data for manuscript review time in hours
# Time allocations for each genre (hours spent per manuscript review)
fiction_times = [30, 45, 40, 55, 60, 50, 65, 70, 55, 45]
non_fiction_times = [40, 35, 45, 50, 55, 65, 60, 70, 55, 45]
mystery_times = [20, 25, 15, 30, 35, 40, 25, 30, 20, 15]
fantasy_times = [50, 55, 60, 70, 65, 75, 80, 85, 70, 60]
historical_times = [45, 50, 55, 60, 50, 55, 60, 65, 70, 75]

# Combine data into a list
data = [fiction_times, non_fiction_times, mystery_times, fantasy_times, historical_times]

# Define genre labels
genres = ['Fiction', 'Non-fiction', 'Mystery', 'Fantasy', 'Historical']

# Define box colors
colors = ['#98abc5', '#8a89a6', '#7b6888', '#6b486b', '#a05d56']

# Create a horizontal box plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot with custom colors and box styles
bp = ax.boxplot(data, vert=False, patch_artist=True, labels=genres,
                boxprops=dict(color='black', facecolor='lightgray', linewidth=1.5),
                whiskerprops=dict(color='black', linewidth=1.5),
                capprops=dict(color='black', linewidth=1.5),
                medianprops=dict(color='red', linewidth=2),
                flierprops=dict(marker='o', color='black', alpha=0.5))

# Customize the color of each box
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Add chart title and labels
ax.set_title("Literary Masterpieces Under the Editorial Lens:\nTime Allocation for Manuscript Review Across Genres", 
             fontsize=16, pad=20)
ax.set_xlabel("Time Spent (Hours)", fontsize=12)
ax.set_ylabel("Literary Genres", fontsize=12)

# Customize the grid and layout for better readability
ax.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()

# Display the chart
plt.show()