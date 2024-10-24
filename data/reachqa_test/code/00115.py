import matplotlib.pyplot as plt
import numpy as np

# Extended Data (Sales figures in thousands from 2000 to 2023)
years = np.arange(2000, 2024)
epic_fantasy_sales = [50, 55, 60, 70, 75, 80, 82, 90, 95, 100, 105, 110, 115, 120, 130, 140, 150, 155, 160, 165, 170, 172, 175, 178]
urban_fantasy_sales = [40, 42, 45, 50, 55, 58, 60, 63, 67, 70, 73, 75, 77, 80, 85, 88, 90, 92, 95, 98, 100, 102, 105, 108]
dark_fantasy_sales = [30, 32, 35, 40, 42, 45, 48, 52, 55, 58, 60, 62, 65, 68, 70, 73, 75, 78, 80, 85, 88, 90, 93, 95]
magical_realism_sales = [20, 22, 25, 27, 30, 32, 35, 37, 40, 43, 45, 47, 50, 52, 55, 58, 60, 63, 65, 68, 70, 72, 74, 76]
paranormal_fantasy_sales = [10, 15, 18, 20, 22, 25, 28, 30, 32, 35, 37, 40, 42, 45, 48, 50, 52, 55, 57, 60, 63, 65, 67, 70]
science_fiction_sales = [35, 37, 39, 42, 45, 48, 50, 54, 58, 62, 66, 69, 72, 75, 78, 80, 85, 88, 90, 92, 95, 97, 100, 103]

# Combine data into a list for the box plot
genre_sales_data = [
    epic_fantasy_sales,
    urban_fantasy_sales,
    dark_fantasy_sales,
    magical_realism_sales,
    paranormal_fantasy_sales,
    science_fiction_sales
]

# Genre labels
genre_labels = ['Epic Fantasy', 'Urban Fantasy', 'Dark Fantasy', 'Magical Realism', 'Paranormal Fantasy', 'Science Fiction']

# Create the vertical box plot
fig, ax = plt.subplots(figsize=(12, 7))
box = ax.boxplot(genre_sales_data, vert=True, patch_artist=True, notch=True,
                 boxprops=dict(facecolor='lightblue', color='darkblue', linewidth=1.5),
                 whiskerprops=dict(color='darkblue', linewidth=1.5),
                 capprops=dict(color='darkblue', linewidth=1.5),
                 medianprops=dict(color='firebrick', linewidth=2))

# Customize chart labels and title
ax.set_xticklabels(genre_labels, fontsize=10, rotation=15, ha='right')
ax.set_title("Popularity Trends in Fantasy Literature Genres\nfrom 2000 to 2023", fontsize=14, weight='bold')
ax.set_ylabel("Annual Book Sales (in thousands)", fontsize=12)

# Color boxes differently for visual distinction
colors = ['#add8e6', '#87ceeb', '#00bfff', '#1e90ff', '#4682b4', '#5f9ea0']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Adding grid lines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add a legend to clarify the color coding
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(handles, genre_labels, loc='upper left', title='Genres', fontsize=10)

# Plot mean line for each genre
for i, genre_data in enumerate(genre_sales_data, start=1):
    mean_value = np.mean(genre_data)
    ax.plot([i-0.3, i+0.3], [mean_value, mean_value], color='orange', linewidth=2, label='Mean' if i == 1 else "")

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()