import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Artificial data for reading habits in percentages
print_books = np.array([70, 65, 60, 58, 55, 50, 45, 40, 35, 30, 25])
ebooks = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
online_articles = np.array([20, 20, 20, 17, 15, 15, 15, 15, 15, 15, 15])

# Calculate bottom positions for stacking
bottom_ebooks = print_books
bottom_online_articles = bottom_ebooks + ebooks

# Set up color gradients
colors = ['#8A2BE2', '#5F9EA0', '#FF6347']

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))
fig.suptitle('The Evolution of Reading Habits in the Digital Age:\n2010-2020', fontsize=16, fontweight='bold')

# Stacked bar chart
ax.bar(years, print_books, label='Print Books', color=colors[0], width=0.6, alpha=0.8)
ax.bar(years, ebooks, bottom=bottom_ebooks, label='E-books', color=colors[1], width=0.6, alpha=0.8)
ax.bar(years, online_articles, bottom=bottom_online_articles, label='Online Articles', color=colors[2], width=0.6, alpha=0.8)

# Axis labeling and limits
ax.set_ylabel('Reading Time Proportion (%)', fontsize=12)
ax.set_xlabel('Year', fontsize=12)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha="right")
ax.set_ylim(0, 100)
ax.yaxis.set_major_formatter(lambda x, _: f'{int(x)}%')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Legend
ax.legend(loc='upper right', title='Reading Format', fontsize=10, title_fontsize='12')

# Annotate data values on bars
for year, pb, eb, oa in zip(years, print_books, ebooks, online_articles):
    ax.text(year, pb / 2, f'{pb}%', ha='center', va='center', color='white', fontsize=9)
    ax.text(year, bottom_ebooks[np.where(years == year)][0] + eb / 2, f'{eb}%', ha='center', va='center', color='white', fontsize=9)
    ax.text(year, bottom_online_articles[np.where(years == year)][0] + oa / 2, f'{oa}%', ha='center', va='center', color='white', fontsize=9)

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show the plot
plt.show()