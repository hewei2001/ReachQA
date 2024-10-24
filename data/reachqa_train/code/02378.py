import matplotlib.pyplot as plt
import numpy as np

# Decades and genres data for histogram plotting
decades = ['1960s', '1970s', '1980s', '1990s', '2000s']
genres = ['Fiction', 'Non-fiction', 'Science Fiction', 'Mystery', 'Romance']

# Manual data of book publications over decades
publication_counts = {
    'Fiction': [20, 25, 30, 28, 40],
    'Non-fiction': [10, 15, 25, 35, 45],
    'Science Fiction': [5, 10, 15, 20, 25],
    'Mystery': [8, 12, 18, 22, 30],
    'Romance': [12, 18, 22, 24, 35]
}

# Setting up the histogram data
data = [publication_counts[genre] for genre in genres]

# Plotting configuration
fig, ax = plt.subplots(figsize=(12, 8))

# Colors corresponding to each decade
colors = ['royalblue', 'seagreen', 'coral', 'goldenrod', 'violet']

# Plot each decade with an offset for clarity and legend
for i, (color, decade) in enumerate(zip(colors, decades)):
    # Offset calculation for side-by-side bars
    x_offsets = np.arange(len(genres)) + i * 0.15
    decade_data = [publication_counts[genre][i] for genre in genres]

    # Bar plotting
    ax.bar(x_offsets, decade_data, width=0.15, label=decade, color=color, alpha=0.8)

# Customizing the plot
ax.set_title('Evolution of Book Genre Popularity\nFrom the 1960s to the 2000s', fontsize=16, fontweight='bold')
ax.set_xlabel('Genres', fontsize=12)
ax.set_ylabel('Number of Books Published', fontsize=12)
ax.set_xticks(np.arange(len(genres)) + 0.3)
ax.set_xticklabels(genres, fontsize=10, rotation=45, ha='right')

# Adding a legend
ax.legend(title='Decades', loc='upper left', fontsize=10)

# Adding gridlines for y-axis
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Enhance layout to prevent label overlap
plt.tight_layout()

# Display the histogram
plt.show()