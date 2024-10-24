import matplotlib.pyplot as plt
import numpy as np

# Define the languages and number of books published each year
languages = ['Elvish', 'Klingon', 'Dothraki', 'Esperanto', 'Na\'vi']
years = ['2018', '2019', '2020', '2021', '2022']
book_counts = [
    [15, 20, 25, 40, 55],  # Elvish
    [10, 15, 20, 30, 45],  # Klingon
    [5, 8, 12, 18, 30],    # Dothraki
    [22, 27, 30, 35, 40],  # Esperanto
    [8, 12, 15, 22, 28]    # Na'vi
]

# Calculate the total number of books published per year across all languages
total_books_per_year = np.sum(book_counts, axis=0)

# Setup bar width and positions for the bar chart
width = 0.15
indices = np.arange(len(years))

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 8))

# Bar chart for the number of books per language per year
colors = ['#8e44ad', '#2980b9', '#27ae60', '#f39c12', '#c0392b']
for i, (language, count) in enumerate(zip(languages, book_counts)):
    ax1.bar(indices + i * width, count, width, label=language, color=colors[i], alpha=0.85)

# Customize the bar chart
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Books Published', fontsize=12)
ax1.set_title('The Rise of Esoteric Languages\nin Literature (2018-2022)', fontsize=14, fontweight='bold', pad=15)
ax1.set_xticks(indices + width * (len(languages) - 1) / 2)
ax1.set_xticklabels(years)
ax1.legend(title='Languages', loc='upper left')
ax1.grid(axis='y', linestyle='--', alpha=0.6)

# Annotate bars with the number of books published
for i, bar_set in enumerate(ax1.containers):
    ax1.bar_label(bar_set, label_type='edge', fontsize=9)

# Line chart for the total number of books published each year
ax2.plot(years, total_books_per_year, marker='o', linestyle='-', color='purple', linewidth=2, label='Total Books')
ax2.fill_between(years, total_books_per_year, color='purple', alpha=0.1)

# Customize the line chart
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Total Books Published', fontsize=12)
ax2.set_title('Total Esoteric Language Books Published\n(2018-2022)', fontsize=14, fontweight='bold', pad=15)
ax2.grid(axis='y', linestyle='--', alpha=0.6)
ax2.legend(loc='upper left')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the chart
plt.show()