import matplotlib.pyplot as plt
import numpy as np

# Data for original bar chart
decades = ['1960s', '1970s', '1980s', '1990s', '2000s']
genres = ['Fiction', 'Non-fiction', 'Science Fiction', 'Mystery', 'Romance']
publication_counts = {
    'Fiction': [20, 25, 30, 28, 40],
    'Non-fiction': [10, 15, 25, 35, 45],
    'Science Fiction': [5, 10, 15, 20, 25],
    'Mystery': [8, 12, 18, 22, 30],
    'Romance': [12, 18, 22, 24, 35]
}
data = [publication_counts[genre] for genre in genres]

# Calculating total publications per decade for the new subplot
total_per_decade = [sum([publication_counts[genre][i] for genre in genres]) for i in range(len(decades))]

# Plot configuration
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Bar Chart
colors = ['royalblue', 'seagreen', 'coral', 'goldenrod', 'violet']
for i, (color, decade) in enumerate(zip(colors, decades)):
    x_offsets = np.arange(len(genres)) + i * 0.15
    decade_data = [publication_counts[genre][i] for genre in genres]
    ax1.bar(x_offsets, decade_data, width=0.15, label=decade, color=color, alpha=0.8)

ax1.set_title('Evolution of Book Genre Popularity\n1960s to 2000s', fontsize=14, fontweight='bold')
ax1.set_xlabel('Genres', fontsize=12)
ax1.set_ylabel('Number of Books Published', fontsize=12)
ax1.set_xticks(np.arange(len(genres)) + 0.3)
ax1.set_xticklabels(genres, fontsize=10, rotation=45, ha='right')
ax1.legend(title='Decades', loc='upper left', fontsize=10)
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Line Chart for Total Publications
ax2.plot(decades, total_per_decade, marker='o', linestyle='-', color='navy', linewidth=2, alpha=0.9)
ax2.set_title('Total Book Publications\nAcross All Genres by Decade', fontsize=14, fontweight='bold')
ax2.set_xlabel('Decades', fontsize=12)
ax2.set_ylabel('Total Number of Books', fontsize=12)
ax2.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Enhance layout to prevent label overlap
plt.tight_layout()

# Display the charts
plt.show()