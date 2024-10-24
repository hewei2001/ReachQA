import matplotlib.pyplot as plt
import numpy as np

# Define the years and fantasy subgenres
years = np.arange(2010, 2020)
high_fantasy = [30, 35, 40, 45, 50, 60, 70, 75, 80, 90]
urban_fantasy = [20, 22, 23, 25, 30, 35, 40, 42, 45, 47]
dark_fantasy = [10, 12, 15, 17, 20, 25, 27, 30, 35, 38]
historical_fantasy = [5, 7, 9, 10, 12, 15, 18, 20, 22, 25]
science_fantasy = [8, 10, 12, 14, 16, 20, 22, 25, 28, 30]

# Total number of books each year
total_books = np.add.reduce([high_fantasy, urban_fantasy, dark_fantasy, historical_fantasy, science_fantasy])

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(14, 9))
colors = ['#4CAF50', '#2196F3', '#F44336', '#FFC107', '#9C27B0']
labels = ['High Fantasy', 'Urban Fantasy', 'Dark Fantasy', 'Historical Fantasy', 'Science Fantasy']

# Plot stacked bars with labels
bottom = np.zeros(len(years))
for genre, color, data in zip(labels, colors, [high_fantasy, urban_fantasy, dark_fantasy, historical_fantasy, science_fantasy]):
    bars = ax.bar(years, data, bottom=bottom, label=genre, color=color, alpha=0.8)
    bottom += data
    ax.bar_label(bars, label_type='center', fmt='%d', fontsize=10)

# Add line plot for total publications
ax.plot(years, total_books, color='black', marker='o', linestyle='--', linewidth=2, label='Total Books')

# Customize chart
ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Number of Books Published', fontsize=14, fontweight='bold')
ax.set_title('Annual Fantasy Book Publications by Genre\n(2010-2019)', fontsize=16, fontweight='bold')
ax.set_xticks(years)
ax.set_yticks(range(0, 301, 25))
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Legend and layout
ax.legend(title='Fantasy Subgenres', title_fontsize='13', fontsize='11', loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()

# Show plot
plt.show()